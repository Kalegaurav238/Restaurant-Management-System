from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import random


class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Restaurant Management System")
        self.root.geometry("1107x462+235+218")
        
        
        # var
        self.var_contact=StringVar()
        self.var_check_in=StringVar()
        self.var_check_out=StringVar()
        self.var_room_type=StringVar()
        self.var_room_no=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_total=StringVar()
        

        
        
        lbl_title=Label(self.root,text="ROOM BOOKING DETAIL",font=("times new romen",18,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1107,height=40)
        
        # lebel frame left 
        
        lableframeleftroom=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Details",font=("times new romen",12,"bold"),padx=2)
        lableframeleftroom.place(x=5,y=40,width=380,height=418)
        
        # Entry and lable
        lbl_cust_contact=Label(lableframeleftroom,text="Cust-Contact:",font=("times new romen",11,"bold"),padx=2,pady=9)
        lbl_cust_contact.grid(row=0,column=0,sticky=W) 

        entry_contact=ttk.Entry(lableframeleftroom,textvariable=self.var_contact,width=19,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)
        
        # button
        btnFetchData=Button(lableframeleftroom,text="Fetch data",command=self.Fetch_contact,font=("times new romen",13,"bold"),bg="black",fg="gold",width=8,bd=0)
        btnFetchData.place(x=280,y=6)
        
        # chack in 
        lbl_cust_chack_in=Label(lableframeleftroom,text="Chack-in:",font=("times new romen",11,"bold"),padx=2,pady=9)
        lbl_cust_chack_in.grid(row=1,column=0,sticky=W) 

        entry_chack_in=ttk.Entry(lableframeleftroom,textvariable=self.var_check_in,width=25,font=("arial",13,"bold"))
        entry_chack_in.grid(row=1,column=1)
        
        # chack out
        lbl_cust_chack_out=Label(lableframeleftroom,text="Check-out:",font=("times new romen",11,"bold"),padx=2,pady=9)
        lbl_cust_chack_out.grid(row=2,column=0,sticky=W) 

        entry_chack_out=ttk.Entry(lableframeleftroom,textvariable=self.var_check_out,width=25,font=("arial",13,"bold"))
        entry_chack_out.grid(row=2,column=1)
        
        # room type
        lbl_cust_ref=Label(lableframeleftroom,text="Room Type:",font=("times new romen",11,"bold"),padx=2,pady=9)
        lbl_cust_ref.grid(row=3,column=0,sticky=W) 

        conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT room_type FROM detailsroom ")
        ide=my_cursor.fetchall()
        
        combo_gender=ttk.Combobox(lableframeleftroom,font=("times new romen",13,"bold"),textvariable=self.var_room_type,state="readonly",width=23)
        combo_gender["value"]=ide
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        
        # no days
        lbl_room_no=Label(lableframeleftroom,text="Room No:",font=("times new romen",11,"bold"),padx=2,pady=9)
        lbl_room_no.grid(row=4,column=0,sticky=W) 

        conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT room_no FROM detailsroom ")
        rows=my_cursor.fetchall()
        
        combo_room_no=ttk.Combobox(lableframeleftroom,textvariable=self.var_room_no,font=("times new romen",13,"bold"),state="readonly",width=23)
        combo_room_no["value"]=rows
        combo_room_no.current(0)
        combo_room_no.grid(row=4,column=1,padx=2)
        
        # no days
        lbl_cust_no_of_days=Label(lableframeleftroom,text="No.of Days:",font=("times new romen",11,"bold"),padx=2,pady=9)
        lbl_cust_no_of_days.grid(row=5,column=0,sticky=W) 

        entry_no_of_days=ttk.Entry(lableframeleftroom,textvariable=self.var_noofdays,width=25,font=("arial",13,"bold"))
        entry_no_of_days.grid(row=5,column=1)
        
        # paid tax
        lbl_cust_paid_tax=Label(lableframeleftroom,text="Paid Tax:",font=("times new romen",11,"bold"),padx=2,pady=9)
        lbl_cust_paid_tax.grid(row=6,column=0,sticky=W) 

        entry_paid_tax=ttk.Entry(lableframeleftroom,textvariable=self.var_paidtax,width=25,font=("arial",13,"bold"))
        entry_paid_tax.grid(row=6,column=1)
        
        # sub total
        #lbl_cust_Sub_Total=Label(lableframeleft,text="Sub Total:",font=("times new romen",13,"bold"),padx=2,pady=9)
        #lbl_cust_Sub_Total.grid(row=6,column=0,sticky=W) 

        #entry_sub_total=ttk.Entry(lableframeleft,width=25,font=("arial",13,"bold"))
        #entry_sub_total.grid(row=6,column=1)
        
        # total cost
        lbl_cust_total_cost=Label(lableframeleftroom,text="Total Cost:",font=("times new romen",11,"bold"),padx=2,pady=9)
        lbl_cust_total_cost.grid(row=7,column=0,sticky=W) 

        entry_total_cost=ttk.Entry(lableframeleftroom,width=25,textvariable=self.var_total,font=("arial",13,"bold"))
        entry_total_cost.grid(row=7,column=1)
        
        
        # bill button
        btnBill=Button(lableframeleftroom,text="Bill",command=self.total,font=("times new romen",13,"bold"),bg="black",fg="gold",width=8)
        #btnAdd.grid(row=7,column=0,padx=1,sticky=W)
        btnBill.place(x=280,y=320,)
        
        # button 
        btn_frame=Frame(lableframeleftroom,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=356,width=370,height=40)
        
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data_room,font=("times new romen",13,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("times new romen",13,"bold"),bg="black",fg="gold",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.mdelet,font=("times new romen",13,"bold"),bg="black",fg="gold",width=8)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("times new romen",13,"bold"),bg="black",fg="gold",width=8)
        btnReset.grid(row=0,column=3,padx=1)
        
        
        # right image
        img6=Image.open(r"C:\study\Restaurant Management System\images\bed.jpg")
        img6=img6.resize((377,210),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        lblimg1=Label(self.root,image=self.photoimg6,bd=4,relief=RIDGE)
        lblimg1.place(x=725,y=42,width=377,height=210)
        
        
        
        # table frame
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new romen",12,"bold"),padx=2)
        table_frame.place(x=390,y=250,width=714,height=208)


        # search
        lbl_serch_by=Label(table_frame,text="Search By",font=("times new romen",13,"bold"),bg="red",fg="white")
        lbl_serch_by.grid(row=0,column=0,sticky=W,padx=2) 
        
        self.var_search=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.var_search,font=("times new romen",13,"bold"),state="readonly",width=20)
        combo_search["value"]=("Contact")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.search_text=StringVar()
        txtSearch=ttk.Entry(table_frame,width=25,textvariable=self.search_text,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(table_frame,text="Search",command=self.search,font=("times new romen",13,"bold"),bg="black",fg="gold",width=8,bd=0)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnShowAll=Button(table_frame,text="Show All",command=self.fetch_data,font=("times new romen",13,"bold"),bg="black",fg="gold",width=8,bd=0)
        btnShowAll.grid(row=0,column=4,padx=1)
        
        
        # table data
        detail_table=Frame(table_frame,bd=2,relief=RIDGE)
        detail_table.place(x=0,y=33,width=707,height=150)
        
        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)
        
        self.room_table=ttk.Treeview(detail_table,column=("contact","check_in","check_out","room_type","no_of_days"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        
        
        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("check_in",text="Check In")
        self.room_table.heading("check_out",text="Check Out")
        self.room_table.heading("room_type",text="Room Type")
        self.room_table.heading("no_of_days",text="No of Days")
       
        
        self.room_table["show"]="headings"
        
        self.room_table.column("contact",width=100)
        self.room_table.column("check_in",width=100)
        self.room_table.column("check_out",width=100)
        self.room_table.column("room_type",width=100)
        self.room_table.column("no_of_days",width=100)

        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Mobile No.",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error","This no is not exist in database",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=400,y=55,width=310,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)
                
                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)
                
                # gender
                conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)
                
                lbl1=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl1.place(x=90,y=30)
                
                # Email
                conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblEmail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblEmail.place(x=0,y=60)
                
                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=60)
                
                # Address
                conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblAddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lblAddress.place(x=0,y=90)
                
                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=90)
                
    def add_data_room(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Name is Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
                my_cursor=conn.cursor()
                #sql=()
                my_cursor.execute("INSERT INTO roomdata VALUES(%s,%s,%s,%s,%s)",(
                                      self.var_contact.get(),
                                      self.var_check_in.get(),
                                      self.var_check_out.get(),
                                      self.var_room_type.get(),
                                      self.var_noofdays.get()
                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Room data added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)
                
    
        
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        containt=self.room_table.item(cursor_row)
        row=containt["values"]
        
        self.var_contact.set(row[0]),
        self.var_check_in.set(row[1]),
        self.var_check_out.set(row[2]),
        self.var_room_type.set(row[3]),
        self.var_noofdays.set(row[4]),
        
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
            my_cursor=conn.cursor()
            my_cursor.execute("UPDATE roomdata SET check_in=%s,check_out=%s,room_type=%s,noofdays=%s WHERE contact=%s",(
                                      self.var_check_in.get(),
                                      self.var_check_out.get(),
                                      self.var_room_type.get(),
                                      self.var_noofdays.get(),
                                      self.var_contact.get()
                                     ))  
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Updated Success","Room Details Updated Successfully",parent=self.root)
        
    # delete
    def mdelet(self):
        mdelet=messagebox.askyesno("DELETE","Do you want to delet this row",parent=self.root)
        if mdelet>0:
            conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
            my_cursor=conn.cursor()
            query=("DELETE from roomdata where contact=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelet:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    # reset
    def reset(self):
       # self.var_ref.set(""),
        self.var_contact.set(""),
       # self.var_gender.set(""),
        self.var_check_in.set(""),
        self.var_check_out.set(""),
       # self.var_idtype.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_total.set("")
       # self.var_addres.set(""),
        #self.var_ref=StringVar()
        #x=random.randint(1,1000)
       # self.var_contact.set(str(x))
        
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM roomdata")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    # search system
    def search(self):
        conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from roomdata where "+str(self.var_search.get())+" LIKE'%"+str(self.search_text.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i) 
            conn.commit()
        conn.close()
        
        
    def total(self):
        inDate=self.var_check_in.get()
        outDate=self.var_check_out.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)
        
        if (self.var_room_type.get()=="Single"):
            q1=float(300)
            q2=float(self.var_noofdays.get())
            q3=float(q1*q2)
            tax="Rs."+str("%.2f"%(q3+((q3)*0.9)))
            st="Rs."+str("%.2f"%((q3)*0.9))
            self.var_total.set(tax)
            self.var_paidtax.set(st)
        
        elif (self.var_room_type.get()=="Double"):
            q1=float(500)
            q2=float(self.var_noofdays.get())
            q3=float(q1*q2)
            tax="Rs."+str("%.2f"%(q3+((q3)*0.9)))
            st="Rs."+str("%.2f"%((q3)*0.9))
            self.var_total.set(tax)
            self.var_paidtax.set(st)
            
        elif(self.var_room_type.get()=="Private"):
            q1=float(400)
            q2=float(self.var_noofdays.get())
            q3=float(q1*q2)
            tax="Rs."+str("%.2f"%(q3+((q3)*0.9)))
            st="Rs."+str("%.2f"%((q3)*0.9))
            self.var_total.set(tax)
            self.var_paidtax.set(st)

        else:
            pass
        
        

        
        
if __name__=="__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()