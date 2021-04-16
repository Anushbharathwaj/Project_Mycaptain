## the School Administration Program from my captain 

import csv
condtion = True
student_num = 1
def write_csv(info):
    with open("school_admintration.csv","a")as file:
        writer = csv.writer(file)
        if file.tell()==0:
            writer.writerow(["Name", "Age", "Phone Number", "Email"])
        writer.writerow(info)
while(condtion):

    student_info = input("Enter The Student Information #{0} in the format of (Name,Age,Phone Number, Email): ".format(student_num))
    print("Entered Information :" + student_info)

    student_info_lst = student_info.split(" ")
    print("Entered The Split UP Information: "+str(student_info_lst))

    print("\nThe Entered Information -\n Name -{0}\n Age -{1}\n Phone Number -{2}\n Email -{3}"
          .format(student_info_lst[0],student_info_lst[1],student_info_lst[2],student_info_lst[3]))
    
    choice_check = input("Is Entered Information Is Correct or Wrong (yes/no): ")
    if choice_check.lower() =="y":
        write_csv(student_info_lst)

        condtion_check = input("Enter Y/N for Entering Another student Information: ")
        if condtion_check.upper() == "Y":
            condtion = True
            student_num += 1
        else :
            condtion = False
    elif choice_check.lower() == "n":
        print("\nPlease reenter the value - ")
        
#### Desired output in school_adminstration.csv

## Name,Age,Phone Number,Email
## M1King,17,7219879879,hkh@gmail.com
## Y3Queen,16,9128691891,jhai@mail.com,
## k8Super,19,7561168781,anj@hot.com
## T7Hailwoon,29,01979879281,husg@lia.com

