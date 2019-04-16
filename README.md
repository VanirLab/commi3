<p align="center">
  <img alt="VanirLab" src="https://github.com/VanirLab/commi3/blob/master/commi3.png" height="142" />
  <p align="center">
    <a href="https://api.travis-ci.org/VanirLab/commi3"><img alt="Build Status" src="https://api.travis-ci.org/VanirLab/commi3.svg?branch=master"></a>
    <a href="https://github.com/VanirLab/commi3/releases/tag/><img alt="Version 1.0" src="https://img.shields.io/badge/Version-1.0-green.svg"></a>
    <a href="http://www.python.org/download/"><img alt="Python 3.6-3.7" src="https://img.shields.io/badge/Python-3.6--3.7-yellow.svg"></a>
    <a href="https://github.com/VanirLab/commi3/blob/master/readme/COPYING"><img alt="MIT License" src="https://img.shields.io/badge/License-MIT-red.svg"></a>

  </p>
</p>

## General Information

**Commi3** (short for [**c**]ryptoanalytic [**o**]ffensive [**m**]ultifunctional [**m**]icrostructure  [**i**]njection [**3**] generation 3) is an Automated Command Line Tool   (ACLT)
that can be used from web developers, penetration testers or even security researchers in order to test web-based applications 
with the view to find bugs, errors or vulnerabilities related to **[command injection](https://www.owasp.org/index.php/Command_Injection)** attacks.
 By using this tool, it is very easy to find and exploit a command injection vulnerability in a certain vulnerable parameter or HTTP/HTTPS header.

## Legal Disclaimer

**With each commi3 run end users are obligated to agree** with the following prelude message:
```
(!) Legal disclaimer: Usage of Commi3 for attacking targets without prior mutual consent is illegal. 
It is the end user's responsibility to obey all applicable local, state and federal laws. 
Developers assume no liability and are not responsible for any misuse or damage caused by this program.
```

## Requirements

**[Python](http://www.python.org/download/)** version **3.6.x** or **3.7.x** is required for running this program.

```python
pip install -r requirements.txt

```


## Installation

Download commi3 by cloning the Git repository:

    git clone https://github.com/VanirLab/commi3.git commi3

Commi3 comes packaged on the **official repositories** of the following Linux distributions, so you can use the **package manager** to install it!

- [ArchStrike](https://archstrike.org/)
- [BlackArch Linux](http://blackarch.org/)
- [BackBox](https://backbox.org/)
- [Kali Linux](https://www.kali.org/)
- [Parrot Security OS](https://www.parrotsec.org/)
- [Pentoo Linux](https://www.pentoo.ch/)
- [Weakerthan Linux](http://www.weaknetlabs.com/)

Commi3 also comes **as a plugin**, on the following penetration testing frameworks:

- [TrustedSec's Penetration Testers Framework (PTF)](https://github.com/trustedsec/ptf)
- [OWASP Offensive Web Testing Framework (OWTF)](https://github.com/owtf/owtf)
- [CTF-Tools](https://github.com/zardus/ctf-tools)
- [PentestBox](https://tools.pentestbox.com/)
- [PenBox](https://github.com/x3omdax/PenBox)
- [Katoolin](https://github.com/LionSec/katoolin)
- [Aptive's Penetration Testing tools](https://github.com/Aptive/penetration-testing-tools)
- [Homebrew Tap - Pen Test Tools ](https://github.com/sidaf/homebrew-pentest)

## Supported Platforms

- Linux
- Mac OS X
- Windows

## Plugins: 
- Inject python code in Commi3 for custom exploits
```python

{
    '0x000001': <module: 'my_new_exploit'>,
    '0x000023': <module: 'my_updated_exploit'>,
}

```

## Usage

To get a list of all options and switches use:

    python commi3.py -h & python3 commi3.py -h
	
