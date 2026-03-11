import pickle
output_file=open ("Visitor.bin", "ab")
pickle . dump ([], output_file)
output_file . close ()

from tkinter import *
choice=0

class Society:
    def __init__(self, name='', reson='', INtim='',Indte='', wing='', adr='', flat=" "):
        self.name = name
        self.reason = reson
        self.In_time = INtim
        self.In_date = Indte
        self.wing = wing
        self.addrress = adr
        self.flat= flat
        
    def input(self):
        import datetime
        window1=Tk()
        window1.title("INPUT")
        window1.geometry("450x425")
        
        def Exit1():
            window1.destroy()
        
        n=StringVar()
        r=StringVar()
        ad=StringVar()
        f=StringVar()
        var=StringVar()

        l=Label(window1,text="Enter Details",relief="solid",width=20,font=("arial",19,"bold"))
        l.place(x=65,y=50)

        l0=Label(window1,text="Enter your name:",font=("arial",12))
        l0.place(x=40,y=140)
        entry0=Entry(window1,textvar=n)
        entry0.place(x=215,y=140)
        
        l1=Label(window1,text="Reason for the visit:",font=("arial",12))
        l1.place(x=40,y=180)
        entry1=Entry(window1,textvar=r)
        entry1.place(x=215,y=180)
        
        l2=Label(window1,text="Enter vistor's addrress:",font=("arial",12))
        l2.place(x=40,y=220)
        entry2=Entry(window1,textvar=ad)
        entry2.place(x=215,y=220)
        
        l3=Label(window1,text="Select wing:",font=("arial",12))
        l3.place(x=40,y=270)
        r1=Radiobutton(window1,text="A",variable=var,value="A").place(x=215,y=270)
        r2=Radiobutton(window1,text="B",variable=var,value='B').place(x=265,y=270)
        r3=Radiobutton(window1,text="C",variable=var,value='C').place(x=315,y=270)
        r3=Radiobutton(window1,text="D",variable=var,value='D').place(x=365,y=270)
        
        l4=Label(window1,text="Enter flat:",font=("arial",12))
        l4.place(x=40,y=320)
        entry3=Entry(window1,textvar=f)
        entry3.place(x=215,y=320)

        b0=Button(window1,text="Save",width=12,bg="brown",fg="white",command=Exit1)
        b0.place(x=183,y=375)

        window1.mainloop()

        self.name = n.get().upper()
        self.reason = r.get().upper()
        a = datetime.datetime.now()
        self.In_date = str(f'{a.strftime("%A %d/%m/%Y")}')
        self.In_time = str(f'{a.strftime("%I:%M:%S %p")}')
        self.addrress = ad.get().upper()
        self.wing = var.get().upper()
        self.flat= f.get()
        
z=[]

def Window():
    window=Tk()
    window.geometry("250x435")
    window.title("START MENU")
    output_file=open ("Visitor.bin", "rb")
    z=pickle . load (output_file)
    output_file . close ()
    b=len(z)
        
    def Exit():
        window.destroy()
        
    def Clear():
        output_file=open ("Visitor.bin", "wb")
        pickle . dump ([], output_file)
        output_file . close ()
        output_file=open ("Visitor.bin", "rb")
        z=pickle . load (output_file)
        output_file . close ()
        b=len(z)
        a=f"No of Entries {b}"
        l1.config(text=a)
        
    def Main1():
        Exit()
        a = [Society() for i in range(1)]
        output_file=open ("Visitor.bin", "rb")
        zb=pickle . load (output_file)
        output_file . close ()
        zb.extend(a)
        for s in range(1):
            a[s].input()
            print()
        output_file=open ("Visitor.bin", "wb")
        pickle . dump (zb, output_file)
        output_file . close ()
        Window()

    def Main2():
        Exit()
        output_file=open ("Visitor.bin", "rb")
        z=pickle . load (output_file)
        output_file . close ()
        b=len(z)
        p1="Name: "+str(z[b-1].name)
        p2="Reason for the visit: "+str(z[b-1].reason)
        p3="Date of entry: "+z[b-1].In_date
        p4="Time of entry: "+z[b-1].In_time
        p5="Wing: "+str(z[b-1].wing)
        p6="Flat: "+str(z[b-1].flat)
        p7="Addrress: "+str(z[b-1].addrress)
        p=p1+"\n"+p2+"\n"+p3+"\n"+p4+"\n"+p5+"\n"+p6+"\n"+p7
        window2=Tk()
        window2.title("LAST ENTRY")
        def Exit2():
            window2.destroy()
        l1=Label(window2,text="Last Entry",relief="solid",font=("arial",19,"bold")).pack()
        l0=Label(window2,text=p,font=("arial",12)).pack()
        b0=Button(window2,text="Exit",width=12,bg="brown",fg="white",command=Exit2).pack()
        window2.mainloop()
        Window()
                
    def Main3():
        Exit()
        output_file=open ("Visitor.bin", "rb")
        z=pickle . load (output_file)
        output_file . close ()
        b=len(z)
        window3=Tk()
        window3.title("ALL ENTRY")
        def Exit3():
            window3.destroy()
        l1=Label(window3,text="All Entries",relief="solid",font=("arial",19,"bold")).pack()
        for y in range(b):
            p1="Name: "+str(z[y].name)
            p2="Reason for the visit: "+str(z[y].reason)
            p3="Date of entry: "+str(z[y].In_date)
            p4="Time of entry: "+str(z[y].In_time)
            p5="Wing: "+str(z[y].wing)
            p6="Flat: "+str(z[y].flat)
            p7="Addrress: "+str(z[y].addrress)
            p=p1+"\n"+p2+"\n"+p3+"\n"+p4+"\n"+p5+"\n"+p6+"\n"+p7+"\n"
            l0=Label(window3,text=p,font=("arial",12)).pack()
        b0=Button(window3,text="Exit",width=12,bg="brown",fg="white",command=Exit3)
        b0.pack()
        window3.mainloop()
        Window()
            
    def Main4():
        Exit()
        output_file=open ("Visitor.bin", "rb")
        z=pickle . load (output_file)
        output_file . close ()
        b=len(z)
        window4=Tk()
        window4.title("SEARCH")
        ser=StringVar()
        l0=Label(window4,text="Enter Name",font=("arial",12,"bold")).pack(padx=50)
        entry0=Entry(window4,textvar=ser).pack(padx=50)
        def Exit4():
            window4.destroy()
        b0=Button(window4,text="Search",width=12,bg="brown",fg="white",command=Exit4).pack()
        window4.mainloop()
        q=ser.get().upper()
        window5=Tk()
        window5.title("RESULTS")
        def Exit5():
            window5.destroy()
        l1=Label(window5,text="Results",relief="solid",font=("arial",19,"bold")).pack()
        for y in range(b):
            if q in z[y].name:
                p1="Name: "+str(z[y].name)
                p2="Reason for the visit: "+str(z[y].reason)
                p3="Date of entry: "+str(z[y].In_date)
                p4="Time of entry: "+str(z[y].In_time)
                p5="Wing: "+str(z[y].wing)
                p6="Flat: "+str(z[y].flat)
                p7="Addrress: "+str(z[y].addrress)
                p=p1+"\n"+p2+"\n"+p3+"\n"+p4+"\n"+p5+"\n"+p6+"\n"+p7+"\n"
                l0=Label(window5,text=p,font=("arial",12)).pack()
        b0=Button(window5,text="Exit",width=12,bg="brown",fg="white",command=Exit5)
        b0.pack()
        window5.mainloop()
        Window()
                
    def Main5():
        Exit()
        output_file=open ("Visitor.bin", "rb")
        z=pickle . load (output_file)
        output_file . close ()
        b=len(z)
        window4=Tk()
        window4.title("SEARCH")
        ser=StringVar()
        l0=Label(window4,text="Select Wing",font=("arial",12,"bold")).pack(padx=50)
        r1=Radiobutton(window4,text="A",variable=ser,value="A").pack(padx=50)
        r2=Radiobutton(window4,text="B",variable=ser,value='B').pack(padx=50)
        r3=Radiobutton(window4,text="C",variable=ser,value='C').pack(padx=50)
        r3=Radiobutton(window4,text="D",variable=ser,value='D').pack(padx=50)
        def Exit4():
            window4.destroy()
        b0=Button(window4,text="Search",width=12,bg="brown",fg="white",command=Exit4).pack()
        window4.mainloop()
        g=ser.get().upper()
        window5=Tk()
        window5.title("RESULTS")
        def Exit5():
            window5.destroy()
        l1=Label(window5,text="Results",relief="solid",font=("arial",19,"bold")).pack()
        for y in range(b):
            if g in z[y].wing:
                p1="Name: "+str(z[y].name)
                p2="Reason for the visit: "+str(z[y].reason)
                p3="Date of entry: "+str(z[y].In_date)
                p4="Time of entry: "+str(z[y].In_time)
                p5="Wing: "+str(z[y].wing)
                p6="Flat: "+str(z[y].flat)
                p7="Addrress: "+str(z[y].addrress)
                p=p1+"\n"+p2+"\n"+p3+"\n"+p4+"\n"+p5+"\n"+p6+"\n"+p7+"\n"
                l0=Label(window5,text=p,font=("arial",12)).pack()
        b0=Button(window5,text="Exit",width=12,bg="brown",fg="white",command=Exit5)
        b0.pack()
        window5.mainloop()
        Window()
        
    def Main6():
        Exit()
        output_file=open ("Visitor.bin", "rb")
        z=pickle . load (output_file)
        output_file . close ()
        b=len(z)
        window4=Tk()
        window4.title("SEARCH")
        ser=StringVar()
        l0=Label(window4,text="Enter Flat",font=("arial",12,"bold")).pack(padx=50)
        entry0=Entry(window4,textvar=ser).pack(padx=50)
        def Exit4():
            window4.destroy()
        b0=Button(window4,text="Search",width=12,bg="brown",fg="white",command=Exit4).pack()
        window4.mainloop()
        g=ser.get().upper()
        window5=Tk()
        window5.title("RESULTS")
        def Exit5():
            window5.destroy()
        l1=Label(window5,text="Results",relief="solid",font=("arial",19,"bold")).pack()
        for y in range(b):
            if g in str(z[y].flat) :
                p1="Name: "+str(z[y].name)
                p2="Reason for the visit: "+str(z[y].reason)
                p3="Date of entry: "+str(z[y].In_date)
                p4="Time of entry: "+str(z[y].In_time)
                p5="Wing: "+str(z[y].wing)
                p6="Flat: "+str(z[y].flat)
                p7="Addrress: "+str(z[y].addrress)
                p=p1+"\n"+p2+"\n"+p3+"\n"+p4+"\n"+p5+"\n"+p6+"\n"+p7+"\n"
                l0=Label(window5,text=p,font=("arial",12)).pack()
        b0=Button(window5,text="Exit",width=12,bg="brown",fg="white",command=Exit5)
        b0.pack()
        window5.mainloop()
        Window()

    def Main7():
        Exit()
        output_file=open ("Visitor.bin", "rb")
        z=pickle . load (output_file)
        output_file . close ()
        b=len(z)
        window4=Tk()
        window4.title("SEARCH")
        ser=StringVar()
        l0=Label(window4,text="Enter Vistor's Addrress",font=("arial",12,"bold")).pack(padx=50)
        entry0=Entry(window4,textvar=ser).pack(padx=50)
        def Exit4():
            window4.destroy()
        b0=Button(window4,text="Search",width=12,bg="brown",fg="white",command=Exit4).pack()
        window4.mainloop()
        g=ser.get().upper()
        window5=Tk()
        window5.title("RESULTS")
        def Exit5():
            window5.destroy()
        l1=Label(window5,text="Results",relief="solid",font=("arial",19,"bold")).pack()
        for y in range(b):
            if g in z[y].addrress:
                p1="Name: "+str(z[y].name)
                p2="Reason for the visit: "+str(z[y].reason)
                p3="Date of entry: "+str(z[y].In_date)
                p4="Time of entry: "+str(z[y].In_time)
                p5="Wing: "+str(z[y].wing)
                p6="Flat: "+str(z[y].flat)
                p7="Addrress: "+str(z[y].addrress)
                p=p1+"\n"+p2+"\n"+p3+"\n"+p4+"\n"+p5+"\n"+p6+"\n"+p7+"\n"
                l0=Label(window5,text=p,font=("arial",12)).pack()
        b0=Button(window5,text="Exit",width=12,bg="brown",fg="white",command=Exit5)
        b0.pack()
        window5.mainloop()
        Window()
           
    def Main8():
        Exit()
        output_file=open ("Visitor.bin", "rb")
        z=pickle . load (output_file)
        output_file . close ()
        b=len(z)
        window4=Tk()
        window4.title("SEARCH")
        ser=StringVar()
        l0=Label(window4,text="Enter Resaon",font=("arial",12,"bold")).pack(padx=50)
        entry0=Entry(window4,textvar=ser).pack(padx=50)
        def Exit4():
            window4.destroy()
        b0=Button(window4,text="Search",width=12,bg="brown",fg="white",command=Exit4).pack()
        window4.mainloop()
        g=ser.get().upper()
        window5=Tk()
        window5.title("RESULTS")
        def Exit5():
            window5.destroy()
        l1=Label(window5,text="Results",relief="solid",font=("arial",19,"bold")).pack()
        for y in range(b):
            if g in z[y].reason:
                p1="Name: "+str(z[y].name)
                p2="Reason for the visit: "+str(z[y].reason)
                p3="Date of entry: "+str(z[y].In_date)
                p4="Time of entry: "+str(z[y].In_time)
                p5="Wing: "+str(z[y].wing)
                p6="Flat: "+str(z[y].flat)
                p7="Addrress: "+str(z[y].addrress)
                p=p1+"\n"+p2+"\n"+p3+"\n"+p4+"\n"+p5+"\n"+p6+"\n"+p7+"\n"
                l0=Label(window5,text=p,font=("arial",12)).pack()
        b0=Button(window5,text="Exit",width=12,bg="brown",fg="white",command=Exit5)
        b0.pack()
        window5.mainloop()
        Window()

    def Main9():
        Exit()
        output_file=open ("Visitor.bin", "rb")
        z=pickle . load (output_file)
        output_file . close ()
        b=len(z)
        window4=Tk()
        window4.title("SEARCH")
        ser=StringVar()
        l0=Label(window4,text="Enter Flat",font=("arial",12,"bold")).pack(padx=50)
        entry0=Entry(window4,textvar=ser).pack(padx=50)
        def Exit4():
            window4.destroy()
        ser1=StringVar()
        l0=Label(window4,text="Select Wing",font=("arial",12,"bold")).pack(padx=50)
        r1=Radiobutton(window4,text="A",variable=ser1,value="A").pack(padx=50)
        r2=Radiobutton(window4,text="B",variable=ser1,value='B').pack(padx=50)
        r3=Radiobutton(window4,text="C",variable=ser1,value='C').pack(padx=50)
        r3=Radiobutton(window4,text="D",variable=ser1,value='D').pack(padx=50)
        b0=Button(window4,text="Search",width=12,bg="brown",fg="white",command=Exit4).pack()
        window4.mainloop()
        g=ser.get().upper()
        g_1=ser1.get().upper()
        window5=Tk()
        window5.title("RESULTS")
        def Exit5():
            window5.destroy()
        l1=Label(window5,text="Results",relief="solid",font=("arial",19,"bold")).pack()
        for y in range(b):
            if g in str(z[y].flat) and g_1 in z[y].wing:
                p1="Name: "+str(z[y].name)
                p2="Reason for the visit: "+str(z[y].reason)
                p3="Date of entry: "+str(z[y].In_date)
                p4="Time of entry: "+str(z[y].In_time)
                p5="Wing: "+str(z[y].wing)
                p6="Flat: "+str(z[y].flat)
                p7="Addrress: "+str(z[y].addrress)
                p=p1+"\n"+p2+"\n"+p3+"\n"+p4+"\n"+p5+"\n"+p6+"\n"+p7+"\n"
                l0=Label(window5,text=p,font=("arial",12)).pack()
        b0=Button(window5,text="Exit",width=12,bg="brown",fg="white",command=Exit5)
        b0.pack()
        window5.mainloop()
        Window()

    def Main():
        choice=rad.get()
        if choice==1:
            Main1()
        elif choice==2:
            Main2()
        elif choice==3:
            Main3()
        elif choice==4:
            Main4()
        elif choice==5:
            Main5()
        elif choice==6:
            Main6()
        elif choice==7:
            Main7()
        elif choice==8:
            Main8()
        elif choice==9:
            Main9()
        else:
            Exit()
            Window()

    rad=IntVar()
    
    l=Label(window,text="KALPATARU HILLS HSc",width=20,relief="solid",font=("arial",15,"bold"))
    l.place(x=2,y=5)
    l0=Label(window,text="VISITORS ENTRY LOG :-",font=("arial",14))
    l0.place(x=10,y=40)

    l=Label(window,text="What do you want to do: ",font=("arial",15,"bold"))
    l.place(x=5,y=70)

    l1=Label(window,text=f"No of Entries {b}",font=("arial",13))
    l1.place(x=55,y=103)

    r1=Radiobutton(window,text="New Entry",variable=rad,value=1)
    r1.place(x=50,y=135)

    r2=Radiobutton(window,text="See Last Entry",variable=rad,value=2)
    r2.place(x=50,y=160)

    r3=Radiobutton(window,text="See All Entries",variable=rad,value=3)
    r3.place(x=50,y=185)

    r4=Radiobutton(window,text="Search by Name",variable=rad,value=4)
    r4.place(x=50,y=210)

    r5=Radiobutton(window,text="Search by Wing",variable=rad,value=5)
    r5.place(x=50,y=235)

    r6=Radiobutton(window,text="Search by Flat",variable=rad,value=6)
    r6.place(x=50,y=260)

    r7=Radiobutton(window,text="Search by Vistor's Addrress",variable=rad,value=7)
    r7.place(x=50,y=285)

    r8=Radiobutton(window,text="Search by Reason",variable=rad,value=8)
    r8.place(x=50,y=310)

    r9=Radiobutton(window,text="Search by Flat and Wing",variable=rad,value=9)
    r9.place(x=50,y=335)

    b1=Button(window,text="Next",width=12,bg="brown",fg="white",command=Main)
    b1.place(x=140,y=370)

    b2=Button(window,text="Exit",width=12,bg="brown",fg="white",command=Exit)
    b2.place(x=20,y=370)

    b3=Button(window,text="Clear Entries",width=12,bg="brown",fg="white",command=Clear)
    b3.place(x=80,y=400)
    
    window.mainloop()
    
Window()
