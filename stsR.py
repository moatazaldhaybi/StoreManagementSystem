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
        self.heading=Label(master,text='Add to database',font=("arial 40 bold"),fg="steelblue")
        self.heading.place(x=400,y=0)
        self.name_l=Label(master,text="Enter product name :",font=("arial 18 bold"))
        self.name_l.place(x=0,y=70)
        self.stock_l=Label(master,text="Enter stocks : ",font=("arial 18 bold"))
        self.stock_l.place(x=0,y=120)
        self.costprice_l=Label(master,text="Enter cost price :",font=("arial 18 bold"))
        self.costprice_l.place(x=0,y=170)
        self.sellprice_l=Label(master,text="Enter selling price :",font=("arial 18 bold"))
        self.sellprice_l.place(x=0,y=220)
        self.vendor_l=Label(master,text="Enter vendor name :",font=("arial 18 bold"))
        self.vendor_l.place(x=0,y=270)
        self.vendor_phone_l=Label(master,text="Enter vendor phone number :",font=("arial 18 bold"))
        self.vendor_phone_l.place(x=0,y=320)
        self.id_l=Label(master,text="Enter ID :",font=("arial 18 bold"))
        self.id_l.place(x=0,y=370)
        self.name_e=Entry(master, width=25,font=("arial 18 bold"))
        self.name_e.place(x=380,y=70)
        self.stock_e=Entry(master, width=25,font=("arial 18 bold"))
        self.stock_e.place(x=380,y=120)
        self.cp_e=Entry(master, width=25,font=("arial 18 bold"))
        self.cp_e.place(x=380,y=170)
        self.sp_e=Entry(master, width=25,font=("arial 18 bold"))
        self.sp_e.place(x=380,y=220)
        self.vendor_e=Entry(master, width=25,font=("arial 18 bold"))
        self.vendor_e.place(x=380,y=270)
        self.vendor_phonenum_e=Entry(master, width=25,font=("arial 18 bold"))
        self.vendor_phonenum_e.place(x=380,y=320)
        self.id_e=Entry(master,width=25,font=("arial 18 bold"))
        self.id_e.place(x=380,y=370)
        self.btn_add=Button(master,text="add to database",width=25,height=2,bg='steelblue',fg='white',command=self.get_items)
        self.btn_add.place(x=520,y=420)
        self.btn_clear=Button(master,text="Clear All Fields",width=18,height=2,bg="lightgreen",fg="white",command=self.clear_all)
        self.btn_clear.place(x=350,y=420)
        self.tbox=Text(master,width=60,height=18)
        self.tbox.place(x=750,y=70)
        self.tbox.insert(END,"ID has reached upto :"+str(id))
    def get_items(self, *args, **kwargs):
        self.name=self.name_e.get()
        self.stock=self.stock_e.get()
        self.costprice=self.cp_e.get()
        self.sellprice=self.sp_e.get()
        self.vendor=self.vendor_e.get()
        self.vendor_phonenum=self.vendor_phonenum_e.get()
        self.totalcp=float(self.costprice) * float(self.stock)
        self.totalsp=float(self.sellprice) * float(self.stock)
        self.assumed_profit=float(self.totalsp - self.totalcp)
        if self.name=='' or self.stock=='' or self.costprice=='' or self.sellprice=='':
            tkinter.messagebox.showinfo("Error" , "Please Fill all the entries.")
        else:
            sql="Insert into inventory(name, stock, costprice, sellprice, totalcp, totalsp, assumed_profit, vendor, vendor_phonenum) Values(?,?,?,?,?,?,?,?,?)"
            c.execute(sql, (self.name,self.stock,self.costprice,self.sellprice,self.totalcp,self.totalsp,self.assumed_profit,self.vendor,self.vendor_phonenum))
            conn.commit()
            self.tbox.insert(END,"\n\nInseted"+str(self.name)+"into the database with code"+str(slef.id_e.get()))
            tkinter.messagebox.showinfo("success" , "successfully added to the database.")
    def clear_all(self, *args, **kwargs):
        self.name_e.delete(0,END)
        self.stock_e.delete(0,END)
        self.cp_e.delete(0,END)
        self.sp_e.delete(0,END)
        self.vendor_e.delete(0,END)
        self.vendor_phonenum_e.delete(0,END)
        self.id_e.delete(0,END)
        
root=Tk()
b=database(root)
root.geometry("1366x768+0+0")
root.title('Add to database')
root.mainloop()