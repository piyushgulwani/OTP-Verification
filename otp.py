from tkinter import *
import os, sys, time
import tkinter.messagebox as tmsg
import random, smtplib


#? Function to get otp
def get_otp() : 

#! Generating Random 4 Digit number 
    number_gen = random.randint(1000,9999)
    str_num = str(number_gen)
    global e1_value 
    
#! Getting Email to be Verified
    x = e1_value.get().lower()

#! Sending OTP
    receiver = x
    content = (f'OTP Verification\n{str_num}')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('exexample829@gmail.com', 'MSDHONI1')
    server.sendmail('exexample829@gmail.com', receiver,  content)
    server.close()

#! Checking OTP
    def login_check() : 
        login_num_check = e2_value.get()
        gui2.update()
        

        if (login_num_check == number_gen) : 
            print(e2_value.get())
            tmsg.showinfo('Sucess!!', 'Login Sucess')

        else: 
            tmsg.showerror('Error!', 'Login Details Has been sent to user!!')
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            content1 = (f"Someone just tried to login\n Login Details: \n \nUserName:  {os.getlogin()}\nTime: {time.strftime('%H:%M:%S')}\n")
            server.login('exexample829@gmail.com', 'MSDHONI1')
            server.sendmail('exexample829@gmail.com', receiver,  content1)
            server.close()
            

    try : 
        tmsg.showinfo('Sent', f'OTP Sent to {x}')
        gui2 = Toplevel(gui)
        gui2.title('OTP Verification')
        gui2.geometry('230x100')
        gui2.iconbitmap('otp.ico')
        e2_value = IntVar()
        e2 = Entry(gui2, textvariable = e2_value, font= 'conicsansms 10 bold')
        e2.pack()
        Button(gui2, text = 'Login', command = login_check).pack()
        gui2.update()


    except Exception as e : 
        print(f"Error occured\n{e}")

gui = Tk()
gui.title('OTP Verification')
gui.geometry('430x200')

f1 = Frame(gui, relief = SUNKEN)

Label(f1, text = 'Enter Email to be verified: ',fg ='black',bg ='white', font = 'comicsansms 10 italic').pack()

e1_value = StringVar()
e1 = Entry(f1, textvariable = e1_value, bd = 5, relief = FLAT, font = 'Arial 20 italic')
e1.pack(fill = X, pady = 10)
Button(f1, text = 'Get OTP', command = get_otp).pack()
f1.update()

f1.pack()


gui.mainloop()