import pytest
import mock

from sample_s3.sample import CR, MAX_HEADER_OFFSET, get_headers


class TestGetHeaders:

    def get_mock_client(self, results):
        return mock.Mock(**{
            'get_object.return_value': {
                'Body': mock.Mock(
                    **{'read.side_effect': results}
                )
            }
        })

    def test_get_header_no_line_break(self):
        """ If we look at a file that has no line break in the first
        MAX_HEADER_OFFSET, then we should raise a ValueError and quit
        attempting. """

        read_results = [b'*garbage*' * int(MAX_HEADER_OFFSET / 4)] * 2

        mock_client = self.get_mock_client(read_results)
        with pytest.raises(ValueError):
            get_headers(mock_client, 'fake_bucket', 'fake_key', ',', sample_bytes=MAX_HEADER_OFFSET + 1)

    def test_get_headers_unicode(self):
        """ Do some crazy unicode things, make sure we get back unicode
        and not binary (how we would normally get it from boto get_object """
        delimiter = '🎃'.encode('utf8')
        cr = CR.encode('utf8')

        expected_header_binary = delimiter.join([b'My', b'Name', b'Is', b'Earl'])

        read_results = [
            expected_header_binary + cr + delimiter.join([b'There', b'Is']),
            delimiter.join([b'No', b'Cow']) + cr + delimiter.join([b'Level', b'!']),

        ]

        mock_client = self.get_mock_client(read_results)
        header_str = get_headers(mock_client, 'fake_bucket', 'fake_key', ',', sample_bytes=100)

        assert header_str == expected_header_binary.decode('utf8')
