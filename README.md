# convert-markmonitor-domain-list-to-mozilla

Tool to convert a MarkMonitor domain export xls file into a JSON file for use with other Mozilla tools.

Reads from `myDomains.xls`, a file that MarkMonitor produces when exporting, and
creates `mozilla-owned-dns-domains.json` which is stored in https://github.com/mozilla/security-private/tree/master/infosec-internal-data/dns-domains