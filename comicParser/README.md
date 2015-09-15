# Comic Parser sample

Example for using Comic Parser python script/program to extract Fingerpori comic url from Helsingin Sanomat

```
python comicParserCli.py -s http://www.hs.fi/fingerpori/ -t webkuva/taysi --tag meta --attribute content --name Fingerpori
```

For saving JSON output that this command produces run this command

```
python comicParserCli.py -s http://www.hs.fi/fingerpori/ -t webkuva/taysi --tag meta --attribute content --name Fingerpori > data.json
```

After this if web app is used to present comic its needed to be moved under html/app

Example with bash:

```
mv data.json ../html/app
```
