from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
time.clock= time.time
import os

data_list = ['What is the capital of India',
             'Delhi is the capital of India',
             'In which language you talk',
             'I mostly talk in english',
             'What you do in free time',
             'Ok bye',
             'I memorize things in my free time',
             'bye take care',
             'which are created by you''who created you',
             'Naresh kr, Atul Kumar, Aakash, Abhishek Kumar created by me',
             'can you sujest best data science course platform',
             'Top five best platform \n 1. Cursera \n 2. W3 SCHOOL'

]


bot = ChatBot('Bot')

trainer = ListTrainer(bot)

'''
for files in os.listdir('data/english/'):
    data = open('data/english/'+files,'r', encoding='utf-8').readlines()
'''

trainer.train(data_list)


def botReply():
    question = questionField.get()
    question = question.capitalize()
    answer =bot.get_response(question)
    textarea.insert(END,"You: "+question+'\n\n' )
    textarea.insert(END, "Bot: "+str(answer)+'\n\n')
    #pyttsx3.speak(answer)
    questionField.delete(0, END)


root = Tk()
root.geometry('500x570+100+50')
root.title("Chat_Bot")
root.iconbitmap('logo.png')

root.config(bg='#00ccff')
logoPic = PhotoImage(file='pic.png')

logoPicLabel=Label(root, image=logoPic, bg="#00ccff")

logoPicLabel.pack(pady=5)

centerFrame = Frame(root)
centerFrame.pack()

scrollbar = Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea = Text(centerFrame, font=('times new roman',20, 'bold'),height=10, yscrollcommand=scrollbar.set, wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)
placeholder_text = 'Type here...'
questionField = Entry(root,font=('verdana', 20, 'bold'))
questionField.pack(pady=15, fill=X)
questionField.insert(0, placeholder_text )


askPic = PhotoImage(file='ask.png')
askButton = Button(root, image=askPic, height=35, width=45, command=botReply)
askButton.pack()

def click(event):
    askButton.invoke()
root.bind('<Return>',click)



root.mainloop()