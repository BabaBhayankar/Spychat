import spy_detail        #import default spy detail
import datetime          #import datetime module
from steganography.steganography import Steganography #import steganography module for secret message

current_status_message=None     #create a variable
old_status=['Anmol']            #create list for store all old status
friends_name=[]                 #create list for store all the friends name
friends_age=[]                  #create list for store the age of all the friends
friends_salutation=[]           #create list for store the salutation of all the friends
friends_rating=[]               #create list for store the ratings of all the friends name
chats={}                         #create dictonary for secret chats of all friends
normal_chats={}                 #create dictonary for chats of all friends
flag=0

def get_now():                                    #function for get the current date and time
    return(datetime.datetime.now())

def add_status(current_status_message):          #function for add the status of the user
    if current_status_message!=None:              #if control statement for checking weather their is already
        print("Your current status is "+current_status_message)
    else:
        print("you don't have any status message")
    print("Do you want to select from older status messages(y/n)?")
    choice=raw_input()
    if choice=='y':
        i=1
        for message in old_status:           #printing all the old messages
            print(str(i)+") "+str(message))
            i=i+1
        message_select=int(raw_input("Select any one ststus="))
        if len(old_status)>=message_select:        #check for correct choice
            updated_status=old_status[message_select-1]
    else:
        new_status=raw_input("Write your new status=")
        if len(new_status)>0:                        #check for correct status
            updated_status=new_status
            old_status.append(new_status)
    return(updated_status)                    #retrun updated status

def add_friend():                                    #function for add a new friend
    friend_name=raw_input("Enter the name of your friend=")
    friend_salutation=raw_input("What should i call your friend(Mr. or Ms.)?=")
    friend_age=int(raw_input("enter the age of your friend="))
    friend_rating=float(raw_input("enter the rating of your friend="))
    if len(friend_name)>0 and friend_age>12 and friend_rating>=spy_rating:
        friends_name.append(friend_name)
        friends_age.append(friend_age)
        friends_salutation.append(friend_salutation)
        friends_rating.append(friend_rating)
    else:
        print("you don't give proper information of your friend")
    return(len(friends_name))                         #return total friends

def select_friend():                                        #function for selecting a friend
    i=1
    for friend in friends_name:
        print(str(i)+") "+str(friend))
        i=i+1
    friend_select=int(raw_input("Select any one friend"))
    return(friend_select-1)                               #return the position of selected friend

def send_message():                                          #function for sending the message
    flag=0
    f=0
    friend_choice=select_friend()
    for friend_choice_key in chats:
        if friend_choice_key==friend_choice:
            flag=1
    for friend_choice_key in normal_chats:
        if friend_choice_key == friend_choice:
            f = 1
    if flag!=1:
        chats[friend_choice] = []
    if f!=1:
        normal_chats[friend_choice]=[]
    print("How you want to send the message:\n1-By image\n2-Normal text");       #menu for secret messsage or normal message
    if int(raw_input())==1:
        original_image=raw_input("enter the path of the image=")
        output_path=raw_input("enter the path of the output file=")
        text=raw_input("what you want to say=")
        Steganography.encode(original_image,output_path,text)                   #encode function of steganography for encode the image
        image_message={
            'image':output_path,
            'time':get_now(),
            'send_by_me':'true'
        }
        chats[friend_choice].append(image_message)                #append the chat in the list of perticular friend
    else:
        text=raw_input("write your meassage");
        text_message = {
            'message':text,
            'time': get_now(),
            'send_by_me': 'true'
        }
        normal_chats[friend_choice].append(text_message)           #append the chat in the list of perticular friend

def read_meassage():
    friend_choice = select_friend()
    print("what you want to read\n1-secreat message\n2-normal message")       #menu for reading the message normal or secret
    if int(raw_input())==1:
        output_path=raw_input("enter the output path of the file")
        secret_text=Steganography.decode(output_path)                         #decode function of steganography for decoding the image and get the message
        if(secret_text=='SOS'):
            print("send out succour");
        else:
            print(secret_text)
    else:
        print(normal_chats[friend_choice]);                             #print the message

def read():                                                                 #read function for raeding all the conversation of a perticular friend
    friend_choice = select_friend()
    print(chats[friend_choice]);                                                  #printing the chats
    print(normal_chats[friend_choice]);

print("Select your choice:\n1-Continue with default user\n2-Create custome user")     #menu for default or custome user
choice=int(raw_input())
if choice==1:
    spy_name=spy_detail.spy_name
    spy_salutation=spy_detail.spy_salutation
    spy_age=spy_detail.spy_age
    spy_rating=spy_detail.spy_rating
    spy_status=spy_detail.spy_status
elif choice==2:                                                          #for entering all the detail of the user
    spy_name = raw_input("First enter your name= ")
    if len(spy_name) > 0:
        spy_salutation = raw_input("what should i call u(Mr. or Mrs.)? ")
        spy_age = int(raw_input("enter your age= "))
        if spy_age > 12 and spy_age < 50:
            spy_rating = float(raw_input("enter your rating= "))
            if spy_rating > 4.5:
                print("great ace")
            elif spy_rating > 3.5 and spy_rating <= 4.5:
                print("you are one of the good ones")
            elif spy_rating >= 2.5 and spy_rating <= 3.5:
                print("you can always do better")
            else:
                print("we can use somebody better")
                exit(0);
        else:
            print("sorry, you are not of the correct age")
            exit(0);
    else:
        print("your name is incorrect")
        exit(0);
else:
    print("you enter wrong choice please try again")
    exit(0);
print("\nWelcome "+spy_salutation+" "+spy_name+" in spychat. Your age is "+str(spy_age)+" and your rating is "+str(spy_rating))
con=1
while con==1:
    print("\nSelect your choice:\n1) Add a status update\n2) Add a friend\n3) Send a message\n4) Read a message\n5) Read chats from a user\n6) Close application")
                                                                                                                         #menu for giving the choices to the user
    choice=int(raw_input())
    if choice==1:                                                                 #for add a status
        current_status_message=add_status(current_status_message)                           #invoke add_status function
        print("Your updated status is "+current_status_message)                     #print updated status message
        print("Your updated status is "+current_status_message)                     #print updated status message
    elif choice==2:
        total_spy_friend=add_friend()                                                 #invoke add_friend function for adding a friend
        print(spy_name+" your total friends are "+str(total_spy_friend))                      #print total frinds
    elif choice==3:                                                                  #for send a message
        send_message()                #invoke send_message function
    elif choice==4:
        read_meassage()               #invoke read_message function
    elif choice==5:
        read()                       #invoke read function
    elif choice==6:
        exit(0);
    else:
        print("you enter wrong choice ");    #for wrong choice
    print("\nDo you want to continue with Chat press 1")                #giving the program continuation
    con=int(raw_input())