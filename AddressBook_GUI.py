from tkinter import *
import tkinter.messagebox as tmsg
import sqlite3

window = Tk()
window.title("AddressBook")
window.geometry("750x430")

#variables
Username=StringVar()
Password=StringVar()
Fname = StringVar()
Mname = StringVar()
Lname = StringVar()
DOB = StringVar()
HN = StringVar()
LN = StringVar()
Landmark = StringVar()
Area = StringVar()
District = StringVar()
City = StringVar()
Cell1 = StringVar()
Email1 = StringVar()
ID = StringVar()

# submit button(data insertion)
def submit():
    conn = sqlite3.connect(r"C:\Harshal\SQLiteStudio\AMS.db")
    cur = conn.cursor()
    sql = """insert into Address1(First_Name,Middle_Name,Last_Name,Date_of_Birth,House_No,Lane_No,Landmark,Area,City,District,Cell_1,Email_1) values(?,?,?,?,?,?,?,?,?,?,?,?)"""
    cur = conn.cursor()
    data = (Fname.get(), Mname.get(), Lname.get(), DOB.get(), HN.get(), LN.get(), Landmark.get(), Area.get(),City.get(), District.get(), Cell1.get(), Email1.get())
    cur.execute(sql, data)
    conn.commit()
    tmsg.showinfo("Good","Data Inserted..")
    Fname.set("")
    Mname.set("")
    Lname.set("")
    DOB.set("")
    HN.set("")
    LN.set("")
    Landmark.set("")
    Area.set("")
    City.set("")
    District.set("")
    Cell1.set("")
    Email1.set("")
    return cur.lastrowid

# reset button(insert window)
def reset():
    Fname.set("")
    Mname.set("")
    Lname.set("")
    DOB.set("")
    HN.set("")
    LN.set("")
    Landmark.set("")
    Area.set("")
    City.set("")
    District.set("")
    Cell1.set("")
    Email1.set("")


#insertion window
def insert():
    f3 = Frame(window,bg="white")
    f3.place(x=0, y=0, height=430, width=750)
    Label(f3, text=" AddressBook ", fg="red",bg="white", font=("Lucida Sans", 20, "bold")).place(x=320, y=1)
    f4 = Frame(f3, bg="#8a2be2")
    f4.place(x=50, y=40, height=350, width=650)
    Button(f3, text="X", bg="white", fg="red", font=("", 10, ""), command=quit).place(x=720, y=2)
    Label(f4, text="FIRST NAME",bg="#8a2be2", fg="white",font=("", 10 )).place(x=20, y=30)
    Label(f4, text="MIDDLE NAME",bg="#8a2be2", fg="white",font=("", 10)).place(x=360, y=30)
    Label(f4, text="LAST NAME", bg="#8a2be2",fg="white",font=("", 10 )).place(x=20, y=70)
    Label(f4, text="DATE OF BIRTH", bg="#8a2be2",fg="white",font=("", 10 )).place(x=360, y=70)
    Label(f4, text="HOUSE NO", bg="#8a2be2", fg="white", font=("", 10)).place(x=20, y=110)
    Label(f4, text="LANE NO", bg="#8a2be2", fg="white", font=("", 10)).place(x=360, y=110)
    Label(f4, text="LANDMARK", bg="#8a2be2", fg="white", font=("", 10)).place(x=20, y=150)
    Label(f4, text="AREA", bg="#8a2be2", fg="white", font=("", 10)).place(x=360, y=150)
    Label(f4, text="CITY", bg="#8a2be2", fg="white", font=("", 10)).place(x=20, y=190)
    Label(f4, text="DISTRICT", bg="#8a2be2", fg="white", font=("", 10)).place(x=360, y=190)
    Label(f4, text="CELL NO", bg="#8a2be2", fg="white", font=("", 10)).place(x=20, y=230)
    Label(f4, text="EMAIL", bg="#8a2be2", fg="white", font=("", 10)).place(x=360, y=230)
    Entry(f4, textvariable=Fname, font=("", 10,)).place(x=125, y=30)
    Entry(f4, textvariable=Mname, font=("", 10,)).place(x=470, y=30)
    Entry(f4, textvariable=Lname, font=("", 10,)).place(x=125, y=70)
    Entry(f4, textvariable=DOB, font=("", 10,)).place(x=470, y=70)
    Entry(f4, textvariable=HN, font=("", 10,)).place(x=125, y=110)
    Entry(f4, textvariable=LN, font=("", 10,)).place(x=470, y=110)
    Entry(f4, textvariable=Landmark, font=("", 10,)).place(x=125, y=150)
    Entry(f4, textvariable=Area, font=("", 10,)).place(x=470, y=150)
    Entry(f4, textvariable=District, font=("", 10,)).place(x=125, y=190)
    Entry(f4, textvariable=City, font=("", 10,)).place(x=470, y=190)
    Entry(f4, textvariable=Cell1, font=("", 10,)).place(x=125, y=230)
    Entry(f4, textvariable=Email1, font=("", 10,)).place(x=470, y=230)
    Button(f3, text="Menu", bg="white", fg="red",font=("", 11,), command=menu).place(x=80, y=395)
    Button(f4, text=" Submit ", font="luicda 10 " ,fg="black",command=submit).place(x=240,y=315)
    Button(f4, text=" Reset ", font="luicda 10 " ,fg="black",command=reset).place(x=360,y=315)
    Button(f3, text="Login", bg="white", fg="red",font=("", 11,), command=loginwindow).place(x=560, y=395)

#data deletion
def delete():
    conn = sqlite3.connect(r"C:\Harshal\SQLiteStudio\AMS.db")
    cur = conn.cursor()
    sql = """delete from Address1 where id=?"""
    cur = conn.cursor()
    data = (ID.get(), )
    cur.execute(sql,data)
    conn.commit()
    tmsg.showinfo("Good", "Data Deleted..")
    return cur.lastrowid

#delete window
def delete1():
    f5 = Frame(window, bg="white")
    f5.place(x=0, y=0, height=430, width=750)
    Label(f5, text=" AddressBook ", fg="red", bg="white", font=("Lucida Sans", 20, "bold")).place(x=320, y=1)
    f6 = Frame(f5, bg="#8a2be2")
    f6.place(x=50, y=40, height=350, width=650)
    Label(f6, text="Enter the ID which you want to delete",bg="#8a2be2", fg="white", font=("", 15)).place(x=140,y=40)
    Entry(f6, textvariable=ID,font=("", 15),width="5").place(x=485,y=40)
    Button(f6,text="Delete",font=("", 11 ),fg="black",command=delete).place(x=310,y=90)
    Button(f5, text="Menu", bg="white",font=("", 11 ), fg="red", command=menu).place(x=80, y=395)
    Button(f5, text="Login", bg="white", fg="red", font=("", 11 ),command=loginwindow).place(x=580, y=395)

#display
def display():
    window.geometry("1080x430")
    f8 = Frame(window, bg="white")
    f8.place(x=0, y=0, height=430, width=1080)
    Label(f8, text=" AddressBook ", fg="red", bg="white", font=("Lucida Sans", 15, "bold")).place(x=400, y=0)
    Label(f8, text="FIRST" ,bg="white", font=("", 9)).place(x=5, y=35)
    Label(f8, text="NAME"  ,bg="white", font=("", 9)).place(x=5, y=50)
    Label(f8, text="MIDDLE", bg="white",  font=("", 9)).place(x=85, y=35)
    Label(f8, text="NAME", bg="white",font=("", 9)).place(x=90, y=50)
    Label(f8, text="LAST", font=("", 9),bg="white").place(x=165, y=35)
    Label(f8, text="NAME",  font=("", 9),bg="white").place(x=165, y=50)
    Label(f8, text="DOB",  font=("", 9),bg="white").place(x=235, y=35)
    Label(f8, text="HOUSE",  font=("", 9),bg="white").place(x=312, y=35)
    Label(f8, text="NO",  font=("", 9),bg="white").place(x=318, y=50)
    Label(f8, text="LANE",  font=("", 9),bg="white").place(x=385, y=35)
    Label(f8, text="NO",   font=("", 9),bg="white").place(x=390, y=50)
    Label(f8, text="LANDMARK",  font=("",9),bg="white").place(x=445, y=35)
    Label(f8, text="AREA",  font=("", 9),bg="white").place(x=535, y=35)
    Label(f8, text="CITY",  font=("", 9),bg="white").place(x=610, y=35)
    Label(f8, text="DISTRICT",  font=("", 9),bg="white").place(x=675, y=35)
    Label(f8, text="CELL ",  font=("", 9),bg="white").place(x=765, y=35)
    Label(f8, text="EMAIL",  font=("", 9),bg="white").place(x=855, y=35)
    Button(f8, text="Menu", bg="white", font=("", 11), fg="red", command=menu).place(x=80, y=395)
    Button(f8, text="Login", bg="white", fg="red", font=("", 11), command=loginwindow).place(x=800, y=395)
    conn = sqlite3.connect(r"C:\Harshal\SQLiteStudio\AMS.db")
    cur = conn.cursor()
    r = cur.execute("""select * from Address1 """)
    y=80
    for r1 in r:
        Label(f8, text=r1[1], font=("", 9), bg = "white").place(x=5, y=y)
        Label(f8, text=r1[2], font=("", 9), bg="white").place(x=80, y=y)
        Label(f8, text=r1[3], font=("", 9), bg="white").place(x=161, y=y)
        Label(f8, text=r1[4], font=("", 9), bg="white").place(x=226, y=y)
        Label(f8, text=r1[5], font=("", 9), bg="white").place(x=325, y=y)
        Label(f8, text=r1[6], font=("", 9), bg="white").place(x=395, y=y)
        Label(f8, text=r1[7], font=("", 9), bg="white").place(x=455, y=y)
        Label(f8, text=r1[8], font=("", 9), bg="white").place(x=530, y=y)
        Label(f8, text=r1[9], font=("", 9), bg="white").place(x=610, y=y)
        Label(f8, text=r1[10], font=("", 9), bg="white").place(x=675, y=y)
        Label(f8, text=r1[11], font=("", 9), bg="white").place(x=760, y=y)
        Label(f8, text=r1[12], font=("", 9), bg="white").place(x=845, y=y)
        y+=40
    conn.commit()
    conn.close()

def update3():
    conn = sqlite3.connect(r"C:\Harshal\SQLiteStudio\AMS.db")
    cur = conn.cursor()
    sql = """update Address1 set First_Name=?, Middle_Name=?, Last_Name=?, Date_of_Birth=?, House_No=?,Lane_No=?,Landmark=?,Area=?,City=?,District=?,Cell_1=?,Email_1=? where id=?"""
    cur = conn.cursor()
    data = (Fname.get(), Mname.get(), Lname.get(), DOB.get(), HN.get(), LN.get(), Landmark.get(), Area.get(), City.get(),District.get(), Cell1.get(), Email1.get(), ID.get())
    cur.execute(sql, data)
    conn.commit()
    tmsg.showinfo("Good", "Data Inserted..")
    return cur.lastrowid
#update
def update():
    f3 = Frame(window,bg="white")
    f3.place(x=0, y=0, height=430, width=750)
    Label(f3, text=" AddressBook ", fg="red",bg="white", font=("Lucida Sans", 20, "bold")).place(x=320, y=1)
    f4 = Frame(f3, bg="#8a2be2")
    f4.place(x=50, y=40, height=350, width=650)
    Button(f3, text="X", bg="white", fg="red", font=("", 10, ""), command=quit).place(x=720, y=2)
    Label(f4, text="Enter the ID which you want to update", bg="#8a2be2", fg="white", font=("", 10)).place(x=140, y=0)
    e = Entry(f4, textvariable=ID, font=("", 10), width="5")
    e.place(x=465, y=0)
    def update2():
        conn = sqlite3.connect(r"C:\Harshal\SQLiteStudio\AMS.db")
        cur = conn.cursor()
        sql = """select * from Address1 where id = ? """
        data = (ID.get(),)
        r = cur.execute(sql,data)

        for r1 in r:
            Label(f4, text="FIRST NAME",bg="#8a2be2", fg="white",font=("", 10 )).place(x=20, y=50)
            u1 = Entry(f4, textvariable=Fname,font=("", 10,))
            u1.insert(0, r1[1])
            u1.place(x=125, y=50)

            Label(f4, text="MIDDLE NAME",bg="#8a2be2", fg="white",font=("", 10)).place(x=360, y=50)
            u2 = Entry(f4,textvariable=Mname,font=("", 10,))
            u2.insert(0,r1[2])
            u2.place(x=470, y=50)

            Label(f4, text="LAST NAME", bg="#8a2be2",fg="white",font=("", 10 )).place(x=20, y=90)
            u3 = Entry(f4,textvariable=Lname, font=("", 10,))
            u3.insert(0,r1[3])
            u3.place(x=125, y=90)

            Label(f4, text="DATE OF BIRTH", bg="#8a2be2",fg="white",font=("", 10 )).place(x=360, y=90)
            u4 = Entry(f4, text=r1[4],textvariable=DOB, font=("", 10,))
            u4.insert(0, r1[4])
            u4.place(x=470, y=90)

            Label(f4, text="HOUSE NO", bg="#8a2be2", fg="white", font=("", 10)).place(x=20, y=130)
            u5 = Entry(f4, text=r1[5], textvariable=HN,font=("", 10,))
            u5.insert(0,r1[5])
            u5.place(x=125, y=130)

            Label(f4, text="LANE NO", bg="#8a2be2", fg="white", font=("", 10)).place(x=360, y=130)
            u6 = Entry(f4, text=r1[6],textvariable=LN, font=("", 10,))
            u6.insert(0, r1[6])
            u6.place(x=470, y=130)

            Label(f4, text="LANDMARK", bg="#8a2be2", fg="white", font=("", 10)).place(x=20, y=170)
            u7 = Entry(f4, text=r1[7],textvariable=Landmark, font=("", 10,))
            u7.insert(0,r1[7])
            u7.place(x=125, y=170)

            Label(f4, text="AREA", bg="#8a2be2", fg="white", font=("", 10)).place(x=360, y=170)
            u8 = Entry(f4, text=r1[8],textvariable=Area, font=("", 10,))
            u8.insert(0, r1[8])
            u8.place(x=470, y=170)

            Label(f4, text="CITY", bg="#8a2be2", fg="white", font=("", 10)).place(x=20, y=210)
            u9 = Entry(f4, text=r1[9], font=("", 10,),textvariable=City)
            u9.insert(0, r1[9])
            u9.place(x=125, y=210)

            Label(f4, text="DISTRICT", bg="#8a2be2", fg="white", font=("", 10)).place(x=360, y=210)
            u10 = Entry(f4, text=r1[10],font=("", 10,),textvariable=District)
            u10.insert(0, r1[10])
            u10.place(x=470, y=210)

            Label(f4, text="CELL NO", bg="#8a2be2", fg="white", font=("", 10)).place(x=20, y=250)
            u11 = Entry(f4, text=r1[11], font=("", 10,),textvariable=Cell1)
            u11.insert(0, r1[11])
            u11.place(x=125, y=250)

            Label(f4, text="EMAIL", bg="#8a2be2", fg="white", font=("", 10)).place(x=360, y=250)
            u12 = Entry(f4, text=r1[12],font=("", 10,),textvariable=Email1)
            u12.insert(0, r1[12])
            u12.place(x=470, y=250)

            def update3():
                conn = sqlite3.connect(r"C:\Harshal\SQLiteStudio\AMS.db")
                sql = """update Address1 set First_Name=?, Middle_Name=?, Last_Name=?, Date_of_Birth=?, House_No=?,Lane_No=?,Landmark=?,Area=?,City=?,District=?,Cell_1=?,Email_1=? where id=?"""
                cur = conn.cursor()
                data = (
                    Fname.get(), Mname.get(), Lname.get(), DOB.get(), HN.get(), LN.get(), Landmark.get(), Area.get(),
                    City.get(),
                    District.get(), Cell1.get(), Email1.get(), ID.get())
                cur.execute(sql, data)
                conn.commit()
                tmsg.showinfo("Good", "Data Updated..")
                u1.delete(0,END)
                u2.delete(0, END)
                u3.delete(0,END)
                u4.delete(0, END)
                u5.delete(0, END)
                u6.delete(0, END)
                u7.delete(0, END)
                u8.delete(0, END)
                u9.delete(0, END)
                u10.delete(0, END)
                u11.delete(0, END)
                u12.delete(0, END)
                e.delete(0, END)
            Button(f4, text=" Update ", font="luicda 10 ", fg="black", command=update3).place(x=280, y=315)
    Button(f4, text="show", font=("", 8), command=update2).place(x=520, y=0)
    Button(f3, text="Menu", bg="white", fg="red",font=("", 11,), command=menu).place(x=80, y=395)
    Button(f3, text="Login", bg="white", fg="red",font=("", 11,), command=loginwindow).place(x=560, y=395)



#menu
def menu():
    window.geometry("750x430")
    f1 = Frame(window, bg="khaki")
    f1.place(x=0, y=0, height=430, width=750)
    f2 = Frame(f1,bg="white")
    f2.place(x=40, y=30, height=350, width=670)
    Label(f2, text=" Welcome ",bg="white", font=("Lucida Sans", 25, "bold"), fg="red").pack()
    Label(f2, text="Click on button for performing respective action", bg="white", font=("Lucida Sans", 14, "bold"), fg="red").pack(pady=5)
    Button(f2, text="  Insert  ", font="luicda 18 ", bg="yellow",command=insert).place(x=150,y=120)
    Button(f2, text=" Update ", font="luicda 18 ", bg="yellow", command=update).place(x=450,y=120)
    Button(f2, text=" Display ", font="luicda 18 ", bg="yellow",command=display).place(x=150,y=230)
    Button(f2, text=" Delete  ", font="luicda 18 ", bg="yellow", command=delete1).place(x=450,y=230)

#main login window
def loginwindow():
    window.geometry("750x430")
    f = Frame(window,bg="khaki")
    f.place(x=0,y=0,height=430,width=750)
    Label(f,text="Welcome to Address Book",bg="khaki",font=("Lucida Sans", 25, "bold"),fg="red").place(x=170,y=20)
    Label(f,text="Enter Username",bg="khaki",fg="#ff0000",font=("", 11 ,"bold")).place(x=250,y=100)
    Label(f,text="Enter Password",bg="khaki",fg="#ff0000",font=("", 11 ,"bold")).place(x=250,y=160)
    e1=Entry(f,textvariable=Username,font=("", 13 ,))
    e1.place(x=380,y=100,width="130")
    e2=Entry(f,textvariable=Password,font=("", 13 ),show="*")
    e2.place(x=380,y=160,width="130")
    Button(f,text="Login",bg="khaki",fg="red",font=("", 11, "bold"),command=login).place(x=350,y=210)
    Button(f,text="X",bg="white",fg="red",font=("", 11 ,""),command=quit).place(x=725,y=2)
    window.mainloop()

#Checks the username n password from database
def login():
    conn = sqlite3.connect(r"C:\Harshal\SQLiteStudio\AMS.db")
    cur=conn.cursor()
    sql = ''' select * from User where UNAME=? and UPASS=? '''
    data = (Username.get(), Password.get())
    x = cur.execute(sql, data)
    for x1 in x:
            menu()
            break
    else:
            tmsg.askretrycancel("Error","Incorrect username or password")
    Username.set("")
    Password.set("")
    conn.commit()
    conn.close()

#Start
loginwindow()