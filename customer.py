from cgitb import text
from tkinter import*
from tkinter import messagebox
import random
from tkinter import ttk
import mysql.connector
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

root = Tk()
root.geometry("1600x800+0+0")
root.title("Customer control")
root.config(background='dark turquoise')

##variable

var_acc_no = StringVar()
x = random.randint(100000000, 999999999)
var_acc_no.set(str(x))

var_date = StringVar()
var_opening_bal = StringVar()
var_acc_holder_name = StringVar()
var_father_name = StringVar()
var_mother_name = StringVar()
var_dob = StringVar()
var_email = StringVar()
var_mobile_no = StringVar()
var_address = StringVar()
var_state = StringVar()
var_district = StringVar()
var_pincode = StringVar()
var_document_no = StringVar()


######Search Type
search_frame = LabelFrame(root, text="Search staff",font=("times new roman",18,"bold"),bg="dark turquoise", fg="gray20", bd=5)
search_frame.place(x=1100, y=280, width=420, height=170)

select_type_lbl = Label(root, text="Search by : ",font=("times new roman",18,"bold"),fg="gray20",bg="dark turquoise")
select_type_lbl.place(x=1110, y=310)

var_search_type = StringVar()
select_type = ttk.Combobox(root, textvariable=var_search_type, width=25, font=("times new roman",15), state="readonly")
select_type['values']=("accno","accholdername","mobileno","email","dob")
select_type.place(x=1235,y=310)

txt_search = StringVar()
type_entry = Entry(root, textvariable=txt_search,font=("times new roman",18,"bold"),bg="gray20",fg="dark turquoise",width=22)
type_entry.place(x=1235, y=350)

###Top frame
top_frame = Frame(root,bg="gray20")
top_frame.place(x=0,y=0,width=1550,height=90)

staff_lbl = Label(top_frame, text="Customer Control Dashboard", bg="gray20", fg="dark turquoise", font=("times new roman",45,"bold"))
staff_lbl.place(x=420, y= 5)

#Customer Information
labelframe = LabelFrame(root, text="Customer Information", fg="gray20",bg="dark turquoise",width="510",height="185",font=("times new roman",20,"bold"),bd=5)
labelframe.place(x=10,y=100)

acc_type = Label(labelframe,text="Account Type   ", font=("times new roman",15,"bold"),bg="dark turquoise", fg="gray20")
acc_type.place(x=10, y=10)

var_acc_type = StringVar()
txt_acc_type = ttk.Combobox(labelframe, textvariable=var_acc_type,width="23", font=("times new roman",15), state="readonly")
txt_acc_type['values']=("Savings","Current")
txt_acc_type.place(x=230,y=10)

acc_date = Label(labelframe,text="Date   ", font=("times new roman",15,"bold"),bg="dark turquoise", fg="gray20")
acc_date.place(x=10, y=60)

txt_acc_date = Entry(labelframe,font=("times new roman",15),bg="gray20",fg="dark turquoise",width="25",textvariable=var_date)
txt_acc_date.place(x=230, y=60)

opening_bal = Label(labelframe,text="Opening Balance   ", font=("times new roman",15,"bold"),bg="dark turquoise", fg="gray20")
opening_bal.place(x=10, y=110)

txt_opening_bal = Entry(labelframe,font=("times new roman",15),bg="gray20",fg="dark turquoise",width="25",textvariable=var_opening_bal)
txt_opening_bal.place(x=230, y=110)


###personal information

labelframe1 = LabelFrame(root, text="Personal Information", fg="gray20",bg="dark turquoise",width="510",height="335",font=("times new roman",20,"bold"),bd=5)
labelframe1.place(x=10,y=295)

acc_no = Label(labelframe1,text="Account No   ", font=("times new roman",15,"bold"),bg="dark turquoise", fg="gray20")
acc_no.place(x=10, y=10)

txt_acc_no = Entry(labelframe1,font=("times new roman",15),bg="gray20",fg="dark turquoise",width="25",textvariable=var_acc_no)
txt_acc_no.place(x=230, y=10)

acc_holder_name = Label(labelframe1,text="Account Holder's Name   ", font=("times new roman",15,"bold"),bg="dark turquoise", fg="gray20")
acc_holder_name.place(x=10, y=60)

txt_acc_holder_name = Entry(labelframe1,font=("times new roman",15),bg="gray20",fg="dark turquoise",width="25",textvariable=var_acc_holder_name)
txt_acc_holder_name.place(x=230, y=60)

acc_father_name = Label(labelframe1,text="Father's Name   ", font=("times new roman",15,"bold"),bg="dark turquoise", fg="gray20")
acc_father_name.place(x=10, y=110)

txt_father_name = Entry(labelframe1,font=("times new roman",15),bg="gray20",fg="dark turquoise",width="25",textvariable=var_father_name)
txt_father_name.place(x=230, y=110)

acc_mother_name = Label(labelframe1,text="Mother's Name   ", font=("times new roman",15,"bold"),bg="dark turquoise", fg="gray20")
acc_mother_name.place(x=10, y=160)

txt_mother_name = Entry(labelframe1,font=("times new roman",15),bg="gray20",fg="dark turquoise",width="25",textvariable=var_mother_name)
txt_mother_name.place(x=230, y=160)

acc_dob = Label(labelframe1,text="Date Of Birth   ", font=("times new roman",15,"bold"),bg="dark turquoise", fg="gray20")
acc_dob.place(x=10, y=210)

txt_dob = Entry(labelframe1,font=("times new roman",15),bg="gray20",fg="dark turquoise",width="25",textvariable=var_dob)
txt_dob.place(x=230, y=210)

acc_gender = Label(labelframe1,text="Gender   ", font=("times new roman",15,"bold"),bg="dark turquoise", fg="gray20")
acc_gender.place(x=10, y=260)

var_acc_gender = StringVar()
txt_acc_gender = ttk.Combobox(labelframe1, textvariable=var_acc_gender,width="23", font=("times new roman",15), state="readonly")
txt_acc_gender['values']=("Male","Female")
txt_acc_gender.place(x=230,y=260)

###Contact Details

labelframe2 = LabelFrame(root, text="Contact Information", fg="gray20",bg="dark turquoise",width="510",height="340",font=("times new roman",20,"bold"),bd=5)
labelframe2.place(x=580,y=100)

acc_gmail = Label(labelframe2,text="Email   ", font=("times new roman",15,"bold"),bg="dark turquoise", fg="gray20")
acc_gmail.place(x=10, y=10)

txt_acc_gmail = Entry(labelframe2,font=("times new roman",15),bg="gray20",fg="dark turquoise",width="25",textvariable=var_email)
txt_acc_gmail.place(x=210, y=10)

acc_mobile_no = Label(labelframe2,text="Mobile Number   ", font=("times new roman",15,"bold"),bg="dark turquoise", fg="gray20")
acc_mobile_no.place(x=10, y=60)

txt_mobile_no = Entry(labelframe2,font=("times new roman",15),bg="gray20",fg="dark turquoise",width="25",textvariable=var_mobile_no)
txt_mobile_no.place(x=210, y=60)


acc_address = Label(labelframe2,text="Address   ", font=("times new roman",15,"bold"),bg="dark turquoise", fg="gray20")
acc_address.place(x=10, y=110)

txt_address = Entry(labelframe2,font=("times new roman",15),bg="gray20",fg="dark turquoise",width="25",textvariable=var_address)
txt_address.place(x=210, y=110)

acc_state = Label(labelframe2,text="State   ", font=("times new roman",15,"bold"),bg="dark turquoise", fg="gray20")
acc_state.place(x=10, y=160)

txt_state = Entry(labelframe2,font=("times new roman",15),bg="gray20",fg="dark turquoise",width="25",textvariable=var_state)
txt_state.place(x=210, y=160)

acc_district = Label(labelframe2,text="District   ", font=("times new roman",15,"bold"),bg="dark turquoise", fg="gray20")
acc_district.place(x=10, y=210)

txt_district = Entry(labelframe2,font=("times new roman",15),bg="gray20",fg="dark turquoise",width="25",textvariable=var_district)
txt_district.place(x=210, y=210)

acc_pincode = Label(labelframe2,text="Pincode   ", font=("times new roman",15,"bold"),bg="dark turquoise", fg="gray20")
acc_pincode.place(x=10, y=260)

txt_pincode = Entry(labelframe2,font=("times new roman",15),bg="gray20",fg="dark turquoise",width="25",textvariable=var_pincode)
txt_pincode.place(x=210, y=260)


###Identity details
labelframe3 = LabelFrame(root, text="Identity Information", fg="gray20",bg="dark turquoise",width="510",height="160",font=("times new roman",20,"bold"),bd=5)
labelframe3.place(x=580,y=450)

acc_id_type = Label(labelframe3,text="ID Type   ", font=("times new roman",15,"bold"),bg="dark turquoise", fg="gray20")
acc_id_type.place(x=10, y=10)

var_id_type = StringVar()
txt_id_type = ttk.Combobox(labelframe3, textvariable=var_id_type,width="23", font=("times new roman",15), state="readonly")
txt_id_type['values']=("Taxpayer","Passport","Alien")
txt_id_type.place(x=210,y=10)

acc_document_no = Label(labelframe3,text="Document no   ", font=("times new roman",15,"bold"),bg="dark turquoise", fg="gray20")
acc_document_no.place(x=10, y=60)

txt_document_no = Entry(labelframe3,font=("times new roman",15),bg="gray20",fg="dark turquoise",width="25",textvariable=var_document_no)
txt_document_no.place(x=210, y=60)



def save_data():
    if var_acc_type.get() == "" or var_email=="":
        messagebox.showerror("Error","All fields are required")
    else:
        try:
            conn = mysql.connector.connect(host = "localhost", username="root", password="",port=3306,database="Bank")
            cur = conn.cursor()
            cur.execute("Insert into customer(accounttype,date,openingbal,accno,accholdername,fathername,mothername,dob,gender,email,mobileno,address,state,district,pincode,idtype,documentno) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                var_acc_type.get(),
                var_date.get(),
                var_opening_bal.get(),
                var_acc_no.get(),
                var_acc_holder_name.get(),
                var_father_name.get(),
                var_mother_name.get(),
                var_dob.get(),
                var_acc_gender.get(),
                var_email.get(),
                var_mobile_no.get(),
                var_address.get(),
                var_state.get(),
                var_district.get(),
                var_pincode.get(),
                var_id_type.get(),
                var_document_no.get()
            ))
            conn.commit()
            fetch_data()
            conn.close()

            messagebox.showinfo("success","Successfully registered")
        except Exception as es:
            messagebox.showerror("Error",f"error due to : {str(es)}")

def fetch_data():
    conn = mysql.connector.connect(host = "localhost", username="root", password="",port=3306,database="Bank")
    cur = conn.cursor()
    cur.execute("select * from customer")
    rows = cur.fetchall()
    if len(rows) != 0:
        customer_details_table.delete(*customer_details_table.get_children())
        for i in rows:
            customer_details_table.insert("",END,values=i)
    conn.commit()
    conn.close()


def search_data():
    conn = mysql.connector.connect(host = "localhost", username="root", password="",port=3306,database="Bank")
    cur = conn.cursor()
    cur.execute("select * from customer where "+str(var_search_type.get())+" LIKE '%"+str(txt_search.get())+"%'")
    rows = cur.fetchall()
    if len(rows) != 0:
        customer_details_table.delete(*customer_details_table.get_children())
        for i in rows:
            customer_details_table.insert("",END,values=i)
    conn.commit()
    conn.close()

def get_cursor(event=""):
    cursor_row = customer_details_table.focus()
    content = customer_details_table.item(cursor_row)
    row= content["values"]

    var_acc_type.set(row[0]),
    var_date.set(row[1]),
    var_opening_bal.set(row[2]),
    var_acc_no.set(row[3])
    var_acc_holder_name.set(row[4]),
    var_father_name.set(row[5]),
    var_mother_name.set(row[6]),
    var_dob.set(row[7]),
    var_acc_gender.set(row[8]),
    var_email.set(row[9]),
    var_mobile_no.set(row[10])
    var_address.set(row[11])
    var_state.set(row[12])
    var_district.set(row[13])
    var_pincode.set(row[14])
    var_id_type.set(row[15])
    var_document_no.set(row[16])

def clear():
    var_acc_type.set("")
    var_date.set("")
    var_opening_bal.set("")
    var_acc_no.set("")
    var_acc_holder_name.set("")
    var_father_name.set("")
    var_mother_name.set("")
    var_dob.set("")
    var_acc_gender.set("")
    var_email.set("")
    var_mobile_no.set("")
    var_address.set("")
    var_state.set("")
    var_district.set("")
    var_pincode.set("")
    var_id_type.set("")
    var_document_no.set("")

def update():
    conn = mysql.connector.connect(host = "localhost", username="root", password="",port=3306,database="Bank")
    cur = conn.cursor()
    cur.execute("update customer set accounttype=%s,date=%s,openingbal=%s,accno=%s,accholdername=%s,fathername=%s,mothername=%s,dob=%s,gender=%s,email=%s,mobileno=%s,address=%s,state=%s,district=%s,pincode=%s,idtype=%s,documentno=%s",(
        var_acc_type.get(),
        var_date.get(),
        var_opening_bal.get(),
        var_acc_no.get(),
        var_acc_holder_name.get(),
        var_father_name.get(),
        var_mother_name.get(),
        var_dob.get(),
        var_acc_gender.get(),
        var_email.get(),
        var_mobile_no.get(),
        var_address.get(),
        var_state.get(),
        var_district.get(),
        var_pincode.get(),
        var_id_type.get(),
        var_document_no.get()
    ))
    conn.commit()
    fetch_data()
    conn.close()
    messagebox.showinfo("success","success")


def delete():
    delete = messagebox.askyesno("Staff Control","Do you want to delete this staff")
    if delete>0:
        conn = mysql.connector.connect(host = "localhost", username="root", password="",port=3306,database="Bank")
        cur = conn.cursor()
        query = "delete from customer where accno=%s"
        value =(var_acc_no.get(),)
        cur.execute(query, value)
    else:
        if not delete:
            return
    conn.commit()
    fetch_data()
    conn.close()

def dashboard():
    root.destroy()
    import main



###show table details
show_frame = Frame(root,bg="gray20")
show_frame.place(x=12,y=640,width=1500,height=150)

scroll_x = ttk.Scrollbar(show_frame,orient=HORIZONTAL)

scroll_y = ttk.Scrollbar(show_frame, orient=VERTICAL)


customer_details_table=ttk.Treeview(show_frame, columns=("accounttype","date","openingbal","accno","accholdername","fathername","mothername","dob","gender","email","mobileno","address","state","district","pincode","idtype","documentno"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_x.config(command=customer_details_table.xview)
scroll_y.config(command=customer_details_table.yview)

customer_details_table.heading("accounttype", text="Account Type")
customer_details_table.heading("date", text="Date")
customer_details_table.heading("openingbal",text="Opening Balance")
customer_details_table.heading("accno", text="Account No")
customer_details_table.heading("accholdername", text="Account Holder Name")
customer_details_table.heading("fathername", text="Father Name")
customer_details_table.heading("mothername",text="Mother Name")
customer_details_table.heading("dob",text="DOB")
customer_details_table.heading("gender",text="Gender")
customer_details_table.heading("email",text="Email")
customer_details_table.heading("mobileno", text="Mobile No")
customer_details_table.heading("address", text="Address")
customer_details_table.heading("state", text="State")
customer_details_table.heading("district", text="District")
customer_details_table.heading("pincode", text="Pincode")
customer_details_table.heading("idtype", text="ID Type")
customer_details_table.heading("documentno", text="Document No")

customer_details_table["show"] = "headings"
customer_details_table.pack(fill=BOTH,expand=1)
fetch_data()
customer_details_table.bind("<ButtonRelease-1>",get_cursor)

#####Right Frame
btn_frame = Frame(root, bg="gray20")
btn_frame.place(x=1100, y=465, width=420, height=170)


save_btn = Button(root, text="Save",bg="dark turquoise", fg="gray20", font=("times new roman",18,"bold"),width=10, activebackground="dark turquoise", activeforeground="gray20",command=save_data)
save_btn.place(x=1150, y=475)

update_btn = Button(root, text="Update",bg="dark turquoise", fg="gray20", font=("times new roman",18,"bold"),width=10, activebackground="dark turquoise", activeforeground="gray20",command=update)
update_btn.place(x=1350, y=475)


clear_btn = Button(root, text="Clear",bg="dark turquoise", fg="gray20", font=("times new roman",18,"bold"),width=10, activebackground="dark turquoise", activeforeground="gray20",command=clear)
clear_btn.place(x=1150, y=530)

delete_btn = Button(root, text="Delete",bg="dark turquoise", fg="gray20", font=("times new roman",18,"bold"),width=10, activebackground="dark turquoise", activeforeground="gray20",command=delete)
delete_btn.place(x=1350, y=530)

dashboard = Button(root, font=("times new roman",18,"bold"),bg="dark turquoise",fg="gray20",text="Dashboard",height=1,width=17,command=dashboard)
dashboard.place(x=1200,y=580)

search_btn = Button(root, font=("times new roman",18,"bold"),fg="dark turquoise",bg="gray20",text="Search", command=search_data,height=1,width=17)
search_btn.place(x=1240,y=390)



b1 = Button(root, text='Upload Image',fg="dark turquoise", bg="gray20", font=("times new roman",18,"bold"),width=10, activebackground="dark turquoise", activeforeground="gray20",command = lambda:upload_file())
b1.place(x=1100,y=120)

b3 = Button(root,bg="white", font=("times new roman",18,"bold"),width=14,height=6)
b3.place(x=1280,y=100)


def upload_file():
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img=Image.open(filename)
    img_resized=img.resize((150,150)) # new width & height
    img=ImageTk.PhotoImage(img_resized)
    b2 =Button(root,image=img) # using Button 
    b2.place(x=1300,y=100)

root.mainloop()
