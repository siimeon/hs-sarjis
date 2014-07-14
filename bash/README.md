# Helsingin Sanomat Comic Parser

## Bash implementation

Bash implementation has three scripts:
- Main script hs_sarjis.sh
- JSON output script sarjis_json.sh
- Test implentation script for Fingerpori comic fingerpori.sh

### How to run

On Ubuntu or Red Hat

```
# Basic usage
./hs_sarjis.sh http://www.hs.fi/fingerpori/
# Outputs image url

# For JSON output
./sarjis_json.sh Fingerpori http://www.hs.fi/fingerpori/
# Outputs json with name of comic and url of comic

# Fingerpori sample
./fingerpori.sh
# Outputs Fingerpori comics json formated name and url
```
