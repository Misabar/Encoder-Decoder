from replit import clear
from time import sleep
import getpass
import smtplib
  
clear()

def gmailnote():
    print("NOTE: To send an email using gmail, you must first allow unsecure apps to send emails in your account settings(ONLY FOR GMAIL) at this url \"https://myaccount.google.com/lesssecureapps\"")

def note():
    print("NOTE: To send an email you must first type your message in the Message.txt file attached\nYou must also type the email adresses of the people you intend to send the message to in the Contacts.txt file attached\n")

def GetUsernames():
    with open("Contacts.txt", "r") as f:
        string = f.readlines()
    return string

def GetMessage():
    with open("Coded.txt", "r") as f:
        string = f.read()
    return string


def getridofns(lists):
    j=(len(lists))-1
    for i in range(j):
        lists[i]=lists[i].rstrip('\n')
    return lists

def CheckRecipient():
    check = int(input("\nDo you wish to\n1.Enter the recipient's email(only one)\n2.Take the recipient's email from file(multiple)\n"))
    clear()
    if check == 1:
        l=[]
        recipient = str(input("Enter recipient's email address: "))
        l.append(recipient)
        return l
    elif check == 2:
        return getridofns(GetUsernames())
        print("Contacts taken from file")
    else:
        print("Invalid!")

def SendEmail():
    count = 0
    choice = int(input("Do you want to send the email from a\n1.Gmail account\n2.Outlook/Hotmail account(recommended)\n"))   
    clear()
    if choice == 1:
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        emailtype = "gmail"   
    elif choice == 2:
        mail = smtplib.SMTP("smtp-mail.outlook.com", 587)
        emailtype = "outlook"
    else:
        print('Invalid!')
    mail.ehlo()
    mail.starttls()
    while True:
        try: 
            if emailtype == "gmail":
                gmailnote()
                username= str(input("Enter gmail username: "))
            elif emailtype == "outlook":
                username= str(input("Enter outlook/hotmail username: "))
            password= str(getpass.getpass("Enter Password: "))
            mail.login(username,password )
            clear()
            print("You have successfully logged in.")
        except Exception:
            clear()
            print('Incorrect Username or Password')
            continue
        else:
            break
    
   
    contacts = CheckRecipient()
    message = GetMessage()
   
    for person in contacts:
        count+=1
        mail.sendmail(username, person , message)
    mail.close()
    print("Your "+str(count) +" mail(s) have been sent\n")

def GetDataForCoding():
    string = str(input("Type a sentence to encode: "))
    clear()
    return string

def GetDataForDecoding():
    with open("ToDecode.txt", "r") as f:
        string = f.read()
    return string

def GetDataForDecoding_2():
    with open("Message.txt", "r") as f:
        string = f.read()
    return string


def listtostr(newstring):
    f = ""
    for letter in newstring:
        f+=letter
    return f

def checkspaceforcoding(newstring):
    n = len(newstring)
    if newstring[n-1] == ' ':
        newstring[n-1]='*'
    return newstring

def checkspacefordecoding(string):
    liststring = []
    for letter in string:
        liststring.append(letter)
    n = len(liststring)
    if liststring[n-1] == '*':
        liststring[n-1]=' '
    string = listtostr(liststring)
    return string

def code_1(string):
    """
    for 1_2 type coding
    for 1_ln type decoding
    """
    newstring = []
    n = len(string)
    if n%2 == 0:
        j=0
        h=n-1
        i=0
        while i < n:
            newstring.append(string[j])
            i+=1
            j+=1
            newstring.append(string[h])
            i+=1
            h-=1
    elif n%2 == 1:
        j=0
        h=n-1
        i=0
        while i<n:
            newstring.append(string[j])
            if i == n-1:
                break
            i+=1
            j+=1
            newstring.append(string[h])
            i+=1
            h-=1
    return newstring

def code_2(string):
    """
    for 1_ln type coding
    for 1_2 type decoding
    """
    newstring = []
    n = len(string)
    if n%2 == 0:
        j = 0
        for i in range(n):
            newstring.append(string[j])
            if j%2 == 0:
                if j == n-2:
                    j+=1
                else:
                    j+=2
            else:
                j-=2
    elif n%2 == 1:
        j=0
        for i in range(n):
            newstring.append(string[j])
            if j%2 == 0:
                if j == n-1:
                    j-=1
                else:
                    j+=2
            else:
                j-=2
    return newstring
    
def printcoded(string,code,send):
    print("The encoded sentence is:")
    newstring = checkspaceforcoding(code(string))
    newstring= listtostr(newstring)
    print(newstring)
    with open("Coded.txt", "w") as f:
        f.write(newstring)
        print("\nCode saved to file\n")
    with open("ToDecode.txt", "w") as f:
        f.write(newstring)
    if send == 1:
        print("please wait...")
        sleep(5)
        clear()
        SendEmail()

def PrintDecoded(string,code):
    print("Code has been copied from file")
    print("The decoded sentence is:")
    string = checkspacefordecoding(string)
    print(listtostr(code(string))) 
    print("\n")

def CoderSender():
    note()
    i = int(input("Which encoder would you like to use\n1. 1_2 type encoder\n2. 1_la type encoder\n"))
    clear()
    if i == 1:
        print("Message taken from file")
        printcoded(GetDataForDecoding_2(), code_1,1)
    elif i == 2:
        print("Message taken from file")
        printcoded(GetDataForDecoding_2(), code_2,1)
    else:
        print("Invalid!")

def Coder():
    i = int(input("Which encoder would you like to use\n1. 1_2 type encoder\n2. 1_la type encoder\n"))
    clear()
    if i == 1:
        printcoded(GetDataForCoding(), code_1,0)
    elif i == 2:
        printcoded(GetDataForCoding(), code_2,0)
    else:
        print("Invalid!")

def Decoder():
    i = int(input("Which Decoder would you like to use\n1. 1_2 type decoder\n2. 1_ln type decoder\n"))
    clear()
    if i == 1:
        PrintDecoded(GetDataForDecoding(), code_2) 
    elif i == 2:
        PrintDecoded(GetDataForDecoding(), code_1)
    else:
        print("Invalid")
 
i=int(input("Do you want to\n1.Encode a sentence\n2.Decode a sentence\n3.Encode and send as email\n4.Exit\n"))    
clear()
while i :

    if i == 1:
       clear()
       Coder()
    elif i == 2:
       clear()
       Decoder()
    elif i == 3:
        clear()
        CoderSender()
    elif i == 4:
        clear()
        print("Thank you for using this program")
        sleep(2)
        break
    else:
       clear()
       print("Invalid!")
    i=int(input("Do you want to\n1.Encode a sentence\n2.Decode a sentence\n3.Encode and send as email\n4.Exit\n"))
