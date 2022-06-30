from tkinter import *
import user_functions

def register_popup(main_screen):
    register_screen = Toplevel(main_screen)
    register_screen.grab_set() #blokuje wyższe okno na czas otwarcia nowego
    register_screen.title("Rejestracja")
    register_screen.geometry("350x270")
    register_screen["bg"]="#4a4de8"
    username_to_file = StringVar()
    password_to_file= StringVar()

    Label(register_screen,text="Podaj dane w celu rejestracji konta",fg="#fffefe", bg="#171d93", width="350", height="2", font =("Microsoft PhagsPa",13)).pack()
    Label(register_screen,text="Pseudonim* ",fg="#fffefe",bg="#4a4de8",font=("Microsoft PhagsPa",9)).pack()
    username_entry_register = Entry(register_screen, textvariable=username_to_file)
    username_entry_register.pack()
    Label(register_screen, text="Hasło* ",fg="#fffefe",bg="#4a4de8",font=("Microsoft PhagsPa",9)).pack()
    password_entry_register = Entry(register_screen, textvariable=password_to_file,show="\u2022")
    password_entry_register.pack()
    Label(register_screen, bg="#4a4de8",height="2").pack()
    Button(register_screen, text="Zarejestruj", command=lambda: user_functions.user_register(register_screen, username_to_file,password_to_file,username_entry_register,password_entry_register),width="10", height="1",fg="#4b4de9",bg="#f1fafb",font=("Microsoft PhagsPa",9)).pack()
    
def login_popup(main_screen):
    login_screen = Toplevel(main_screen)
    login_screen.grab_set()
    login_screen["bg"] = "#4a4de8"
    login_screen.title("Logowanie")
    login_screen.geometry("350x270")
    Label(login_screen,text="Podaj dane w celu zalogowania.", fg="#4b4de9",bg="#f1fafb", width="100", height="2", font=("Gadugi",15)).pack()
    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen,text="Pseudonim * ",fg="#fffefe",bg="#4a4de8",font=("Microsoft PhagsPa",9)).pack()
    username_entry_login= Entry(login_screen, textvariable=username_verify)
    username_entry_login.pack()
    Label(login_screen,text="Hasło * ",fg="#fffefe",bg="#4a4de8",font=("Microsoft PhagsPa",9)).pack()
    password_entry_login= Entry(login_screen, textvariable=password_verify,show="\u2022")
    password_entry_login.pack()
    Label(login_screen,bg="#4a4de8", height="1").pack()
    Button(login_screen, text="Zaloguj się",command=lambda: user_functions.user_verify(login_screen,username_verify,password_verify,username_entry_login,password_entry_login),width="10", height="1",fg="#4b4de9",bg="#f1fafb",font=("Microsoft PhagsPa",9)).pack()

def session_popup(login_screen,username_from_file):
    user_screen= Toplevel(login_screen)
    user_screen.grab_set()
    user_screen.geometry("600x600")
    user_screen.title("Twoja tablica")
    user_screen["bg"]="#171d93"
    Label(user_screen,text=f"Witaj na twojej tablicy, {username_from_file}",width="600", height="6", fg="#fffefe", bg="#171d93", font=("Gadugi",20,"bold")).pack()
    Label(user_screen,bg="#171d93",height="3").pack()
    clock = Label(user_screen, width="9",height="1",bg="#f1fafb",fg="#4b4de9",font=("Gadugi",60))
    clock.pack()
    user_functions.get_time(clock)
    Label(user_screen,height="3",bg="#171d93").pack()
    Button(user_screen,text="Zamknij sesję", command=lambda:user_screen.destroy()).pack()