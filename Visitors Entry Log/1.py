class Society:
    def __init__(self, name='', reson='', INtim='', wing='', adr='', flat=" "):
        self.name = name
        self.reason = reson
        self.In_time = INtim
        self.wing = wing
        self.addrress = adr
        self.flat= flat
        
    def input(self):
        import datetime
        self.name = input("Enter your name: ").upper()
        self.reason = input("Reason for the visit: ").upper()
        self.In_time = datetime.datetime.now()
        self.addrress = input("Enter vistor's addrress: ").upper()
        try:
            self.flat= int(input("Enter flat: "))
        except:
            print("Enter number only")
            self.flat= int(input("Enter flat: "))
        self.wing = input("Enter wing (A,B,C,D): ").upper()
        if self.wing not in ("A","B","C","D"):
            print("Enter A,B,C,D only")
            self.wing = input("Enter wing (A,B,C,D): ").upper()

counter=wrong=choice=0
z=[]
print("***************** KALPATARU HILLS HSc. *****************")
print()
print("         ********* VISITORS ENTRY LOG *********         ")
print()
print("1] New Entry")
print("2] Exit")
try:
    print()
    choice=int(input("Enter your choice: "))
    print()
except:
    wrong+=1
    
if choice==1:
    a = [Society() for i in range(1)]
    z.extend(a)
    for s in range(1):
        a[s].input()
        counter+=1
        print()
elif choice==2:
    print("Exiting Program")
    raise SystemExit
    
print()
choice=0

while 1>0:
    print("No. of Entries Recorded:",counter)
    print("What do you want to do: ")
    print("1]  New Entry")
    print("2]  See Last Entry")
    print("3]  See All Entries")
    print("4]  Search by Name")
    print("5]  Search by Wing")
    print("6]  Search by Flat")
    print("7]  Search by Vistor's Addrress")
    print("8]  Search by Reason")
    print("9]  Search by Flat and Wing")
    print("10] Exit the Program")

    try:
        print()
        choice=int(input("Enter your choice: "))
        print()
    except:
        if wrong<5:
            print("Enter number between 1 to 10")
            print()
            print()
            wrong+=1
        else:
            print("You have not entered any number.\nSo ending the program")
            break

    wrong=0
    if choice==1:
        a = [Society() for i in range(1)]
        z.extend(a)
        for s in range(1):
            a[s].input()
            counter+=1
            print()

    elif choice==2:
        b=len(z)
        print("Name:",z[b-1].name)
        print("Reason for the visit:",z[b-1].reason)
        print("Day of entry:",z[b-1].In_time.strftime("%A"),z[b-1].In_time.strftime("%d"),z[b-1].In_time.strftime("%m"),z[b-1].In_time.strftime("%Y"))
        print("Time of entry:",z[b-1].In_time.strftime("%I"),z[b-1].In_time.strftime("%M"),z[b-1].In_time.strftime("%p"))
        print("Wing:",z[b-1].wing)
        print("Flat:",z[b-1].flat)
        print("Addrress:",z[b-1].addrress)
        print()
        
        
    elif choice==3:
        b=len(z)
        for y in range(b):
            print("Name:",z[y].name)
            print("Reason for the visit:",z[y].reason)
            print("Day of entry:",z[y].In_time.strftime("%A"),z[y].In_time.strftime("%d"),z[y].In_time.strftime("%m"),z[y].In_time.strftime("%Y"))
            print("Time of entry:",z[y].In_time.strftime("%I"),z[y].In_time.strftime("%M"),z[y].In_time.strftime("%p"))
            print("Wing:",z[y].wing)
            print("Flat:",z[y].flat)
            print("Addrress:",z[y].addrress)
            print()
        
    elif choice==4:
        b=len(z)
        q=input("Enter Name: ").upper()
        print()
        for y in range(b):
            if q in z[y].name:
                print("Name:",z[y].name)
                print("Reason for the visit:",z[y].reason)
                print("Day of entry:",z[y].In_time.strftime("%A"),z[y].In_time.strftime("%d"),z[y].In_time.strftime("%m"),z[y].In_time.strftime("%Y"))
                print("Time of entry:",z[y].In_time.strftime("%I"),z[y].In_time.strftime("%M"),z[y].In_time.strftime("%p"))
                print("Wing:",z[y].wing)
                print("Flat:",z[y].flat)
                print("Addrress:",z[y].addrress)
                print()
                
    elif choice==5:
        b=len(z)
        g=input("Enter Wing (A,B,C,D): ").upper()
        if g not in ("A","B","C","D"):
            print("Enter A,B,C,D only")
            g = input("Enter wing (A,B,C,D): ").upper()
        if g not in ("A","B","C","D"):
            g="NO ENTRY"
        print()
        for y in range(b):
            if g in z[y].wing:
                print("Name:",z[y].name)
                print("Reason for the visit:",z[y].reason)
                print("Day of entry:",z[y].In_time.strftime("%A"),z[y].In_time.strftime("%d"),z[y].In_time.strftime("%m"),z[y].In_time.strftime("%Y"))
                print("Time of entry:",z[y].In_time.strftime("%I"),z[y].In_time.strftime("%M"),z[y].In_time.strftime("%p"))
                print("Wing:",z[y].wing)
                print("Flat:",z[y].flat)
                print("Addrress:",z[y].addrress)
                print()

    elif choice==6:
        b=len(z)
        try:
            g= input("Enter flat: ")
        except:
            print("Enter number only")
        print()
        for y in range(b):
            if g in str(z[y].flat) :
                print("Name:",z[y].name)
                print("Reason for the visit:",z[y].reason)
                print("Day of entry:",z[y].In_time.strftime("%A"),z[y].In_time.strftime("%d"),z[y].In_time.strftime("%m"),z[y].In_time.strftime("%Y"))
                print("Time of entry:",z[y].In_time.strftime("%I"),z[y].In_time.strftime("%M"),z[y].In_time.strftime("%p"))
                print("Wing:",z[y].wing)
                print("Flat:",z[y].flat)
                print("Addrress:",z[y].addrress)
                print()

    elif choice==7:
        b=len(z)
        g=input("Enter Vistor's Addrress: ").upper()
        print()
        for y in range(b):
            if g in z[y].addrress:
                print("Name:",z[y].name)
                print("Reason for the visit:",z[y].reason)
                print("Day of entry:",z[y].In_time.strftime("%A"),z[y].In_time.strftime("%d"),z[y].In_time.strftime("%m"),z[y].In_time.strftime("%Y"))
                print("Time of entry:",z[y].In_time.strftime("%I"),z[y].In_time.strftime("%M"),z[y].In_time.strftime("%p"))
                print("Wing:",z[y].wing)
                print("Flat:",z[y].flat)
                print("Addrress:",z[y].addrress)
                print()
           
    elif choice==8:
        b=len(z)
        g=input("Enter Reason: ").upper()
        print()
        for y in range(b):
            if g in z[y].reason:
                print("Name:",z[y].name)
                print("Reason for the visit:",z[y].reason)
                print("Day of entry:",z[y].In_time.strftime("%A"),z[y].In_time.strftime("%d"),z[y].In_time.strftime("%m"),z[y].In_time.strftime("%Y"))
                print("Time of entry:",z[y].In_time.strftime("%I"),z[y].In_time.strftime("%M"),z[y].In_time.strftime("%p"))
                print("Wing:",z[y].wing)
                print("Flat:",z[y].flat)
                print("Addrress:",z[y].addrress)
                print()

    elif choice==9:
        b=len(z)
        try:
            g= (input("Enter flat: "))
        except:
            print("Enter number only")
            g= (input("Enter flat: "))
        g_1=input("Enter Wing (A,B,C,D): ").upper()

        if g_1 not in ("A","B","C","D"):
            print("Enter A,B,C,D only")
            g_1 = input("Enter wing (A,B,C,D): ").upper()       
        print()
        for y in range(b):
            if g in str(z[y].flat) and g_1 in z[y].wing:
                print("Name:",z[y].name)
                print("Reason for the visit:",z[y].reason)
                print("Day of entry:",z[y].In_time.strftime("%A"),z[y].In_time.strftime("%d"),z[y].In_time.strftime("%m"),z[y].In_time.strftime("%Y"))
                print("Time of entry:",z[y].In_time.strftime("%I"),z[y].In_time.strftime("%M"),z[y].In_time.strftime("%p"))
                print("Wing:",z[y].wing)
                print("Flat:",z[y].flat)
                print("Addrress:",z[y].addrress)
                print()
                
    elif choice==10:
        print("Thank you for using")
        break
    
    elif choice>=11:
        wrong+=1
        if wrong<5:
            print("Enter number between 1 to 10")
            print()
            print()
        else:
            print("You have entered wrong number.\nSo ending the program")
            break
