# EXIF CLI

CLI to automated EXIF manipulation on a batch of pictures.

**This project relies on Python module [exif](https://gitlab.com/TNThieding/exif), which is not actively maintained.** Use this project for inspiration only.

I use it to process batch of files while scanning old pictures before archival.


## Installation

```
$ pip3 install git+https://github.com/julien-sobczak/exif-cli.git
```


## Usage

The CLI supports a single command with various flags:

```shell
$ exif-cli add -h
usage: exif-cli add [-h] [--date DATE [DATE ...]] [--date-unique] [--location LOCATION] [--override OVERRIDE] files

positional arguments:
  files                 pictures to edit

optional arguments:
  -h, --help            show this help message and exit
  --date DATE [DATE ...]
                        original date
  --date-unique         increment dates to be unique
  --location LOCATION   GPS coordinates
  --override OVERRIDE   override files
```


## Development

### Run locally

```shell
$ cd exifcli/
$ python3 setup.py install # The binary exif-cli is now present in $PATH
$ exif-cli add --date 2020 *.jpg
# OR
$ python3 -m exifcli add --date 2020 *.jpg
```


### Test locally

```
$ python3 -m unittest discover exifcli
```
