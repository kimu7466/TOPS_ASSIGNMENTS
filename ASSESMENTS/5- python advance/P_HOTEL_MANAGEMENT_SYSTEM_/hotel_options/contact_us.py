from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime

class contact_info :
    def __init__(self,root):
        self.root = root
        self.root.title("Hspital Management System")
        self.root.geometry("1295x550+230+220")
        
        # ============== title ==================

        lbl_title = Label(self.root,text="CONTACT US", font=("times new roman", 18, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # ============== label frame ================
        
        labelframe = LabelFrame(self.root,bd=2, relief=RIDGE ,text="CONTACT INFO", font=("times new roman",12,"bold"))
        labelframe.place(x=5,y=50,width=1200,height=490)

        # ============== variables ==================

        name__lbl = Label(labelframe, text="Name : IMROZ KHAN",font=("times new roman",20,"bold"))
        name__lbl.pack(side="top")

        contact_no_lbl = Label(labelframe, text="Contact No. : +91 9898787866",font=("times new roman",20,"bold"))
        contact_no_lbl.pack(side="top")

        contact_no_lbl = Label(labelframe, text="Email : kimu7466@gmail.com",font=("times new roman",20,"bold"))
        contact_no_lbl.pack(side="top")

        contact_no_lbl = Label(labelframe, text="Address : 62, 3rd Street, New colony, Old city, Rajasthan, 327001, INDIA.",font=("times new roman",20,"bold"))
        contact_no_lbl.pack(side="top")





if __name__ == "__main__":
    root = Tk()
    obj = contact_info(root)
    root.mainloop()
