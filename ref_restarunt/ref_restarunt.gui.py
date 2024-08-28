from tkinter import *
import cx_Oracle
import datetime
import mysql.connector
root=Tk()
root.title("Restarunt Management")
root.geometry('1600x700')
# connection = cx_Oracle.connect(user="hr", password="hr",dsn="localhost/xe")
connection = mysql.connector.connect(
    user="root",
    password="prabhu@33",
    host="localhost",
    database="restarunt"
)

cursor=connection.cursor()
#--------for current time-----------
local=datetime.datetime.now()

topframe=Frame(root,width=1600,height=50)
bottomframe=Frame(root,width=1600,height=50)
leftframe=Frame(root,width=900,height=700)
rightframe=Frame(root,width=900,height=700)


topframe.pack(side=TOP)
bottomframe.pack(side=BOTTOM)
leftframe.pack(side=LEFT)
rightframe.pack(side=RIGHT)

fries=IntVar()
burger=IntVar()
pizza=IntVar()
drink=IntVar()
chicken=IntVar()
taxcost=IntVar()
totalcost=IntVar()


label=Label(topframe,text="Restarunt Management System",font=('aria',25,'bold'))
label.grid(row=0,column=0)
label=Label(topframe,text=local,font=('aria',25,'bold'))
label.grid(row=1,column=0)

def clear():
    fries.set("")
    burger.set("")
    pizza.set("")
    drink.set("")
    chicken.set("")
    taxcost.set("")
    totalcost.set("")


def exit():
    root.destroy()

def enter():
    fri=float(fries.get())
    bur=float(burger.get())
    piz=float(pizza.get())
    dri=float(drink.get())
    chik=float(chicken.get())

    costoffries=fri*25
    costofburger=bur*30
    costofpizza=piz*40
    costofdrink=dri*20
    costofchicken=chik*50

    tax=((costoffries+costofburger+costofpizza+costofdrink+costofchicken)*0.10)
    total=((costoffries+costofburger+costofpizza+costofdrink+costofchicken))
    taxcost.set(tax)
    totalcost.set(total)

    sql=f"insert into restarunt1 values('{fri}','{bur}','{piz}','{dri}','{chik}','{tax}','{total}')"
    print(sql)
    cursor.execute(sql)
    connection.commit()

def price():
    roo =Tk()
    roo.geometry("400x300+0+0")
    roo.title("Price List")
    roo.resizable(0,0)
    labelin=Label(roo,font=('aria',15,'bold'),text="ITEM",fg='black')
    labelin.grid(row=0,column=0)
    labelin=Label(roo,font=('aria',15,'bold'),text="____________",fg='white')
    labelin.grid(row=0,column=1)
    labelin=Label(roo,font=('aria',15,'bold'),text="PRICE",fg='black')
    labelin.grid(row=0,column=3)
    labelin=Label(roo,font=('aria',15,'bold'),text="Fries",fg='black')
    labelin.grid(row=1,column=0)
    labelin=Label(roo,font=('aria',15,'bold'),text="25",fg='black')
    labelin.grid(row=1,column=2)
    labelin=Label(roo,font=('aria',15,'bold'),text="Burger",fg='black')
    labelin.grid(row=2,column=0)
    labelin=Label(roo,font=('aria',15,'bold'),text="30",fg='black')
    labelin.grid(row=2,column=2)
    labelin=Label(roo,font=('aria',15,'bold'),text="Pizza",fg='black')
    labelin.grid(row=3,column=0)
    labelin=Label(roo,font=('aria',15,'bold'),text="40",fg='black')
    labelin.grid(row=3,column=2)
    labelin=Label(roo,font=('aria',15,'bold'),text="Drinks",fg='black')
    labelin.grid(row=4,column=0)
    labelin=Label(roo,font=('aria',15,'bold'),text="20",fg='black')
    labelin.grid(row=4,column=2)
    labelin=Label(roo,font=('aria',15,'bold'),text="Chicken",fg='black')
    labelin.grid(row=5,column=0)
    labelin=Label(roo,font=('aria',15,'bold'),text="50",fg='black')
    labelin.grid(row=5,column=2)
    roo.mainloop()

labelfries=Label(leftframe,text="fries",font=('aria' ,20, 'bold'),fg='#1B2845',bd=3,anchor='w').grid(row=0,column=0)
textfries=Entry(leftframe,font=('aria',12,'bold'),textvariable=fries,bg='yellow',borderwidth=5).grid(row=0,column=1)
fries.set("")
labelburger=Label(leftframe,text="burger",font=('aria' ,20, 'bold'),fg='#1B2845',bd=3,anchor='w').grid(row=1,column=0)
textburger=Entry(leftframe,font=('aria',12,'bold'),textvariable=burger,bg='yellow',borderwidth=5).grid(row=1,column=1)
burger.set("")
labelpizza=Label(leftframe,text="pizza",font=('aria' ,20, 'bold'),fg='#1B2845',bd=3,anchor='w').grid(row=2,column=0)
textpizza=Entry(leftframe,font=('aria',12,'bold'),textvariable=pizza,bg='yellow',borderwidth=5).grid(row=2,column=1)
pizza.set("")
labeldrink=Label(leftframe,text="drink",font=('aria' ,20, 'bold'),fg='#1B2845',bd=3,anchor='w').grid(row=0,column=4)
Textdrink=Entry(leftframe,font=('aria',12,'bold'),textvariable=drink,bg='yellow',borderwidth=5).grid(row=0,column=5)
drink.set("")
labelchicken=Label(leftframe,text="chicken",font=('aria' ,20, 'bold'),fg='#1B2845',bd=3,anchor='w').grid(row=1,column=4)
textchicken=Entry(leftframe,font=('aria',12,'bold'),textvariable=chicken,bg='yellow',borderwidth=5).grid(row=1,column=5)
chicken.set("")
labelgst=Label(leftframe,text="GST",font=('aria' ,20, 'bold'),fg='#1B2845',bd=3,anchor='w').grid(row=2,column=4)
textgst=Entry(leftframe,font=('aria',12,'bold'),textvariable=taxcost,bg='yellow',borderwidth=5).grid(row=2,column=5)
taxcost.set("")
labelchicken=Label(leftframe,text="Total",font=('aria' ,20, 'bold'),fg='#1B2845',bd=3,anchor='w').grid(row=3,column=4)
textchicken=Entry(leftframe,font=('aria',12,'bold'),textvariable=totalcost,bg='yellow',borderwidth=5).grid(row=3,column=5)
totalcost.set("")

button1=Button(leftframe,text="Price",font=('aria',15),command=price,bg='#786F52',fg='white').grid(row=4,column=0)
button2=Button(leftframe,text="enter",font=('aria',15),command=enter,bg='#786F52',fg='white').grid(row=4,column=1)
button3=Button(leftframe,text="Clear",font=('aria',15),command=clear,bg='#786F52',fg='white').grid(row=4,column=2)
button4=Button(leftframe,text="Exit",font=('aria',15),command=exit,bg='#786F52',fg='white').grid(row=4,column=4)

root.mainloop()