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


# Scale
'''
import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')
l = tk.Label(window, bg = 'green', fg='white', width=20, text='empty')
l.pack()

def print_selection(v):
    l.config(text='You have selected'+v)
    
s = tk.Scale(window, label='try me', from_ =0, to= 10, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()

window.mainloop()
'''

# Canvas
'''
import tkinter as tk
window = tk.Tk()
window.title('My Window')
window.geometry('500x300')
canvas = tk.Canvas(window, bg='green',height=200, width=500)
image_file = tk.PhotoImage(file='pic.gif') #must be in the same folder
image = canvas.create_image(250, 0, anchor='n', image=image_file)

x0, y0, x1, y1 = 100,100,150,150
line = canvas.create_line(x0-50, y0-50, x1-50, y1-50)
oval = canvas.create_oval(x0+120, y0+50, x1+120, y1+50, fill='yellow')
arc = canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent = 180)
rect = canvas.create_rectangle(330, 30, 330+20, 30+20)
canvas.pack()

def moveit():
    canvas.move(rect, 2, 2)

b = tk.Button(window, text='move item', command=moveit).pack()

window.mainloop()
'''




# Menu
'''
import tkinter as tk
window = tk.Tk()
window.title()
window.geometry('500x300')
l = tk.Label(window, text=' ', bg='green')
l.pack()

counter = 0
def do_job():
    global counter
    l.config(text='do '+str(counter))
    counter += 1

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu = filemenu)

filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit',menu=editmenu)

editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Paste',command=do_job)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import',menu=submenu, underline=0)

submenu.add_command(label='Submenu_1', command=do_job)


window.config(menu = menubar)
window.mainloop()
'''


#Frame 
'''
import tkinter as tk
window = tk.Tk()
window.title('My Window')
window.geometry('500x300')
tk.Label(window, text = 'On the window', bg='red', font=('Arial',16)).pack()

frame = tk.Frame(window)
frame.pack()
frame_l = tk.Frame(frame)
frame_r = tk.Frame(frame)
frame_l.pack(side='left')
frame_r.pack(side='right')

tk.Label(frame_l, text='on the frame_l1', bg='green').pack()
tk.Label(frame_l, text='on the frame_l2', bg='green').pack()
tk.Label(frame_l, text='on the frame_l3', bg='green').pack()
tk.Label(frame_r, text='on the frame_r1', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r2', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r3', bg='yellow').pack()

window.mainloop()

'''

# messageBox
'''
import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

def hit_me():
    #tkinter.messagebox.showinfo(title='Hi',message='你好！')
    #tkinter.messagebox.showwarning(title='Hi',messange='警告')
    #tkinter.messagebox.showerror(title='Hi',messange='错误')
    print(tkinter.messagebox.askquestion(title='Hi',message='你好'))
    #print(tkinter.messagebox.askyesno(title='Hi', message='你好'))

tk.Button(window, text='hit me', bg='green',font=('Arial',14), command=hit_me).pack()

window.mainloop()
'''

# The Grid/Pack/Place geometry Manager

# Real Practice, Dynamic Login page

'''编写一个用户登录界面， 用户可以登录账户信息，如果账户已经存在，
可以直接登录， 登录名或者登录密码输入错误会提示， 如果账户不存在，
提示用户注册，点击注册进去注册页面， 输入注册信息，确定后便可以返回
登录界面进行登录
'''

import tkinter as tk
import tkinter.messagebox
import pickle

window = tk.Tk()

window.title('Welcome to 3K04!')

window.geometry('400x300')

# welcome page
canvas = tk.Canvas(window, width=400, height=135, bg='green')
image_file = tk.PhotoImage(file='3k04.gif')
image = canvas.create_image(200,0, anchor='n',image=image_file)
canvas.pack(side='top')
tk.Label(window, text='Welcome',font=('Arial',16)).pack()

#User information
tk.Label(window, text='MAC ID:',font=('Arial',14)).place(x=10,y=170)
tk.Label(window, text='MAC Password:',font=('Arial',14)).place(x=10,y=210)

# User login entry
#usr name
var_usr_name = tk.StringVar()
var_usr_name.set('example@mcmaster.ca')
entry_usr_name = tk.Entry(window, textvariable = var_usr_name, font=('Arial',14))
entry_usr_name.place(x=120,y=175)
#usr password
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial',14), show='*')
entry_usr_pwd.place(x=120,y=215)

#define user login function:
def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()

    try:
        with open('usrs_info.pickle','rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle','wb') as usr_file:
            usrs_info = {'admin':'admin'}
            pickle.dump(usrs_info, usr_file)
            usr_file.close()

    #if user name and password match the record in the file, login success
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tkinter.messagebox.showinfo(title='Welcome',message='You have signed into the pacemaker monitor center!'+usr_name)

        else:
            tkinter.messagebox.showerror(message='Error, your password is wrong, try again!')

    else:
        is_sign_up = tkinter.messagebox.askyesno('Welcome! ','You have not registered yet. Sign up now?')

        if is_sign_up:
            usr_sign_up()

# define usr registration function
def usr_sign_up():
    def sign_to_pacemaker_MonitorCenter():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()

        with open('usrs_info.pickle','rb')as usr_file:
            exist_usr_info = pickle.load(usr_file)

        if np != npf:
            tkinter.messagebox.showerror('Error','Password and confirm password must be the same!')
        
        elif nn in exist_usr_info:
            tkinter.messagebox.showerror('Error','The user has already signed up!')
        
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
                
            tkinter.messagebox.showinfo('Welcome','You have successfully signed up!')

            window_sign_up.destroy()


    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('300x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('example@mcmaster.ca')
    tk.Label(window_sign_up, text='User name: ').place(x=10,y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=130, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10,y=90)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=130,y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm Password: ').place(x=10,y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=130,y=50)

    btn_confirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_pacemaker_MonitorCenter)
    btn_confirm_sign_up.place(x=180,y=120)

btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=120,y=240)
btn_sign_up = tk.Button(window, text='Sign up',command=usr_sign_up)
btn_sign_up.place(x=200,y=240)

window.mainloop()


        
        