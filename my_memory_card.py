#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3= wrong3

app =QApplication([])
main = QWidget()
main.setWindowTitle('Memory Card')

v_main_layout= QVBoxLayout()

label1 = QLabel('Вопрос')
group1 = QGroupBox("Варианты ответов")
button1= QPushButton('Ответить')

v_grp_layout1=QVBoxLayout()
v_grp_layout2=QVBoxLayout()
h_grp_layout1=QHBoxLayout()

RadioGroup= QButtonGroup()

radio1=QRadioButton('вопрос1')
radio2=QRadioButton('вопрос2')
radio3=QRadioButton('вопрос3')
radio4=QRadioButton('вопрос4')

radio1.setStyleSheet('QRadioButton {background-color :  lightskyblue}')
radio2.setStyleSheet('QRadioButton {background-color :  lightskyblue}')
radio3.setStyleSheet('QRadioButton {background-color :  lightskyblue}')
radio4.setStyleSheet('QRadioButton {background-color :  lightskyblue}')

RadioGroup.addButton(radio1)
RadioGroup.addButton(radio2)
RadioGroup.addButton(radio3)
RadioGroup.addButton(radio4)

v_grp_layout1.addWidget(radio1)
v_grp_layout1.addWidget(radio2)

v_grp_layout2.addWidget(radio3)
v_grp_layout2.addWidget(radio4)

h_grp_layout1.addLayout(v_grp_layout1)
h_grp_layout1.addLayout(v_grp_layout2)

group1.setLayout(h_grp_layout1)

group2 = QGroupBox("Результат")
labelresult= QLabel('Правильно/Неправильно')
labelanswer=QLabel('Правильный ответ')
v_grp_layout3=QVBoxLayout()
v_grp_layout3.addWidget(labelresult)
v_grp_layout3.addWidget(labelanswer,alignment = Qt.AlignHCenter)
group2.setLayout(v_grp_layout3)

v_main_layout.addWidget(label1, alignment = Qt.AlignHCenter)
v_main_layout.addWidget(group1)
v_main_layout.addWidget(group2)
v_main_layout.addWidget(button1, alignment = Qt.AlignCenter)

main.setLayout(v_main_layout)

main.total = 0
main.score = 0

def show_result():
    group1.hide()
    group2.show()
    button1.setText('Следующий вопрос')

def show_question():
    group1.show()
    group2.hide()
    button1.setText('Ответить')
    RadioGroup.setExclusive(False)
    radio1.setChecked(False)
    radio2.setChecked(False)
    radio3.setChecked(False)
    radio4.setChecked(False)
    RadioGroup.setExclusive(True)
   
answer=[radio1, radio2 , radio3, radio4]
question_list=[]
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
question_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
question_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
question_list.append(Question('Самое глубокое озеро в мире', 'Байкал', 'Виктория', 'Мичиган', 'Танганьика'))
question_list.append(Question('Сколько штатов в США?', '50', '48', '52', '65'))



def ask(q:Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    label1.setText(q.question)
    labelanswer.setText(q.right_answer)
    show_question()

def show_correct(result):
    labelresult.setText(result)
    show_result()

def check():
    if answer[0].isChecked():
        main.score = main.score +1
        show_correct('Правильно')
    elif answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
        show_correct('Неправильно')
    print("Статистика")
    print("Всего вопросов:", main.total)
    print("Правильных ответов:", main.score)
    print('Рейтинг:', main.score / main.total * 100)
main.cur_question= -1
def next_question():
    #main.cur_question += 1
    #if main.cur_question >= len(question_list):
    #    main.cur_question = 0
    main.total = main.total + 1
    cur = randint(0,len(question_list)-1)
    q = question_list[cur]
    ask(q)
    print("Статистика")
    print("Всего вопросов:", main.total)
    print("Правильных ответов:", main.score)
    print('Рейтинг:', main.score / main.total * 100)

def but_ok():
    if button1.text() == 'Ответить':
        check()
    else:
        next_question()


button1.clicked.connect(but_ok)
next_question()
group1.show()
group2.hide()

main.show()
app.exec()