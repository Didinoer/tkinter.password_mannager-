# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    if len(website) > 0 or len(email) > 0 or  len(password) >0:
        data_json = {website :{
                                'email' : email,
                               'password' : password
                               }
                     }
        is_ok = messagebox.askokcancel(title='validasi',
                           message=f'website :{website} \n email : {email} \n password :{password} \n telah benar dan siap untuk disimpan?? ')
        if is_ok :
            try:
                with open(file='password_data.json',mode='r') as data :
                    data_load = json.load(data)
                    data_load.update(data_json)    
                with open(file='password_data.json',mode='w') as data_file :
                    json.dump(data_load,data_file, indent=4)
                entry_website.delete(0,END)
                entry_email.delete(0,END)
                entry_password.delete(0,END)
            except :
                 with open(file='password_data.json',mode='w') as data :
                    json.dump(data_json,data)
                    entry_website.delete(0,END)
                    entry_email.delete(0,END)
                    entry_password.delete(0,END)
    
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = entry_website.get()
    try:
        with open("password_data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
import tkinter
from tkinter import messagebox
import json
import random
from random import randint,choice,shuffle
#windows
windows = tkinter.Tk()
windows.title("Password Manager")
windows.minsize(height=600, width=800)


#image
canvas=tkinter.Canvas(height= 200, width= 200,highlightthickness=0)
photo = PhotoImage(file= 'logo.png')
canvas.create_image(100,100,image=photo)

#label
label_website = tkinter.Label(text="Website",font=('Arial',12,'bold'))
label_email = tkinter.Label(text="Email/UserName",font=('Arial',12,'bold'))
label_password = tkinter.Label(text="Password",font=('Arial',12,'bold'))


#entry
entry_website = tkinter.Entry()
entry_website.config(fg='black',width=60)
entry_email = tkinter.Entry()
entry_email.config(fg='black',width=75)
entry_password = tkinter.Entry()
entry_password.config(fg='black',width=45)

#button
button_generate_password = tkinter.Button(text='Generate Password',font=('Arial',12,'bold'),command=generate_password)
button_add= tkinter.Button(text='Add',font=('Arial',12,'bold'),width=44,command=save)
search_button = tkinter.Button(text='Search',font=('Arial',12,'bold'),command=find_password)
  
#places
canvas.place(x=300,y=75)
label_website.place(x=80,y=350)
entry_website.place(x=250,y=350)
search_button.place(x=635,y=350)
label_email.place(x=50,y=400)
entry_email.place(x=250,y=400)
label_password.place(x=80,y=450)
entry_password.place(x=250,y=450)
button_generate_password.place(x=535,y=450)
button_add.place(x=250,y=500)





windows.mainloop()
