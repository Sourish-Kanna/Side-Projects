import pickle
output_file=open ("Visitor.bin", "ab")
pickle . dump ([], output_file)
output_file . close ()

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
        self.name = input("Enter your name: ").upper()
        self.reason = input("Reason for the visit: ").upper()
        a = datetime.datetime.now()
        self.In_date = str(f'{a.strftime("%A %d/%m/%Y")}')
        self.In_time = str(f'{a.strftime("%I:%M:%S %p")}')
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

wrong=choice=0

print("***************** KALPATARU HILLS HSc. *****************")
print()
print("         ********* VISITORS ENTRY LOG *********         ")

while 1>0:
    output_file=open ("Visitor.bin", "rb")
    z=pickle . load (output_file)
    output_file . close ()
    counter=len(z)
    print("No. of Entries Recorded:",counter)
    print("What do you want to do: ")
    print("0]  Exit the Program")    
    print("1]  New Entry")
    print("2]  See Last Entry")
    print("3]  See All Entries")
    print("4]  Search by Name")
    print("5]  Search by Wing")
    print("6]  Search by Flat")
    print("7]  Search by Vistor's Addrress")
    print("8]  Search by Reason")
    print("9]  Search by Flat and Wing")
    print("10] Clear entry")

    try:
        print()
        choice=int(input("Enter your choice: "))
        print()
    except:
        if wrong<5:
            print("Enter number between 0 to 10")
            print()
            print()
            wrong+=1
        else:
            print("You have not entered any number.\nSo ending the program")
            break

    wrong=0
    if choice==1:
        a = [Society() for i in range(1)]
        output_file=open ("Visitor.bin", "rb")
        zb=pickle . load (output_file)
        output_file . close ()
        zb.extend(a)
        for s in range(1):
            a[s].input()
            counter+=1
            print()
        output_file=open ("Visitor.bin", "wb")
        pickle . dump (zb, output_file)
        pickle . dump (counter, output_file)
        output_file . close ()

    elif choice==2:
        output_file=open ("Visitor.bin", "rb")
        z=pickle . load (output_file)
        output_file . close ()
        b=len(z)
        if b==0:
            print("No entry\n")
            pass
        else:
            print("Name:",z[b-1].name)
            print("Reason for the visit:",z[b-1].reason)
            print("Date of entry:",z[b-1].In_date)
            print("Time of entry:",z[b-1].In_time)
            print("Wing:",z[b-1].wing)
            print("Flat:",z[b-1].flat)
            print("Addrress:",z[b-1].addrress)
            print()
        
    elif choice==3:
        output_file=open ("Visitor.bin", "rb")
        z=pickle . load (output_file)
        output_file . close ()
        b=len(z)
        if b==0:
            print("No entry\n")
            pass
        else:
            for y in range(b):
                print("Name:",z[y].name)
                print("Reason for the visit:",z[y].reason)
                print("Date of entry:",z[y].In_date)
                print("Time of entry:",z[y].In_time)
                print("Wing:",z[y].wing)
                print("Flat:",z[y].flat)
                print("Addrress:",z[y].addrress)
                print()
        
    elif choice==4:
        output_file=open ("Visitor.bin", "rb")
        z=pickle . load (output_file)
        output_file . close ()
        b=len(z)
        if b==0:
            print("No entry\n")
            pass
        else:
            q=input("Enter Name: ").upper()
            print()
            for y in range(b):
                if q in z[y].name:
                    print("Name:",z[y].name)
                    print("Reason for the visit:",z[y].reason)
                    print("Date of entry:",z[y].In_date)
                    print("Time of entry:",z[y].In_time)
                    print("Wing:",z[y].wing)
                    print("Flat:",z[y].flat)
                    print("Addrress:",z[y].addrress)
                    print()
                
    elif choice==5:
        output_file=open ("Visitor.bin", "rb")
        z=pickle . load (output_file)
        output_file . close ()
        b=len(z)
        if b==0:
            print("No entry\n")
            pass
        else:
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
                    print("Date of entry:",z[y].In_date)
                    print("Time of entry:",z[y].In_time)
                    print("Wing:",z[y].wing)
                    print("Flat:",z[y].flat)
                    print("Addrress:",z[y].addrress)
                    print()

    elif choice==6:
        output_file=open ("Visitor.bin", "rb")
        z=pickle . load (output_file)
        output_file . close ()
        b=len(z)
        g=""
        if b==0:
            print("No entry\n")
            pass
        else:
            try:
                g= input("Enter flat: ")
            except:
                print("Enter number only")
            print()
            for y in range(b):
                if g in str(z[y].flat) :
                    print("Name:",z[y].name)
                    print("Reason for the visit:",z[y].reason)
                    print("Date of entry:",z[y].In_date)
                    print("Time of entry:",z[y].In_time)
                    print("Wing:",z[y].wing)
                    print("Flat:",z[y].flat)
                    print("Addrress:",z[y].addrress)
                    print()
                
    elif choice==7:
        output_file=open ("Visitor.bin", "rb")
        z=pickle . load (output_file)
        output_file . close ()
        b=len(z)
        if b==0:
            print("No entry\n")
            pass
        else:
            g=input("Enter Vistor's Addrress: ").upper()
            print()
            for y in range(b):
                if g in z[y].addrress:
                    print("Name:",z[y].name)
                    print("Reason for the visit:",z[y].reason)
                    print("Date of entry:",z[y].In_date)
                    print("Time of entry:",z[y].In_time)
                    print("Wing:",z[y].wing)
                    print("Flat:",z[y].flat)
                    print("Addrress:",z[y].addrress)
                    print()

    elif choice==8:
        output_file=open ("Visitor.bin", "rb")
        z=pickle . load (output_file)
        output_file . close ()
        b=len(z)
        if b==0:
            print("No entry\n")
            pass
        else:
            g=input("Enter Reason: ").upper()
            print()
            for y in range(b):
                if g in z[y].reason:
                    print("Name:",z[y].name)
                    print("Reason for the visit:",z[y].reason)
                    print("Date of entry:",z[y].In_date)
                    print("Time of entry:",z[y].In_time)
                    print("Wing:",z[y].wing)
                    print("Flat:",z[y].flat)
                    print("Addrress:",z[y].addrress)
                    print()

    elif choice==9:
        output_file=open ("Visitor.bin", "rb")
        z=pickle . load (output_file)
        output_file . close ()
        b=len(z)
        if b==0:
            print("No entry\n")
            pass
        else:
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
                    print("Date of entry:",z[y].In_date)
                    print("Time of entry:",z[y].In_time)
                    print("Wing:",z[y].wing)
                    print("Flat:",z[y].flat)
                    print("Addrress:",z[y].addrress)
                    print()
    
    elif choice==10:
        output_file=open ("Visitor.bin", "wb")
        pickle . dump ([], output_file)
        output_file . close ()
        print("Cleared\n")
                
    elif choice==0:
        print("Thank you for using")
        break

    else:
        wrong+=1
        if wrong<5:
            print("Enter number between 1 to 11")
            print()
            print()
        else:
            print("You have entered wrong number.\nSo ending the program")
            break
