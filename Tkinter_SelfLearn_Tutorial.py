#Tutorial

#initialize a window
'''
import tkinter as tk

window = tk.Tk()

window.title('My Window')

window.geometry('500x300')

l = tk.Label(window, text='Banzai!',bg = 'green',font=('Arial',12),width=30,height=2)

l.pack()

window.mainloop()

'''


'''
# register a button with command--------------

import tkinter as tk

window = tk.Tk()

window.title('My Window')

window.geometry('500x300')

var = tk.StringVar()

l = tk.Label(window, textvariable = var, bg = 'green', fg = 'white', font = ('Arial',12), width = 30, height = 2)

l.pack()

on_hit = False

def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('You hit me!')
    else:
        on_hit = False;
        var.set('');

b = tk.Button(window, text='hit me', font = ('Arial',12), width = 10, height = 1, command=hit_me)

b.pack() #place the button

window.mainloop()
'''

# Entry 是 tkinter类中提供的一个单行文本输入域，用来输入显示一行文本，收集键盘输入
'''
import tkinter as tk

window = tk.Tk()

window.title('My Window')

window.geometry('500x300')

e1 = tk.Entry(window, show='*', font=('Arial',14))
e2 = tk.Entry(window, show='h',font=('Arial',14))
e1.pack()
e2.pack()

window.mainloop()
'''

# Text-----------
'''
import tkinter as tk

window = tk.Tk()
window.title('My Window') 
window.geometry('500x300')
e = tk.Entry(window, show=None)
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert',var)

def insert_end():
    var = e.get()
    t.insert('end',var)

b1 = tk.Button(window, text='insert point', width = 10, height = 2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert back',width = 10, height = 2, command=insert_end)
b2.pack()

t = tk.Text(window, height = 3)
t.pack()

window.mainloop()
'''

# Listbox
'''
import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

var1 = tk.StringVar()
l = tk.Label(window, bg='green',fg='white',font=('Arial',12),width=10, textvariable = var1)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

b1 = tk.Button(window, text='print selection',width=15, height=2, command=print_selection)
b1.pack()


var2 = tk.StringVar()
var2.set((1,2,3,4))

lb = tk.Listbox(window, listvariable=var2)
list_items = [11,22,33,44]
for item in list_items:
    lb.insert('end',item)

lb.insert(1,'first')
lb.insert(2,'second')
lb.delete(2)
lb.pack()
 
window.mainloop()
'''


# Radiobutton 代表一个变量， 它可以有多个值中的一个， 点击它将为这个变量设置值，并且清除与这同一变量相关的其他radiobutton
'''
import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')
var = tk.StringVar()
l = tk.Label(window, bg='yellow',width=20,text='empty')
l.pack()
def print_selection():
    l.config(text='you have selected '+var.get())

r1 = tk.Radiobutton(window, text='Option A',variable = var, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B',variable = var, value='B',command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C',variable =var, value='C',command=print_selection)
r3.pack()

window.mainloop()
'''

#Checkbutton  代表一个变量，有个不同的值，点击这个按钮将会在这两这个值间切换，选择和取消选择
'''
import tkinter as tk
window = tk.Tk()
window.title('My Window')
window.geometry('500x300')
l = tk.Label(window, bg='yellow',width=20,text='empty')
l.pack()

def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love only Python')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both!')

var1 = tk.IntVar()
var2 = tk.IntVar()

c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue = 1, offvalue = 0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='C++', variable = var2, onvalue = 1, offvalue = 0, command = print_selection)
c2.pack()

window.mainloop()
'''







