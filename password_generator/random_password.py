from tkinter import *
import random
import string
root=Tk()
root.title("Random Password Generatorr")
root.geometry('1600x700')

number=IntVar()
digit=StringVar()
special=StringVar()

topframe=Frame(root,width=1600,height=50)
bottomframe=Frame(root,width=1600,height=50)
leftframe=Frame(root,width=900,height=700)
rightframe=Frame(root,width=900,height=700)


topframe.pack(side=TOP)
bottomframe.pack(side=BOTTOM)
leftframe.pack(side=LEFT)
rightframe.pack(side=RIGHT)

def password():
    allchar=string.ascii_letters
    password_length=number.get()
    include_digit=digit.get()=='yes'
    include_char=special.get()=='yes'
    if include_digit:
        allchar+=string.digits
    if include_char:
        allchar+=string.punctuation

    generated_pass=''.join(random.choices(allchar,k=password_length))
    entry2.insert(0,generated_pass)

def reset():
    entry2.delete(0, END)
    number.set("")
    entry3.delete(0, END)
    entry4.delete(0, END)

label1=Label(topframe,text="Enter length of password",font=('Times New Roman',18,'bold'))
label1.grid(row=0,column=0)
entry1=Entry(topframe,font=('Times New Roman',18,'bold'),textvariable=number,borderwidth=6,bg="#B8B8AA")
entry1.grid(row=0,column=1)
number.set(" ")
label3=Label(topframe,text="You want numbers in your password (yes/no):",font=('Times New Roman',18,'bold'))
label3.grid(row=1,column=0)
entry3=Entry(topframe,font=('Times New Roman',18,'bold'),textvariable=digit,borderwidth=6,bg="#B8B8AA")
entry3.grid(row=1,column=1)
label4=Label(topframe,text="You want special characters in your password (yes/no):",font=('Times New Roman',18,'bold'))
label4.grid(row=2,column=0)
entry4=Entry(topframe,font=('Times New Roman',18,'bold'),textvariable=special,borderwidth=6,bg="#B8B8AA")
entry4.grid(row=2,column=1)
label2=Label(topframe,text="Your Password Is:",font=('Times New Roman',18,'bold'),borderwidth=6)
label2.grid(row=3,column=0)
entry2=Entry(topframe,font=('Times New Roman',18,'bold'),borderwidth=6,bg="#B8B8AA")
entry2.grid(row=3,column=1)
button1=Button(topframe,text="Submit",command=password,borderwidth=6)
button1.grid(row=4,column=0)
button2=Button(topframe,text="Reset",command=reset,borderwidth=6)
button2.grid(row=4,column=1)


root.mainloop()
