from tkinter import*
from tkinter import messagebox
import mysql.connector

root = Tk()
root.geometry("1600x800+0+0")
root.title("deposite control")
root.config(background='dark turquoise')

def upd():
    accno= StringVar()
    accno = (e_acc_no.get())
    if (accno == "" ):
        messagebox.showinfo("ID is required for delete", "All Fields are Required")    
    else:
        con=mysql.connector.connect(host= "localhost", user="root" , password="", database="Bank")
        cursor= con.cursor()
        cursor.execute("select openingbal from customer where accno='" + accno + "'")
        myresul = cursor.fetchall()
        for x in myresul:
            print(x)
            e_updated_bal.insert(0,x)
            cursor.execute("commit")
            messagebox.showinfo("Update Status", "deposited Successfully")
            con.close()

def dept():
    amtn= e_amm_no.get()
    accno= StringVar()
    accno = (e_acc_no.get())
    if (accno == "" ):
        messagebox.showinfo("ID is required for delete", "All Fields are Required")    
    else:
        con=mysql.connector.connect(host= "localhost", user="root" , password="", database="Bank")
        cursor= con.cursor()
        cursor.execute("update customer set openingbal= openingbal + ('" + amtn + "') where accno='" + accno + "'")
        cursor.execute("commit")
        con.close()
        upd()


def sub():
    accno= StringVar()
    accno = (e_acc_no.get())
    if (accno == "" ):
        messagebox.showinfo("Illegal insert", "All Fields are Required")    
    else:
        con=mysql.connector.connect(host= "localhost", user="root" , password="", database="Bank")
        cursor= con.cursor()
        cursor.execute("select openingbal from Customer where accno='" + accno + "'")
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
            e_cur_bal.insert(0,x)
        cursor.execute("commit")
        con.close()










top_frame = Frame(root,bg="gray20")
top_frame.place(x=0,y=0,width=1550,height=90)

staff_lbl = Label(top_frame, text="Money deposit Control", bg="gray20", fg="dark turquoise", font=("times new roman",45,"bold"))
staff_lbl.place(x=420, y= 5)

accno= StringVar()
acc_no = Label(root,text="Account No   ", font=("times new roman",20,"bold"),bg="dark turquoise", fg="gray20")
acc_no.place(x=200, y=180)

e_acc_no= Entry(root, font=("times new roman",18),bg="gray20",fg="dark turquoise",width="45",textvariable=accno)
e_acc_no.place(x=480, y=185,height="30")

curr_bal = Label(root,text="Current Balance   ", font=("times new roman",20,"bold"),bg="dark turquoise", fg="gray20")
curr_bal.place(x=200,y=260)

e_cur_bal = Entry(root, font=("times new roman",18),bg="gray20",fg="dark turquoise",width="45")
e_cur_bal.place(x=480, y=260,height="30")

ammount = Label(root,text="Ammount   ", font=("times new roman",20,"bold"),bg="dark turquoise", fg="gray20")
ammount.place(x=200,y=340)

e_amm_no = Entry(root, font=("times new roman",18),bg="gray20",fg="dark turquoise",width="45")
e_amm_no.place(x=480, y=340,height="30")

updated_bal = Label(root,text="Updated Balance   ", font=("times new roman",20,"bold"),bg="dark turquoise", fg="gray20")
updated_bal.place(x=200,y=420)

e_updated_bal = Entry(root, font=("times new roman",18),bg="gray20",fg="dark turquoise",width="45")
e_updated_bal.place(x=480,y=420)


submit = Button(root, text="Submit",fg="dark turquoise", bg="gray20", font=("times new roman",18,"bold"),width=10, activebackground="dark turquoise", activeforeground="gray20",command=sub)
submit.place(x=250,y=520)

deposit = Button(root, text="deposit",fg="dark turquoise", bg="gray20", font=("times new roman",18,"bold"),width=10, activebackground="dark turquoise", activeforeground="gray20",command=dept)
deposit.place(x=460,y=520)






root.mainloop()