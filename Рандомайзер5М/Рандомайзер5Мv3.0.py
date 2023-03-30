import random
import tkinter as tk
bgcol = '#512299'
fgcol = 'white'
list = ['Алеева Альфина', 'Бало Альбина', 'Герасимов Борис', 'Гришанович Игорь', 'Гудков Ростислав',
        'Домра Евгений', 'Захаров Микаэл', 'Каринов Александр',
        'Козлова Дарья', 'Кудряшов Тимофей', 'Курганов Егор', 'Лаврентьев Максим', 'Маркова Любовь',
        'Меркулов Александр', 'Прошунин Глеб', 'Фёдоров Артём', 'Филин Антон',
        'Филиппов Александр', 'Цибанов Артемий', 'Шиенок Александра', 'Шляхтун Максим'
        ]


def generate():
    try:
        b = random.choice(list)
    except:
        label['text'] = 'Список кончился'
    label['text'] = b
    list.remove(b)


def reload():
    global list
    list = ['Алеева Альфина', 'Бало Альбина', 'Герасимов Борис', 'Гришанович Игорь', 'Гудков Ростислав',
            'Домра Евгений', 'Захаров Микаэл', 'Каринов Александр',
            'Козлова Дарья', 'Кудряшов Тимофей', 'Курганов Егор', 'Лаврентьев Максим', 'Маркова Любовь',
            'Меркулов Александр', 'Прошунин Глеб', 'Фёдоров Артём', 'Филин Антон',
            'Филиппов Александр', 'Цибанов Артемий', 'Шиенок Александра', 'Шляхтун Максим'
            ]
    label['text'] = 'Список обновлён'


window = tk.Tk()
window.title('Рандомайзер 5М')
window.state('zoomed')

buttonGen = tk.Button(
    text='Сгенерировать',
    bg=bgcol,
    font='Times 40',
    activebackground='white',
    activeforeground='white',
    command=generate,
    fg=fgcol
)
buttonRel = tk.Button(
    text='Обновить список',
    bg=bgcol,
    font='Times 40',
    activebackground='white',
    activeforeground='white',
    command=reload,
    fg=fgcol
)
buttonGen.pack(fill=tk.BOTH, side=tk.TOP, expand=False)
buttonRel.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=False)
label = tk.Label(
    bg=bgcol,
    width=500,
    font='Times 40',
    fg=fgcol
)
label.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
window.mainloop()