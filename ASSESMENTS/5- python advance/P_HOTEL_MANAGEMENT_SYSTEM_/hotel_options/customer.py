from tkinter import *
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class Cust_Win :
    def __init__(self,root):
        self.root = root
        self.root.title("Hspital Management System")
        self.root.geometry("1295x550+230+220")

        # =================== variables ===================

        self.id_var = StringVar()
        self.ref_var = StringVar()
        x= random.randint(1000,9999)
        self.ref_var.set(str(x))

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
        
        # ============== title ==================

        lbl_title = Label(self.root,text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        # ============== label frame left ================
        labelframeleft = LabelFrame(self.root,bd=2, relief=RIDGE ,text="CUSTOMER DETAILS", font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)


        # ============== label and entries ================


        # customer Reference
        lbl_cust_ref = Label(labelframeleft,text="Customer Ref.", font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref = ttk.Entry(labelframeleft, width=29, font=("arial",13,"bold"),textvariable=self.ref_var,state="readonly")
        entry_ref.grid(row=0,column=1)

        # customer name
        cname = Label(labelframeleft,text="Customer's Name", font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        cname_entry = ttk.Entry(labelframeleft,textvariable=self.cname_var, width=29, font=("arial",13,"bold"))
        cname_entry.grid(row=1,column=1)

        # mother name
        mother_name = Label(labelframeleft,text="Mother's Name", font=("arial",12,"bold"),padx=2,pady=6)
        mother_name.grid(row=2,column=0,sticky=W)

        mname_entry = ttk.Entry(labelframeleft, width=29, textvariable=self.mother_var,font=("arial",13,"bold"))
        mname_entry.grid(row=2,column=1)

        # gender
        gender_lbl = Label(labelframeleft,text="Gender.", font=("arial",12,"bold"),padx=2,pady=6)
        gender_lbl.grid(row=3,column=0,sticky=W)

        gender_entry = ttk.Combobox(labelframeleft,font=("arial",13,"bold"),width=27,textvariable=self.gender_var,state="readonly")
        gender_entry["value"]= ('Male',"Female","Other")
        gender_entry.current(0)
        gender_entry.grid(row=3,column=1)

        # postal code
        postcode_lbl = Label(labelframeleft,text="Postal Code", font=("arial",12,"bold"),padx=2,pady=6)
        postcode_lbl.grid(row=4,column=0,sticky=W)

        pcode_entry = ttk.Entry(labelframeleft,textvariable=self.post_var, width=29, font=("arial",13,"bold"))
        pcode_entry.grid(row=4,column=1)

        # mobile
        mobile_lbl = Label(labelframeleft,text="Mobile", font=("arial",12,"bold"),padx=2,pady=6)
        mobile_lbl.grid(row=5,column=0,sticky=W)

        mobile_entry = ttk.Entry(labelframeleft, width=29, textvariable=self.mobile_var,font=("arial",13,"bold"))
        mobile_entry.grid(row=5,column=1)

        # email
        email_lbl = Label(labelframeleft,text="Email", font=("arial",12,"bold"),padx=2,pady=6)
        email_lbl.grid(row=6,column=0,sticky=W)

        email_entry = ttk.Entry(labelframeleft,textvariable=self.email_var, width=29, font=("arial",13,"bold"))
        email_entry.grid(row=6,column=1)

        # nationality
        nationality_lbl = Label(labelframeleft,text="Nationality", font=("arial",12,"bold"),padx=2,pady=6)
        nationality_lbl.grid(row=7,column=0,sticky=W)

        nation_entry = ttk.Combobox(labelframeleft,font=("arial",13,"bold"),textvariable=self.nationality_var,width=27,state="readonly")
        nation_entry["value"]= ('Indian',"American","British")
        nation_entry.current(0)
        nation_entry.grid(row=7,column=1)

        # ID Proof
        idproof_lbl = Label(labelframeleft,text="ID Proof", font=("arial",12,"bold"),padx=2,pady=6)
        idproof_lbl.grid(row=8,column=0,sticky=W)

        idproof_entry = ttk.Combobox(labelframeleft,textvariable=self.idproof_var,font=("arial",13,"bold"),width=27,state="readonly")
        idproof_entry["value"]= ('Adhar Card',"Licence","Pan Card", "Voter ID")
        idproof_entry.current(0)
        idproof_entry.grid(row=8,column=1)

        # ID Number
        idnumber_lbl = Label(labelframeleft,text="ID Number", font=("arial",12,"bold"),padx=2,pady=6)
        idnumber_lbl.grid(row=9,column=0,sticky=W)

        idnumber_emtry = ttk.Entry(labelframeleft, width=29,textvariable=self.idnum_var, font=("arial",13,"bold"))
        idnumber_emtry.grid(row=9,column=1)

        # Address
        address_lbl = Label(labelframeleft,text="Address", font=("arial",12,"bold"),padx=2,pady=6)
        address_lbl.grid(row=10,column=0,sticky=W)

        address_entry = ttk.Entry(labelframeleft, width=29, textvariable=self.address_var,font=("arial",13,"bold"))
        address_entry.grid(row=10,column=1)

        # ======================= button ===========================

        btn_frame_cust = Frame(labelframeleft,bd=4,relief=RIDGE)
        btn_frame_cust.place(x=0,y=400,width=412,height=40)

        btnadd = Button(btn_frame_cust, text="Add", command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate = Button(btn_frame_cust,text="Update",command=self.update_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete = Button(btn_frame_cust,text="Delete",command=self.delete_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset = Button(btn_frame_cust,text="Reset",command=self.reset_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)

        # ============== Tabel frame search right ================

        tabelframeright = LabelFrame(self.root,bd=2, relief=RIDGE ,text="View Details And Search System", font=("times new roman",12,"bold"))
        tabelframeright.place(x=435,y=50,width=860,height=490)

        searchby_lbl = Label(tabelframeright,text="Search By:", font=("arial",12,"bold"),bg="red",padx=2,pady=6)
        searchby_lbl.grid(row=0,column=0,padx=1)

        self.search_var = StringVar()
        search_entry = ttk.Combobox(tabelframeright,textvariable=self.search_var,font=("arial",13,"bold"),width=24,state="readonly")
        search_entry["value"]= ('mobile',"ref")
        search_entry.grid(row=0,column=1)


        self.txt_search_var = StringVar()
        searchby_entry = ttk.Entry(tabelframeright,textvariable=self.txt_search_var, width=29, font=("arial",13,"bold"))
        searchby_entry.grid(row=0,column=2)
        
        btnsearchby = Button(tabelframeright,text="Search",command=self.search_data, font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnsearchby.grid(row=0,column=3,padx=1)

        btnshowall = Button(tabelframeright,text="Shaw All",command=self.fetch_data, font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnshowall.grid(row=0,column=4,padx=1)


        # ============== details frame right ================

        details_table = LabelFrame(tabelframeright,bd=2, relief=RIDGE ,text="Details", font=("times new roman",12,"bold"))
        details_table.place(x=0,y=50,width=850,height=350)

        scroll_x = ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_detail_table = ttk.Treeview(details_table,columns=("id","ref","Name","Mother's Name","Gender","Postal Code","Mobile","Email","Nationality","ID Proof","ID Number", "Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_detail_table.xview)
        scroll_y.config(command=self.cust_detail_table.yview)

        dummy = ["id", "ref", "name", "mothers_name", "gender", "postal_code", "mobile", "email", "nationality", "id_proof", "id_number", "address"]
        text = ["ID", "Reference", "Name", "Mother's Name", "Gender", "Postal Code", "Mobile", "Email", "Nationality", "ID Proof", "ID Number", "Address"]

        for i in range(len(dummy)):
            self.cust_detail_table.heading(f"{i}", text=f"{text[i]}")
            self.cust_detail_table.column(f"{i}", width=150)

        self.cust_detail_table["show"]="headings"

        self.cust_detail_table.pack(fill=BOTH,expand=1)
        self.cust_detail_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.mobile_var.get() == "" or self.mother_var.get() == "":
            messagebox.showerror(title="Not Null Field", message="Mobile Number and Mother's name field are required",parent=self.root)
        else :
            try:
                conn = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    password = "root",
                    database = "hotel_management_cwk"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("""INSERT INTO customer_table
                                (ref, name, mothers_name, gender, postal_code, mobile, email, nationality, address, id_proof, id_number) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                  """, 
                                (
                    self.ref_var.get(),
                    self.cname_var.get(),
                    self.mother_var.get(),
                    self.gender_var.get(),
                    self.post_var.get(),
                    self.mobile_var.get(),
                    self.email_var.get(),
                    self.nationality_var.get(),
                    self.address_var.get(),
                    self.idproof_var.get(),
                    self.idnum_var.get()    
                ))
                conn.commit()
                
                conn.close()
                self.fetch_data()
                messagebox.showinfo("success","Data has been Successfully Saved to Database",parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning",f"few things went wrong :{str(es)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    password = "root",
                    database = "hotel_management_cwk"
                )
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM customer_table")
        dbrows = my_cursor.fetchall()
        if len(dbrows)!= 0:
            self.cust_detail_table.delete(*self.cust_detail_table.get_children())

            for i in dbrows :
                self.cust_detail_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.cust_detail_table.focus()
        content = self.cust_detail_table.item(cursor_row)
        row = content["values"]

        self.ref_var.set(row[1])
        self.cname_var.set(row[2])
        self.mother_var.set(row[3])
        self.gender_var.set(row[4])
        self.post_var.set(row[5])
        self.mobile_var.set(row[6])
        self.email_var.set(row[7])
        self.nationality_var.set(row[8])
        self.idproof_var.set(row[9])
        self.idnum_var.set(row[10])
        self.address_var.set(row[11])

    def update_data(self):
        if self.mobile_var.get() == "" or self.mother_var.get() == "":
            messagebox.showerror(title="Not Null Field", message="Mobile Number and Mother's name field are required",parent=self.root)
        else :
            try:
                conn = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    password = "root",
                    database = "hotel_management_cwk"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("""update customer_table set name=%s, mothers_name=%s, gender=%s, postal_code=%s, mobile=%s, email=%s, nationality=%s, address=%s, id_proof=%s, id_number=%s where ref=%s""",(
                                                                                self.cname_var.get(),
                                                                                self.mother_var.get(),
                                                                                self.gender_var.get(),
                                                                                self.post_var.get(),
                                                                                self.mobile_var.get(),
                                                                                self.email_var.get(),
                                                                                self.nationality_var.get(),
                                                                                self.address_var.get(),
                                                                                self.idproof_var.get(),
                                                                                self.idnum_var.get(),    
                                                                                self.ref_var.get()
                                                                                            ))
                conn.commit()
                
                conn.close()
                self.fetch_data()
                messagebox.showinfo("success","Data has been Successfully Updated to Database",parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning",f"few things went wrong :{str(es)}",parent=self.root)

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
            query = ("delete from customer_table where ref=%s")
            value= (self.ref_var.get(),)
            my_cursor.execute(query,value)
        
        else:
            if not message:
                return
        conn.commit()
        conn.close()
        self.fetch_data()

    def reset_data(self):
        # self.ref_var.set(""),
        self.cname_var.set(""),
        self.mother_var.set(""),
        # self.gender_var.set(""),
        self.post_var.set(""),
        self.mobile_var.set(""),
        self.email_var.set(""),
        # self.nationality_var.set(""),
        # self.idproof_var.set(""),
        self.idnum_var.set(""),
        self.address_var.set(""),

        x= random.randint(1000,99999)
        self.ref_var.set(str(x))

    def search_data(self):
        conn = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    password = "root",
                    database = "hotel_management_cwk"
                )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer_table where " + str(self.search_var.get()) + " like '%" + str(self.txt_search_var.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_detail_table.delete(*self.cust_detail_table.get_children())
            for i in rows :
                self.cust_detail_table.insert("",END,values=i)
            conn.commit()
            conn.close()

        else :
            messagebox.showerror("error","data not available.",parent= self.root)
        

if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
