from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

root = Tk()
root.geometry("1548x800+0+0")
root.title("Bank login")
root.config(background='dark turquoise')

#####Functions
def staff_control():
    root.destroy()
    import staff

def customer_control():
    root.destroy()
    import customer

def deposite_window():
    root.destroy()
    import deposite


# def depositeWindow():
#     global newWindow
#     newWindow = Toplevel(root)
#     newWindow.title("Deposite")
#     newWindow.geometry("550x220+570+250")
#     newWindow.resizable(width=False,height=False)
#     newWindow.config(background='dark turquoise')
#     Label(newWindow,text ="Enter Account No  : ",font=("times new roman",18,"bold"),bg="dark turquoise", fg="gray20").place(x=10,y=40)
#     global txt_accno
#     txt_accno = Entry(newWindow,font=("times new roman",18),bg="gray20",fg="dark turquoise",width="25")
#     txt_accno.place(x=230,y=40)
#     Button(newWindow, text="Continue",fg="dark turquoise", bg="gray20", font=("times new roman",18,"bold"),width=20,command=continue_btn).place(x=140,y=120)


# def continue_btn():
#     if txt_accno.get() =="":
#         messagebox.showerror("Error", "All fields are required")
#     else:
#         try:
#             conn = mysql.connector.connect(host='localhost',username='root', password='',port=3306,database='Bank')
#             cur = conn.cursor()
#             cur.execute("SELECT * FROM customer where accno=%s",(
#                 txt_accno.get(),
#             ))
#             row = cur.fetchone()
#             if row == None:
#                 messagebox.showerror("Error","Invalid Account Number")
#             else:
#                 root.destroy()
#                 import deposite
        
#         except Exception as es:
#             messagebox.showerror("Error",f"error due to : {str(es)}")\


##Frame
top_frame = Frame(root,bg="gray20")
top_frame.place(x=150,y=10,width=1370,height=120)

left_frame = Frame(root, bg='gray20')
left_frame.place(x=10, y=10,width=130, height=780)


bank_img = Image.open("bank1.jpg")
bank_img = bank_img.resize((1350, 620), Image.ANTIALIAS)
bank = ImageTk.PhotoImage(bank_img)
bank_lbl = Label(root, image=bank)
bank_lbl.place(x=155, y=160)

##Top Frame
bank_name = Label(top_frame, text="Bank Of Mumbai", font=("times new romane", 55,"bold"), bg="gray20", fg="dark turquoise")
bank_name.place(x=400, y=20)

##Left frame
staff_img = Image.open("staff.png")
staff_img = staff_img.resize((100, 100), Image.ANTIALIAS)
staff = ImageTk.PhotoImage(staff_img)
staff_lbl_img = Button(left_frame, image=staff, bg="white", fg="dark turquoise", command=staff_control)
staff_lbl_img.place(x=12, y=10)
staff_lbl = Label(left_frame, text="     Staff \n    Manage", bg="gray20", fg="dark turquoise", font=("times new roman",15,"bold"))
staff_lbl.place(x=5, y=120)

customer_img = Image.open("customer.jpg")
customer_img = customer_img.resize((100, 100), Image.ANTIALIAS)
customer = ImageTk.PhotoImage(customer_img)
customer_lbl_img = Button(left_frame, image=customer, bg="white", fg="dark turquoise",command=customer_control)
customer_lbl_img.place(x=12, y=200)
customer_lbl = Label(left_frame, text="   Customer \n  Manage", bg="gray20", fg="dark turquoise", font=("times new roman",15,"bold"))
customer_lbl.place(x=5, y=310)

deposite_img = Image.open("deposite.png")
deposite_img = deposite_img.resize((100, 100), Image.ANTIALIAS)
deposite = ImageTk.PhotoImage(deposite_img)
deposite_lbl_img = Button(left_frame, image=deposite, bg="white", fg="dark turquoise",command=deposite_window)
deposite_lbl_img.place(x=12, y=390)
deposite_lbl = Label(left_frame, text="     Money \n   Deposite", bg="gray20", fg="dark turquoise", font=("times new roman",15,"bold"))
deposite_lbl.place(x=5, y=500)

withdraw_img = Image.open("withdraw.png")
withdraw_img = withdraw_img.resize((100, 100), Image.ANTIALIAS)
withdraw = ImageTk.PhotoImage(withdraw_img)
withdraw_lbl_img = Button(left_frame, image=withdraw, bg="white", fg="dark turquoise")
withdraw_lbl_img.place(x=12, y=580)
withdraw_lbl = Label(left_frame, text="     Money \n   Withdraw", bg="gray20", fg="dark turquoise", font=("times new roman",15,"bold"))
withdraw_lbl.place(x=5, y=690)


root.mainloop()
