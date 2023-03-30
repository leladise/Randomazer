import random
import time
import tkinter as tk

list = ['Алеева Альфина', 'Бало Альбина', 'Герасимов Борис', 'Гришанович Игорь', 'Гудков Ростислав',
        'Домра Евгений', 'Захаров Микаэл', 'Каринов Александр',
        'Козлова Дарья', 'Кудряшов Тимофей', 'Курганов Егор', 'Лаврентьев Максим', 'Маркова Любовь',
        'Меркулов Александр', 'Прошунин Глеб', 'Фёдоров Артём', 'Филин Антон',
        'Филиппов Александр', 'Цибанов Артемий', 'Шиенок Александра', 'Шляхтун Максим'
        ]


def a():
    global list
    try:
        b = random.choice(list)
        time.sleep(0.3)
        label['text'] = b
        list.remove(b)
    except:
        label['text'] = 'Список кончился!'


window = tk.Tk()
window.title('рандомайзер 5 "М"')
window.state('zoomed')

buttonA= tk.Button(
    text='Сгенерировать',
    bg='SkyBlue3',
    font='SDK_SC_Web 40',
    command=a
)
buttonA.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
label = tk.Label(
    bg='SkyBlue3',
    width=500,
    font='SDK_SC_Web 40'
)
label.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
window.mainloop()
