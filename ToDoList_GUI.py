import tkinter as tk
from tkinter import ttk,Frame
import os

os.chdir(os.getcwd())

class Task(Frame):
    def __init__(self,x,y,task_text):
        Frame.__init__(self,root)
        self.x = x
        self.y = y
        self.task_text = task_text
        
        self.task_entry = ttk.Entry(self,width=30,font=(10))
        self.task_entry.insert(0,self.task_text)
        self.task_entry.grid(row=0,column=0)
        self.task_entry.bind('<KeyRelease>', self.update_task_text)
        
        check_button = ttk.Checkbutton(self,text="Done",state='',width=5)
        check_button.grid(row=0,column=1)
        
        delete_button = tk.Button(self,text="X",font=("arial",13,'bold'),command=self.delete_task,width=5)
        delete_button.grid(row=0,column=2)
    
    
    def update_task_text(self, event):
        self.task_text = self.task_entry.get()
    
    
    
    def delete_task(self):
        self.destroy()
        task_list.remove(self)
        save_tasks()
        
    
    
    
    def display(self):
        self.place(x=self.x,y=self.y)


def save_tasks():
    with open('tasks.txt','w') as file:
        for task in task_list:
            file.write(task.task_text + '\n')


def load_tasks():
    if os.path.exists('tasks.txt'):
        with open('tasks.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                task_text = line.strip()
                task = Task(50,(len(task_list) + 1 )* 50,task_text)
                task_list.append(task)
                task.display()


task_list = []

def add_task():
    
    if len(task_list) > 0:
        task = Task(task_list[-1].x , task_list[-1].y + 50,"")
        task_list.append(task)
    else:
        task =  Task(50,50,"")
        task_list.append(task)
    
    for task in task_list:
        task.display()
    
    save_tasks()



root = tk.Tk()
root.geometry("600x600")
root.title("To Do List")
root['background'] = 'white'
app_name = ttk.Label(root,text="My Tasks",font=('arial',24))
app_name.place(x=240,y=0)
add_task_button = tk.Button(root,text="Add Task",width=15,font=('arial',10),command=add_task)
add_task_button.place(x = 240,y=550)

load_tasks()

root.mainloop()
save_tasks()