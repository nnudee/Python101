from tkinter import *
from tkinter import ttk # theme of tk
from tkinter import messagebox

GUI = Tk() #หน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x400') #ขนาดโปรแกรม

L1 = Label(GUI, text='โปรแกรมบันทึกความรู้', font=('Angsana New',30),fg ='Green')
L1.place(x=30,y=20)
##########################
def button1():
    text = 'ตอนนี้มีเงินเหลือ 20 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=button1) #่มีttk
B2.pack(ipadx=20,ipady=20)
##########################
def button2():
    text = 'Python101 , Math'
    messagebox.showinfo('วิชาที่เรียนวันนี้',text)

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=100,y=180)
B2 = Button(FB2,text='วิชาที่เรียนวันนี',command=button2) #ไม่มีttk
B2.pack(ipadx=20,ipady=20)

GUI.mainloop()

