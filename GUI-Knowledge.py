from tkinter import *
from tkinter import ttk #theme od tk
from tkinter import messagebox

GUI = Tk() #นี่คือหน้าจอหลักของโปรอแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อโปรแกรม
GUI.geometry('600x400') #นี่คือขนาดโปรแกรม

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green') #Angsana New
L1.place(x=175,y=20)

L1 = Label(GUI,text='By Kunsin Kosai',font=('Angsana New',20),fg='blue') #Saraban Bold
L1.place(x=180,y=70)
#####################
#B1 = ttk.Button(GUI,text='มีเงินอยู่กี่บาท')
#B1.pack(ipadx=20,ipady=20)

####################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชี 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)
    #warning
    #info
    #error

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=230,y=150) 
B2 = ttk.Button(FB1,text='มีเงินอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=15)
####################

def Button3():
    text = 'Python 101, Math'
    messagebox.showwarning('วิชาเรียนวันที่ 10-20 ก.พ.',text)
    #warning
    #info

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=230,y=170)
B3 = ttk.Button(FB1,text='สัปดาห์เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=15)
####################

def Button4():
    text = 'Yellow'
    messagebox.showwarning('สี',text)
    #warning
    #info

FB3 = Frame(GUI) #คล้ายกระดาน
FB3.place(x=230,y=170)
B4 = ttk.Button(FB1,text='อย่างสีเหลือง',command=Button4)
B4.pack(ipadx=20,ipady=15)
####################

def Button5():
    text = 'เด็กขี้งอแง'
    messagebox.showerror('อาการ',text)
    #warning
    #info

FB4 = Frame(GUI) #คล้ายกระดาน
FB4.place(x=230,y=170)
B5 = ttk.Button(FB1,text='แก้มเหม่ง',command=Button5)
B5.pack(ipadx=20,ipady=15)
####################

GUI.mainloop()
