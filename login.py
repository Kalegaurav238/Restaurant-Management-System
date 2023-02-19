from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from time import strftime
from signin import Sign_in
from subprocess import call


class Login_win:
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
        
        
        
        lableframe=LabelFrame(self.root,bd=4,relief=RIDGE,text="Login",font=("times new romen",14,"bold"),padx=2,pady=2)
        lableframe.place(x=500,y=100,width=360,height=422)
        
        lbl_floor=Label(lableframe,text="Wel-Come",font=("Engravers MT",22,"bold"),padx=2,pady=8,fg="green")
        lbl_floor.place(x=65,y=10) 
        
        lbl_floor=Label(lableframe,text="Login-Id:",font=("times new romen",12,"bold"),padx=2,pady=8,fg="red")
        lbl_floor.place(x=50,y=90) 

        entry_floor=ttk.Entry(lableframe,width=15,textvariable=self.var_user_id,font=("arial",13,"bold"))
        entry_floor.place(x=160,y=97)
        
        lbl_floor=Label(lableframe,text="Password:",font=("times new romen",12,"bold"),padx=2,pady=8,fg="red")
        lbl_floor.place(x=50,y=130) 

        entry_floor=ttk.Entry(lableframe,width=15,textvariable=self.var_pass,font=("arial",13,"bold"),show="*")
        entry_floor.place(x=160,y=137)
        
        btnlogin=Button(lableframe,text="LOGIN",command=self.add_data_admin,font=("times new romen",13,"bold"),bg="black",fg="gold",width=8,bd=0)
        btnlogin.place(x=200,y=190)
        
        lbl_floor=Label(lableframe,text="Forgot Password....",font=("times new romen",10,"bold"),cursor="hand2")
        lbl_floor.place(x=120,y=250)
        
        lbl_floor=Button(lableframe,text="SignIn,create new account....",command=self.sigin,font=("times new romen",10,"bold"),cursor="hand2")
        lbl_floor.place(x=90,y=280,)
        
    def add_data_admin(self):
        if self.var_user_id.get()=="":
            messagebox.showerror("Error","Name is Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Gaurav@2310",database="restaurant")
                my_cursor=conn.cursor()
                user_id=self.var_user_id.get()
                password=self.var_pass.get()
                sql=("SELECT * FROM userdata where user_id=%s and password=%s")
                my_cursor.execute(sql,[(user_id),(password)])
                result=my_cursor.fetchall()
                conn.commit()
                if result:
                    messagebox.showinfo(" ","Login Successfully",parent=self.root)
                    #root.destroy()
                    call(["python", "hotel.py"])
                    return True
                else:
                    messagebox.showerror("Error","Login_id or Password is incorrect!",parent=self.root)
                conn.close()
                
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)
          
    def sigin(self):
        self.new_window=Toplevel(self.root)
        self.app=Sign_in(self.new_window)
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Login_win(root)
    root.mainloop()