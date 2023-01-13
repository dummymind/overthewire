https://github.com/robertdavidgraham/masscan

# MASSCAN: Mass IP port scanner

This is an Internet-scale port scanner. It can scan the entire Internet in under 5 minutes, transmitting 10 million packets per second, from a single machine.

Its usage (parameters, output) is similar to `nmap`, the most famous port scanner. When in doubt, try one of those features -- features that support widespread scanning of many machines are supported, while in-depth scanning of single machines aren't.

Internally, it uses asynchronous transmission, similar to port scanners like `scanrand`, `unicornscan`, and `ZMap`. It's more flexible, allowing arbitrary port and address ranges.

NOTE: masscan uses its own **ad hoc TCP/IP stack**. Anything other than simple port scans may cause conflict with the local TCP/IP stack. This means you need to use either the `--src-ip` option to run from a different IP address, or use `--src-port` to configure which source ports masscan uses, then also configure the internal firewall (like `pf` or `iptables`) to firewall those ports from the rest of the operating system.


https://nmap.org/

_Nmap Network Scanning_ is the official guide to the [Nmap Security Scanner](https://nmap.org/), a free and open source utility used by millions of people for network discovery, administration, and security auditing. From explaining port scanning basics for novices to detailing low-level packet crafting methods used by advanced hackers, this book suits all levels of security and networking professionals. A 42-page reference guide documents every Nmap feature and option, while the rest of the book demonstrates how to apply those features to quickly solve real-world tasks. Examples and diagrams show actual communication on the wire.

