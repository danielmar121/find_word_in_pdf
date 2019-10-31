import os
from tika import parser
import tkinter as tk
from tkinter import filedialog

# global vars
HEIGHT = 400
WIDTH = 400
FOLDER_PATH = ''


def get_folder_path():
    global FOLDER_PATH
    FOLDER_PATH = filedialog.askdirectory()


def search(the_word):
    files_with_word = ''
    # os.walk makes iteration on all the files in the chosen folder
    for subdir, dirs, files in os.walk(FOLDER_PATH):
        for file_name in files:
            # we are taking only the files that end with pdf
            # file of pdf type
            if file_name.endswith('.pdf'):
                # to get the right path to the file
                pdf_file_obj = parser.from_file(os.path.join(subdir, file_name))
                # content give you all the tet in the pdf object
                if the_word.lower() in pdf_file_obj['content'].lower():
                    files_with_word += file_name + '\n'
    # change the text on the label
    the_files_label['text'] = files_with_word


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Word Finder')

    # making the size of the window
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    # making frames
    frame_search_label = tk.Frame(root, bd=5)
    frame_search_label.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor='n')
    frame_search2 = tk.Frame(root, bg='#80c1ff', bd=5)
    frame_search2.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
    frame_folder = tk.Frame(root, bg='#80c1ff', bd=5)
    frame_folder.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor='n')
    lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
    lower_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.6, anchor='n')

    # making entry
    entry_search = tk.Entry(frame_search2, font=40)
    entry_search.place(relwidth=0.65, relheight=1)

    # making a label
    search_label = tk.Label(frame_search_label, text='please enter the word you willing to search', font=30)
    search_label.place(rely=0, relwidth=1, relheight=1)
    the_files_label = tk.Label(lower_frame, font=('Arial', 14))
    the_files_label.place(relx=0, relwidth=1, relheight=1)

    # making the button of the program
    search_button = tk.Button(frame_search2, text='Search', font=40, command=lambda: search(entry_search.get()))
    search_button.place(relx=0.7, relheight=1, relwidth=0.3)
    open_folder_button = tk.Button(frame_folder, text='Open Folder', font=40, command=lambda: get_folder_path())
    open_folder_button.place(relx=0.3, relheight=1, relwidth=0.4)

    root.mainloop()
