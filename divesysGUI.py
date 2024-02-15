import tkinter as tk

window_height = 600
window_width = 400
root = tk.Tk()
root.geometry(f'{window_height}x{window_width}')
root.title("Dive system")
def toggle_menu():
    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_btn.config(text='☰',command=toggle_menu)




    toggle_menu_fm = tk.Frame(root,bg='#158aff')
    toggle_menu_fm.place(x=0,y=50,height=root.winfo_height(),width=window_width*0.4)
    toggle_btn.config(text='X',command=collapse_toggle_menu)

    home_btn = tk.Button(toggle_menu_fm, text='Home',font=('Bold',20),
                         bd=1,bg='#158aff',fg='white')
    home_btn.place(x=20,y=toggle_menu_fm.winfo_height())

    inventory_btn = tk.Button(toggle_menu_fm, text='instructors', font=('Bold', 20),
                         bd=1, bg='#158aff', fg='white')
    inventory_btn.place(x=20, y=60)

    dives_btn = tk.Button(toggle_menu_fm, text='Dives', font=('Bold', 20),
                         bd=1, bg='#158aff', fg='white')
    dives_btn.place(x=20, y=120)

    divers_btn = tk.Button(toggle_menu_fm, text='Divers', font=('Bold', 20),
                         bd=1, bg='#158aff', fg='white')
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









root.mainloop()
