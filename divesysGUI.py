import tkinter as tk
import Diver_Club
import Diver
import Equipment

#create the base of hte diver club
diver_club = Diver_Club.Diver_Club("boomChakaLaka")

#main window initialization
window_height = 600
window_width = 400
root = tk.Tk()
root.geometry(f'{window_height}x{window_width}')
root.title("Dive system")
def switch(page):
    for fm in main_frame.winfo_children():
        fm.destroy()
        root.update()

    page()


def toggle_menu():
    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_btn.config(text='☰',command=toggle_menu)

    toggle_menu_fm = tk.Frame(root,bg='#158aff')
    toggle_menu_fm.place(x=0,y=50,height=root.winfo_height(),width=window_width*0.4)
    toggle_btn.config(text='X',command=collapse_toggle_menu)

    home_btn = tk.Button(toggle_menu_fm, text='Home',font=('Bold',20),
                         bd=0,bg='#158aff',fg='white',
                         command=lambda:switch(page=Home_page))
    home_btn.place(x=20,y=toggle_menu_fm.winfo_height())

    inventory_btn = tk.Button(toggle_menu_fm, text='instructors', font=('Bold', 20),
                         bd=0, bg='#158aff', fg='white',
                              command=lambda:switch(page=Inventory_page))
    inventory_btn.place(x=20, y=60)

    dives_btn = tk.Button(toggle_menu_fm, text='Dives', font=('Bold', 20),
                         bd=0, bg='#158aff', fg='white',
                          command=lambda:switch(page=Dives_page))
    dives_btn.place(x=20, y=120)

    divers_btn = tk.Button(toggle_menu_fm, text='Divers', font=('Bold', 20),
                         bd=0, bg='#158aff', fg='white',
                           command=lambda:switch(page=Divers_page))
    divers_btn.place(x=20, y=180)



#top frame creation
head_frame = tk.Frame(root,bg='#158aff',highlightbackground='white',highlightthickness=0.5)
head_frame.pack(side=tk.TOP,fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)

#manu button creation
toggle_btn = tk.Button(head_frame,text='☰',bg='#158aff',fg='white',
                       font=('Bold',20),bd=0,activebackground='#158aff',activeforeground='black'
                       ,command=toggle_menu)
toggle_btn.pack(side=tk.LEFT)

#title creation
title_lbl = tk.Label(head_frame,text="Dive System",bg='#158aff',fg='white',
                       font=('Bold',20),bd=0,)
title_lbl.pack(side=tk.LEFT)


main_frame = tk.Frame(root,bg='gray')
main_frame.pack(fill=tk.BOTH,expand=True)


def Home_page():
    home_page_fm = tk.Frame(main_frame)
    home_page_lb = tk.Label(home_page_fm,text="Home Page",
                            font=('Arial',25),fg='#0097e8')
    home_page_lb.pack(pady=80)
    home_page_fm.pack(fill=tk.BOTH,expand=True)

def Inventory_page():
    inventory_page_fm = tk.Frame(main_frame)
    inventory_page_lb = tk.Label(inventory_page_fm,text="Inventory Page",
                            font=('Arial',25),fg='#0097e8')
    inventory_page_lb.pack(pady=80)
    inventory_page_fm.pack(fill=tk.BOTH,expand=True)

def Divers_page():
    divers_page_fm = tk.Frame(main_frame)
    divers_page_lb = tk.Label(divers_page_fm,text="Divers Page",
                            font=('Arial',25),fg='#0097e8')
    divers_page_lb.pack(pady=80)
    divers_page_fm.pack(fill=tk.BOTH,expand=True)

def Dives_page():
    dives_page_fm = tk.Frame(main_frame)
    dives_page_lb = tk.Label(dives_page_fm,text="Dives Page",
                            font=('Arial',25),fg='#0097e8')
    dives_page_lb.pack(pady=80)
    dives_page_fm.pack(fill=tk.BOTH,expand=True)


root.mainloop()
