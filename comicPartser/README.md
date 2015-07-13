# Helsingin Sanomat Comic Parser

Helsingin sanomat comic parser for parsing all latest comics. This script supports few different comics 
form Helsingin Sanomat, Talousanomat and Iltasanomat.

## Supported comics

Supported comics

- www.hs.fi/fingerpori/ for Fingerpori
- http://www.hs.fi/viivijawagner/ for Viivi ja Wagner
- http://www.iltasanomat.fi/suomiklassikko/ for Suomiklassikko
- http://www.taloussanomat.fi/ for Dilbert

### How to run

```
# Basic usage
python hs_sarjis.py --name Fingerpori --url http://www.hs.fi/fingerpori/
# Output is json formated result
```

### Example of result
```
{"url": "http://hs13.snstatic.fi/webkuva/sarjis/560/1305847479322?ts=102", "name": "figerpori"}
```

### Options
```
usage: hs_sarjis.py [-h] [-n NAME] -u URL [-is] [--dilbert]

Helsingin Sanomat comic parser

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Name of comic
  -u URL, --url URL     Url address of comic
  -is, --iltasanomat    Option if Iltasanomat site is source of comic
  --dilbert             Option if Dilbert from Talousanomat is used
```