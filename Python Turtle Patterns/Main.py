import subprocess

while True:
    
    print("Which one do you want to exceute: ")
    print("0]  Exit")
    print("1]  Pattern 1")
    print("2]  Pattern 2")
    print("3]  Pattern 3")
    print("4]  Pattern 4")
    print("5]  Pattern 5")
    print("6]  Pattern 6")
              
    choice=int(input("Enter your choice: "))

    if choice==0:
        print("Thank you for Using")
        raise SystemExit
    elif choice in range(1,7):
        subprocess.Popen(['python', f'Pattern {choice}.py'])
        print()
    else:
        print("Enter Valid Number")
