from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from time import strftime
from subprocess import call



class Sign_in:
    def __init__(self,root):
        self.root=root
        self.root.title("Restaurant Management System")
        self.root.geometry("1366x800+0+0",)
        
        img1=Image.open(r"C:\study\Restaurant Management System\images\up.jpg")
        img1=img1.resize((1360,700),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1360,height=700)
        
        self.var_name=StringVar()
        self.var_user_id=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_con_pass=StringVar()

        
        lableframe=LabelFrame(self.root,bd=4,relief=RIDGE,text="Registration...",font=("times new romen",14,"bold"),padx=2,pady=2)
        lableframe.place(x=500,y=100,width=360,height=422)
        
         
        
        lbl_name=Label(lableframe,text="Name:",font=("times new romen",12,"bold"),padx=2,pady=8,fg="red")
        lbl_name.grid(row=2,column=0,sticky=W) 

        entry_name=ttk.Entry(lableframe,width=17,textvariable=self.var_name,font=("arial",13,"bold"))
        entry_name.grid(row=2,column=1) 
        
        lbl_user_id=Label(lableframe,text="User Id:",font=("times new romen",12,"bold"),padx=2,pady=8,fg="red")
        lbl_user_id.grid(row=3,column=0,sticky=W) 

        entry_user_id=ttk.Entry(lableframe,width=17,textvariable=self.var_user_id,font=("arial",13,"bold"))
        entry_user_id.grid(row=3,column=1) 
        
        
        lbl_email=Label(lableframe,text="Email:",font=("times new romen",12,"bold"),padx=2,pady=8,fg="red")
        lbl_email.grid(row=4,column=0,sticky=W) 

        entry_email=ttk.Entry(lableframe,width=17,textvariable=self.var_email,font=("arial",13,"bold"))
        entry_email.grid(row=4,column=1) 
        
        lbl_pass=Label(lableframe,text="Password:",font=("times new romen",12,"bold"),padx=2,pady=8,fg="red")
        lbl_pass.grid(row=5,column=0,sticky=W) 

        entry_pass=ttk.Entry(lableframe,width=17,textvariable=self.var_pass,font=("arial",13,"bold"),show="*")
        entry_pass.grid(row=5,column=1) 
        
        lbl_con_pass=Label(lableframe,text="Conform Password:",font=("times new romen",12,"bold"),padx=2,pady=8,fg="red")
        lbl_con_pass.grid(row=6,column=0,sticky=W) 

        entry_con_pass=ttk.Entry(lableframe,width=17,textvariable=self.var_con_pass,font=("arial",13,"bold"),show="*")
        entry_con_pass.grid(row=6,column=1) 
        
        
        btnlogin=Button(lableframe,text="SignIn",font=("times new romen",13,"bold"),command=self.add_data_admin,bg="black",fg="gold",width=8,bd=0)
        btnlogin.place(x=200,y=210)
        
        
        lbl_floor=Button(lableframe,text="LogIn,aleready have account....",font=("times new romen",10,"bold"),cursor="hand2")
        lbl_floor.place(x=90,y=280,)
        
    
        
    def add_data_admin(self):
        if self.var_user_id.get()=="":
            messagebox.showerror("Error","Name is Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
                my_cursor=conn.cursor()
                #sql=()
                my_cursor.execute("INSERT INTO userdata VALUES(%s,%s,%s,%s,%s)",(
                                      self.var_name.get(),
                                      self.var_user_id.get(),
                                      self.var_email.get(),
                                      self.var_pass.get(),
                                      self.var_con_pass.get()
                                                            ))
                conn.commit()
                #self.fetch_data()
                if my_cursor:
                    messagebox.showinfo(" ","SignUp Successfully",parent=self.root)
                    #root.destroy()
                    call(["python", "login.py"])
                    return True
                conn.close()
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)
        
        
        
   
        
        
if __name__=="__main__":
    root=Tk()
    obj=Sign_in(root)
    root.mainloop()