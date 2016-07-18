This utility allows you to take samples from an Amazon S3 key.

What it does is grab random bytes from the key and assemble unbroken lines from
the file to create as sample.

The use case is for determining a file format, file contents, etc. See the
cognoscenti project for an example.

_Usage:_

    ./sample.py s3://bucket/key.csv [LINES]

LINES allows you to indicate the number of lines you hope to recieve. It will
grab 1000 lines by default.

You can also attempt to grab the header row of the file.

    ./sample.py s3://bucket/key.csv --headers [LINES]
