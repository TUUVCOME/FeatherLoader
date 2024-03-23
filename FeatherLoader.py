# Импорт библиотеки
from tkinter import *
from tkinter import ttk
import psutil # CHANGED!!! ИЗМЕНЁН!!!
from tkinter import messagebox
from tkinter import filedialog
from concurrent.futures import process
from pymem import *

# Функция инжекта
def Inject():
    if combobox.get():
        processName = combobox.get()
        f_types = [('DLL', '*.dll')]
        directory = filedialog.askopenfile(mode='r', title='Выберите DLL!', initialdir="/", filetypes=f_types, multiple=False)
        dll_path_bytes = bytes(directory.name, "UTF-8")
        open_process = Pymem(processName)
        process.inject_dll(open_process.process_handle, dll_path_bytes)
        info_str = 'DLL Успешно заинжектилась!'
        messagebox.showinfo(title="Успешно!", message=info_str)
        print(directory.name)
    else:
        info_str = 'Похоже, вы что-то пропустили!'
        messagebox.showinfo(title="Ошибка!", message=info_str)

# Окно программы
root = Tk()

# Получение списка процессов
processlist=list()
for processes in psutil.process_iter():
    processlist.append(processes.name())

# Иконка программы
root.iconbitmap("G:/!бз/tkinter/leaf_feather_icon_179057.ico")

# Изменение параметров программы
# Цвет фона
root['bg'] = '#000000'
# Название Окна
root.title('FeatherLoader ❤️')
# Размер окна
root.geometry('300x250')
# Возможность менять размер окна
root.resizable(width=False, height=False)

# Canvas (необязательный)
canvas = Canvas(root, height=300, width=250)
canvas.pack()

# Frame
frame = Frame(root, bg='#B2DFDB')
frame.place(relheight=1, relwidth=1)

# label
title = Label(frame, text="FeatherLoader", bg='#B2DFDB', font='Montserrat 20', fg='#004D40')
title.pack()
# button
btn = Button(frame, text='Инжект', command=Inject, padx=100, fg='#004D40', bg='#B2DFDB')
btn.place(x=30, y=220)
# label 2
processs = Label(frame, text="Процесс", bg='#B2DFDB', font='Montserrat 10', fg='#004D40')
processs.place(x=120, y=140)
# input
# processInput = Entry(frame, bg='#B2DFDB')
# processInput.place(x=93, y=180)
# combobox
languages = processlist

combobox = ttk.Combobox(frame, values=languages, background='#B2DFDB', font='Montserrat 10', foreground='#004D40')
combobox.place(x=55, y=170)

# Запуск
root.mainloop()
