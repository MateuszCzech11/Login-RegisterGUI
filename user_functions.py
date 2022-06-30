from tkinter import *
import os
from PIL import Image, ImageTk
import popups
import time

def user_register(register_screen, username_to_file,password_to_file,username_entry_register,password_entry_register):
    username_info = username_to_file.get()
    password_info = password_to_file.get()
    if len(username_info)<8 or len(password_info)<8:
        errormsg = Label(register_screen, text="Minimalna dł. pseudonimu/hasła: 8 znaków", fg="#ed524e",bg="#4a4de8", font= ("Calibri",8,"bold"))
        errormsg.pack()
        return errormsg.after(2000,errormsg.destroy)
    if not os.path.isdir("registered_users"):
        os.mkdir("registered_users")
    file = open("registered_users/"+ username_info,"w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry_register.delete(0,END) #czyści pola z wpisanymi danymi po naciśnięciu przycisku
    password_entry_register.delete(0,END)

    register_success_msg = Label(register_screen, text="Rejestracja się powiodła. \n Okno zamknie się automatycznie za 3s", fg="#7fa6f5", bg="#4a4de8", font=("Calibri",11,"bold"))
    register_success_msg.pack()
    register_success_msg.after(3000,register_screen.destroy)

def user_verify(login_screen,username_verify,password_verify,username_entry_login,password_entry_login):
    global username_from_file #wymagane w celu pokazania username w jego sesji
    username_from_file = username_verify.get()
    password_from_file = password_verify.get()

    username_entry_login.delete(0,END) #czyści pola z wpisanymi danymi po naciśnięciu przycisku
    password_entry_login.delete(0,END)

    list_of_users= os.listdir("registered_users/")
    if username_from_file in list_of_users:
        file= open("registered_users/"+ username_from_file,"r")
        credentials_to_verification = file.read().splitlines()
        if password_from_file in credentials_to_verification:
            login_success(login_screen,username_from_file)
        else:
            wrong_password(login_screen)
    else:
        wrong_username(login_screen)


def login_success(login_screen,username_from_file):
    success_alert = Toplevel(login_screen)
    success_alert.grab_set()
    success_alert.title("Sukces")
    success_alert.geometry("400x250")
    success_alert["bg"]="#171d93"
    global logo
    logo = ImageTk.PhotoImage(Image.open("misc/logo.png"))
    Label(success_alert, text="   Zalogowano poprawnie",width="400", height="100", fg="#4b4de9", bg="#f1fafb", font=("Gadugi",14,"bold"),image = logo, compound="left").pack()
    Label(success_alert, height="2", bg="#171d93").pack()
    session_bridge = Label(success_alert, text="Jesteś przenoszony do Swojej sesji...", width="400", fg="#fffefe", bg="#171d93", font=("Gadugi",12))
    session_bridge.pack()
    session_bridge.after(4000,lambda:open_session(success_alert,login_screen,username_from_file))

def open_session(success_alert,login_screen,username_from_file):
    success_alert.destroy()
    popups.session_popup(login_screen,username_from_file)

def wrong_password(login_screen):
    badpasswd_alert = Toplevel(login_screen)
    badpasswd_alert.grab_set()
    badpasswd_alert.title("Błędne hasło")
    badpasswd_alert.geometry("400x200")
    badpasswd_alert["bg"]="#171d93"
    global errorimage #bez tego obrazek się nie wczyta
    errorimage = ImageTk.PhotoImage(Image.open("misc/errorimg.png"))
    Label(badpasswd_alert, text="    Coś poszło nie tak!", width="400", height="40", fg="#fffefe", bg="#4a4de8", font=("Gadugi",15,"bold"), image = errorimage, compound="left").pack()
    Label(badpasswd_alert, height="2", bg="#171d93").pack()
    Label(badpasswd_alert, text="Podane hasło jest niepoprawne.\nSpróbuj ponownie", width="300", fg="#fffefe", bg="#171d93", font=("Gadugi",12)).pack()
    Button(badpasswd_alert, text="Zamknij okno", command=lambda: badpasswd_alert.destroy(), width="10",height="1",fg="#4b4de9",bg="#f1fafb").pack()

    

def wrong_username(login_screen):
    badname_alert = Toplevel(login_screen)
    badname_alert.grab_set()
    badname_alert.title("Błędny pseudonim")
    badname_alert.geometry("400x200")
    badname_alert["bg"]="#171d93"
    global errorimage #bez tego obrazek się nie wczyta
    errorimage = ImageTk.PhotoImage(Image.open("misc/errorimg.png"))
    Label(badname_alert, text="    Coś poszło nie tak!", width="400", height="40", fg="#fffefe", bg="#4a4de8", font=("Gadugi",15,"bold"), image = errorimage, compound="left").pack()
    Label(badname_alert, height="2", bg="#171d93").pack()
    Label(badname_alert, text="Błędny pseudonim i/lub hasło.\nSprawdź poprawość zapisu", width="400", fg="#fffefe", bg="#171d93", font=("Gadugi",12)).pack()
    Button(badname_alert, text="Zamknij okno", command=lambda: badname_alert.destroy(), width="10",height="1",fg="#4b4de9",bg="#f1fafb").pack()

def get_time(clock):
    current_time = time.strftime("%H : %M : %S")
    clock.config(text= current_time)
    clock.after(200,lambda:get_time(clock))
