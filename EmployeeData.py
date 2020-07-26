from tkinter import *
from tkinter import ttk
from tkinter import messagebox



frm=Tk()

fnt   = 'None 30 bold'
bg    = '#00eeff'
bgtxt = '#ffffff'
fg    ='blue'
fw    =700
fh    =500
x     = (frm.winfo_screenwidth()-fw)/2
y     = (frm.winfo_screenheight() -fh)/2-50
pad   = 10
frm.geometry('%dx%d+%d+%d'%(fw,fh,x,y))
frm.title('Employee File Data')
frm.iconbitmap('my.ico')
frm.config(bg=bg)

frm.iconbitmap('my.ico')

Label(frm,text= "Employee Data ", bg='navy',fg='lightblue',font=fnt).pack(pady=pad)
frame=Frame(frm,bg=bg)
frame.pack(pady=pad)


Label(frame,text='Code:',bg=bg,fg=fg,font=fnt).grid(row=0,column=0)
Label (frame,text='Name:',bg=bg,fg=fg,font=fnt).grid(row=1,column=0)
Label(frame,text='address:',bg=bg,fg=fg,font=fnt).grid(row=2,column=0)
svcode=StringVar()
svname=StringVar()
svaddress=StringVar()
txtcode=Entry(frame,bg=bgtxt,fg=fg,font=fnt,textvariable=svcode)
txtname=Entry(frame,bg=bgtxt,fg=fg,font=fnt,textvariable=svname)
txtaddress=Entry(frame,bg=bgtxt,fg=fg,font=fnt,textvariable=svaddress)

txtcode.grid(row=0,column=1,pady=pad)
txtname.grid(row=1,column=1,pady=pad)
txtaddress.grid(row=2,column=1,pady=pad)

def Create():
    if svcode.get().strip()=='':#strip تعمل على حذف مسافات
        messagebox.showinfo('','Code is Empty !')
        txtcode.focus()
    elif svname.get().strip()=='':
        messagebox.showinfo('','Name is Empty !')
        txtname.focus()
    elif svaddress.get().strip()=='':
        messagebox.showinfo('','Adress is Empty !')
        txtaddress.focus()#هذا عشان يرجع السهم تاع الكتابة باول خانة
    else:
        filename=svcode.get() + '_' + svname.get() + '.xlx'
        f =open(filename,'w+')#هنا لاظافة سطر شاهد الحلقة لمعرفة التفاصيل
        f.write('code      : ' + svcode.get() + '\n')
        f.write('Name      : ' + svname.get() + '\n')
        f.write('addresse   : ' + svaddress.get() + '\n')
        f.close()
        svcode.set('')
        svname.set('')
        svaddress.set('')
        messagebox.showinfo('','Employee File is Create...')
        
        
btnstyle=ttk.Style()
btnstyle.configure('TButton',font=fnt,pady=pad,padding=pad)
ttk.Button(frm,text="Create Employee File Now",command=Create).pack()
ttk.Button(frm,text='Exit Now',command=frm.destroy).pack()#destroyمعناها تدمير استخدمناها عشان نطلع من البرنامج
frm.mainloop()
