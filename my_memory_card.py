#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QMessageBox)
from random import randint, shuffle
class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
            self.question = question
            self.right_answer = right_answer
            self.wrong1 = wrong1
            self.wrong2 = wrong2
            self.wrong3 = wrong3
question_list = list()
question_list.append(Question('?','да','нет','возможно','неизвестно',))
question_list.append(Question('Во что тапаешь?','хомяк','капибара','арбуз','хз',))
question_list.append(Question('Лол','кек','чебурек','узбек','арбуз',))
question_list.append(Question('В каком положении находится язык при закрытом рте?','у нёба','внизу','в невесомости так сказать','прижат к зубам',))
question_list.append(Question('Кто из данных животных откладывает яйца?','птицы','рыбы','обезьяны','микробы',))
question_list.append(Question('Стоит ли тушить кипящее масло водой ?','нельзя','можно','нельзяБ но в редких случаях можно','можноБ но есть ограничения по технике безопасности',))
question_list.append(Question('Как по французски будет меня зовут?','Je ma pell','je ma pooll','Je mi nome','Je mi ninet',))
app  = QApplication([])
btn_OK = QPushButton("Ответить")
lb_Question = QLabel("кек")
RadioGroupBox = QGroupBox("Ваврианты ответов")
rbtn_1 = QRadioButton("атмосфера")
rbtn_2 = QRadioButton("вайб")
rbtn_3 = QRadioButton("иориг")
rbtn_4 = QRadioButton("ееееееее")

RadioGrop = QButtonGroup()
RadioGrop.addButton(rbtn_1)
RadioGrop.addButton(rbtn_2)
RadioGrop.addButton(rbtn_3)
RadioGrop.addButton(rbtn_4)

layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("результаты")
lb_Result = QLabel("Правильный ответ")
lb_Correct = QLabel("ответ тут")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result,alignment=(Qt.AlignLeft|Qt.AlignTop))
layout_res.addWidget(lb_Correct,alignment=Qt.AlignHCenter,stretch = 2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question,alignment=(Qt.AlignHCenter|Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK,stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1,stretch = 2)
layout_card.addLayout(layout_line2,stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
RadioGroupBox.show()
AnsGroupBox.hide()
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Следующий вопрос")
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText("Ответить")
    RadioGrop.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGrop.setExclusive(True)
answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно!")
        window.score +=1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Неверно!")

def next_question(): #рандомадизация вопросов 
    window.total +=1
    print("Статистика:")
    print("Колл-во вопросов:", window.total)
    print("Процент правильных ответов(рейтинг):", window.score/window.total*100)
    cur_question =randint(0,len(question_list)-1)
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[cur_question]
    
    ask(q)
def click_OK():
    if btn_OK.text()=='Ответить':
        check_answer()
    else:
        next_question()
btn_OK.clicked.connect(click_OK) 


window = QWidget()
window.cur_question = -1
window.setLayout(layout_card)
window.setWindowTitle("Memory card")
window.resize(500,300)
window.show()


#счётчик статистики
window.total = 0 #все
window.score = 0 #верные
app.exec()
