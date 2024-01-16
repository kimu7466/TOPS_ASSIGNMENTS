from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class room_arrange :
    def __init__(self,root):
        self.root = root
        self.root.title("Hspital Management System")
        self.root.geometry("1295x550+230+220")

        self.floor_var = StringVar()
        self.room_no_var = StringVar()
        self.room_type_var = StringVar()

        # ============== title ==================

        lbl_title = Label(self.root,text="ADD ROOMS", font=("times new roman", 18, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # ============== label frame left ================

        labelframeleft = LabelFrame(self.root,bd=2, relief=RIDGE ,text="ROOM DETAILS", font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=400)

        # ============== label and entries ================

        # add floor
        floor_lbl = Label(labelframeleft,text="Floor", font=("arial",17,"bold"),padx=5,pady=16)
        floor_lbl.grid(row=0,column=0,sticky=W)

        floor_entry = ttk.Entry(labelframeleft, textvariable=self.floor_var, width=12, font=("arial",17,"bold"))
        floor_entry.grid(row=0,column=1,sticky=W)
        
        # add room number
        room_no_lbl = Label(labelframeleft,text="Room Number", font=("arial",17,"bold"),padx=5,pady=16)
        room_no_lbl.grid(row=1,column=0,sticky=W)

        room_no_entry = ttk.Entry(labelframeleft, textvariable=self.room_no_var, width=12, font=("arial",17,"bold"))
        room_no_entry.grid(row=1,column=1,sticky=W)
        
        # room type
        contact_room_type = Label(labelframeleft,text="Room Type", font=("arial",17,"bold"),padx=5,pady=16)
        contact_room_type.grid(row=2,column=0,sticky=W)

        room_type_entry = ttk.Combobox(labelframeleft, textvariable=self.room_type_var, width=12, font=("arial",17,"bold"), state="readonly")
        room_type_entry['value']=("Deluxe","General","Full Deluxe","Joint")
        room_type_entry.current(0)
        room_type_entry.grid(row=2,column=1,sticky=W)

        # ======================= button ===========================

        btn_frame = Frame(labelframeleft,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=250,width=412,height=40)

        btnadd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate = Button(btn_frame,text="Update", command=self.update_data, font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete = Button(btn_frame,text="Delete", command=self.delete_data, font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset = Button(btn_frame,text="Reset", command=self.reset_data, font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)

        # ============== Tabel frame search right ================

        tabelframeright = LabelFrame(self.root,bd=2, relief=RIDGE ,text="Show Room Details", font=("times new roman",12,"bold"))
        tabelframeright.place(x=435,y=50,width=860,height=400)

        # ============== details frame right ================

        scroll_x = ttk.Scrollbar(tabelframeright,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tabelframeright,orient=VERTICAL)

        self.displayroomtable = ttk.Treeview(tabelframeright,columns=(["Floor","RoomNo","RoomType"]),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.displayroomtable.xview)
        scroll_y.config(command=self.displayroomtable.yview)

        dummy = ["Floor","RoomNo","RoomType"]
        text  = ["Floor","RoomNo","RoomType"]

        for i in range(len(dummy)):
            self.displayroomtable.heading(f"{i}", text=f"{text[i]}")
            self.displayroomtable.column(f"{i}", width=200)

        self.displayroomtable["show"]="headings"

        self.displayroomtable.pack(fill=BOTH,expand=1)
        self.displayroomtable.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    # ================= add data ================

    def add_data(self):
        if self.floor_var.get() == "" or self.room_no_var.get() == "" or self.room_type_var.get() == "":
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
                my_cursor.execute("""INSERT INTO add_room
                                ( Floor , RoomNo , RoomType ) 
                                VALUES (%s, %s, %s)
                                  """, 
                                (
                    self.floor_var.get(),
                    self.room_no_var.get(),
                    self.room_type_var.get(),
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
        my_cursor.execute("SELECT * FROM add_room")
        dbrows = my_cursor.fetchall()
        if len(dbrows)!= 0:
            self.displayroomtable.delete(*self.displayroomtable.get_children())

            for i in dbrows :
                self.displayroomtable.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ================= get cursor ================

    def get_cursor(self, event=""):
        cursor_row = self.displayroomtable.focus()
        content = self.displayroomtable.item(cursor_row)
        row = content["values"]

        self.floor_var.set(row[0])
        self.room_no_var.set(row[1])
        self.room_type_var.set(row[2])

    # # ================= update button ================
 
    def update_data(self):
        if self.floor_var.get() == "" or self.room_no_var.get() == "" or self.room_type_var.get() == "":
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
                my_cursor.execute("""update add_room set Floor=%s , RoomType=%s where RoomNo=%s""",(
                                                                                self.floor_var.get(),
                                                                                self.room_type_var.get(),
                                                                                self.room_no_var.get()
                                                                                ))
                conn.commit()
                
                conn.close()
                self.fetch_data()
                messagebox.showinfo("success","Data has been Updated Successfully",parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning",f"few things went wrong :{str(es)}",parent=self.root)

    # ================= reset button ================

    def reset_data(self):
        self.floor_var.set(""),
        self.room_no_var.set(""),
        self.room_type_var.set(""),
        
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
            query = ("delete from add_room where RoomNo=%s")
            value= (self.room_no_var.get(),)
            my_cursor.execute(query,value)
        
        else:
            if not message:
                return
        conn.commit()
        conn.close()
        self.fetch_data()

if __name__ == "__main__":
    root = Tk()
    obj = room_arrange(root)
    root.mainloop()
