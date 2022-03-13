# cipher
一个简单的命令行程序，可以将输入的英文加密

    cipher [--lock | --unlock] [filename_in] [--echo | filename_out]
    
        没有参数      显示帮助。这和键入 /? 是一样的。
        /?            显示帮助。这和不键入任何选项是一样的。
        version       显示版本号。
        lock          加密一个文件。
        unlock        解密一个文件。
        filename_in   被加密/解密的文件名或路径。
        echo          开启后不用输出文件，直接显示解密文字。
        filename_out  加密/解密后输出的文件名或路径，可以使用echo参数代替。
