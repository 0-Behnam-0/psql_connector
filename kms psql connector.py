from tkinter import Tk, messagebox, StringVar, Listbox, IntVar
import psycopg2
import tkinter.ttk as ttk


conn = psycopg2.connect(
    host="78.38.35.219",
    database="g2",
    user="g2",
    password="123456",
    options="-c search_path=dbo,kms"
)


def tab_info():
    global selected_id
    global table_name
    global table_data
    index = nb.index(nb.select())
    if index == 0:
        selected_id = document_link_id_entry.get()
        table_name = 'document_link'
        table_data = {
            'related_part': document_link_related_part_entry.get(),
            'description': document_link_description_entry.get(),
            'main_id': document_link_main_id_entry.get(),
            'repository_id': document_link_repository_id_entry.get(),
        }
    if index == 1:
        selected_id = main_id_entry.get()
        table_name = 'main'
        table_data = {
            'title': main_title_entry.get(),
            'publish_date': main_publish_date_entry.get(),
            'description': main_description_entry.get(),
            'user_id': main_user_id_entry.get(),
            'tree_id': main_tree_id_entry.get(),
        }
    # if index == 2:
    # if index == 3:
    # if index == 4:
    # if index == 5:
    if index == 6:
        selected_id = tag_id_entry.get()
        table_name = 'tag'
        table_data = {
            'title': tag_title_entry.get(),
            'publish_date': tag_publish_date_entry.get(),
            'description': tag_description_entry.get(),
        }
    # if index == 7:
    # if index == 8:
    # if index == 9:
    print(index)


# def create_table():
#     cur = conn.cursor()
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS my_table (
#             id SERIAL PRIMARY KEY,
#             name VARCHAR(50),
#             age INTEGER);
#         """)
#     conn.commit()
#     cur.close()


def insert_data():
    tab_info()

    values = str(list(table_data.values()))
    values = selected_id + ", " + values[1:-1]

    keys = table_name + "_id"
    for item in list(table_data.keys()):
        keys = keys + ", " + item

    cur = conn.cursor()
    cur.execute(f"INSERT INTO {table_name} ({keys}) VALUES ({values})")
    conn.commit()
    cur.close()
    messagebox.showinfo("Success", "Data inserted successfully")
    # name_entry.delete(0, 'end')
    # age_entry.delete(0, 'end')


def select_data():
    tab_info()
    print(table_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM "+ table_name)
    rows = cur.fetchall()
    cur.close()
    messagebox.showinfo("Data", str(rows))
    # print(t)


def update_data():
    query = ""
    for key, value in table_data:
        query = str(key+" = "+value) + query
    print(query)
    # id = int(id_entry.get())
    # name = name_entry.get()
    # age = age_entry.get()
    cur = conn.cursor()
    cur.execute(f"UPDATE {table_name} SET {query} WHERE id = {id_entry.get()}")
    conn.commit()
    cur.close()
    messagebox.showinfo("Success", "Data updated successfully")
    id_entry.delete(0, 'end')
    name_entry.delete(0, 'end')
    age_entry.delete(0, 'end')


def delete_data():
    id = int(id_entry.get())
    cur = conn.cursor()
    cur.execute(f"DELETE FROM {table_name} WHERE {table_name}_id = {str(id)}")
    conn.commit()
    cur.close()
    messagebox.showinfo("Success", "Data deleted successfully")
    id_entry.delete(0, 'end')


table_list = {
    'Document Link': 'document_link',
    'Main': 'main',
    'Media Link': 'media_link',
    'Position': 'position',
    'Position Link': 'position_link',
    'Repository': 'repository',
    'Tag': 'tag',
    'Tag Link': 'tag_link',
    'Tree': 'tree',
    'User': 'user'
}


window = Tk()
window.title("SQL Database")

window.minsize(350, 150)
window.resizable(0, 0)

style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', font=('Helvetica', 11), padding=5)
style.configure('TEntry', font=('Helvetica', 12), padding=5)

MASSAGE_TEXT = StringVar(window, "foobar")
LAST_ROW = 0


nb = ttk.Notebook(window, padding=5)
# Loop through the dictionary and create a new tab for each key-value pair
for key, value in table_list.items():
    # Create a new tab
    tab = ttk.Frame(nb, padding=5)
    
    if key=='Document Link':
        document_link_id_label = ttk.Label(tab, text="ID")
        document_link_id_label.grid(row=0, column=0, sticky='w', pady=2)
        document_link_id_entry = ttk.Entry(tab)
        document_link_id_entry.grid(row=0, column=1, pady=2)

        document_link_related_part_label = ttk.Label(tab, text="Related Part")
        document_link_related_part_label.grid(row=1, column=0, sticky='w', pady=2)
        document_link_related_part_entry = ttk.Entry(tab)
        document_link_related_part_entry.grid(row=1, column=1, pady=2)

        document_link_description_label = ttk.Label(tab, text="Description")
        document_link_description_label.grid(row=2, column=0, sticky='w', pady=2)
        document_link_description_entry = ttk.Entry(tab)
        document_link_description_entry.grid(row=2, column=1, pady=2)

        document_link_main_id_label = ttk.Label(tab, text="Main ID")
        document_link_main_id_label.grid(row=3, column=0, sticky='w', pady=2)
        document_link_main_id_entry = ttk.Entry(tab)
        document_link_main_id_entry.grid(row=3, column=1, pady=2)

        document_link_repository_id_label = ttk.Label(tab, text="Repository ID")
        document_link_repository_id_label.grid(row=4, column=0, sticky='w', pady=2)
        document_link_repository_id_entry = ttk.Entry(tab)
        document_link_repository_id_entry.grid(row=4, column=1, pady=2)
    
    if key=='Main':
        main_id_label = ttk.Label(tab, text="ID")
        main_id_label.grid(row=0, column=0, sticky='w', pady=2)
        main_id_entry = ttk.Entry(tab)
        main_id_entry.grid(row=0, column=1, pady=2)

        main_title_label = ttk.Label(tab, text="Title")
        main_title_label.grid(row=1, column=0, sticky='w', pady=2)
        main_title_entry = ttk.Entry(tab)
        main_title_entry.grid(row=1, column=1, pady=2)

        main_publish_date_label = ttk.Label(tab, text="Publish Date")
        main_publish_date_label.grid(row=2, column=0, sticky='w', pady=2)
        main_publish_date_entry = ttk.Entry(tab)
        main_publish_date_entry.grid(row=2, column=1, pady=2)

        main_description_label = ttk.Label(tab, text="Description")
        main_description_label.grid(row=3, column=0, sticky='w', pady=2)
        main_description_entry = ttk.Entry(tab)
        main_description_entry.grid(row=3, column=1, pady=2)

        main_user_id_label = ttk.Label(tab, text="User ID")
        main_user_id_label.grid(row=4, column=0, sticky='w', pady=2)
        main_user_id_entry = ttk.Entry(tab)
        main_user_id_entry.grid(row=4, column=1, pady=2)

        main_tree_id_label = ttk.Label(tab, text="Tree ID")
        main_tree_id_label.grid(row=5, column=0, sticky='w', pady=2)
        main_tree_id_entry = ttk.Entry(tab)
        main_tree_id_entry.grid(row=5, column=1, pady=2)

    if key=='Media Link':
        media_link_id_label = ttk.Label(tab, text="ID")
        media_link_id_label.grid(row=0, column=0, sticky='w', pady=2)
        media_link_id_entry = ttk.Entry(tab)
        media_link_id_entry.grid(row=0, column=1, pady=2)

        media_link_start_time_label = ttk.Label(tab, text="Start Time")
        media_link_start_time_label.grid(row=1, column=0, sticky='w', pady=2)
        media_link_start_time_entry = ttk.Entry(tab)
        media_link_start_time_entry.grid(row=1, column=1, pady=2)

        media_link_end_time_label = ttk.Label(tab, text="End Time")
        media_link_end_time_label.grid(row=2, column=0, sticky='w', pady=2)
        media_link_end_time_entry = ttk.Entry(tab)
        media_link_end_time_entry.grid(row=2, column=1, pady=2)
        
        media_link_description_label = ttk.Label(tab, text="Description")
        media_link_description_label.grid(row=3, column=0, sticky='w', pady=2)
        media_link_description_entry = ttk.Entry(tab)
        media_link_description_entry.grid(row=3, column=1, pady=2)

        media_link_main_id_label = ttk.Label(tab, text="Main ID")
        media_link_main_id_label.grid(row=4, column=0, sticky='w', pady=2)
        media_link_main_id_entry = ttk.Entry(tab)
        media_link_main_id_entry.grid(row=4, column=1, pady=2)

        media_link_repository_id_label = ttk.Label(tab, text="Repository ID")
        media_link_repository_id_label.grid(row=5, column=0, sticky='w', pady=2)
        media_link_repository_id_entry = ttk.Entry(tab)
        media_link_repository_id_entry.grid(row=5, column=1, pady=2)

    if key=='Position':
        position_id_label = ttk.Label(tab, text="ID")
        position_id_label.grid(row=0, column=0, sticky='w', pady=2)
        position_id_entry = ttk.Entry(tab)
        position_id_entry.grid(row=0, column=1, pady=2)

        position_title_label = ttk.Label(tab, text="Title")
        position_title_label.grid(row=1, column=0, sticky='w', pady=2)
        position_title_entry = ttk.Entry(tab)
        position_title_entry.grid(row=1, column=1, pady=2)

        position_description_label = ttk.Label(tab, text="Description")
        position_description_label.grid(row=2, column=0, sticky='w', pady=2)
        position_description_entry = ttk.Entry(tab)
        position_description_entry.grid(row=2, column=1, pady=2)

    if key=='Position Link':
        position_link_id_label = ttk.Label(tab, text="ID")
        position_link_id_label.grid(row=0, column=0, sticky='w', pady=2)
        position_link_id_entry = ttk.Entry(tab)
        position_link_id_entry.grid(row=0, column=1, pady=2)

        position_link_apointment_date_label = ttk.Label(tab, text="Appointment Date")
        position_link_apointment_date_label.grid(row=1, column=0, sticky='w', pady=2)
        position_link_apointment_date_entry = ttk.Entry(tab)
        position_link_apointment_date_entry.grid(row=1, column=1, pady=2)

        position_link_dismissal_date_label = ttk.Label(tab, text="Dismissal Date")
        position_link_dismissal_date_label.grid(row=2, column=0, sticky='w', pady=2)
        position_link_dismissal_date_entry = ttk.Entry(tab)
        position_link_dismissal_date_entry.grid(row=2, column=1, pady=2)

        position_link_user_id_label = ttk.Label(tab, text="User ID")
        position_link_user_id_label.grid(row=3, column=0, sticky='w', pady=2)
        position_link_user_id_entry = ttk.Entry(tab)
        position_link_user_id_entry.grid(row=3, column=1, pady=2)

        position_link_position_id_label = ttk.Label(tab, text="Position ID")
        position_link_position_id_label.grid(row=4, column=0, sticky='w', pady=2)
        position_link_position_id_entry = ttk.Entry(tab)
        position_link_position_id_entry.grid(row=4, column=1, pady=2)

    if key=='Repository':
        repository_id_label = ttk.Label(tab, text="ID")
        repository_id_label.grid(row=0, column=0, sticky='w', pady=2)
        repository_id_entry = ttk.Entry(tab)
        repository_id_entry.grid(row=0, column=1, pady=2)

        repository_name_label = ttk.Label(tab, text="Name")
        repository_name_label.grid(row=1, column=0, sticky='w', pady=2)
        repository_name_entry = ttk.Entry(tab)
        repository_name_entry.grid(row=1, column=1, pady=2)

        repository_type_label = ttk.Label(tab, text="Type")
        repository_type_label.grid(row=2, column=0, sticky='w', pady=2)
        repository_type_entry = ttk.Entry(tab)
        repository_type_entry.grid(row=2, column=1, pady=2)

        repository_url_label = ttk.Label(tab, text="Url")
        repository_url_label.grid(row=3, column=0, sticky='w', pady=2)
        repository_url_entry = ttk.Entry(tab)
        repository_url_entry.grid(row=3, column=1, pady=2)
        
        repository_description_label = ttk.Label(tab, text="Description")
        repository_description_label.grid(row=4, column=0, sticky='w', pady=2)
        repository_description_entry = ttk.Entry(tab)
        repository_description_entry.grid(row=4, column=1, pady=2)

    if key=='Tag':
        tag_id_label = ttk.Label(tab, text="ID")
        tag_id_label.grid(row=0, column=0, sticky='w', pady=2)
        tag_id_entry = ttk.Entry(tab)
        tag_id_entry.grid(row=0, column=1, pady=2)

        tag_title_label = ttk.Label(tab, text="Title")
        tag_title_label.grid(row=1, column=0, sticky='w', pady=2)
        tag_title_entry = ttk.Entry(tab)
        tag_title_entry.grid(row=1, column=1, pady=2)

        tag_publish_date_label = ttk.Label(tab, text="Publish Date")
        tag_publish_date_label.grid(row=2, column=0, sticky='w', pady=2)
        tag_publish_date_entry = ttk.Entry(tab)
        tag_publish_date_entry.grid(row=2, column=1, pady=2)

        tag_description_label = ttk.Label(tab, text="Description")
        tag_description_label.grid(row=3, column=0, sticky='w', pady=2)
        tag_description_entry = ttk.Entry(tab)
        tag_description_entry.grid(row=3, column=1, pady=2)

    if key=='Tag Link':
        tag_link_id_label = ttk.Label(tab, text="ID")
        tag_link_id_label.grid(row=0, column=0, sticky='w', pady=2)
        tag_link_id_entry = ttk.Entry(tab)
        tag_link_id_entry.grid(row=0, column=1, pady=2)

        tag_link_tag_id_label = ttk.Label(tab, text="Tag ID")
        tag_link_tag_id_label.grid(row=1, column=0, sticky='w', pady=2)
        tag_link_tag_id_entry = ttk.Entry(tab)
        tag_link_tag_id_entry.grid(row=1, column=1, pady=2)
        
        tag_link_main_id_label = ttk.Label(tab, text="Main ID")
        tag_link_main_id_label.grid(row=2, column=0, sticky='w', pady=2)
        tag_link_main_id_entry = ttk.Entry(tab)
        tag_link_main_id_entry.grid(row=2, column=1, pady=2)

    if key=='Tree':
        tree_id_label = ttk.Label(tab, text="ID")
        tree_id_label.grid(row=0, column=0, sticky='w', pady=2)
        tree_id_entry = ttk.Entry(tab)
        tree_id_entry.grid(row=0, column=1, pady=2)

        tree_title_label = ttk.Label(tab, text="Title")
        tree_title_label.grid(row=1, column=0, sticky='w', pady=2)
        tree_title_entry = ttk.Entry(tab)
        tree_title_entry.grid(row=1, column=1, pady=2)

        tree_code_label = ttk.Label(tab, text="Code")
        tree_code_label.grid(row=2, column=0, sticky='w', pady=2)
        tree_code_entry = ttk.Entry(tab)
        tree_code_entry.grid(row=2, column=1, pady=2)

        tree_root_code_label = ttk.Label(tab, text="Root Code")
        tree_root_code_label.grid(row=3, column=0, sticky='w', pady=2)
        tree_root_code_entry = ttk.Entry(tab)
        tree_root_code_entry.grid(row=3, column=1, pady=2)

    if key=='User':
        user_id_label = ttk.Label(tab, text="ID")
        user_id_label.grid(row=0, column=0, sticky='w', pady=2)
        user_id_entry = ttk.Entry(tab)
        user_id_entry.grid(row=0, column=1, pady=2)

        user_first_name_label = ttk.Label(tab, text="First Name")
        user_first_name_label.grid(row=1, column=0, sticky='w', pady=2)
        user_first_name_entry = ttk.Entry(tab)
        user_first_name_entry.grid(row=1, column=1, pady=2)

        user_last_name_label = ttk.Label(tab, text="Last Name")
        user_last_name_label.grid(row=2, column=0, sticky='w', pady=2)
        user_last_name_entry = ttk.Entry(tab)
        user_last_name_entry.grid(row=2, column=1, pady=2)

        user_national_code_label = ttk.Label(tab, text="National Code")
        user_national_code_label.grid(row=3, column=0, sticky='w', pady=2)
        user_national_code_entry = ttk.Entry(tab)
        user_national_code_entry.grid(row=3, column=1, pady=2)

        user_phone_label = ttk.Label(tab, text="Phone Number")
        user_phone_label.grid(row=4, column=0, sticky='w', pady=2)
        user_phone_entry = ttk.Entry(tab)
        user_phone_entry.grid(row=4, column=1, pady=2)
        
        user_username_label = ttk.Label(tab, text="Username")
        user_username_label.grid(row=5, column=0, sticky='w', pady=2)
        user_username_entry = ttk.Entry(tab)
        user_username_entry.grid(row=5, column=1, pady=2)
        
        user_password_label = ttk.Label(tab, text="Password")
        user_password_label.grid(row=6, column=0, sticky='w', pady=2)
        user_password_entry = ttk.Entry(tab)
        user_password_entry.grid(row=6, column=1, pady=2)
        
        user_evidence_label = ttk.Label(tab, text="Evidence")
        user_evidence_label.grid(row=7, column=0, sticky='w', pady=2)
        user_evidence_entry = ttk.Entry(tab)
        user_evidence_entry.grid(row=7, column=1, pady=2)
        
        user_email_label = ttk.Label(tab, text="Email")
        user_email_label.grid(row=8, column=0, sticky='w', pady=2)
        user_email_entry = ttk.Entry(tab)
        user_email_entry.grid(row=8, column=1, pady=2)

    # Add the tab to the notebook
    nb.add(tab, text=key)

# Pack the notebook widget
nb.grid(row=LAST_ROW, column=0, columnspan=4, sticky='nsew')
LAST_ROW =+ 1

insert_button = ttk.Button(window, text="Insert", command=insert_data)
insert_button.grid(row=LAST_ROW, column=0)

select_button = ttk.Button(window, text="Select", command=select_data)
select_button.grid(row=LAST_ROW, column=1)

update_button = ttk.Button(window, text="Update", command=update_data)
update_button.grid(row=LAST_ROW, column=2)

delete_button = ttk.Button(window, text="Delete", command=delete_data)
delete_button.grid(row=LAST_ROW, column=3)
LAST_ROW += 1

message_label = ttk.Label(window, text="Message :")
message_label.grid(row=LAST_ROW, column=0, sticky='w')

status_label = ttk.Label(window, textvariable=MASSAGE_TEXT)
status_label.grid(row=LAST_ROW, column=1, columnspan=2)
LAST_ROW += 1

window.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform=1)
window.grid_rowconfigure(0, weight=1)
window.configure(bg='#dcdad3')

# TODO create_table()

window.mainloop()
