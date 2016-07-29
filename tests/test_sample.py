import pytest
import mock

from samples3.sample import MAX_HEADER_OFFSET, get_headers


class TestGetHeaders:

    def test_get_header_no_line_break(self):
        """ If we look at a file that has no line break in the first
        MAX_HEADER_OFFSET, then we should raise a ValueError and quit
        attempting. """

        read_results = [b'*garbage*' * int(MAX_HEADER_OFFSET / 4)] * 2

        mock_client = mock.Mock(**{
            'get_object.return_value': {
                'Body': mock.Mock(
                    **{'read.side_effect': read_results}
                )
            }
        })
        with pytest.raises(ValueError):
            get_headers(mock_client, 'fake_bucket', 'fake_key', ',', sample_bytes=MAX_HEADER_OFFSET + 1)
