import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mg
from os import walk
import shutil

#TODO show folder function/button
#TODO keep code more organise class/function etc.
root = tk.Tk()

def organise():
    try:
        type_file = open(config_file_name_entry.get(), 'r')
    except:
        mg.showerror(message="File Load Error!")

    type_of_file_extension = type_file.read().split(';')

    main_dir_path = dict_to_organise_entry.get()

    dir_already_exist_in_dir_path = []
    list_of_all_file_in_main_dir = []

    for (dirpath, dirnames, filenames) in walk(main_dir_path):
        dir_already_exist_in_dir_path.extend(dirnames)
        list_of_all_file_in_main_dir.extend(filenames)
        break  # if not break, it goes to subfolder of each folder

    for type in type_of_file_extension:
        if type not in dir_already_exist_in_dir_path:
            os.mkdir("{}\{}".format(main_dir_path, type))

        [shutil.move("{}\{}".format(main_dir_path, filename), "{}\{}\{}".format(main_dir_path, type, filename)) for
         filename in list_of_all_file_in_main_dir if filename.endswith(type)]


file_frame = tk.LabelFrame(root,
                           text="Choose a config file")
config_file_name_entry = tk.Entry(file_frame,
                                  width=50)
config_file_browse_button = tk.Button(file_frame,
                                      text="Browse",
                                      command= lambda : config_file_name_entry.insert(0,
                                                                                      fd.askopenfilename()))
dict_frame = tk.LabelFrame(root,
                           text="Choose dictionary to organise")
dict_browse_button = tk.Button(dict_frame,
                                      text="Browse",
                                      command= lambda : dict_to_organise_entry.insert(0,
                                                                                      fd.askdirectory()))
dict_to_organise_entry = tk.Entry(dict_frame,
                                  width=50)
run_organise_button = tk.Button(root,
                                text="Organise!",
                                command=organise)

file_frame.pack(padx=20, pady=20)
config_file_name_entry.grid(row=0, column=0, padx=20, pady=20)
config_file_browse_button.grid(row=0, column=1, padx=20, pady=20)
dict_frame.pack(padx=20, pady=20)
dict_to_organise_entry.grid(row=0, column=0, padx=20, pady=20)
dict_browse_button.grid(row=0, column=1, padx=20, pady=20)
run_organise_button.pack(padx=20, pady=20)

root.mainloop()