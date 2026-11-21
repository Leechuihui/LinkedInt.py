**English** | [简体中文](README.zh-CN.md)

# 🔗 LinkedInt.py

[![Python](https://img.shields.io/badge/Python-3.8%2B-3fb950?logo=python&logoColor=white)](https://python.org)
[![LinkedIn](https://img.shields.io/badge/Source-LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://linkedin.com)
[![Tor Ready](https://img.shields.io/badge/Network-Tor_Ready-8b5cf6?logo=tor-project&logoColor=white)](https://torproject.org)

Fork of [vysecurity/LinkedInt](https://github.com/vysecurity/LinkedInt) — LinkedIn OSINT enumerator, updated 2026.

<p align="center">
<img src="https://github.com/vysecurity/LinkedInt/blob/master/asset/linkedint.png?raw=true">
</p>

# Disclaimer

* The project is to be used for educational and testing purposes only.

# Authors

* Developed update by Leechuihui version 2.0

Contributors:

* Leesoh
* harshil-shah004

# Installation
```
git clone https://github.com/Leechuihui/LinkedInt.py.git
cd LinkedInt.py
pip install -r requirements.txt
```

# Usage

1. Put in LinkedIn credentials in LinkedInt.cfg
2. Put Hunter.io API key in LinkedInt.cfg
3. Run LinkedInt.py and follow instructions (example below).

# Example

Using General Motors as the target as they have a bug bounty program.

```
██╗     ██╗███╗   ██╗██╗  ██╗███████╗██████╗ ██╗███╗   ██╗████████╗
██║     ██║████╗  ██║██║ ██╔╝██╔════╝██╔══██╗██║████╗  ██║╚══██╔══╝
██║     ██║██╔██╗ ██║█████╔╝ █████╗  ██║  ██║██║██╔██╗ ██║   ██║
██║     ██║██║╚██╗██║██╔═██╗ ██╔══╝  ██║  ██║██║██║╚██╗██║   ██║
███████╗██║██║ ╚████║██║  ██╗███████╗██████╔╝██║██║ ╚████║   ██║
╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝╚═╝  ╚═══╝   ╚═╝

Providing you with Linkedin Intelligence
Author: Vincent Yiu 2021
Update by leechuihui 19,May 2026
Original version by @DisK0nn3cT
[*] Enter search Keywords (use quotes for more precise results)
"General Motors"

[*] Enter filename for output (exclude file extension)
generalmotors

[*] Filter by Company? (Y/N):
Y

[*] Specify a Company ID (Provide ID or leave blank to automate):


[*] Enter e-mail domain suffix (eg. contoso.com):
gm.com

[*] Select a prefix for e-mail generation (auto,full,firstlast,firstmlast,flast,first.last,fmlast):
auto

[*] Automatically using Hunter IO to determine best Prefix
[!] {first}.{last}
[+] Found first.last prefix
```

Output (HTML):

![Output HTML Report](asset/htmlreport.png)
