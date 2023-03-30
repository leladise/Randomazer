import random
import tkinter as tk
window = tk.Tk()
window.title('Рандомайзер 5М')
window.state('zoomed')
bgcol = '#bf8095'
fgcol = '#000000'
fgcol1 = '#301d7a'
list = ['Алеева Альфина', 'Бало Альбина', 'Герасимов Борис', 'Гришанович Игорь', 'Гудков Ростислав',
        'Домра Евгений', 'Захаров Микаэл', 'Каринов Александр',
        'Козлова Дарья', 'Кудряшов Тимофей', 'Курганов Егор', 'Лаврентьев Максим', 'Маркова Любовь',
        'Меркулов Александр', 'Прошунин Глеб', 'Фёдоров Артём', 'Филин Антон',
        'Филиппов Александр', 'Цибанов Артемий', 'Шиенок Александра', 'Шляхтун Максим'
        ]
def generate():
    try:
        human= random.choice(list)
    except:
        label['text'] = 'Список кончился'
    label['text'] = human
    list.remove(human)
def reload():
    global list
    list = ['Алеева Альфина', 'Бало Альбина', 'Герасимов Борис', 'Гришанович Игорь', 'Гудков Ростислав',
            'Домра Евгений', 'Захаров Микаэл', 'Каринов Александр',
            'Козлова Дарья', 'Кудряшов Тимофей', 'Курганов Егор', 'Лаврентьев Максим', 'Маркова Любовь',
            'Меркулов Александр', 'Прошунин Глеб', 'Фёдоров Артём', 'Филин Антон',
            'Филиппов Александр', 'Цибанов Артемий', 'Шиенок Александра', 'Шляхтун Максим'
            ]
    label['text'] = 'Список обновлён'
buttonGen = tk.Button(
    text='Сгенерировать',
    bg=bgcol,
    font='Times 40',
    activebackground='white',
    activeforeground='white',
    command=generate,
    fg=fgcol
)
buttonGen.pack(fill=tk.BOTH, side=tk.TOP, expand=False)
buttonRel = tk.Button(
    text='Обновить список',
    bg=bgcol,
    font='Times 40',
    activebackground='white',
    activeforeground='white',
    command=reload,
    fg=fgcol
)
buttonRel.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=False)
label = tk.Label(
    bg=bgcol,
    width=500,
    font='Times 40',
    fg=fgcol1
)
label.pack(fill=tk.BOTH, side=tk.RIGHT, expand=False)
window.mainloop()
