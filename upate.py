from tkinter import *
import sqlite3
import tkinter.messagebox


#conn=sqlite3.connect("C:\\Users\\Admin\\Documents\\store management system\\Database\\store.db")
conn=sqlite3.connect("C:\\Users\\Admin\\Documents\\store.db")
c=conn.cursor()
result=c.execute(" SELECT Max(id) from inventory")
for r in result:
    id=r[0]
class database:
    def __init__(self,master, *args, **kwargs):
        self.master=master
        self.heading=Label(master,text='Update the database',font=("arial 40 bold"),fg="steelblue")
        self.heading.place(x=400,y=0)
        self.id_le=Label(master,text="Enter ID :",font=("arial 18 bold"))
        self.id_le.place(x=0,y=70)
        self.id_leb=Entry(master,width=10,font=("arial 18 bold"))
        self.id_leb.place(x=380,y=70)
        self.btn_search=Button(master,text="search",width=15,height=2,bg="orange",command=self.search)
        self.btn_search.place(x=550,y=70)
        self.name_l=Label(master,text="Enter product name :",font=("arial 18 bold"))
        self.name_l.place(x=0,y=120)
        self.stock_l=Label(master,text="Enter stocks : ",font=("arial 18 bold"))
        self.stock_l.place(x=0,y=170)
        self.costprice_l=Label(master,text="Enter cost price :",font=("arial 18 bold"))
        self.costprice_l.place(x=0,y=220)
        self.sellprice_l=Label(master,text="Enter selling price :",font=("arial 18 bold"))
        self.sellprice_l.place(x=0,y=270)
        self.totalcp_l=Label(master,text="Enter selling price :",font=("arial 18 bold"))
        self.totalsp_l.place(x=0,y=270)
        self.sellprice_l=Label(master,text="Enter selling price :",font=("arial 18 bold"))
        self.sellprice_l.place(x=0,y=270)
        self.vendor_l=Label(master,text="Enter vendor name :",font=("arial 18 bold"))
        self.vendor_l.place(x=0,y=320)
        self.vendor_phone_l=Label(master,text="Enter vendor phone number :",font=("arial 18 bold"))
        self.vendor_phone_l.place(x=0,y=370)
        self.name_e=Entry(master, width=25,font=("arial 18 bold"))
        self.name_e.place(x=380,y=120)
        self.stock_e=Entry(master, width=25,font=("arial 18 bold"))
        self.stock_e.place(x=380,y=170)
        self.cp_e=Entry(master, width=25,font=("arial 18 bold"))
        self.cp_e.place(x=380,y=220)
        self.sp_e=Entry(master, width=25,font=("arial 18 bold"))
        self.sp_e.place(x=380,y=270)
        self.vendor_e=Entry(master, width=25,font=("arial 18 bold"))
        self.vendor_e.place(x=380,y=320)
        self.vendor_phonenum_e=Entry(master, width=25,font=("arial 18 bold"))
        self.vendor_phonenum_e.place(x=380,y=370)
        self.btn_add=Button(master,text="add to database",width=25,height=2,bg='steelblue',fg='white')
        self.btn_add.place(x=520,y=420)
        self.btn_clear=Button(master,text="Clear All Fields",width=18,height=2,bg="lightgreen",fg="white")
        self.btn_clear.place(x=350,y=420)
        self.tbox=Text(master,width=60,height=18)
        self.tbox.place(x=750,y=70)
        self.tbox.insert(END,"ID has reached upto :"+str(id))
    def search(self, *args, **kwargs):
        sql="SELECT * FROM inventory WHERE id=? "
        result=c.execute(sql,(self.id_leb.get(), ))
        for r in result:
            self.n1=r[1]#name
            self.n2=r[2]#stock
            self.n3=r[3]#cp
            self.n4=r[4]#sp
            self.n5=r[5]#totalcp
            self.n6=r[6]#totalsp
            self.n7=r[7]#assumed_profit
            self.n8=r[8]#vendor
            self.n9=r[9]#vendor_phonenum
        conn.commit()
        #insert into the entries to update
        self.name_e.delete(0,END)
        self.name_e.insert(0,str(self.n1))
        self.stock_e.delete(0,END)
        self.stock_e.insert(0,str(self.n2))
        self.cp_e.delete(0,END)
        self.cp_e.insert(0,str(self.n3))
        self.sp_e.delete(0,END)
        self.sp_e.insert(0,str(self.n4))
        self.vendor_e.delete(0,END)
        self.vendor_e.insert(0,str(self.n8))
        self.vendor_phonenum_e.delete(0,END)
        self.vendor_phonenum_e.insert(0,str(self.n9))

root=Tk()
b=database(root)
root.geometry("1366x768+0+0")
root.title('Update the database')
root.mainloop()