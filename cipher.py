from easy_functions import Cipher, find_file
from sys import argv
from sys import exit as _exit
from tkinter import Tk
from tkinter import messagebox as msg

Tk().withdraw()
l = Cipher()

__version__ = '0.2.10'

def _help():
    h = """加密或解密一个文件。\n
cipher [--lock filename_in | --unlock filename_in [--echo | [filename_out]]] [--version]

    没有参数                    显示帮助。这和键入 /? 是一样的。
    /?                          显示帮助。这和不键入任何选项是一样的。
    --version                   显示版本号。
    --lock   filename_in        加密一个文件。
    --unlock filename_in        解密一个文件。
    --echo                      开启后不用输出文件，直接显示解密文字。
    [filename_out]              加密/解密后输出的文件名或路径，可以使用echo参数代替。
    """
    print(h)
    
try:
    tmp = argv[1]
except IndexError:
    _help()
    _exit(2)
else:
    if argv[1] == '/?':
        _help()
        _exit(1)
    elif argv[1] == '--version':
        print('cipher.exe v%s'%__version__)
        _exit(1)
try:
    tmp = argv[2]
except IndexError:
    print('无效语法。\n')
    _help()
    _exit(2)
try:
    tmp = argv[3]
except IndexError:
    print('无效语法。\n')
    _help()
    _exit(2)
    
if not find_file(argv[2],'exist?'):
    msg.showerror('错误','找不到文件 "%s"。\n请确认文件名是否正确后，再试一次。'%argv[2])
    print('系统找不到文件 %s。'%argv[2])
    _exit(2)
    
if argv[2] == argv[3]:
    msg.showwarning('无法新建文件','出于对文件的安全考虑，本程序不允许输入文件与输出文件相同。\n请更换一个文件名后，再试一次。')
    print('文件覆盖保护。')
    _exit(2)
    
if argv[3] == '--echo':
    with open(argv[2],'r') as f:
        print(l.unlock(f.read()))
        _exit(1)
    
if argv[1] == '--lock':
    with open(argv[2],'r') as f:
        with open(argv[3],'w') as r:
            r.write(l.lock(f.read()))
elif argv[1] == '--unlock':
    with open(argv[2],'r') as f:
        with open(argv[3],'w') as r:
            r.write(l.unlock(f.read()))
else:
    msg.showerror('错误','找不到此参数。\n请确认参数名是否正确后，再试一次。')
    print('系统找不到名为 "%s" 的参数。'%argv[1])
    _exit(2)