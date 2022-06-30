from tkinter import *
from PIL import Image, ImageTk
import popups

def main_popup():
    global main_screen
    main_screen = Tk()
    logo = ImageTk.PhotoImage(Image.open("misc/logo.png"))
    main_screen["bg"]="#161d92"
    main_screen.geometry("600x500")
    main_screen.title("Ekran logowania")

    Label(text="  Twój dostawca usług sieciowych", fg="#4b4de9",bg="#f1fafb", width="600", height="100", font=("Gadugi",20), image = logo, compound='left').pack()
    Label(text="Podaj dane w celu zalogowania",fg="#fffefe", bg="#4b4de9", width="600", height="2", font =("Microsoft PhagsPa",13)).pack()
    Label(bg="#161d92", height="3").pack() #Cel pustego Labela - pozostawienie lini przerwy kolejnymi elementami, czysto estetyczny wybór
    
    Button(text= "Zaloguj", command=lambda: popups.login_popup(main_screen),width="25", height="2",fg="#4b4de9",bg="#f1fafb",font=("Microsoft PhagsPa",9)).pack() 
    Label(text="Nie masz konta? Zarejestruj się!",fg="#fffefe", bg="#161d92", font=("Microsoft PhagsPa",9)).pack()
    Button(text="Zarejestruj konto",command=lambda: popups.register_popup(main_screen),width="25", height="2",fg="#4b4de9",bg="#f1fafb",font=("Microsoft PhagsPa",9)).pack()

    main_screen.mainloop()


main_popup()