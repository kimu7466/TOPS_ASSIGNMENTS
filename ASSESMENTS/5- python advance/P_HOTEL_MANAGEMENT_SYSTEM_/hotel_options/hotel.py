from tkinter import *
from PIL import Image, ImageTk
from .customer import Cust_Win
from .room import Roombooking
from .roomarrange import room_arrange

class hotelmanagementsystem:
    def __init__(self, root):
        self.root = root 
        self.root.title("Hotel Management System")
        self.root.geometry("1540x800+0+0")

        # ==============images ==================

        img1 = Image.open(r"C:\Users\kimu7\Desktop\CWk_HMS\images\image1.jpg")
        img1 = img1.resize((1540, 140), resample=Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=1540, height=140)

        # ============== title ==================

        lbl_title = Label(self.root,text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1540,height=50)

        # ============== main frame ==================

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        # ============== menu ==================

        lbl_menu = Label(main_frame,text="MENU", font=("times new roman", 20, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        # ============== button frame ==================

        button_frame = Frame(main_frame,bd=4,relief=RIDGE)
        button_frame.place(x=0,y=35,width=228,height=190)

        cust_btn = Button(button_frame,width= 22, text="CUSTOMER", command=self.cust_details, font=("times new roman", 14, "bold"),bg="black", fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0, pady=1)

        room_btn = Button(button_frame,width= 22,text="ROOM", command=self.Roombooking, font=("times new roman", 14, "bold"),bg="black", fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0, pady=1)

        add_room_btn = Button(button_frame,width= 22,text="ADD ROOM", command=self.room_arrange, font=("times new roman", 14, "bold"),bg="black", fg="gold",bd=0,cursor="hand1")
        add_room_btn.grid(row=2,column=0, pady=1)

        generate_receipt_btn = Button(button_frame,width= 22,text="GENERATE RECEIPT",font=("times new roman", 14, "bold"),bg="black", fg="gold",bd=0,cursor="hand1")
        generate_receipt_btn.grid(row=3,column=0, pady=1)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def Roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)

    def room_arrange(self):
        self.new_window = Toplevel(self.root)
        self.app = room_arrange(self.new_window)

if __name__ == '__main__':
    root = Tk()
    obj = hotelmanagementsystem(root)
    root.mainloop()
