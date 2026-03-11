import subprocess
import os
a=1
while a<=5:
    a+=1
    print("Which one do you want to exceute: ")
    print("0]  Exit")
    print("1]  Project In comand line Form with data storage")
    print("2]  Project In GUI Form with data storage")
              
    choice=int(input("Enter your choice: "))
    print()

    if choice==0:
        print("Thank you for Using")
        raise SystemExit
    elif choice==1:
        os.system('1-1.py')
        print()
    elif choice==2:
        subprocess.Popen(['python', '2-2.py'])
        print()
