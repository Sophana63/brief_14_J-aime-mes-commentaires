from tkinter import* 
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
import csv

base = Tk()  

base.geometry('500x500')  
base.title("Ajout d'employé")  

labl_0 = Label(base, text="Ajout d'un employé",width=20,font=("bold", 20))  
labl_0.place(x=90,y=53)  
  
### Champ Nom
labl_1 = Label(base, text="Nom",width=20,font=("bold", 10))  
labl_1.place(x=80,y=130)  

entry_02 = Entry(base)  
entry_02.place(x=240,y=130)  

### Champ prénom
labl_2 = Label(base, text="Prénom",width=20,font=("bold", 10))  
labl_2.place(x=80,y=160)  

entry_03 = Entry(base)  
entry_03.place(x=240,y=160) 

### Champ date
labl_3 = Label(base, text="Date",width=20,font=("bold", 10))  
labl_3.place(x=80,y=190)  

entry_04 = DateEntry(base,bg="darkblue",fg="white",year=2022)
entry_04.grid()
entry_04.place(x=240,y=190) 
  
### Champ métier
labl_4 = Label(base, text="Profession",width=20,font=("bold", 10))  
labl_4.place(x=80,y=220)  

listeProfession = open("./files/postes.txt", "r").read()
listeProfession = listeProfession.split()
entry_05 = ttk.Combobox(base, values=listeProfession)
entry_05.current(0)
entry_05.pack() 
entry_05.place(x=240,y=220) 


#fonction pour envoyer
def envoyer():    

    with open('./docs/csv/liste_employes.csv','a',newline='') as fichiercsv:
        writer=csv.writer(fichiercsv)
        writer.writerow([str(entry_03.get().capitalize()),  str(entry_02.get().capitalize()), str(entry_04.get()),  str(entry_05.get())])  
    base.destroy()    

#bouton envoyer
Envoyer= Button (base, text="ENVOYER",command=envoyer, pady=2).place(x=240,y=280)

base.mainloop() 

print("Enregistrement bien effectué.") 

