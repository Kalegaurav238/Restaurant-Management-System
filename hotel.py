from tkinter import *
from PIL import Image,ImageTk
from Customer import customer_win
from room import RoomBooking
from details import DetailsRoom
from login import Login_win

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Restaurant Management System")
        self.root.geometry("1550x800+0+0")

        
        img1=Image.open(r"C:\study\Restaurant Management System\images\logo1.jpg")
        img1=img1.resize((1350,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1350,height=130)
        
      #  img2=Image.open(r"C:\study\Restaurant Management System\images\logo.jpg")
      #  img2=img2.resize((200,140),Image.ANTIALIAS)
      #  self.photoimg2=ImageTk.PhotoImage(img2)
      #  lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
      #  lblimg.place(x=0,y=0,width=200,height=140)
        
        lbl_title=Label(self.root,text="RESTAURANT MANAGEMENT SYSTEM",font=("times new romen",40,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=130,width=1350,height=50)
        
        # main
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=180,width=1350,height=620)
        
        # menu
        lbl_menu=Label(main_frame,text="MENU",font=("times new romen",20,"bold"),bg="black",fg="gold")
        lbl_menu.place(x=0,y=0,width=230)
        
        # main
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)
        
        cust_btn=Button(btn_frame,text="CUSTOMR",command=self.cust_details,width=18,font=("times new romen",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)
        
        room_btn=Button(btn_frame,text="ROOM",width=18,command=self.room_details,font=("times new romen",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)
        
        details_btn=Button(btn_frame,text="DETAILS",command=self.details,width=18,font=("times new romen",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)
        
        report_btn=Button(btn_frame,text="REPORT",width=18,font=("times new romen",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        report_btn.grid(row=4,column=0,pady=1)
        
        logout_btn=Button(btn_frame,text="LOGIN",command=self.login,width=18,font=("times new romen",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        logout_btn.grid(row=5,column=0,pady=1)
        
        
        # img right
        img3=Image.open(r"C:\study\Restaurant Management System\images\room.jpeg")
        img3=img3.resize((1117,500),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1117,height=500)
        
        # down
        img4=Image.open(r"C:\study\Restaurant Management System\images\up.jpg")
        img4=img4.resize((230,140),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=230,height=140)
        
        img5=Image.open(r"C:\study\Restaurant Management System\images\up2.jpg")
        img5=img5.resize((230,140),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=359,width=230,height=140)
        
        
    def cust_details(self):
      self.new_window=Toplevel(self.root)
      self.app=customer_win(self.new_window)
      
    def room_details(self):
      self.new_window=Toplevel(self.root)
      self.app=RoomBooking(self.new_window)
      
    def details(self):
      self.new_window=Toplevel(self.root)
      self.app=DetailsRoom(self.new_window)
      
    def login(self):
      self.new_window=Toplevel(self.root)
      self.app=Login_win(self.new_window)
          
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()