import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mg
from os import walk
import shutil

tk.Tk().iconify() # in order to fix empty open window appear

try:
    type_file = open(fd.askopenfilename(), 'r')
except:
    mg.showerror(message="File Load Error!")

type_of_file_extension = type_file.read().split(';')

main_dir_path = fd.askdirectory()

dir_already_exist_in_dir_path = []
list_of_all_file_in_main_dir = []

for (dirpath, dirnames, filenames) in walk(main_dir_path):
    dir_already_exist_in_dir_path.extend(dirnames)
    list_of_all_file_in_main_dir.extend(filenames)
    break # if not break, it goes to subfolder of each folder

for type in type_of_file_extension:
    if type not in dir_already_exist_in_dir_path:
        os.mkdir("{}\{}".format(main_dir_path,type))

    [shutil.move("{}\{}".format(main_dir_path,filename), "{}\{}\{}".format(main_dir_path,type,filename)) for filename in list_of_all_file_in_main_dir if filename.endswith(type)]
