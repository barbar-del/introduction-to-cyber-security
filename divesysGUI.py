import tkinter as tk
from tkinter import ttk
import pandas as pd
import Diver_Club
import Diver
import Equipment

#create the base of hte diver club
diver_club = Diver_Club.Diver_Club("boomChakaLaka")

#main window initialization
window_width = 1100
window_height = 500
btn_width = window_width*0.2
root_padx_left = (window_width - btn_width)//2 - btn_width
root = tk.Tk()
root.geometry(f'{window_width}x{window_height}')
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
    toggle_menu_fm.place(x=0,y=50,height=root.winfo_height(),width=btn_width)
    toggle_btn.config(text='X',command=collapse_toggle_menu)

    home_btn = tk.Button(toggle_menu_fm, text='Home',font=('Bold',20),
                         bd=0,bg='#158aff',fg='white',
                         command=lambda:switch(page=Home_page))
    home_btn.place(x=20,y=toggle_menu_fm.winfo_height())

    inventory_btn = tk.Button(toggle_menu_fm, text='Inventory', font=('Bold', 20),
                         bd=0, bg='#158aff', fg='white',
                              command=lambda:switch(page=Inventory_page))
    inventory_btn.place(x=20, y=60)

    divers_btn = tk.Button(toggle_menu_fm, text='Divers', font=('Bold', 20),
                         bd=0, bg='#158aff', fg='white',
                           command=lambda:switch(page=Divers_page))
    divers_btn.place(x=20, y=120)

    divers_btn = tk.Button(toggle_menu_fm, text='Instructors', font=('Bold', 20),
                         bd=0, bg='#158aff', fg='white',
                           command=lambda:switch(page=Instructors_page))
    divers_btn.place(x=20, y=180)
    
    dives_btn = tk.Button(toggle_menu_fm, text='Dives', font=('Bold', 20),
                         bd=0, bg='#158aff', fg='white',
                          command=lambda:switch(page=Dives_page))
    dives_btn.place(x=20, y=240)





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
    home_page_lb.pack(pady=20,padx=(root_padx_left, 0))
    home_page_fm.pack(fill=tk.BOTH,expand=True)

def Inventory_page():
    inventory_page_fm = tk.Frame(main_frame)
    inventory_page_lb = tk.Label(inventory_page_fm,text="Inventory Page",
                            font=('Arial',25),fg='#0097e8')
    label_width = inventory_page_lb.winfo_reqwidth()
    inventory_page_lb.pack(pady=20,padx=(root_padx_left , 0))
    
    button_frame = tk.Frame(inventory_page_fm)
    button_frame.pack()
    add_button = tk.Button(button_frame, text="Add Item", relief=tk.RAISED, borderwidth=2, 
                    background="#0097e8", foreground="white", font=('Arial', 14),
                    highlightthickness=0)
    add_button.pack(side=tk.LEFT, padx=(root_padx_left,20))  # Adjust padx as needed
    delete_button = tk.Button(button_frame, text="Delete Item", relief=tk.RAISED, borderwidth=2, 
                    background="#0097e8", foreground="white", font=('Arial', 14),
                    highlightthickness=0)
    delete_button.pack(side=tk.LEFT, padx=0)  # Adjust padx as needed

    # Create a table
    table = ttk.Treeview(inventory_page_fm)
    table['columns'] = ('Item', 'Quantity')
    table.column('#0', width=0, stretch=tk.NO)  # Hide the first column
    table.column('Item', anchor=tk.CENTER, width=150)
    table.column('Quantity', anchor=tk.CENTER, width=100)
    table.heading('#0', text='', anchor=tk.W)
    table.heading("Item", text="Item", anchor=tk.CENTER, command=lambda: sort_by_name(table, 'Item', False))
    # table.heading('Quantity', text='Quantity', anchor=tk.CENTER)
    table.heading("Quantity", text="Quantity", anchor=tk.CENTER, command=lambda: sort_by_quantity(table, 'Quantity', False))
    table.pack(pady=20, padx = (root_padx_left ,0) )



    inventory_page_fm.pack(fill=tk.BOTH,expand=True)

    upload_table('InventoryXL.csv',table)


def Divers_page():
    divers_page_fm = tk.Frame(main_frame)
    divers_page_lb = tk.Label(divers_page_fm,text="Divers Page",
                            font=('Arial',25),fg='#0097e8')
    label_width = divers_page_lb.winfo_reqwidth()
    divers_page_lb.pack(pady=20,padx=(root_padx_left,0))

    button_frame = tk.Frame(divers_page_fm)
    button_frame.pack()
    add_button = tk.Button(button_frame, text="Add Diver", relief=tk.RAISED, borderwidth=2, 
                    background="#0097e8", foreground="white", font=('Arial', 14),
                    highlightthickness=0)
    add_button.pack(side=tk.LEFT, padx=(root_padx_left,20))  # Adjust padx as needed
    delete_button = tk.Button(button_frame, text="Delete Diver", relief=tk.RAISED, borderwidth=2, 
                    background="#0097e8", foreground="white", font=('Arial', 14),
                    highlightthickness=0)
    delete_button.pack(side=tk.LEFT, padx=0)  # Adjust padx as needed


    # Create a table
    table = ttk.Treeview(divers_page_fm)
    table['columns'] = ('ID', 'Name','Rank')
    table.column('#0', width=0, stretch=tk.NO)  # Hide the first column
    table.column('ID', anchor=tk.CENTER, width=100)
    table.column('Name', anchor=tk.CENTER, width=150)
    table.column('Rank', anchor=tk.CENTER, width=100)
    table.heading('#0', text='', anchor=tk.W)
    # table.heading('ID',text = 'ID', anchor=tk.CENTER)
    table.heading("ID", text="ID", anchor=tk.CENTER, command=lambda: sort_by_quantity(table, 'ID', False))
    # table.heading('Name',text = 'Name', anchor=tk.CENTER)
    table.heading("Name", text="Name", anchor=tk.CENTER, command=lambda: sort_by_name(table, 'Name', False))
    # table.heading('Rank',text = 'Rank', anchor=tk.CENTER)
    table.heading("Rank", text="Rank", anchor=tk.CENTER,command=lambda: sort_by_quantity(table, 'Rank', False))
    table.pack(pady=20, padx = (root_padx_left,0))

    divers_page_fm.pack(fill=tk.BOTH,expand=True)

    upload_table('DiversXL.csv',table)

def Instructors_page():
    Instructors_page_fm = tk.Frame(main_frame)
    Instructors_page_lb = tk.Label(Instructors_page_fm,text="Instructors Page",
                            font=('Arial',25),fg='#0097e8')
    label_width = Instructors_page_lb.winfo_reqwidth()
    Instructors_page_lb.pack(pady=20,padx=(root_padx_left,0))

    button_frame = tk.Frame(Instructors_page_fm)
    button_frame.pack()
    add_button = tk.Button(button_frame, text="Add Instructor", relief=tk.RAISED, borderwidth=2, 
                    background="#0097e8", foreground="white", font=('Arial', 14),
                    highlightthickness=0)
    add_button.pack(side=tk.LEFT, padx=(root_padx_left,20))  # Adjust padx as needed
    delete_button = tk.Button(button_frame, text="Delete Instructor", relief=tk.RAISED, borderwidth=2, 
                    background="#0097e8", foreground="white", font=('Arial', 14),
                    highlightthickness=0)
    delete_button.pack(side=tk.LEFT, padx=0)  # Adjust padx as needed

    # Create a table
    table = ttk.Treeview(Instructors_page_fm)
    table['columns'] = ('ID', 'Name','Rank','Company')
    table.column('#0', width=0, stretch=tk.NO)  # Hide the first column
    table.column('ID', anchor=tk.CENTER, width=100)
    table.column('Name', anchor=tk.CENTER, width=150)
    table.column('Rank', anchor=tk.CENTER, width=100)
    table.column('Company', anchor=tk.CENTER, width=100)
    table.heading('#0', text='', anchor=tk.W)
    # table.heading('ID',text = 'ID', anchor=tk.CENTER)
    table.heading("ID", text="ID", anchor=tk.CENTER, command=lambda: sort_by_quantity(table, 'ID', False))
    # table.heading('Name',text = 'Name', anchor=tk.CENTER)
    table.heading("Name", text="Name", anchor=tk.CENTER, command=lambda: sort_by_name(table, 'Name', False))
    # table.heading('Rank',text = 'Rank', anchor=tk.CENTER)
    table.heading("Rank", text="Rank", anchor=tk.CENTER, command=lambda: sort_by_quantity(table, 'Rank', False))
    # table.heading('Company',text = 'Company', anchor=tk.CENTER)
    table.heading("Company", text="Company", anchor=tk.CENTER, command=lambda: sort_by_name(table, 'Company', False))
    table.pack(pady=20, padx = (root_padx_left,0))

    Instructors_page_fm.pack(fill=tk.BOTH,expand=True)

    upload_table('InstructorsXL.csv',table)



def Dives_page():
    dives_page_fm = tk.Frame(main_frame)
    dives_page_lb = tk.Label(dives_page_fm,text="Dives Page",
                            font=('Arial',25),fg='#0097e8')
    label_width = dives_page_lb.winfo_reqwidth()

    dives_page_lb.pack(pady=20,padx=(root_padx_left,0))

    button_frame = tk.Frame(dives_page_fm)
    button_frame.pack()
    add_button = tk.Button(button_frame, text="Add Dive", relief=tk.RAISED, borderwidth=2, 
                    background="#0097e8", foreground="white", font=('Arial', 14),
                    highlightthickness=0)
    add_button.pack(side=tk.LEFT, padx=(root_padx_left,20))  # Adjust padx as needed
    delete_button = tk.Button(button_frame, text="Delete Dive", relief=tk.RAISED, borderwidth=2, 
                    background="#0097e8", foreground="white", font=('Arial', 14),
                    highlightthickness=0)
    delete_button.pack(side=tk.LEFT, padx=0)  # Adjust padx as needed

    # Create a table
    table = ttk.Treeview(dives_page_fm)
    table['columns'] = ('Dive ID', 'Depth','Instructor name','Instructor ID','Location','Club','Equipment')
    table.column('#0', width=0, stretch=tk.NO)  # Hide the first column
    table.column('Dive ID', anchor=tk.CENTER, width=100)
    table.column('Instructor name', anchor=tk.CENTER, width=150)
    table.column('Instructor ID', anchor=tk.CENTER, width=100)
    table.column('Depth', anchor=tk.CENTER, width=100)
    table.column('Location', anchor=tk.CENTER, width=150)
    table.column('Club', anchor=tk.CENTER, width=100)
    table.column('Equipment', anchor=tk.CENTER, width=100)
    table.heading('#0', text='', anchor=tk.CENTER)
    # table.heading('Dive ID', text='Dive ID', anchor=tk.CENTER)
    table.heading("Dive ID", text="Dive ID", anchor=tk.CENTER, command=lambda: sort_by_quantity(table, 'Dive ID', False))
    # table.heading('Instructor name', text='Instructor name', anchor=tk.CENTER)
    table.heading("Instructor name", text="Instructor name", anchor=tk.CENTER, command=lambda: sort_by_name(table, 'Instructor name', False))
    # table.heading('Instructor ID', text='Instructor ID', anchor=tk.CENTER)
    table.heading("Instructor ID", text="Instructor ID", anchor=tk.CENTER, command=lambda: sort_by_quantity(table, 'Instructor ID', False))
    # table.heading('Depth', text='Depth', anchor=tk.CENTER)
    table.heading("Depth", text="Depth", anchor=tk.CENTER,command=lambda: sort_by_quantity(table, 'Depth', False))
    # table.heading('Location', text='Location', anchor=tk.CENTER)
    table.heading("Location", text="Location", anchor=tk.CENTER,command=lambda: sort_by_name(table, 'Location', False))
    # table.heading('Club', text='Club', anchor=tk.CENTER)
    table.heading("Club", text="Club", anchor=tk.CENTER, command=lambda: sort_by_name(table, 'Club', False))
    # table.heading('Equipment', text='Equipment', anchor=tk.CENTER)
    table.heading("Equipment", text="Equipment", anchor=tk.CENTER, command=lambda: sort_by_name(table, 'Equipment', False))

    table.pack(pady=20, padx = (root_padx_left,0))

    dives_page_fm.pack(fill=tk.BOTH,expand=True)

    upload_table('DivesXL.csv',table)

def upload_table(file_path, table):
    try:
        print(file_path)
        # Read the Excel file into a DataFrame
        df = pd.read_csv(file_path)
        df = df.dropna()
        if 'Quantity' in df.columns:
            df['Quantity'] = df['Quantity'].astype(int)
        print(df)
        # Clear the existing data in the table
        table.delete(*table.get_children())

        # Insert each row from the DataFrame into the table
        for index, row in df.iterrows():
            table.insert('', 'end', values=row.tolist())
            
        print("Data uploaded successfully.")
    except Exception as e:
        print("Error uploading data:", str(e))

# Function to sort the items in the treeview
def sort_by_quantity(tree, col, reverse):
    # Retrieve the list of items in the treeview
    l = [(tree.set(k, col), k) for k in tree.get_children('')]
    # Sort the list in place, converting values to integers for proper numerical sorting
    l.sort(key=lambda t: int(t[0]), reverse=reverse)

    # Rearrange the items in sorted order
    for index, (_, k) in enumerate(l):
        tree.move(k, '', index)

    # Reverse the sorting order for the next time
    tree.heading(col, command=lambda: sort_by_quantity(tree, col, not reverse))

def sort_by_name(tree, col, reverse):
    # Retrieve the list of items in the treeview
    l = [(tree.set(k, col), k) for k in tree.get_children('')]
    # Sort the list in place, this time without converting to integers since we're dealing with strings
    l.sort(key=lambda t: t[0], reverse=reverse)

    # Rearrange the items in sorted order
    for index, (_, k) in enumerate(l):
        tree.move(k, '', index)

    # Reverse the sorting order for the next time
    tree.heading(col, command=lambda: sort_by_name(tree, col, not reverse))

root.mainloop()
