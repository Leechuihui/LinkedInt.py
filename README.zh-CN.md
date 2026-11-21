[English](README.md) | **简体中文**

# 🔗 LinkedInt.py

[![Python](https://img.shields.io/badge/Python-3.8%2B-3fb950?logo=python&logoColor=white)](https://python.org)
[![LinkedIn](https://img.shields.io/badge/Source-LinkedIn-0A66C2?logo=linkedin&logoColor=white)](https://linkedin.com)
[![Tor Ready](https://img.shields.io/badge/Network-Tor_Ready-8b5cf6?logo=tor-project&logoColor=white)](https://torproject.org)

[vysecurity/LinkedInt](https://github.com/vysecurity/LinkedInt) 的分支 — LinkedIn OSINT 枚举工具，2026 年更新。

<p align="center">
<img src="https://github.com/vysecurity/LinkedInt/blob/master/asset/linkedint.png?raw=true">
</p>

# 免责声明

* 本项目仅用于教育和测试目的。

# 作者

* 由 Leechuihui 开发更新至 2.0 版本

贡献者：

* Leesoh
* harshil-shah004

# 安装
```
git clone https://github.com/Leechuihui/LinkedInt.py.git
cd LinkedInt.py
pip install -r requirements.txt
```

# 用法

1. 在 LinkedInt.cfg 中填入 LinkedIn 凭据
2. 在 LinkedInt.cfg 中填入 Hunter.io API 密钥
3. 运行 LinkedInt.py 并按提示操作（示例如下）。

# 示例

以通用汽车（General Motors）为目标，因为它设有漏洞赏金计划。

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

输出（HTML）：

![Output HTML Report](asset/htmlreport.png)
