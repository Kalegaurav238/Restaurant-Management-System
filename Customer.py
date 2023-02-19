from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import random


class customer_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Restaurant Management System")
        self.root.geometry("1107x462+235+218")
        
        # variable
        self.var_ref=StringVar()
        x=random.randint(1,1000)
        self.var_ref.set(str(x))
        
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_idtype=StringVar()
        self.var_idnum=StringVar()
        self.var_addres=StringVar()
        
        
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAIL",font=("times new romen",18,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1107,height=50)
        
        
        # lebel frame left 
        
        lableframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new romen",12,"bold"),padx=2)
        lableframeleft.place(x=5,y=50,width=380,height=408)
        
        # customer ref
        lbl_cust_ref=Label(lableframeleft,text="Custemer Ref",font=("times new romen",13,"bold"),padx=2,pady=9)
        lbl_cust_ref.grid(row=0,column=0,sticky=W) 

        entry_ref=ttk.Entry(lableframeleft,width=25,textvariable=self.var_ref,font=("arial",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)
        
        # customer name
        lbl_cust_ref=Label(lableframeleft,text="Custemer Name:",font=("times new romen",13,"bold"),padx=2,pady=9)
        lbl_cust_ref.grid(row=1,column=0,sticky=W) 

        entry_ref=ttk.Entry(lableframeleft,width=25,textvariable=self.var_name,font=("arial",13,"bold"))
        entry_ref.grid(row=1,column=1)
        
        
        # gender
        lbl_cust_ref=Label(lableframeleft,text="Gender",font=("times new romen",13,"bold"),padx=2,pady=9)
        lbl_cust_ref.grid(row=2,column=0,sticky=W) 

        combo_gender=ttk.Combobox(lableframeleft,font=("times new romen",13,"bold"),textvariable=self.var_gender,state="readonly",width=23)
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1)
       
       
       
       
        # postcode
        #lbl_cust_ref=Label(lableframeleft,text="PostCode:",font=("times new romen",13,"bold"),padx=2,pady=9)
        #lbl_cust_ref.grid(row=3,column=0,sticky=W) 

        #entry_ref=ttk.Entry(lableframeleft,width=25,font=("arial",13,"bold"))
        #entry_ref.grid(row=3,column=1)
        
        # mobile
        lbl_cust_ref=Label(lableframeleft,text="Mobile:",font=("times new romen",13,"bold"),padx=2,pady=9)
        lbl_cust_ref.grid(row=4,column=0,sticky=W) 

        entry_ref=ttk.Entry(lableframeleft,width=25,textvariable=self.var_mobile,font=("arial",13,"bold"))
        entry_ref.grid(row=4,column=1)
        
        
        # email
        lbl_cust_ref=Label(lableframeleft,text="Email:",font=("times new romen",13,"bold"),padx=2,pady=9)
        lbl_cust_ref.grid(row=5,column=0,sticky=W) 

        entry_ref=ttk.Entry(lableframeleft,width=25,textvariable=self.var_email,font=("arial",13,"bold"))
        entry_ref.grid(row=5,column=1)
        
        
        # id prop
        lbl_cust_ref=Label(lableframeleft,text="Id Proop Type:",font=("times new romen",13,"bold"),padx=2,pady=9)
        lbl_cust_ref.grid(row=6,column=0,sticky=W) 
        
        combo_id=ttk.Combobox(lableframeleft,font=("times new romen",13,"bold"),textvariable=self.var_idtype,state="readonly",width=23)
        combo_id["value"]=("AdharCard","PanCard","DrivingLicance","Passport")
        combo_id.current(0)
        combo_id.grid(row=6,column=1)

        
        
        # id no
        lbl_cust_ref=Label(lableframeleft,text="Id Number",font=("times new romen",13,"bold"),padx=2,pady=9)
        lbl_cust_ref.grid(row=7,column=0,sticky=W) 

        entry_ref=ttk.Entry(lableframeleft,width=25,textvariable=self.var_idnum,font=("arial",13,"bold"))
        entry_ref.grid(row=7,column=1)
        
        # address
        lbl_cust_ref=Label(lableframeleft,text="Address:",font=("times new romen",13,"bold"),padx=2,pady=9)
        lbl_cust_ref.grid(row=8,column=0,sticky=W) 

        entry_ref=ttk.Entry(lableframeleft,width=25,font=("arial",13,"bold"),textvariable=self.var_addres)
        entry_ref.grid(row=8,column=1)

        # button 
        btn_frame=Frame(lableframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=340,width=370,height=40)
        
        
        btnAdd=Button(btn_frame,text="Add",font=("times new romen",13,"bold"),command=self.add_data,bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("times new romen",13,"bold"),bg="black",fg="gold",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.mdelet,font=("times new romen",13,"bold"),bg="black",fg="gold",width=8)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("times new romen",13,"bold"),bg="black",fg="gold",width=8)
        btnReset.grid(row=0,column=3,padx=1)
        
        
        # table frame
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new romen",12,"bold"),padx=2)
        table_frame.place(x=390,y=50,width=714,height=408)


        # search
        lbl_serch_by=Label(table_frame,text="Search By",font=("times new romen",13,"bold"),bg="red",fg="white")
        lbl_serch_by.grid(row=0,column=0,sticky=W,padx=2) 
        
        self.var_search=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.var_search,font=("times new romen",13,"bold"),state="readonly",width=20)
        combo_search["value"]=("Ref","Mobile No","Name")
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
        detail_table.place(x=0,y=33,width=707,height=300)
        
        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)
        
        self.cust_detail_table=ttk.Treeview(detail_table,column=("Ref","Name","Gender","Mobile","Email","Id type","Id Number","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.cust_detail_table.xview)
        scroll_y.config(command=self.cust_detail_table.yview)
        
        
        
        self.cust_detail_table.heading("Ref",text="Customer No")
        self.cust_detail_table.heading("Name",text="Customer Name")
        self.cust_detail_table.heading("Gender",text="Gender")
        self.cust_detail_table.heading("Mobile",text="Mobile No")
        self.cust_detail_table.heading("Email",text="Email Id")
        self.cust_detail_table.heading("Id type",text="Id Proof")
        self.cust_detail_table.heading("Id Number",text="Id Number")
        self.cust_detail_table.heading("Address",text="Address")
        
        self.cust_detail_table["show"]="headings"
        
        self.cust_detail_table.column("Ref",width=100)
        self.cust_detail_table.column("Name",width=100)
        self.cust_detail_table.column("Gender",width=100)
        self.cust_detail_table.column("Mobile",width=100)
        self.cust_detail_table.column("Email",width=100)
        self.cust_detail_table.column("Id type",width=100)
        self.cust_detail_table.column("Id Number",width=100)
        self.cust_detail_table.column("Address",width=100)
        
        self.cust_detail_table.pack(fill=BOTH,expand=1)
        self.cust_detail_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        
    def add_data(self):
        

        if self.var_name.get()=="":
            messagebox.showerror("Error","Name is Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
                my_cursor=conn.cursor()
                #sql=()
                my_cursor.execute("INSERT INTO customer VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                      self.var_ref.get(),
                                      self.var_name.get(),
                                      self.var_gender.get(),
                                      self.var_mobile.get(),
                                      self.var_email.get(),
                                      self.var_idtype.get(),
                                      self.var_idnum.get(),
                                      self.var_addres.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)
                
                
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_detail_table.delete(*self.cust_detail_table.get_children())
            for i in rows:
                self.cust_detail_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.cust_detail_table.focus()
        containt=self.cust_detail_table.item(cursor_row)
        row=containt["values"]
        
        self.var_ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_mobile.set(row[3]),
        self.var_email.set(row[4]),
        self.var_idtype.set(row[5]),
        self.var_idnum.set(row[6]),
        self.var_addres.set(row[7]),
        
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please Enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
            my_cursor=conn.cursor()
            my_cursor.execute("UPDATE customer SET Name=%s,Gender=%s,Mobile=%s,Email=%s,Id_type=%s,Id_Number=%s,Address=%s WHERE Ref=%s",(
                                      self.var_name.get(),
                                      self.var_gender.get(),
                                      self.var_mobile.get(),
                                      self.var_email.get(),
                                      self.var_idtype.get(),
                                      self.var_idnum.get(),
                                      self.var_addres.get(),
                                      self.var_ref.get(),))  
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Updated Success","Customer has been Updated",parent=self.root)
            
    def mdelet(self):
        mdelet=messagebox.askyesno("DELETE","Do you want to delet this row",parent=self.root)
        if mdelet>0:
            conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
            my_cursor=conn.cursor()
            query=("DELETE from customer where Ref=%s")
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelet:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    def reset(self):
       # self.var_ref.set(""),
        self.var_name.set(""),
       # self.var_gender.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
       # self.var_idtype.set(""),
        self.var_idnum.set(""),
        self.var_addres.set(""),
        #self.var_ref=StringVar()
        x=random.randint(1,1000)
        self.var_ref.set(str(x))


    def search(self):
        conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.var_search.get())+" LIKE'%"+str(self.search_text.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.cust_detail_table.delete(*self.cust_detail_table.get_children())
            for i in rows:
                self.cust_detail_table.insert("",END,values=i) 
            conn.commit()
        conn.close()
        



if __name__=="__main__":
    root=Tk()
    obj=customer_win(root)
    root.mainloop()