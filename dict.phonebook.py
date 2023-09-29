# import pprint
# import pprint
import pprint


def createbook():
    phone = {}
    while True:
        name = input("Enter the name of the person:")
        try:
            num = int(input("Enter the number:"))
        except ValueError:
            print("invalid Input please try again")
            continue
        phone[name] = num
        return "number successfully stored"
    return phone


def addnewperson(phone):
    while True:
        name = str(input("Enter the name of the person>>"))
        if name in phone.keys():
            print("Name already exist")
        else:
            try:
                newpnum: int = int(input("Enter the number:"))
            except ValueError:
                print("invalid Input please try again")
                continue
            phone.update(name, newpnum)
            another = input("Do you want to add another person(yes or no)?")
            if another == "no":
                break


def checkperson(phone):
    pname = input("Enter the name of the person you want to find>>")
    if pname in phone.keys():
        return phone[pname]
    else:
        return "name not found"


def display(phone):
    """for k in phone.keys():
        print(f"{k}:{phone[k]}")
"""
    pprint.pprint(phone)

# what is left is file handling(with texts) and adding some gui will be using pyqt6


if __name__ == '__main__':
    print("Welcome to this new phonebook")

    while True:
        choice = int(input("would you like to\n1.Create \n2.Add\n3.Search\n4.Display\n"))
        phonebook = {}
        if choice == 1:
            phonebook = createbook()
        elif choice == 2:
            addnewperson(phonebook)
        elif choice == 3:
            checkperson(phonebook)
        elif choice == 4:
            display(phonebook)
        else:
            print("Invalid entry\nThank you for your time\nGoodbye")
