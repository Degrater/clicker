import tkinter as tk
import json

win = tk.Tk()  # Объявляй окно в начале файла, потом кнопки/лейблы и т.п., потом функции для кнопок а потом отрисовывай их(place)
win.title("Кликер")
win.geometry('350x550')
win.config(bg='blue')

fog = 0

def openLoadJson():
    global clickSave
    with open("count.json", "r") as f:
        countList = json.loads(f.read())
        clickSave = countList["a"]

def openSaveJson(count):
    with open("count.json", "w") as file:
        listSave = {
            "a": count
        }
        file.write(json.dumps(listSave))


def reloadCounter():
    counterClicks.config(text=f'Счет: {fog}')


def resetSave():
    openSaveJson(0)


def counter():
    global fog
    fog = fog + 1
    reloadCounter()


def reset():
    global fog
    fog = 0
    reloadCounter()


def boostClick():
    global fog
    fog += 2
    reloadCounter()


def exitWin():
    openSaveJson(fog)
    win.quit()

def save():
    openSaveJson(fog)

def loader():
    global fog
    openLoadJson()
    fog = clickSave
    reloadCounter()


logo = tk.Label(win, text='Clicker',
                bg='purple',
                font=('Montserrat', '18'),
                foreground='red')
counterClicks = tk.Label(win, text=f'Cчет: {fog}',
                         font=('Arial', '12', 'bold'),
                         bg='white',
                         foreground='red')

click = tk.Button(win, text='Кликни',
                  font=('Montserrat', '10'),
                  command=counter,
                  activebackground='purple',
                  foreground='red',
                  bg='white')

resetSaveClick = tk.Button(win, text='Сброс сохраненных кликов',
                           font=('Montserrat', '10'),
                           command=resetSave,
                           activebackground='purple',
                           foreground='red',
                           bg='white')

save = tk.Button(win, text='Сохранить',
                 font=('Montserrat', '10'),
                 command=save,
                 activebackground='purple',
                 foreground='red',
                 bg='white')

boost = tk.Button(win, text='Скорость 2x',
                  font=('Montserrat', '10'),
                  activebackground='purple',
                  foreground='red',
                  bg='white',
                  command=boostClick)

saveAndLeave = tk.Button(win, text='Сохранить и выйти',
                         font=('Montserrat', '10'),
                         activebackground='purple',
                         foreground='red',
                         bg='white',
                         command=exitWin)

loadSave = tk.Button(win, text='Загрузить прогресс?',
                     font=('Montserrat', '10'),
                     activebackground='purple',
                     foreground='red',
                     bg='white',
                     command=loader)

resetClick = tk.Button(win, text='Сбросить прогресс?',
                       font=('Montserrat', '10'),
                       activebackground='purple',
                       foreground='red',
                       bg='white',
                       command=reset)

win.resizable(False, False)
boost.place(relx=0.38, rely=0.7)
saveAndLeave.place(relx=0.65, rely=0.95)
save.place(relx=0.79, rely=0)
logo.place(relx=0.4, rely=0.2)
resetSaveClick.place(relx=0.001, rely=0.95)
counterClicks.place(relx=0.4, rely=0.5)
loadSave.place(relx=0, rely=0)
click.place(relx=0.42, rely=0.8)
resetClick.place(relx=0.3, rely=0.575)
win.mainloop()
