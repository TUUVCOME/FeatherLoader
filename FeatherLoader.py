# Импорт библиотеки
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from concurrent.futures import process
from pymem import *

# Функция инжекта
def Inject():
    if processInput.get():
        processName = processInput.get()
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

# Изменение параметров программы
# Цвет фона
root['bg'] = '#000000'
# Название Окна
root.title('DLL Loader ❤️')
# Размер окна
root.geometry('300x250')
# Возможность менять размер окна
root.resizable(width=False, height=False)

# Canvas (необязательный)
canvas = Canvas(root, height=300, width=250)
canvas.pack()

# Frame
frame = Frame(root, bg='gray')
frame.place(relheight=1, relwidth=1)

# label
title = Label(frame, text="DLL Loader", bg='gray', font='Montserrat 30', fg='white')
title.pack()
# button
btn = Button(frame, text='Инжект', bg='white', command=Inject, padx=100,)
btn.place(x=30, y=220)
# label 2
processs = Label(frame, text="Имя Процесса", bg='gray', font='Montserrat 10', fg='white')
processs.place(x=101, y=150)
# input
processInput = Entry(frame, bg='white')
processInput.place(x=93, y=180)

# Запуск
root.mainloop()