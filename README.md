<p align="center">
  <img src="https://user-images.githubusercontent.com/23141800/121086278-a1291c00-c7eb-11eb-92dd-b2a0d75d97b5.png" alt="banner" />
</p>

**WeaponizeKali.sh** is a Bash script aimed at automating the process of downloading and installing extra tools for internal penetration tests with Kali Linux.

Basic principles behind this project are:

1. Use bleeding-edge versions of offensive toolkits to possess their latest features and fixes.
2. When installing 3rd party software, use isolated environments to minimize potential dependency hell.
3. Keep Windows exploitation scripts and binaries on hand in case you find yourself in an "offline situation".

The script will create two directories within CWD: `tools` and `www`. The [first](#tools) one contains all the tools that will be installed on Kali. The [second](#www) one contains all the scripts and binaries that will be downloaded and may be delivered onto the victim host later.

> **DISCLAIMER.** All information contained in this repository is provided for educational and research purposes only. The author is not responsible for any illegal misuse of this tool.

## Usage

WeaponizeKali.sh heavily relies on Python virtual environments and uses [pipx](https://pipxproject.github.io/pipx/) and [poetry](https://python-poetry.org/) to orchestra venvs.

In order to launch the bleeding-edge version of a tool installed with pipx and not the version that is already shipped with Kali, you should modify the `PATH` variables:

1. Modify `PATH` for a normal user with any method you want (`.bashrc` / `.profile` / `.zshrc` / etc.): `export PATH="$HOME/.local/bin:$PATH"`.
2. Modify `PATH` for the superuser by modifying `secure_path` within sudoers (`sudo visudo`):

![sudoers](https://user-images.githubusercontent.com/23141800/103461896-b5e02000-4d32-11eb-936e-6764ceae1372.png)

Now you can download WeaponizeKali.sh and run it from your home directory (pip may prompt for unlocking the keyring during the process). When it's done, you can check the results in `~/tools` and `~/www`:

```console
~$ cd
~$ bash <(curl -sL https://github.com/penetrarnya-tm/WeaponizeKali.sh/raw/main/WeaponizeKali.sh) -cidtw
~$ ls -la tools www
```

:warning: **Warning:** when using the `-i` switch, existing `./tools` and `./www` directories will be deleted.

If you only want to get the deliverable scripts and binaries (i.e., `www` directory), you can do it like this:

```console
~$ mkdir www
~$ bash <(curl -sL https://github.com/penetrarnya-tm/WeaponizeKali.sh/raw/main/WeaponizeKali.sh) -w
~$ ls -la www
```

It's recommended to run WeaponizeKali.sh **once** on a clean installation of Kali Linux.

### Rerun the Installations

To execute WeaponizeKali.sh with full set of arguments again after it has already been ran once, remove the existent virtual environments first and then run the script:

```console
~$ cd
~$ pipx uninstall-all
~$ sudo rm -rf ~/{.local/pipx,tools,www}
~$ ./WeaponizeKali.sh -cidtw
```

### Help

```
~$ ./WeaponizeKali.sh -h
                                                         )
 (  (                                                  ( /(       (                )
 )\))(   '   (     )                    (         (    )\())   )  )\ (          ( /(
((_)()\ )   ))\ ( /(  `  )    (    (    )\  (    ))\  ((_)\ ( /( ((_))\     (   )\())
_(())\_)() /((_))(_)) /(/(    )\   )\ )((_) )\  /((_) _ ((_))(_)) _ ((_)    )\ ((_)\
\ \((_)/ /(_)) ((_)_ ((_)_\  ((_) _(_/( (_)((_)(_))  | |/ /((_)_ | | (_)   ((_)| |(_
 \ \/\/ / / -_)/ _` || '_ \)/ _ \| ' \))| ||_ // -_) | ' < / _` || | | | _ (_-<| ' \
  \_/\_/  \___|\__,_|| .__/ \___/|_||_| |_|/__|\___| |_|\_\\__,_||_| |_|(_)/__/|_||_|
                     |_|
                           "the more tools you install, the more you are able to PWN"
                    { https://github.com/penetrarnya-tm/WeaponizeKali.sh } { vX.Y.Z }

usage: WeaponizeKali.sh [-h] [-i] [-d] [-t] [w]

optional arguments:
  -c                    use Docker when installing tools if possible
  -h                    show this help message and exit
  -i                    initialize filesystem (re-create ./tools and ./www directories)
  -d                    resolve dependencies
  -t                    download and install tools on Kali Linux
  -w                    download scripts and binaries for delivering onto the victim host
```

## Misc

### Evil-WinRM

Install the laster version of [Evil-WinRM](https://github.com/Hackplayers/evil-winrm) using `rbenv`:

```console
~$ zsh <(curl -sSL https://github.com/penetrarnya-tm/WeaponizeKali.sh/raw/sh/misc/evil-winrm.sh)
```

### PowerShellArmoury

Create armored `.ps1` scripts containing all the PowerShell tools you want with [PowerShellArmoury](https://github.com/cfalta/PowerShellArmoury):

```powershell
PS > git clone https://github.com/cfalta/PowerShellArmoury
PS > cd PowerShellArmoury
PS > curl https://github.com/penetrarnya-tm/WeaponizeKali.sh/raw/main/misc/PSArmoury.json -o PSArmoury.json
PS > . .\New-PSArmoury.ps1
PS > New-PSArmoury -ValidateOnly -Config PSArmoury.json
PS > New-PSArmoury -Path armored.ps1 -Config PSArmoury.json
PS > cat -raw .\armored.ps1 | iex
```

### Random Filenames

Get a random name of a `.exe` or `.dll` binary:

```console
~$ EXE="`curl -sL https://github.com/penetrarnya-tm/WeaponizeKali.sh/raw/main/misc/binaries.txt | shuf -n1`.exe"
~$ DLL="`curl -sL https://github.com/penetrarnya-tm/WeaponizeKali.sh/raw/main/misc/system32-dlls.txt | shuf -n1`.dll"
```

## Available Tools

### `tools/`

- [x] [APIHashReplace](https://github.com/matthewB-huntress/APIHashReplace)
- [x] [AutoBlue-MS17-010](https://github.com/3ndG4me/AutoBlue-MS17-010)
- [x] [Amsi-Bypass-Powershell](https://github.com/S3cur3Th1sSh1t/Amsi-Bypass-Powershell/blob/master/README.md)
- [x] [BloodHound](https://github.com/BloodHoundAD/BloodHound/releases) · [FORK](https://github.com/ly4k/BloodHound/releases)
- [x] [BloodHound.py](https://github.com/fox-it/BloodHound.py)
- [x] [CVE-2019-1040-scanner](https://github.com/fox-it/cve-2019-1040-scanner)
- [x] [CVE-2020-1472-checker](https://github.com/SecuraBV/CVE-2020-1472)
- [x] [CVE-2021-1675 (MS-RPRN)](https://github.com/cube0x0/CVE-2021-1675/blob/main/CVE-2021-1675.py) · [CVE-2021-1675 (MS-PAR)](https://github.com/cube0x0/CVE-2021-1675/blob/main/SharpPrintNightmare/CVE-2021-1675.py) · [CVE-2021-1675](https://github.com/m8sec/CVE-2021-34527/blob/main/CVE-2021-34527.py) · [SharpPrintNightmare](https://github.com/cube0x0/CVE-2021-1675/tree/main/SharpPrintNightmare)
- [x] [Certipy](https://github.com/ly4k/Certipy)
- [x] [Coercer](https://github.com/p0dalirius/Coercer)
- [x] [Covenant](https://github.com/cobbr/Covenant) · [Stageless_Covenant_HTTP.cs](https://gist.github.com/S3cur3Th1sSh1t/967927eb89b81a5519df61440357f945)
- [x] [CrackMapExec](https://github.com/Porchetta-Industries/CrackMapExec)
- [x] [DFSCoerce](https://github.com/Wh04m1001/DFSCoerce)
- [x] [DInjector](https://github.com/snovvcrash/DInjector)
- [x] [DLLsForHackers](https://github.com/Mr-Un1k0d3r/DLLsForHackers)
- [x] [DivideAndScan](https://github.com/snovvcrash/DivideAndScan)
- [x] [DonPAPI](https://github.com/login-securite/DonPAPI)
- [x] [Ebowla](https://github.com/Genetic-Malware/Ebowla)
- [x] [Empire](https://github.com/BC-SECURITY/Empire)
- [x] [InvisibilityCloak](https://github.com/h4wkst3r/InvisibilityCloak)
- [x] [ItWasAllADream](https://github.com/byt3bl33d3r/ItWasAllADream)
- [x] [LDAPPER](https://github.com/shellster/LDAPPER)
- [x] [LDAPmonitor](https://github.com/p0dalirius/LDAPmonitor)
- [x] [LdapRelayScan](https://github.com/zyn3rgy/LdapRelayScan)
- [x] [LightMe](https://github.com/WazeHell/LightMe)
- [x] [MS17-010](https://github.com/helviojunior/MS17-010)
- [ ] [MANSPIDER](https://github.com/blacklanternsecurity/MANSPIDER)
- [x] [Masky](https://github.com/Z4kSec/Masky) · [PS1 (Agent)](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/ps1/Invoke-Masky.ps1)
- [x] [Max](https://github.com/knavesec/Max)
- [x] [MeterPwrShell](https://github.com/GetRektBoy724/MeterPwrShell/releases)
- [x] [Neo-reGeorg](https://github.com/L-codes/Neo-reGeorg)
- [x] [Nim](https://nim-lang.org/install_unix.html) · [choosenim](https://github.com/dom96/choosenim)
- [x] [Nimcrypt2](https://github.com/icyguider/Nimcrypt2)
- [x] [NimlineWhispers](https://github.com/snovvcrash/NimlineWhispers)
- [x] [Obsidian](https://github.com/obsidianmd/obsidian-releases/releases)
- [x] [PCredz](https://github.com/snovvcrash/PCredz)
- [x] [PEzor](https://github.com/phra/PEzor)
- [x] [PKINITtools](https://github.com/dirkjanm/PKINITtools)
- [x] [PetitPotam](https://github.com/topotam/PetitPotam)
- [x] [PetitPotam-Ext](https://github.com/ly4k/PetitPotam)
- [x] [Physmem2profit](https://github.com/snovvcrash/physmem2profit) · [PS1](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/ps1/Invoke-Physmem2profit.ps1)
- [x] [PoshC2](https://github.com/nettitude/PoshC2)
- [x] [PrivExchange](https://github.com/dirkjanm/PrivExchange)
- [x] [Responder](https://github.com/lgandx/Responder)
- [x] [RustScan](https://github.com/RustScan/RustScan/releases)
- [x] [SCShell](https://github.com/Mr-Un1k0d3r/SCShell)
- [x] [ScareCrow](https://github.com/optiv/ScareCrow)
- [x] [ShadowCoerce](https://github.com/ShutdownRepo/ShadowCoerce)
- [x] [SharpGen](https://github.com/cobbr/SharpGen)
- [x] [ShellPop](https://github.com/0x00-0x00/ShellPop)
- [x] [Shhhloader](https://github.com/icyguider/Shhhloader)
- [x] [SilentHound](https://github.com/snovvcrash/SilentHound)
- [x] [Sliver](https://github.com/BishopFox/sliver)
- [x] [TrustVisualizer](https://github.com/snovvcrash/TrustVisualizer)
- [x] [WebclientServiceScanner](https://github.com/Hackndo/WebclientServiceScanner)
- [x] [Windows-Exploit-Suggester](https://github.com/a1ext/Windows-Exploit-Suggester)
- [ ] [ZeroTier](https://github.com/zerotier/ZeroTierOne)
- [x] [aced](https://github.com/garrettfoster13/aced)
- [ ] [ack3](https://github.com/beyondgrep/ack3)
- [x] [aclpwn.py](https://github.com/fox-it/aclpwn.py)
- [x] [adidnsdump](https://github.com/dirkjanm/adidnsdump)
- [x] [aquatone](https://github.com/michenriksen/aquatone/releases)
- [x] [arsenal](https://github.com/Orange-Cyberdefense/arsenal)
- [x] [bettercap](https://github.com/bettercap/bettercap/releases)
- [x] [bloodhound-import](https://github.com/fox-it/bloodhound-import)
- [x] [bloodhound-quickwin](https://github.com/kaluche/bloodhound-quickwin)
- [x] [bloodyAD](https://github.com/CravateRouge/bloodyAD)
- [x] [certi](https://github.com/zer1t0/certi)
- [x] [chisel](https://github.com/jpillora/chisel/releases) · [SharpChisel](https://github.com/shantanu561993/SharpChisel) · [EXE](https://github.com/Flangvik/SharpCollection/blob/master/NetFramework_4.0_Any/SharpChisel.exe)
- [x] [crowbar](https://github.com/galkan/crowbar)
- [x] [dementor.py](https://gist.github.com/3xocyte/cfaf8a34f76569a8251bde65fe69dccc#file-dementor-py)
- [x] [dnsx](https://github.com/projectdiscovery/dnsx/releases)
- [x] [donut](https://github.com/S4ntiagoP/donut/tree/syscalls)
- [x] [dsniff](https://github.com/tecknicaltom/dsniff)
- [x] [eavesarp](https://github.com/arch4ngel/eavesarp)
- [x] [enum4linux-ng](https://github.com/cddmp/enum4linux-ng)
- [x] [evil-winrm](https://github.com/Hackplayers/evil-winrm)
- [x] [feroxbuster](https://github.com/epi052/feroxbuster)
- [x] [ffuf](https://github.com/ffuf/ffuf/releases)
- [x] [gMSADumper](https://github.com/micahvandeusen/gMSADumper)
- [x] [gateway-finder-imp](https://github.com/whitel1st/gateway-finder-imp)
- [x] [go-windapsearch](https://github.com/ropnop/go-windapsearch) · [windapsearch.bin](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/elf/windapsearch)
- [x] [gobuster](https://github.com/OJ/gobuster/releases)
- [x] [hashcat-utils](https://github.com/hashcat/hashcat-utils)
- [x] [hoaxshell](https://github.com/t3l3machus/hoaxshell)
- [x] [http-server](https://github.com/http-party/http-server)
- [x] [httpx](https://github.com/projectdiscovery/httpx/releases)
- [x] [impacket](https://github.com/SecureAuthCorp/impacket) · [impacket-snovvcrash](https://github.com/snovvcrash/impacket)
- [x] [iCULeak.py](https://github.com/llt4l/iCULeak.py)
- [x] [ipmitool](https://github.com/ipmitool/ipmitool)
- [x] [kerbrute](https://github.com/ropnop/kerbrute/releases)
- [x] [krbrelayx](https://github.com/dirkjanm/krbrelayx)
- [x] [ldap_shell](https://github.com/PShlyundin/ldap_shell)
- [x] [ldapdomaindump](https://github.com/dirkjanm/ldapdomaindump)
- [x] [ldapsearch-ad](https://github.com/yaap7/ldapsearch-ad)
- [x] [ldeep](https://github.com/franc-pentest/ldeep)
- [x] [ligolo-proxy](https://github.com/tnpitsecurity/ligolo-ng)
- [x] [lsassy](https://github.com/Hackndo/lsassy)
- [x] [mapcidr](https://github.com/projectdiscovery/mapcidr)
- [x] [masscan](https://github.com/robertdavidgraham/masscan)
- [x] [mitm6](https://github.com/fox-it/mitm6)
- [x] [mscache](https://github.com/QAX-A-Team/mscache)
- [x] [nac_bypass-snovvcrash](https://github.com/snovvcrash/nac_bypass)
- [x] [nextnet](https://github.com/hdm/nextnet)
- [x] [nishang](https://github.com/samratashok/nishang)
- [x] [noPac](https://github.com/Ridter/noPac)
- [x] [ntlm-scanner](https://github.com/preempt/ntlm-scanner)
- [x] [ntlmv1-multi](https://github.com/evilmog/ntlmv1-multi)
- [x] [nullinux](https://github.com/m8r0wn/nullinux)
- [x] [odat](https://github.com/quentinhardy/odat)
- [x] [paperify](https://github.com/alisinabh/paperify)
- [x] [payloadGenerator](https://github.com/smokeme/payloadGenerator)
- [x] [powerview.py](https://github.com/aniqfakhrul/powerview.py)
- [x] [pretender](https://github.com/RedTeamPentesting/pretender/releases)
- [x] [pywsus](https://github.com/GoSecure/pywsus)
- [x] [pyGPOAbuse](https://github.com/Hackndo/pyGPOAbuse)
- [x] [pyKerbrute](https://github.com/3gstudent/pyKerbrute)
- [x] [pypykatz](https://github.com/skelsec/pypykatz)
- [x] [pywerview](https://github.com/the-useless-one/pywerview)
- [x] [pywhisker](https://github.com/ShutdownRepo/pywhisker)
- [x] [rbcd-attack](https://github.com/tothi/rbcd-attack)
- [x] [rbcd_permissions](https://github.com/NinjaStyle82/rbcd_permissions)
- [x] [rdp-tunnel](https://github.com/NotMedic/rdp-tunnel)
- [x] [rtfm](https://github.com/leostat/rtfm)
- [x] [sRDI](https://github.com/monoxgas/sRDI)
- [x] [seclists](https://github.com/danielmiessler/SecLists)
- [x] [sgn](https://github.com/EgeBalci/sgn/releases)
- [x] [smartbrute](https://github.com/ShutdownRepo/smartbrute)
- [x] [snmpwn](https://github.com/hatlord/snmpwn)
- [x] [spraykatz](https://github.com/aas-n/spraykatz)
- [x] [ssb](https://github.com/kitabisa/ssb/releases)
- [x] [sshspray](https://github.com/mcorybillington/sshspray)
- [x] [sshuttle](https://github.com/sshuttle/sshuttle)
- [x] [targetedKerberoast](https://github.com/ShutdownRepo/targetedKerberoast)
- [x] [ticket_converter](https://github.com/eloypgz/ticket_converter)
- [x] [traitor](https://github.com/liamg/traitor/releases)
- [x] [transfer.sh](https://github.com/dutchcoders/transfer.sh/releases)
- [x] [updog](https://github.com/sc0tfree/updog)
- [x] [webpage2html](https://github.com/snovvcrash/webpage2html)
- [x] [wesng](https://github.com/bitsadmin/wesng)
- [x] [windapsearch](https://github.com/ropnop/windapsearch)
- [x] [wmiexec-RegOut](https://github.com/XiaoliChan/wmiexec-RegOut)
- [ ] [xc](https://github.com/xct/xc)
- [x] [yersina](https://github.com/tomac/yersinia)

### `www/`

- [x] [ADCSPwn](https://github.com/bats3c/ADCSPwn) · [PS1](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/ps1/Invoke-ADCSPwn.ps1)
- [x] [ADRecon.ps1](https://github.com/adrecon/ADRecon/blob/master/ADRecon.ps1)
- [x] [ADSearch](https://github.com/tomcarver16/ADSearch) · [EXE](https://github.com/Flangvik/SharpCollection/blob/master/NetFramework_4.7_Any/ADSearch.exe)
- [x] [ASREPRoast.ps1](https://github.com/HarmJ0y/ASREPRoast/blob/master/ASREPRoast.ps1)
- [x] [AccessChk (Sysinternals)](https://docs.microsoft.com/en-us/sysinternals/downloads/accesschk) · [AccessChk (accepteula)](https://xor.cat/2017/09/05/sysinternals-accesschk-accepteula/)
- [x] [Certify](https://github.com/GhostPack/Certify) · [EXE](https://github.com/Flangvik/SharpCollection/blob/master/NetFramework_4.0_Any/Certify.exe)
- [x] [DDexec](https://github.com/arget13/DDexec)
- [x] [DefenderStop](https://github.com/dosxuz/DefenderStop)
- [x] [Discover-PSMSExchangeServers](https://github.com/PyroTek3/PowerShell-AD-Recon/blob/master/Discover-PSMSExchangeServers)
- [x] [Discover-PSMSSQLServers](https://github.com/PyroTek3/PowerShell-AD-Recon/blob/master/Discover-PSMSSQLServers)
- [x] [Divert](https://github.com/basil00/Divert) · [SYS](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/sysWinDivert64.sys)
- [x] [DomainPasswordSpray.ps1](https://github.com/dafthack/DomainPasswordSpray/blob/master/DomainPasswordSpray.ps1)
- [x] [Get-RdpLogonEvent.ps1](https://gist.github.com/awakecoding/5fda938a5fd2d29ebffb31eb023fe51c#file-get-rdplogonevent-ps1)
- [ ] [Grouper2](https://github.com/l0ss/Grouper2/releases)
- [x] [HandleKatz](https://github.com/codewhitesec/HandleKatz) · [PS1](https://gist.github.com/S3cur3Th1sSh1t/9f328fc411ff103c0800294c523503e2#file-invoke-handlekatzinject-ps1)
- [ ] [HiveNightmare](https://github.com/GossiTheDog/HiveNightmare/releases) · [ShadowSteal](https://github.com/HuskyHacks/ShadowSteal) · [EXE](https://github.com/FireFart/hivenightmare/blob/main/release/hive.exe)
- [x] [Intercept-NG](http://sniff.su/)
- [x] [Inveigh](https://github.com/Kevin-Robertson/Inveigh) · [PS1](https://github.com/Kevin-Robertson/Inveigh/blob/master/Inveigh.ps1) · [EXE](https://github.com/Flangvik/SharpCollection/blob/master/NetFramework_4.0_Any/Inveigh.exe)
- [x] [Invoke-ACLPwn.ps1](https://github.com/fox-it/Invoke-ACLPwn/blob/master/Invoke-ACLPwn.ps1)
- [x] [Invoke-ConPtyShell.ps1](https://github.com/antonioCoco/ConPtyShell/blob/master/Invoke-ConPtyShell.ps1)
- [x] [Invoke-ImpersonateUser-PTH.ps1](https://github.com/S3cur3Th1sSh1t/NamedPipePTH/blob/main/Invoke-ImpersonateUser-PTH.ps1)
- [x] [Invoke-PSInject.ps1](https://github.com/EmpireProject/PSInject/blob/master/Invoke-PSInject.ps1)
- [x] [Invoke-PatchWdigest.ps1](https://gist.github.com/snovvcrash/43e976779efdd20df1596c6492198c99#file-invoke-patchwdigestinject-ps1)
- [x] [Invoke-Portscan.ps1](https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/Invoke-Portscan.ps1)
- [x] [Invoke-RunasCs.ps1](https://github.com/antonioCoco/RunasCs/blob/master/Invoke-RunasCs.ps1)
- [x] [Invoke-SMBClient.ps1](https://github.com/Kevin-Robertson/Invoke-TheHash/blob/master/Invoke-SMBClient.ps1)
- [x] [Invoke-SMBEnum.ps1](https://github.com/Kevin-Robertson/Invoke-TheHash/blob/master/Invoke-SMBEnum.ps1)
- [x] [Invoke-SMBExec.ps1](https://github.com/Kevin-Robertson/Invoke-TheHash/blob/master/Invoke-SMBExec.ps1)
- [x] [Invoke-WMIExec.ps1](https://github.com/Kevin-Robertson/Invoke-TheHash/blob/master/Invoke-WMIExec.ps1)
- [x] [Invoke-noPac.ps1](https://gist.github.com/S3cur3Th1sSh1t/0ed2fb0b5ae485b68cbc50e89581baa6#file-invoke-nopac-ps1)
- [x] [JAWS](https://github.com/411Hall/JAWS/blob/master/jaws-enum.ps1)
- [x] [JuicyPotato64](https://github.com/ohpe/juicy-potato/releases) · [JuicyPotato32](https://github.com/ivanitlearning/Juicy-Potato-x86/releases)
- [x] [KSC-Console](https://www.kaspersky.ru/small-to-medium-business-security/downloads/endpoint)
- [x] [KeeThief](https://github.com/GhostPack/KeeThief) · [PS1](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/ps1/Invoke-KeeTheftSyscalls.ps1)
- [x] [KrbRelay](https://github.com/cube0x0/KrbRelay) · [EXE](https://github.com/Flangvik/SharpCollection/blob/master/NetFramework_4.7_Any/KrbRelay.exe)
- [x] [KrbRelayUp](https://github.com/Dec0ne/KrbRelayUp) · [EXE](https://github.com/Flangvik/SharpCollection/blob/master/NetFramework_4.7_Any/KrbRelayUp.exe)
- [x] [LaZagne](https://github.com/AlessandroZ/LaZagne/releases)
- [x] [MirrorDump](https://github.com/snovvcrash/MirrorDump) · [PS1](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/ps1/Invoke-MirrorDump.ps1)
- [x] [OffensivePythonPipeline](https://github.com/Qazeer/OffensivePythonPipeline/tree/main/binaries)
- [x] [Out-EncryptedScript.ps1](https://github.com/PowerShellMafia/PowerSploit/blob/master/ScriptModification/Out-EncryptedScript.ps1)
- [x] [PEASS](https://github.com/carlospolop/PEASS-ng/releases)
- [x] [PSTools](https://docs.microsoft.com/en-us/sysinternals/downloads/pstools)
- [x] [PingCastle](https://github.com/vletoux/pingcastle/releases)
- [x] [PowerShellArmoury](https://github.com/cfalta/PowerShellArmoury) · [PSArmoury.json](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/misc/PSArmoury.json)
- [x] [PowerUp.ps1](https://github.com/PowerShellMafia/PowerSploit/blob/master/Privesc/PowerUp.ps1)
- [x] [PowerUpSQL.ps1](https://github.com/NetSPI/PowerUpSQL/blob/master/PowerUpSQL.ps1)
- [x] [PowerView2.ps1](https://github.com/PowerShellEmpire/PowerTools/blob/master/PowerView/powerview.ps1)
- [x] [PowerView3.ps1](https://github.com/PowerShellMafia/PowerSploit/blob/26a0757612e5654b4f792b012ab8f10f95d391c9/Recon/PowerView.ps1) ([New-GPOImmediateTask](https://www.harmj0y.net/blog/redteaming/abusing-gpo-permissions/))
- [x] [PowerView3.ps1](https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1)
- [x] [PowerView4.ps1](https://github.com/ZeroDayLab/PowerSploit/blob/master/Recon/PowerView.ps1) (by [@exploitph](https://exploit.ph/powerview.html))
- [x] [Powermad.ps1](https://github.com/Kevin-Robertson/Powermad/blob/master/Powermad.ps1)
- [x] [PrivescCheck.ps1](https://github.com/itm4n/PrivescCheck/blob/master/PrivescCheck.ps1)
- [x] [PrintSpoofer](https://github.com/itm4n/PrintSpoofer)
- [x] [PwnKit](https://github.com/ly4k/PwnKit/blob/main/PwnKit)
- [x] [Python 2.7.18](https://www.python.org/downloads/release/python-2718/)
- [x] [RawCopy](https://github.com/jschicht/RawCopy/blob/master/RawCopy64.exe)
- [x] [RemotePotato0](https://github.com/antonioCoco/RemotePotato0/releases)
- [x] [RoguePotato](https://github.com/antonioCoco/RoguePotato)
- [x] [RestrictedAdmin](https://github.com/GhostPack/RestrictedAdmin) · [PS1](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/ps1/Invoke-RestrictedAdmin.ps1)
- [x] [Rubeus](https://github.com/GhostPack/Rubeus) · [EXE](https://github.com/r3motecontrol/Ghostpack-CompiledBinaries/blob/master/Rubeus.exe)
- [x] [RunOF](https://github.com/nettitude/RunOF) · [PS1](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/ps1/Invoke-RunOF.ps1)
- [x] [SandboxDefender](https://github.com/plackyhacker/SandboxDefender) · [EXE](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/exe/SandboxDefender.exe)
- [x] [Seatbelt](https://github.com/GhostPack/Seatbelt) · [EXE](https://github.com/r3motecontrol/Ghostpack-CompiledBinaries/blob/master/Seatbelt.exe)
- [x] [SessionGopher.ps1](https://github.com/Arvanaghi/SessionGopher/blob/master/SessionGopher.ps1)
- [x] [SharpChrome](https://github.com/GhostPack/SharpDPAPI/tree/master/SharpChrome) · [EXE](https://github.com/r3motecontrol/Ghostpack-CompiledBinaries/blob/master/SharpChrome.exe)
- [x] [SharpDPAPI](https://github.com/GhostPack/SharpDPAPI/tree/master/SharpDPAPI) · [EXE](https://github.com/r3motecontrol/Ghostpack-CompiledBinaries/blob/master/SharpDPAPI.exe)
- [x] [SharpGPOAbuse](https://github.com/FSecureLABS/SharpGPOAbuse) · [EXE](https://github.com/Flangvik/SharpCollection/blob/master/NetFramework_4.0_Any/SharpGPOAbuse.exe)
- [x] [SharpHandler](https://github.com/jfmaes/SharpHandler) · [EXE](https://github.com/Flangvik/SharpCollection/blob/master/NetFramework_4.0_Any/SharpHandler.exe)
- [x] [SharpHound](https://github.com/BloodHoundAD/SharpHound/releases)
- [x] [SharpLAPS](https://github.com/swisskyrepo/SharpLAPS/releases)
- [x] [SharpNamedPipePTH](https://github.com/S3cur3Th1sSh1t/SharpNamedPipePTH) · [EXE](https://github.com/Flangvik/SharpCollection/blob/master/NetFramework_4.0_Any/SharpNamedPipePTH.exe) · [PS1](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/ps1/Invoke-SharpNamedPipePTH.ps1)
- [x] [SharpRDP](https://github.com/0xthirteen/SharpRDP) · [EXE](https://github.com/Flangvik/SharpCollection/blob/master/NetFramework_4.5_Any/SharpRDP.exe)
- [x] [SharpRdpThiefInjector](https://github.com/snovvcrash/SharpRdpThief) · [PS1](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/ps1/Invoke-SharpRdpThiefInjector.ps1)
- [x] [SharpRelay](https://github.com/pkb1s/SharpRelay) · [EXE](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/exe/SharpRelay.exe)
- [x] [SharpSCCM](https://github.com/Mayyhem/SharpSCCM) · [PS1](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/ps1/Invoke-SharpSCCM.ps1)
- [x] [SharpSecDump](https://github.com/G0ldenGunSec/SharpSecDump) · [EXE](https://github.com/Flangvik/SharpCollection/blob/master/NetFramework_4.0_Any/SharpSecDump.exe)
- [x] [SharpStrike](https://github.com/iomoath/SharpStrike) · [EXE (Console)](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/exe/SharpStrike.exe) · [EXE (GUI)](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/exe/SharpStrikeGUI.exe)
- [x] [SharpSystemTriggers](https://github.com/cube0x0/SharpSystemTriggers) · [PS1](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/ps1/Invoke-SharpSpoolTrigger.ps1)
- [x] [SharpView](https://github.com/tevora-threat/SharpView) · [EXE](https://github.com/tevora-threat/SharpView/blob/master/Compiled/SharpView.exe)
- [x] [SharpWMI](https://github.com/GhostPack/SharpWMI) · [EXE](https://github.com/Flangvik/SharpCollection/blob/master/NetFramework_4.0_Any/SharpWMI.exe)
- [x] [SharpWebServer](https://github.com/Flangvik/SharpCollection/blob/master/NetFramework_4.0_Any/SharpWebServer.exe)
- [x] [Sherlock.ps1](https://github.com/rasta-mouse/Sherlock/blob/master/Sherlock.ps1)
- [x] [Snaffler](https://github.com/SnaffCon/Snaffler/releases)
- [x] [SpoolSample](https://github.com/leechristensen/SpoolSample/) · [EXE](https://github.com/BlackDiverX/WinTools/blob/master/SpoolSample-Printerbug/SpoolSample.exe)
- [x] [StandIn](https://github.com/FuzzySecurity/StandIn) · [EXE](https://github.com/Flangvik/SharpCollection/blob/master/NetFramework_4.0_Any/StandIn.exe)
- [x] [VeraCryptThiefInjector](https://github.com/snovvcrash/VeraCryptThief) · [PS1](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/ps1/Invoke-VeraCryptThiefInjector.ps1)
- [x] [WerTrigger](https://github.com/sailay1996/WerTrigger)
- [x] [WinPwn](https://github.com/S3cur3Th1sSh1t/WinPwn) · [PowerSharpPack](https://github.com/S3cur3Th1sSh1t/PowerSharpPack/tree/master/PowerSharpBinaries) · [Creds](https://github.com/S3cur3Th1sSh1t/Creds)
- [x] [Wireshark](https://www.wireshark.org/download.html)
- [x] [arpfox](https://github.com/malfunkt/arpfox/releases)
- [x] [chisel](https://github.com/jpillora/chisel/releases)
- [x] [les.sh](https://github.com/mzet-/linux-exploit-suggester/blob/master/linux-exploit-suggester.sh)
- [x] [lse.sh](https://github.com/diego-treitos/linux-smart-enumeration/blob/master/lse.sh)
- [x] [mimikatz](https://github.com/gentilkiwi/mimikatz/releases)
- [x] [nanodump](https://github.com/helpsystems/nanodump/tree/main/dist) · [PS1](https://gist.github.com/snovvcrash/5487fc83a3c878eaa07c0ca30b709c30#file-invoke-nanodumpsspinject-ps1)
- [x] [netcat for Windows](https://eternallybored.org/misc/netcat/)
- [x] [pamspy](https://github.com/citronneur/pamspy/releases)
- [x] [plink](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
- [x] [powercat.ps1](https://github.com/besimorhino/powercat/blob/master/powercat.ps1)
- [x] [pspy](https://github.com/DominicBreuker/pspy/releases)
- [x] [rdp-tunnel](https://github.com/NotMedic/rdp-tunnel) · [rdp2tcp.exe](https://github.com/NotMedic/rdp-tunnel/blob/master/rdp2tcp.exe)
- [x] [revsocks](https://github.com/kost/revsocks/releases)
- [x] [static-binaries](https://github.com/andrew-d/static-binaries)
- [x] [suid3num.py](https://github.com/Anon-Exploiter/SUID3NUM/blob/master/suid3num.py)
- [x] [tokenduplicator](https://github.com/magnusstubman/tokenduplicator) · [PS1](https://github.com/penetrarnya-tm/WeaponizeKali.sh/blob/main/ps1/Invoke-TokenDuplicator.ps1)
