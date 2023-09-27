import string
from random import randint, choice
from tkinter import *


def generate_password():
    password_min = 6
    password_max = 24
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars)for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    with open("old_passwords.txt", "a+") as file:
        file.write(password + "\n")
        file.close()


# création de la fênetre.
window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.iconbitmap("proxy-image.ico")
window.config(background="#4065A4")

# créer la frame principale
frame = Frame(window, bg="#4065A4")

# création d'image
width = 300
height = 300
image = PhotoImage(file="mot-de-passe.png").zoom(15).subsample(42)
canvas = Canvas(frame, width=width, height=height, bg="#4065A4", bd=0, highlightthickness=0)
canvas.create_image(width/3, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# créer une sous boite.(frame)
right_frame = Frame(frame, bg="#4065A4")

#créer un titre.
label_title = Label(right_frame, text="Mot de passe", font=("Helvetica", 20), bg="#4065A4", fg="white")
label_title.pack()

#créer un chapm/input
password_entry = Entry(right_frame, font=("Gothic", 20), bg="#4065A4", fg="white")
password_entry.pack()

#créer un bouton.
generate_password_button = Button(right_frame, text="Générer", font=("Helvetica", 20), bg="#4065A4", fg="white", command=generate_password)
generate_password_button.pack(fill=X)

#ici on place la boite a droite de la frame principal.
right_frame.grid(row=0, column=1, sticky=W)

# afficher la frame
frame.pack(expand=YES)

# creation d'une barre de menu
menu_bar = Menu(window)
# créer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# configurer notre fenetre pour ajouter cette menu bar
window.config(menu=menu_bar)
# afficher
window.mainloop()