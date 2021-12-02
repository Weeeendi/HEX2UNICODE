import tkinter as tk
import tkinter.messagebox
from tkinter.constants import BOTH, E, END, INSERT, LEFT, N, TOP, W, X, YES
from typing import Text
import UnicodeTohex as UT
import traceback
#first craet a new window
windows = tk.Tk()

#take a name for this windows
windows.title("Unicode and Hex translate")

#set window size for GUI
windows.geometry('500x300')

fm1 = tk.Frame()
fm2 = tk.Frame()
fm3 = tk.Frame()


# 第4步，在图形界面上设定标签
varFIRST_CODE = tk.StringVar()
varSECOND_CODE = tk.StringVar()
FIRST_CODE = tk.Label(fm1, textvariable=varFIRST_CODE,height=2,bg='white', font=('Courier New', 12))
SECOND_CODE = tk.Label(fm3,  textvariable=varSECOND_CODE,height=2,bg='white', font=('Courier New', 12))

varFIRST_CODE.set('HEX')
varSECOND_CODE.set('STRING')

# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高


# 第4步，在图形界面上设定输入框控件entry并放置控件
#Edit1 = tk.Text(fm1, show='*', font=('Courier New', 12))   # 显示成密文形式
Edit1 = tk.Text(fm1,width=20, height=5, undo = True,font=("微软雅黑",10))
#Edit2 = tk.Text(fm3, show=None, font=('Courier New', 12))  # 显示成明文形式
Edit2 = tk.Text(fm3,width=20, height=5, undo = True,font=("微软雅黑",10))

Edit1.insert(INSERT, 'Input text at here......')

Edit1.configure(fg='grey')  # 修改字体颜色，修改其它参数只需要传入对应的参数即可


'''
鼠标点击事件
<Button-1>  鼠标左键
<Button-2>   鼠标中间键（滚轮）
<Button-3>  鼠标右键
<Double-Button-1>   双击鼠标左键
<Double-Button-3>   双击鼠标右键
<Triple-Button-1>   三击鼠标左键
<Triple-Button-3>   三击鼠标右键
'''

def TransfromA2B():
    var= Edit1.get('1.0',END)
    Edit2.delete('1.0',END)
    if(varFIRST_CODE.get()=="HEX"):
        var2 = UT.Hex2Unicode(var)
    else:
        #varTemp=var.encode('unicode_escape').decode('utf-8') 
        try:
            varTemp = bytes(var,encoding='utf_16_be').hex()  
        except Exception as e:
            traceback.print_exc()
        var2 = UT.Unicode2Hex(varTemp)
    if var2 == None:
        tkinter.messagebox.showinfo(title='Topic', message='Please enter the correct content')            # 提示信息对话窗
        return
    Edit2.insert(INSERT,var2)
    print(var)

def back():
    Edit1.edit_undo()


def callback():
    Edit1.edit_redo()

def exchange_code():
    temp = varFIRST_CODE.get()
    varFIRST_CODE.set(varSECOND_CODE.get()) 
    varSECOND_CODE.set(temp)
    return

Translate_Button = tk.Button(fm2,text='Translate →',width=10,height=2,command=TransfromA2B,bg="pink")
exchange_button = tk.Button(fm2,text='← exchange →',width=5,height=2,command=exchange_code)
back_button= tk.Button(fm2,text='◀Undo',width=5,height=2,command=back)
callback_button= tk.Button(fm2,text='Redo▶',width=5,height=2,command=callback)

#右键 剪切复制黏贴
def callback1(event=None):
    global root
    Edit1.event_generate('<<Cut>>')
    Edit2.event_generate('<<Cut>>')
    
def callback2(event=None):
    global root
    Edit1.event_generate('<<copy>>')
    Edit2.event_generate('<<copy>>')
    
def callback3(event=None):
    global root
    Edit1.event_generate('<<Paste>>')
    Edit2.event_generate('<<Paste>>')

def callback4(event=None):
    global root
    Edit1.event_generate('<<Paste>>')
    Edit2.event_generate('<<Paste>>')

'''创建一个弹出菜单'''
menu = tk.Menu(windows,
            tearoff=False,
            #bg="grey",
            )
menu.add_command(label="Cut", command=callback1)
menu.add_command(label="Copy", command=callback2)
menu.add_command(label="Paste", command=callback3)

def popup(event):
    menu.post(event.x_root, event.y_root)   # post在指定的位置显示弹出菜单

Edit_firstClike = 1

def clearEdit(event):
    global Edit_firstClike    
    if(Edit_firstClike):
        Edit1.delete('1.0',END)
        Edit1.configure(fg='black')  # 修改字体颜色，修改其它参数只需要传入对应的参数即可
        Edit_firstClike = 0



Edit1.bind("<Button-3>", popup)                 # 绑定鼠标右键,执行popup函数
Edit2.bind("<Button-3>", popup)                 # 绑定鼠标右键,执行popup函数
 
Edit1.bind("<Button-1>",clearEdit)              # 绑定鼠标左键,执行clearEdit函数


#Frame1
FIRST_CODE.pack(side=TOP,anchor=W,fill=X,expand=N)
Edit1.pack(side=TOP,anchor=W,fill=BOTH,expand=YES)

#Frame2
exchange_button.pack(side=TOP,anchor=W,fill=X,expand=N)
Translate_Button.pack(side=TOP,anchor=W,fill=BOTH,expand=YES)
back_button.pack(side=LEFT,anchor=W,fill=X,expand=YES)
callback_button.pack(side=LEFT,anchor=W,fill=X,expand=YES)

#Frame3
SECOND_CODE.pack(side=TOP,anchor=W,fill=X,expand=N)
Edit2.pack(side=TOP,anchor=W,fill=BOTH,expand=YES)

fm1.pack(side=LEFT, fill=BOTH, expand=YES)
fm2.pack(side=LEFT, fill=BOTH, expand=YES)
fm3.pack(side=LEFT, fill=BOTH, expand=YES)
# 第6步，主窗口循环显示
windows.mainloop()