import tkinter as tk
from tkinter import ttk
from time import sleep
from random import randint

punkty = 0
punktyplus = 1

root = tk.Tk()
root.resizable(False, False)
root.geometry('700x350')
root.config(bg='#0f1f4a')
root.title('Jajeczny Clicker')


#Powerupy
wscieklakura = False
duck = False
melisa = False
kura = False

def main():
    global punkty, eggbutton, ramka1, ramka2, ramka3, ramka4, punktyplus
    root.geometry('700x350')

    #Forgety
    wscieklakura_Description.place_forget()
    wscieklakura_Label.place_forget()
    kuraimg.place_forget()
    ZaGierkaToBylo.place_forget()
    kurabutton.place_forget()
    RzadyPisu.place_forget()
    duckimglabel.place_forget()
    duckbutton.place_forget()
    ducklabel.place_forget()
    RzadyPisu2.place_forget()
    ZaGierkaToBylo2.place_forget()
    RzadyPisu3.place_forget()
    ZaGierkaToBylo3.place_forget()
    duckdescription.place_forget()
    melisalabel.place_forget()
    melisabutton.place_forget()
    melisadescription.place_forget()
    melisaimglabel.place_forget()
    
    #Powerupy if statements
    if wscieklakura:
        punktyplus = punktyplus + 2
        kuraimg.place(x=325, y=40)
        wscieklakura_Label.place(x=405, y=45)
        wscieklakura_Description.config(text='Metal jest super')
        wscieklakura_Description.place(x=405, y=65)
    else:
        pass
    if kura:
        punktyplus = punktyplus * 3
        spokojnakuraimg.place(x=325, y=40)
        spokojnakuralabel.place(x=405, y=45)
        spokojnakuradescription.place(x=405, y=65)

    if duck:
        punktyplus = punktyplus + randint(1, 5)
        duckimglabel.place(x=325, y=120)
        ducklabel.place(x=405, y=125)
        duckdescription.config(text='KWAK!')
        duckdescription.place(x=405, y=145)

    
    if melisa:
        melisaimglabel.place(x=325, y=200)
        melisalabel.place(x=405, y=205)
        melisadescription.place(x=405, y=225)
    
    if melisa == 'GONE':
        melisaimglabel.place_forget()
        melisalabel.place_forget()
        melisadescription.place_forget()

    if melisa and wscieklakura:
        spokojnakurabutton.place(x=540, y=50)
    #Place
    ramka1.place(x=310)
    ramka2.place(x=310, y=340)
    ramka3.place(x=690)
    ramka4.place(x=320)
    mexicanborder.place(x=300)
    mojeszpargaly.place(x=325, y=20)
    frame.focus()
    frame.place(x=16, y=20)
    eggbutton.place(x=65, y=65)
    sklepbutton.place(x=211, y=300)
    pointbox.place(x=14, y=300)

mainbutton = ttk.Button(root, text='Powrot', command=main)

def Powerupbuykura():
    global punkty, kurabutton, wscieklakura
    wscieklakura = True
    punkty = punkty - 100
    kurabutton.place_forget()

def Powerupbuyduck():
    global punkty, duckbutton, duck
    duck = True
    punkty = punkty - 500
    duckbutton.place_forget()

def Powerupbuymelisa():
    global punkty, melisabutton, melisa
    melisa = True
    punkty = punkty - 1500
    melisabutton.place_forget()

def Powerupbuyspokojnakura():
    global punkty, kura, spokojnakurabutton, wscieklakura, melisa
    melisa = 'GONE'
    wscieklakura = False
    kura = True
    spokojnakurabutton.place_forget()
    main()


def sklep():
    global punkty
    #Forgety
    root.geometry('700x500')
    eggbutton.place_forget()
    sklepbutton.place_forget()
    frame.place_forget()
    mexicanborder.place_forget()
    mojeszpargaly.place_forget()
    ramka1.place_forget()
    ramka2.place_forget()
    ramka3.place_forget()
    ramka4.place_forget()
    pointbox.place_forget()
    mainbutton.place_forget()
    spokojnakuradescription.place_forget()
    spokojnakuraimg.place_forget()
    spokojnakuralabel.place_forget()
    

    #wscieklakura
    wscieklakura_Label.place(x=85, y=10)
    kuraimg.place(x=10, y=10)
    wscieklakura_Description.config(text="Metal jest super. Daje 3 pkt na klikniecie. (koszt: 100pkt)")
    wscieklakura_Description.place(x=85, y=35)

    #kaczka
    duckimglabel.place(x=10, y=90)
    ducklabel.place(x=85, y=90)
    duckdescription.config(text='KWAK! Daje od 1-5 punktow plus (koszt: 500pkt)')
    duckdescription.place(x=85, y=115)

    #Melisa
    melisaimglabel.place(x=10, y=170)
    melisalabel.place(x=85, y=170)
    melisadescription.place(x=85, y=195)
    
    pointbox.place(x=14, y=460)
    mainbutton.place(x=211, y=460)
    
    #wscieklakura button
    if punkty >= 100 and wscieklakura == False and kura == False:
        kurabutton.place(x=500, y=20)
    else:
        if wscieklakura == False and kura == False:
            ZaGierkaToBylo.place(x=500, y=20)
        else:
            RzadyPisu.place(x=500, y=20)

    #duck button
    if punkty >= 500 and duck == False:
        duckbutton.place(x=500, y=100)
    else:
        if duck == False:
            ZaGierkaToBylo2.place(x=500, y=100)
        else:
            RzadyPisu2.place(x=500, y=100)

    #melisa button
    if punkty >= 1500 and melisa == False:
        melisabutton.place(x=500, y=180)
    else:
        if melisa == False:
            ZaGierkaToBylo3.place(x=500, y=180)
        else:
            RzadyPisu3.place(x=500, y=180)
    
    if melisa == 'GONE':
        melisabutton.place_forget()
        ZaGierkaToBylo3.place_forget()
        RzadyPisu3.place_forget()
        melisaimglabel.place_forget()
        melisadescription.place_forget()
        melisalabel.place_forget()

def pointup(numer):
    global punkty
    punkty = punkty + numer
    pointbox.config(text='masz ' + str(punkty) + ' punktow')

#Fap Folder
wscieklakura_img = tk.PhotoImage(file='wscieklakura.png')
duckphoto =tk.PhotoImage(file='kaczka.png')
duckimglabel = tk.Label(root, image=duckphoto)
melisaphoto = tk.PhotoImage(file='meliska-20-torebek-po-2-g.png')
melisaimglabel = tk.Label(root, image=melisaphoto)


#wariaty
kuraimg = tk.Label(image=wscieklakura_img)
sklepbutton = ttk.Button(root, text='Sklep', command=sklep)
frame = tk.Frame(height=270, width=270, background='#112457')
blank = tk.Label(root, text="", background='#0f1f4a')
pointbox = tk.Label(root, text="Masz " + str(punkty) + ' punktów', font='Impact',
foreground='#FFFFFF', background='#0f1f4a')
eggimg = tk.PhotoImage(file='jajeczny.png')
eggbutton = ttk.Button(root, image=eggimg, command=lambda: pointup(punktyplus))
bigarial = 'Arial', 12
smallarial = 'Arial', 10
mojeszpargaly = ttk.Label(root, text='Moje szpargały:', background='#0f1f4a', font=bigarial, foreground='#FFFFFF')
mexicanborder = tk.Frame(root, width=10, height=350, background='#00030a')
wscieklakura_Label = tk.Label(root, text="Wsciekla kura", font=bigarial, background='#0f1f4a', foreground='#FFFFFF')
wscieklakura_Description = tk.Label(root, text="Metal jest super, daje 3 pkt na klikniecie. (koszt: 100pkt)", font=smallarial, background='#0f1f4a', foreground='#FFFFFF')
PowerButtonkura = tk.Button(root, text='KUP', command=Powerupbuykura)
impact = 'Impact', 12
ZaGierkaToBylo = tk.Label(root, text='NIE STAC CIE BIEDAKU', font=impact, foreground='#FFFFFF', background='#0f1f4a')
kurabutton = tk.Button(root, text='KUP', command=Powerupbuykura)
RzadyPisu = tk.Label(root, background='#0f1f4a', foreground='#FFFFFF', text='Posiadane', font=bigarial)
ramka1 = tk.Frame(root, background='#112457', height=350, width=10)
ramka2 = tk.Frame(root, background='#112457', height=10, width=400)
ramka3 = tk.Frame(root, background='#112457', height=350, width=10)
ramka4 = tk.Frame(root, background='#112457', height=10, width=400)
ducklabel = tk.Label(root, text='Kaczka Malgorzatka', background='#0f1f4a', foreground='#FFFFFF', font=bigarial)
duckdescription = tk.Label(root, text='KWAK! daje od 1-5 punktow plus (koszt: 500pkt)', background='#0f1f4a', foreground='#FFFFFF', font=smallarial)
duckbutton = tk.Button(root, text='KUP', command=Powerupbuyduck)
ZaGierkaToBylo2 = tk.Label(root, text='NIE STAC CIE BIEDAKU', font=impact, foreground='#FFFFFF', background='#0f1f4a')
RzadyPisu2 = tk.Label(root, background='#0f1f4a', foreground='#FFFFFF', text='Posiadane', font=bigarial)
ZaGierkaToBylo3 = tk.Label(root, text='NIE STAC CIE BIEDAKU', font=impact, foreground='#FFFFFF', background='#0f1f4a')
RzadyPisu3 = tk.Label(root, background='#0f1f4a', foreground='#FFFFFF', text='Posiadane', font=bigarial)
melisalabel = tk.Label(root, foreground='#FFFFFF', background='#0f1f4a', text='Melisa', font=bigarial)
melisadescription = tk.Label(root, foreground='#FFFFFF', background='#0f1f4a', text='Herbatka na uspokojenie (koszt: 1500pkt)', font=smallarial)
melisabutton = tk.Button(root, text='KUP', command=Powerupbuymelisa)
spokojnakurabutton = tk.Button(root, text='Daj kurze melise', command=Powerupbuyspokojnakura)
spokojnakuralabel = tk.Label(root, foreground='#FFFFFF', background='#0f1f4a', text='Spokojna kura', font=bigarial)
spokojnakuradescription = tk.Label(root, foreground='#FFFFFF', background='#0f1f4a', text='PKT X 3, METAL JEST DO DUPY', font=smallarial)
spokojnakuraphoto = tk.PhotoImage(file='kura.png')
spokojnakuraimg = tk.Label(root, image=spokojnakuraphoto)


if __name__ == "__main__":
    main()
    root.mainloop()