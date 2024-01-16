from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime

class generate_receipt :
    def __init__(self,root):
        self.root = root
        self.root.title("Hspital Management System")
        self.root.geometry("1295x550+230+220")

        # ============== variables ==================

        self.id_var = StringVar()
        self.ref_var = StringVar()
        self.cname_var = StringVar()
        self.mother_var = StringVar()
        self.gender_var = StringVar()
        self.post_var = StringVar()
        self.mobile_var = StringVar()
        self.email_var = StringVar()
        self.nationality_var = StringVar()
        self.address_var = StringVar()
        self.idproof_var = StringVar()
        self.idnum_var = StringVar()

        self.contact_var = StringVar()
        self.checkin_var = StringVar()
        self.checkout_var = StringVar()
        self.roomtype_var = StringVar()
        self.room_number = StringVar()
        self.no_days_var = StringVar()
        self.paid_tax_var = StringVar()
        self.sub_total_amt_var = StringVar()
        self.total_amt_var = StringVar()

        
        # ============== title ==================

        lbl_title = Label(self.root,text="GENERATE RECEIPT", font=("times new roman", 18, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # ============== label frame left ================
        
        labelframeleft = Frame(self.root,bd=2, relief=RIDGE , font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)







        # ================= fetch all data by contact ================
        
    # def fetch_contact(self):
    #     if self.contact_var.get() == "":
    #         messagebox.showerror("error","please enter a contact to fetch data",parent= self.root)

    #     else:
    #         conn = mysql.connector.connect(host="localhost",user="root",password="root",database="hotel_management_cwk")
    #         my_cursor = conn.cursor()
    #         query = ("select name from customer_table where mobile = %s")
    #         value = (self.contact_var.get(),)
    #         my_cursor.execute(query,value)
    #         name = my_cursor.fetchone()

    #         if name == None :
    #             messagebox.showerror("error","this number not found",parent= self.root)
    #         else:
    #             conn.commit()
    #             conn.close()

    #             showdataframe = Frame(self.root,bd=5,relief=RIDGE,padx=2)
    #             showdataframe.place(x=455,y=55,width=370,height=200)

    #             lblemail = Label(showdataframe,text="Name:",font=("arial",12,"bold"))
    #             lblemail.place(x=0,y=0)

    #             data_gender = Label(showdataframe,text=name[0],font=("arial",12,"bold"))
    #             data_gender.place(x=110,y=0)

    #             conn = mysql.connector.connect(host="localhost",user="root",password="root",database="hotel_management_cwk")
    #             my_cursor = conn.cursor()
    #             query = ("select gender from customer_table where mobile = %s")
    #             value = (self.contact_var.get(),)
    #             my_cursor.execute(query,value)
    #             gender = my_cursor.fetchone()
                
    #             lblgender = Label(showdataframe,text="Gender:",font=("arial",12,"bold"))
    #             lblgender.place(x=0,y=30)

    #             data_gender = Label(showdataframe,text=gender[0],font=("arial",12,"bold"))
    #             data_gender.place(x=110,y=30)

    #             query = ("select mobile from customer_table where mobile = %s")
    #             value = (self.contact_var.get(),)
    #             my_cursor.execute(query,value)
    #             mobile = my_cursor.fetchone()
                
    #             lblmobile = Label(showdataframe,text="Mobile:",font=("arial",12,"bold"))
    #             lblmobile.place(x=0,y=60)

    #             data_mobile = Label(showdataframe,text=mobile[0],font=("arial",12,"bold"))
    #             data_mobile.place(x=110,y=60)

    #             query = ("select email from customer_table where mobile = %s")
    #             value = (self.contact_var.get(),)
    #             my_cursor.execute(query,value)
    #             email = my_cursor.fetchone()
                
    #             lblemail = Label(showdataframe,text="Email:",font=("arial",12,"bold"))
    #             lblemail.place(x=0,y=90)

    #             data_email = Label(showdataframe,text=email[0],font=("arial",12,"bold"))
    #             data_email.place(x=110,y=90)

    #             query = ("select address from customer_table where mobile = %s")
    #             value = (self.contact_var.get(),)
    #             my_cursor.execute(query,value)
    #             address = my_cursor.fetchone()
                
    #             lbladdress = Label(showdataframe,text="Address:",font=("arial",12,"bold"))
    #             lbladdress.place(x=0,y=120)

    #             data_address = Label(showdataframe,text=address[0],font=("arial",12,"bold"))
    #             data_address.place(x=110,y=120)

    #             query = ("select postal_code from customer_table where mobile = %s")
    #             value = (self.contact_var.get(),)
    #             my_cursor.execute(query,value)
    #             p_code = my_cursor.fetchone()
                
    #             lbl_p_code = Label(showdataframe,text="Postal code:",font=("arial",12,"bold"))
    #             lbl_p_code.place(x=0,y=150)

    #             data_p_code = Label(showdataframe,text=p_code[0],font=("arial",12,"bold"))
    #             data_p_code.place(x=110,y=150)

    #             conn.commit()
    #             conn.close()







if __name__ == "__main__":
    root = Tk()
    obj = generate_receipt(root)
    root.mainloop()
