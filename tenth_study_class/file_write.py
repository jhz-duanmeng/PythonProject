"""
open()参数：model：r 代表读取
                  w 代表写入(会清空文件原内容)
                  a 代表附加
                  r+ 代表读取和写入（会清空文件原内容）
"""

filename = "papijiang"
with open(filename, "a") as files:
    files.write("我日天，五年开发经验，今天我就要70k，没唬住，只要了7k！\n")
    files.write("窝草\n")

