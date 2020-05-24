import csv
def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact Number","Email-Id"])
        
        writer.writerow(info_list)
if __name__=='__main__':
    check=True
    id=1
    while(check):
        student_info=input("Enter student information for student #{} in the following format(Name Age Contact_Number Email-Id".format(id))
        student_info_list=student_info.split(' ')
        print("The Entered info is :\nName:{}\nAge:{}\nContact Number:{}\nEmail-ID:{}"
              .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))              
        result=input("Is the entered info correct ?(yes/no):")
        if result=="yes":
            write_into_csv(student_info_list)
            next_student=input("Enter (yes/no) if you want to enter info for another student:")
            if next_student=="yes":
                check=True
                id+=1
            elif next_student=="no":
                check=False
        elif result=="no":
            print("Please re-enter the values")
            
