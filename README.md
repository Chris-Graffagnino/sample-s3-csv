This utility allows you to take samples from an Amazon S3 key.

What it does is grab random bytes from the key and assemble unbroken lines from
the file to create as sample.

The use case is for determining a file format, file contents, etc. See the
cognoscenti project for an example.

_Usage: sample.py [OPTIONS]_

    Options:
      --bucket TEXT             bucket name
      --key TEXT                key name
      --headers / --no-headers  Include headers in output, defaults to include.
      -d, --delimiter TEXT      File delimiter, defaults to ,
      -l, --lines INTEGER       How many sample lines do you want? Defaults to 1000.
      --help                    Show this message and exit.

Allows you to indicate the number of lines you hope to recieve. It will
grab 1000 lines by default.

#### Example

  python sample.py --bucket foo --key path/to/bar.csv > sample_file.csv
