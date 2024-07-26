from tkinter import Tk,Entry,Button,StringVar

equ:str=' '
def press(charr:str) -> None:
    global equ
    if equ[-1] in "+-*/" and charr in "+-*/":
        equ=equ[0:len(equ)-1]
        equ+=charr
    elif charr not in ('=','CLR'):
        equ+=charr
    elif charr=='CLR':
        equ=' '
    elif charr=='=':
        equ=str(eval(equ))
    disp.set(equ)

if __name__=="__main__":
    win = Tk()
    disp = StringVar()

    display=Entry(win,textvariable=disp,width=60,state='readonly')
    display.grid(row=0,column=0,columnspan=4,pady=5,padx=5,ipady=5)
    
    b_add=Button(win,text="+",command= lambda: press('+'),width=10)
    b_add.grid(row=1,column=3,pady=5,padx=5,ipady=5)
    b_sub=Button(win,text="-",command= lambda: press('-'),width=10)
    b_sub.grid(row=2,column=3,pady=5,padx=5,ipady=5)
    b_mul=Button(win,text="*",command= lambda: press('*'),width=10)
    b_mul.grid(row=3,column=3,pady=5,padx=5,ipady=5)
    b_div=Button(win,text="/",command= lambda: press('/'),width=10)
    b_div.grid(row=4,column=3,pady=5,padx=5,ipady=5)

    b_num_1=Button(win,text="1",command= lambda: press('1'),width=10)
    b_num_1.grid(row=1,column=0,pady=5,padx=5,ipady=5)
    b_num_2=Button(win,text="2",command= lambda: press('2'),width=10)
    b_num_2.grid(row=1,column=1,pady=5,padx=5,ipady=5)
    b_num_3=Button(win,text="3",command= lambda: press('3'),width=10)
    b_num_3.grid(row=1,column=2,pady=5,padx=5,ipady=5)

    b_num_4=Button(win,text="4",command= lambda: press('4'),width=10)
    b_num_4.grid(row=2,column=0,pady=5,padx=5,ipady=5)
    b_num_5=Button(win,text="5",command= lambda: press('5'),width=10)
    b_num_5.grid(row=2,column=1,pady=5,padx=5,ipady=5)
    b_num_6=Button(win,text="6",command= lambda: press('6'),width=10)
    b_num_6.grid(row=2,column=2,pady=5,padx=5,ipady=5)

    b_num_7=Button(win,text="7",command= lambda: press('7'),width=10)
    b_num_7.grid(row=3,column=0,pady=5,padx=5,ipady=5)
    b_num_8=Button(win,text="8",command= lambda: press('8'),width=10)
    b_num_8.grid(row=3,column=1,pady=5,padx=5,ipady=5)
    b_num_9=Button(win,text="9",command= lambda: press('9'),width=10)
    b_num_9.grid(row=3,column=2,pady=5,padx=5,ipady=5)

    b_clear=Button(win,text="(",command= lambda: press('('),width=10)
    b_clear.grid(row=4,column=0,pady=5,padx=5,ipady=5)
    b_num_0=Button(win,text="0",command= lambda: press('0'),width=10)
    b_num_0.grid(row=4,column=1,pady=5,padx=5,ipady=5)
    b_equal=Button(win,text=")",command= lambda: press(')'),width=10)
    b_equal.grid(row=4,column=2,pady=5,padx=5,ipady=5)

    b_clear=Button(win,text="CLR",command= lambda: press('CLR'),width=10)
    b_clear.grid(row=5,column=0,pady=5,padx=5,ipady=5)
    b_num_0=Button(win,text=".",command= lambda: press('.'),width=10)
    b_num_0.grid(row=5,column=1,pady=5,padx=5,ipady=5)
    b_equal=Button(win,text="=",command= lambda: press('='),width=20)
    b_equal.grid(row=5,column=2,pady=5,padx=5,ipady=5,columnspan=2)

    win.mainloop()