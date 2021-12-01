from tkinter.constants import INSERT, NONE
from tkinter.messagebox import OK
from typing import Text
import string
import traceback
"""
#小端字节序转为大端字节序
def little2big_endian(hex_string):
	big_endian_str = '' #定义一个空字符串
	for i in range(int(len(hex_string)/4)):#因为Unicode是4个字符表示一个汉字，每四个一组
		little_endian_char = hex_string[i*4: i*4+4] #取的是四位连续的数字
		big_endian_char = little_endian_char[2:4] + little_endian_char[0:2] #逆字节序
		big_endian_str = big_endian_str + big_endian_char
	return big_endian_str
 
#十六进制数字(大端序)转换成汉字(unicode编码)
def HextoHanzi(hex_string):
	unicode_Hanzi = '' #定义一个空字符串
	for i in range(int(len(hex_string)/4)): #因为Unicode是4个字符表示一个汉字，每四个一组
		Hex_char = hex_string[i*4: i*4+4]
		unicode_char = "\\u" + Hex_char
		unicode_Hanzi = unicode_Hanzi + unicode_char
	return unicode_Hanzi.encode().decode('unicode_escape')

hex_string = input("input hex:")
big_endian_str = little2big_endian(hex_string)
print(HextoHanzi(big_endian_str))


"""


def delSpace(s):
    s1 = s.split()
    s2 = "".join(s1)
    if (len(s2)%4)!=0 or len(s2)==0:
        return None
    Hexlist = '' #定义一个空字符串
    for i in range(int(len(s2)/4)):
            Hex_2char = s2[(i*4): (i*4+4)]
            little_endian_char = Hex_2char[2:4]+Hex_2char[0:2]
            Hexlist+=little_endian_char
    
    return Hexlist

    
   
    return s2

def insert_single(list,single,interval):
    i = 0
    if(all(c in string.hexdigits for c in list)):
        while(i<len(list)):
            list.insert(i,single)
            i+=(interval+1)
        return OK
    return None



def Hex2Unicode(hexStr):
    # hexStr = input("input hex:")
    hexStrNospace = delSpace(hexStr)
    if(hexStrNospace == None):
        return hexStrNospace
    try:
        Conevt_hexStr = list(hexStrNospace)
    except Exception as e:
        traceback.print_exc()
        return NONE
    REG = insert_single(Conevt_hexStr,r"\u",4)
    if(REG != OK):
        return REG
    hexStr2 = ''.join(Conevt_hexStr)    

    return hexStr2.encode().decode('unicode_escape')

def Unicode2Hex(UnicodeStr):
    unicode_Hex = '' #定义一个空字符串
    for i in range(int(len(UnicodeStr)/4)):
        Unicode_char = UnicodeStr[(i*4): (i*4+4)]
        big_endian_char = Unicode_char[2:4]+" "+Unicode_char[0:2]+" "
        unicode_Hex += big_endian_char
    return unicode_Hex
#TestSTR = "56 00 6F 00 69  00 63 00 65 00 20 00 63  00 61 00 6C 00 6C 00 20   00 69 00 6E 00 20 00 75 00 73 00 65 00  "   £TestSTR = Hex2Unicode()
#print(TestSTR)
