import random
from tkinter import *

def klicked():
    lbl.configure(text="Я же просил...")


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry("500x400")
frame=Frame(window, padx = 10, pady=10)
frame.pack(expand=True)
lbl = Label(frame, text="Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос", font=("Arial Bold", 9))
lbl.grid(column=1, row=3)
txt = Entry(frame, width=10)
txt.grid(column=1, row=4)
btn=Button(frame, text="Не нажимать!", command=klicked, bg="black", fg="red",)
btn.grid(column=1, row=5)
window.mainloop()


answers=["Бесспорно","Предрешено","Никаких сомнений","Определённо да","Можешь быть уверен в этом","Мне кажется - да","Вероятнее всего","Хорошие перспективы","Знаки говорят - да","Да","Пока неясно, попробуй снова","Спроси позже","Лучше не рассказывать","Сейчас нельзя предсказать","Сконцентрируйся и спроси опять","Даже не думай","Мой ответ - нет","По моим данным - нет","Перспективы не очень хорошие","Весьма сомнительно"]
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input("Как тебя зовут?")
print(f"Привет, {name}")
again = 'д'
while again.lower() == 'д':
    question = input("Задай мне вопрос на которых хочешь получить ответ")
    print(random.choice(answers))
    again = input("Хотите задать еще один вопрос?(д=да, н=нет):")
    if again.lower() == "н":
        print("Возвращайся если возникнут вопросы!")
        break



