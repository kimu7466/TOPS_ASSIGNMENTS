from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime

class Roombooking :
    def __init__(self,root):
        self.root = root
        self.root.title("Hspital Management System")
        self.root.geometry("1295x550+230+220")

        # ============== variables ==================

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

        lbl_title = Label(self.root,text="ADD ROOM BOOKING DETAILS", font=("times new roman", 18, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # ============== label frame left ================

        labelframeleft = LabelFrame(self.root,bd=2, relief=RIDGE ,text="ROOM DETAILS", font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)

        # ============== label and entries ================

        # customer mobile
        contact_lbl = Label(labelframeleft,text="Customer Mobile", font=("arial",12,"bold"),padx=2,pady=6)
        contact_lbl.grid(row=0,column=0,sticky=W)

        mobile_entry = ttk.Entry(labelframeleft, width=20, textvariable=self.contact_var, font=("arial",13,"bold"))
        mobile_entry.grid(row=0,column=1,sticky=W)
        
        # fetch data button
        fetch_data_btn = Button(labelframeleft,text="Fetch data",command=self.fetch_contact,font=("arial",8,"bold"),bg="black",fg="gold",width=10 )
        fetch_data_btn.grid(row=0,column=1,sticky=E)

        # # check in date
        checkin_lbl = Label(labelframeleft,text="Check In Date", font=("arial",12,"bold"),padx=2,pady=6)
        checkin_lbl.grid(row=1,column=0,sticky=W)

        checkin_entry = ttk.Entry(labelframeleft, width=29, textvariable=self.checkin_var, font=("arial",13,"bold"))
        checkin_entry.grid(row=1,column=1)

        # check out date
        checkout_date = Label(labelframeleft,text="Check Out Date", font=("arial",12,"bold"),padx=2,pady=6)
        checkout_date.grid(row=2,column=0,sticky=W)

        checkout_entry = ttk.Entry(labelframeleft, width=29, textvariable=self.checkout_var, font=("arial",13,"bold"))
        checkout_entry.grid(row=2,column=1)

        # room type
        roomtype_lbl = Label(labelframeleft,text="Room Type.", font=("arial",12,"bold"),padx=2,pady=6)
        roomtype_lbl.grid(row=3,column=0,sticky=W)

        # room type combobox
        roomtype_entry = ttk.Combobox(labelframeleft, textvariable=self.roomtype_var, font=("arial", 13, "bold"), width=27, state="readonly")
        roomtype_entry['value']=("Deluxe","General","Full Deluxe","Joint")
        roomtype_entry.current(0)
        roomtype_entry.grid(row=3, column=1)

        # room number
        room_number = Label(labelframeleft, text="Room Number", font=("arial", 12, "bold"), padx=2, pady=6)
        room_number.grid(row=4, column=0, sticky=W)

        conn = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    password = "root",
                    database = "hotel_management_cwk"
                )
        my_cursor = conn.cursor()
        my_cursor.execute(f"SELECT RoomNo FROM add_room WHERE RoomType = '{self.roomtype_var.get()}'")
        dbrows = my_cursor.fetchall()

        # room number combobox
        room_number_entry = ttk.Combobox(labelframeleft, textvariable=self.room_number, font=("arial", 13, "bold"), width=27, state="readonly")
        room_number_entry['value']=dbrows
        room_number_entry.grid(row=4, column=1)

        # number of days
        no_of_days = Label(labelframeleft,text="No. of Days", font=("arial",12,"bold"),padx=2,pady=6)
        no_of_days.grid(row=5,column=0,sticky=W)

        days_entry = ttk.Entry(labelframeleft, width=29, textvariable=self.no_days_var, font=("arial",13,"bold"))
        days_entry.grid(row=5,column=1)

        # sub total
        sub_total_lbl = Label(labelframeleft,text="Sub Total (₹)", font=("arial",12,"bold"),padx=2,pady=6)
        sub_total_lbl.grid(row=6,column=0,sticky=W)

        sub_total_entry = ttk.Entry(labelframeleft, textvariable=self.sub_total_amt_var, width=29, font=("arial",13,"bold"))
        sub_total_entry.grid(row=6,column=1)

        # paid Tax
        paid_tax_lbl = Label(labelframeleft,text="Paid Tax (₹) (18%)", font=("arial",12,"bold"),padx=2,pady=6)
        paid_tax_lbl.grid(row=7,column=0,sticky=W)

        paid_tax_entry = ttk.Entry(labelframeleft, textvariable=self.paid_tax_var, width=29, font=("arial",13,"bold"))
        paid_tax_entry.grid(row=7,column=1)

        # total cost
        total_cost_lbl = Label(labelframeleft,text="TOTAL (₹)", font=("arial",12,"bold"),padx=2,pady=6)
        total_cost_lbl.grid(row=8,column=0,sticky=W)

        total_cost_entry = ttk.Entry(labelframeleft, textvariable=self.total_amt_var, width=29, font=("arial",13,"bold"))
        total_cost_entry.grid(row=8,column=1)

        # ======================= bill button ===========================

        bill_button = Button(labelframeleft, text="BILL", command=self.total, font=("arial", 15, "bold"), bg="green", fg="gold", bd=5,relief=GROOVE, width=15)
        bill_button.grid(row=10,column=0,padx=1,sticky=E,columnspan=2)

        # ======================= button ===========================

        btn_frame_cust = Frame(labelframeleft,bd=4,relief=RIDGE)
        btn_frame_cust.place(x=0,y=400,width=412,height=40)

        btnadd = Button(btn_frame_cust, text="Add", command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate = Button(btn_frame_cust,text="Update", command=self.update_data, font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete = Button(btn_frame_cust,text="Delete", command=self.delete_data, font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset = Button(btn_frame_cust,text="Reset", command=self.reset_data, font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)

        # ============== right side image ================

        imgroomright = Image.open(r"C:\Users\kimu7\Desktop\CWk_HMS\images\image4.jpg")
        imgroomright = imgroomright.resize((450, 200), resample=Image.LANCZOS)
        self.photoimgroomright = ImageTk.PhotoImage(imgroomright)

        lblimg1 = Label(self.root, image=self.photoimgroomright, bd=4, relief=RIDGE)
        lblimg1.place(x=830, y=55, width=450, height=200)

        # ============== Tabel frame search right ================

        tabelframeright = LabelFrame(self.root,bd=2, relief=RIDGE ,text="View Details And Search System", font=("times new roman",12,"bold"))
        tabelframeright.place(x=435,y=280,width=860,height=260)

        searchby_lbl = Label(tabelframeright,text="Search By:", font=("arial",12,"bold"),bg="red",padx=2,pady=6)
        searchby_lbl.grid(row=0,column=0,padx=1)

        self.search_var = StringVar()
        search_entry = ttk.Combobox(tabelframeright,textvariable=self.search_var, font=("arial",13,"bold"),width=24,state="readonly")
        search_entry["value"]= ('contact',"room_number")
        search_entry.grid(row=0,column=1)

        self.txt_search_var = StringVar()
        searchby_entry = ttk.Entry(tabelframeright, textvariable=self.txt_search_var, width=29, font=("arial",13,"bold"))
        searchby_entry.grid(row=0,column=2)
        
        btnsearchby = Button(tabelframeright,text="Search", command=self.search_data, font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnsearchby.grid(row=0,column=3,padx=1)

        btnshowall = Button(tabelframeright,text="Shaw All", command=self.fetch_data, font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnshowall.grid(row=0,column=4,padx=1)

        # ============== details frame right ================

        details_table = LabelFrame(tabelframeright,bd=2, relief=RIDGE ,text="Details", font=("times new roman",12,"bold"))
        details_table.place(x=0,y=50,width=850,height=180)

        scroll_x = ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table,orient=VERTICAL)

        self.roomtable = ttk.Treeview(details_table,columns=("id","contact","checkin_date","checkout_date","room_number","no_of_days"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.roomtable.xview)
        scroll_y.config(command=self.roomtable.yview)

        dummy = ["contact","check_in","check_out","roomtype","room_number","no_of_days"]
        text  = ["contact","check_in","check_out","roomtype","room_number","no_of_days"]

        for i in range(len(dummy)):
            self.roomtable.heading(f"{i}", text=f"{text[i]}")
            self.roomtable.column(f"{i}", width=150)

        self.roomtable["show"]="headings"

        self.roomtable.pack(fill=BOTH,expand=1)
        self.roomtable.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    # ================= reset button ================

    def reset_data(self):
        self.contact_var.set(""),
        self.checkin_var.set(""),
        self.checkout_var.set(""),
        # self.roomtype_var.set(""),
        self.room_number.set(""),
        self.no_days_var.set(""),

    # ================= delete button ================

    def delete_data(self):
        message = messagebox.askyesno("hotel management system","Do you want to delete data",parent=self.root)
        if message > 0 :
            conn = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    password = "root",
                    database = "hotel_management_cwk"
                )
            my_cursor = conn.cursor()
            query = ("delete from room_table where contact=%s")
            value= (self.contact_var.get(),)
            my_cursor.execute(query,value)
        
        else:
            if not message:
                return
        conn.commit()
        conn.close()
        self.fetch_data()

    # ================= update button ================
 
    def update_data(self):
        if self.contact_var.get() == "" or self.checkin_var.get() == "":
            messagebox.showerror(title="Not Null Field", message="All fields are required",parent=self.root)
        else :
            try:
                conn = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    password = "root",
                    database = "hotel_management_cwk"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("""update room_table set check_in=%s, check_out=%s, roomtype=%s, room_number=%s, no_of_days=%s where contact=%s""",(
                                                                                self.checkin_var.get(),
                                                                                self.checkout_var.get(),
                                                                                self.roomtype_var.get(),
                                                                                self.room_number.get(),
                                                                                self.no_days_var.get(),
                                                                                self.contact_var.get()
                                                                                ))
                conn.commit()
                
                conn.close()
                self.fetch_data()
                messagebox.showinfo("success","Data has been Updated Successfully",parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning",f"few things went wrong :{str(es)}",parent=self.root)

    # ================= get cursor ================

    def get_cursor(self, event=""):
        cursor_row = self.roomtable.focus()
        content = self.roomtable.item(cursor_row)
        row = content["values"]

        self.contact_var.set(row[0])
        self.checkin_var.set(row[1])
        self.checkout_var.set(row[2])
        self.roomtype_var.set(row[3])
        self.room_number.set(row[4])
        self.no_days_var.set(row[5])

    # ================= add data ================

    def add_data(self):
        if self.contact_var.get() == "" or self.checkin_var.get() == "":
            messagebox.showerror(title="error", message="All field are required",parent=self.root)
        else :
            try:
                conn = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    password = "root",
                    database = "hotel_management_cwk"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("""INSERT INTO room_table
                                ( contact , check_in , check_out , roomtype , room_number , no_of_days ) 
                                VALUES (%s, %s, %s, %s, %s, %s)
                                  """, 
                                (
                    self.contact_var.get(),
                    self.checkin_var.get(),
                    self.checkout_var.get(),
                    self.roomtype_var.get(),
                    self.room_number.get(),
                    self.no_days_var.get()
                ))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("success","Data has been Successfully Saved to Database",parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning",f"few things went wrong :{str(es)}",parent=self.root)

    # ================= fetch all data ================

    def fetch_data(self):
        conn = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    password = "root",
                    database = "hotel_management_cwk"
                )
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM room_table")
        dbrows = my_cursor.fetchall()
        if len(dbrows)!= 0:
            self.roomtable.delete(*self.roomtable.get_children())

            for i in dbrows :
                self.roomtable.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ================= fetch all data by contact ================
        
    def fetch_contact(self):
        if self.contact_var.get() == "":
            messagebox.showerror("error","please enter a contact to fetch data",parent= self.root)

        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="root",database="hotel_management_cwk")
            my_cursor = conn.cursor()
            query = ("select name from customer_table where mobile = %s")
            value = (self.contact_var.get(),)
            my_cursor.execute(query,value)
            name = my_cursor.fetchone()

            if name == None :
                messagebox.showerror("error","this number not found",parent= self.root)
            else:
                conn.commit()
                conn.close()

                showdataframe = Frame(self.root,bd=5,relief=RIDGE,padx=2)
                showdataframe.place(x=455,y=55,width=370,height=200)

                lblemail = Label(showdataframe,text="Name:",font=("arial",12,"bold"))
                lblemail.place(x=0,y=0)

                data_gender = Label(showdataframe,text=name[0],font=("arial",12,"bold"))
                data_gender.place(x=110,y=0)

                conn = mysql.connector.connect(host="localhost",user="root",password="root",database="hotel_management_cwk")
                my_cursor = conn.cursor()
                query = ("select gender from customer_table where mobile = %s")
                value = (self.contact_var.get(),)
                my_cursor.execute(query,value)
                gender = my_cursor.fetchone()
                
                lblgender = Label(showdataframe,text="Gender:",font=("arial",12,"bold"))
                lblgender.place(x=0,y=30)

                data_gender = Label(showdataframe,text=gender[0],font=("arial",12,"bold"))
                data_gender.place(x=110,y=30)

                query = ("select mobile from customer_table where mobile = %s")
                value = (self.contact_var.get(),)
                my_cursor.execute(query,value)
                mobile = my_cursor.fetchone()
                
                lblmobile = Label(showdataframe,text="Mobile:",font=("arial",12,"bold"))
                lblmobile.place(x=0,y=60)

                data_mobile = Label(showdataframe,text=mobile[0],font=("arial",12,"bold"))
                data_mobile.place(x=110,y=60)

                query = ("select email from customer_table where mobile = %s")
                value = (self.contact_var.get(),)
                my_cursor.execute(query,value)
                email = my_cursor.fetchone()
                
                lblemail = Label(showdataframe,text="Email:",font=("arial",12,"bold"))
                lblemail.place(x=0,y=90)

                data_email = Label(showdataframe,text=email[0],font=("arial",12,"bold"))
                data_email.place(x=110,y=90)

                query = ("select address from customer_table where mobile = %s")
                value = (self.contact_var.get(),)
                my_cursor.execute(query,value)
                address = my_cursor.fetchone()
                
                lbladdress = Label(showdataframe,text="Address:",font=("arial",12,"bold"))
                lbladdress.place(x=0,y=120)

                data_address = Label(showdataframe,text=address[0],font=("arial",12,"bold"))
                data_address.place(x=110,y=120)

                query = ("select postal_code from customer_table where mobile = %s")
                value = (self.contact_var.get(),)
                my_cursor.execute(query,value)
                p_code = my_cursor.fetchone()
                
                lbl_p_code = Label(showdataframe,text="Postal code:",font=("arial",12,"bold"))
                lbl_p_code.place(x=0,y=150)

                data_p_code = Label(showdataframe,text=p_code[0],font=("arial",12,"bold"))
                data_p_code.place(x=110,y=150)

                conn.commit()
                conn.close()

    # ================= total time and date calculate ================

    def total(self):
        indate  = self.checkin_var.get()
        outdate = self.checkout_var.get()
        indate  = datetime.strptime(indate,"%d/%m/%Y")
        outdate = datetime.strptime(outdate,"%d/%m/%Y")
        self.no_days_var.set(abs(outdate-indate).days)

        if self.roomtype_var.get() == "Deluxe":
            charge = float(700)
            days = float(self.no_days_var.get())
            t_charge = float(charge*days)
            sub_t = str("%0.2f"%(t_charge))
            tax = str("%0.2f"%(t_charge*0.18))
            grand_t = str("%0.2f"%(float(sub_t)+float(tax)))

            self.paid_tax_var.set(tax)
            self.sub_total_amt_var.set(sub_t)
            self.total_amt_var.set(grand_t)
            

        elif self.roomtype_var.get() == "General":
            charge = float(800)
            days = float(self.no_days_var.get())
            t_charge = float(charge*days)
            sub_t = str("%0.2f"%(t_charge))
            tax = str("%0.2f"%(t_charge*0.18))
            grand_t = str("%0.2f"%(float(sub_t)+float(tax)))

            self.paid_tax_var.set(tax)
            self.sub_total_amt_var.set(sub_t)
            self.total_amt_var.set(grand_t)
            

        elif self.roomtype_var.get() == "Full Deluxe":
            charge = float(900)
            days = float(self.no_days_var.get())
            t_charge = float(charge*days)
            sub_t = str("%0.2f"%(t_charge))
            tax = str("%0.2f"%(t_charge*0.18))
            grand_t = str("%0.2f"%(float(sub_t)+float(tax)))

            self.paid_tax_var.set(tax)
            self.sub_total_amt_var.set(sub_t)
            self.total_amt_var.set(grand_t)
            

        elif self.roomtype_var.get() == "Joint":
            charge = float(1000)
            days = float(self.no_days_var.get())
            t_charge = float(charge*days)
            sub_t = str("%0.2f"%(t_charge))
            tax = str("%0.2f"%(t_charge*0.18))
            grand_t = str("%0.2f"%(float(sub_t)+float(tax)))

            self.paid_tax_var.set(tax)
            self.sub_total_amt_var.set(sub_t)
            self.total_amt_var.set(grand_t)
            
    # ================= update room number ================
            
    def search_data(self):
        conn = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    password = "root",
                    database = "hotel_management_cwk"
                )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room_table where " + str(self.search_var.get()) + " like '%" + str(self.txt_search_var.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.roomtable.delete(*self.roomtable.get_children())
            for i in rows :
                self.roomtable.insert("",END,values=i)
            conn.commit()
            conn.close()

        else :
            messagebox.showerror("error","data not available.",parent= self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
