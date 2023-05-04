# convert-markmonitor-domain-list-to-mozilla

Tool to convert a MarkMonitor domain export xls file into a JSON file for use with other Mozilla tools.

Reads from `myDomains.xls`, a file that MarkMonitor produces when exporting, and
creates `mozilla-owned-dns-domains.json` which is stored in https://github.com/mozilla/security-private/tree/master/infosec-internal-data/dns-domains

# Usage

1. Install the tool with `pip install convert_markmonitor_domain_list_to_mozilla`
2. Ensure that you have a `myDomains.xls` file in the current working directory
3. Run `convert-markmonitor-domain-list-to-mozilla`
4. Look at the `mozilla-owned-dns-domains.json` file that's produced