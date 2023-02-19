from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import random


class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Restaurant Management System")
        self.root.geometry("1107x462+235+218")
        
        #var
        self.var_room_no=StringVar()
        self.var_room_type=StringVar()
        self.var_floor=StringVar()
        
        lbl_title=Label(self.root,text="ROOM BOOKING DETAIL",font=("times new romen",18,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1107,height=40)
        
        # lebel frame left 
        
        lableframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new romen",12,"bold"),padx=2)
        lableframeleft.place(x=35,y=40,width=500,height=350)
        
        lbl_floor=Label(lableframeleft,text="Floor:",font=("times new romen",11,"bold"),padx=2,pady=9)
        lbl_floor.grid(row=0,column=0,sticky=W) 

        entry_floor=ttk.Entry(lableframeleft,width=19,textvariable=self.var_floor,font=("arial",13,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)
        
        lbl_room_no=Label(lableframeleft,text="Room No:",font=("times new romen",11,"bold"),padx=2,pady=9)
        lbl_room_no.grid(row=1,column=0,sticky=W) 

        entry_room_no=ttk.Entry(lableframeleft,width=19,textvariable=self.var_room_no,font=("arial",13,"bold"))
        entry_room_no.grid(row=1,column=1,sticky=W)
        
        lbl_room_type=Label(lableframeleft,text="Room Type:",font=("times new romen",11,"bold"),padx=2,pady=9)
        lbl_room_type.grid(row=2,column=0,sticky=W) 

        entry_room_type=ttk.Entry(lableframeleft,width=19,textvariable=self.var_room_type,font=("arial",13,"bold"))
        entry_room_type.grid(row=2,column=1,sticky=W)
        
        # button 
        btn_frame=Frame(lableframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=50,y=220,width=370,height=40)
        
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data_room,font=("times new romen",13,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("times new romen",13,"bold"),bg="black",fg="gold",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.mdelet,font=("times new romen",13,"bold"),bg="black",fg="gold",width=8)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("times new romen",13,"bold"),bg="black",fg="gold",width=8)
        btnReset.grid(row=0,column=3,padx=1)
        
        # right fream
        lableframeright=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Details",font=("times new romen",12,"bold"),padx=2)
        lableframeright.place(x=570,y=40,width=500,height=350)
        
        
        # table data
        detail_table=Frame(lableframeright,bd=2,relief=RIDGE)
        detail_table.place(x=1,y=1,width=500,height=320)
        
        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)
        
        self.room_table=ttk.Treeview(detail_table,column=("room_no","room_type","floor"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        self.room_table.heading("room_no",text="Room No")
        self.room_table.heading("room_type",text="Room Type")
        self.room_table.heading("floor",text="Floor")
       
        self.room_table["show"]="headings"
        
        self.room_table.column("room_no",width=100)
        self.room_table.column("room_type",width=100)
        self.room_table.column("floor",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM detailsroom ")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def add_data_room(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Name is Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
                my_cursor=conn.cursor()
                #sql=()
                my_cursor.execute("INSERT INTO detailsroom VALUES(%s,%s,%s)",(
                                      self.var_room_no.get(),
                                      self.var_room_type.get(),
                                      self.var_floor.get()
                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","New Room added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)
                
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        containt=self.room_table.item(cursor_row)
        row=containt["values"]
        
        self.var_room_no.set(row[0]),
        self.var_room_type.set(row[1]),
        self.var_floor.set(row[2]),
        
        
                
    def update(self):
        if self.var_room_type.get()=="":
            messagebox.showerror("Error","Please Enter Room number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
            my_cursor=conn.cursor()
            my_cursor.execute("UPDATE detailsroom SET room_type=%s,floor=%s WHERE room_no=%s",(
                                        self.var_room_type.get(),
                                        self.var_floor.get(),
                                        self.var_room_no.get()
                                     ))  
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Updated Success","Room Details Updated Successfully",parent=self.root)
                    
    
    def mdelet(self):
        mdelet=messagebox.askyesno("DELETE","Do you want to delet this row",parent=self.root)
        if mdelet>0:
            conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
            my_cursor=conn.cursor()
            query=("DELETE from detailsroom where room_no=%s")
            value=(self.var_room_no.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelet:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    def reset(self):
        self.var_room_no.set(""),
        self.var_room_type.set(""),
        self.var_floor.set(""),
   
        
if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()