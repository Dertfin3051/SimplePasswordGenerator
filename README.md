# Simple Password Generator

## How to install
You can install this program in two ways: download it via the website and download it via the command line (recommended).
Let's consider the second way:
Install Git on your computer. Open a terminal and call:
```
git clone https://github.com/Dertfin3051/SimplePasswordGenerator.git
cd Simple Password Generator
```

## How to use
To quickly generate a password, call:
`python spasswd.py`

There are additional parameters that can be used when calling the command:
`-f` *or* `--file` - File name for recording the prepared password
`-rw` *or* `--rawfile` - File name for recording the prepared password with deleting another data
`-t` *or* `--type` - Selecting a password generation template *(for advanced users)*

Examples:

`python spasswd.py -f passwords.txt`

`python spasswd.py --file passwords.txt`

`python spasswd.py -rw passwords.txt`

`python spasswd.py --type 2`

`python spasswd.py --type 0 --file passwords.txt`
