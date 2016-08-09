This utility allows you to extsact sample lines from a CSV hosted on Amazon S3.
The use case is that you have a really large CSV on S3 that you want to look at,
but you do not want to download the entire file.

What it does is grab random bytes from the key and assemble unbroken lines from
the file to create as sample.

The use case is for determining a file format, file contents, etc. See the
cognoscenti project for an example. (Um, this doesn't exist yet. Check back later.)

_Usage: sample.py [OPTIONS]_

	Options:
	  --bucket TEXT             Amazon S3 Bucket
	  --key TEXT                Amazon S3 Key (e.g., file you want to inspect)
	  --headers / --no-headers  Include the first row from the file?
	  -d, --delimiter TEXT      Field delimiter
	  -l, --lines INTEGER       How many sample lines do you want (at minimum)?
	  --help                    Show this message and exit.

Allows you to indicate the number of lines you hope to recieve. It will
grab 1000 lines by default.

#### Installing

You can install via pip:

pip install sample-s3

#### Example

  ss3 --bucket foo --key path/to/bar.csv > sample_file.csv
