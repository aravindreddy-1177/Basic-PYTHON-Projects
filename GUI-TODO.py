from tkinter import *
from tkinter import simpledialog
from tkinter.font import Font
root=Tk()
root.geometry('500x450+500+200')
root.title("To do List")
root.config(bg="#ff7f50")
root.iconbitmap('todo.ico')
task_l=[]
def add_t():
    t=simpledialog.askstring("input","Enter The Task:")
    if t:
        task_l.append(t) 
        update_list()
def update_list():
    list_view.delete(0, END)  # Clear the Listbox
    for i in task_l:
        list_view.insert(END,i)
def del_task():
        task_idx = list_view.curselection()[0]
        del task_l[task_idx]
        update_list()
h=Label(root,text="Tasks To Be Done!",font=("Areial",18,'bold'),bg='#ff7f50',fg='black')
h.pack()
text_frame = Frame(root, borderwidth=6, bg="white",padx=10,pady=10)
text_frame.pack()
button_frame = Frame(root,bg="#fcefef")
button_frame.pack(pady=10)
b1= Button(button_frame,fg="black",bg="#7fd8be",text="Add Task",font=("Areial",14,'bold'),command=add_t)
b1.pack(side=LEFT,padx=15,pady=10)
b2=Button(button_frame,fg='black',bg="#7fd8be",text="Delete Task",font=("Areial",14,'bold'),command=del_task)
b2.pack(side=LEFT,padx=15,pady=10)
l_frame=Frame(root)
l_frame.pack(pady=10)
l_font=Font(
    family='Areial',
    size=12,
    weight="bold",
)
list_view=Listbox(
    l_frame,
    width=45,
    height=14,
    bd=0,
    font=l_font,
    fg='black',
    highlightthickness=0,
    selectbackground='grey',
    bg='#7fd8be',
    activestyle='none',
)
list_view.pack(side=LEFT, fill=BOTH)
scrollbar = Scrollbar(l_frame)
scrollbar.pack(side=RIGHT, fill=Y)
list_view.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list_view.yview)
root.mainloop()