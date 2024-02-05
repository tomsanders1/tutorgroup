import csv



def LoginPage():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == "admin" and password == "SecurePass":
            print("Login successful")
            return True
        else:
            print("Incorrect username or password. Please try again.")

#Student / Teacher login page

def EnterDetails():
    with open("Students.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        print("\nEnter student details:")
        UniqueID = str(input("Enter Student ID: "))
        Surname = str(input("Enter Surname: "))
        Forename = str(input("Enter Forename; "))
        DateOfBirth = str(input("Enter Date Of Birth: "))
        HomeAddress = str(input("Enter Home Address: "))
        PhoneNum = str(input("Enter Phone Number: "))
        Gender = str(input("Enter Gender: "))
        if Gender != 'male' or 'female':
            print('Student gender defined incorrectly')
            EnterDetails()
        Tutor = str(input("Enter Tutor Group: "))

        writer.writerow([UniqueID, Surname, Forename, DateOfBirth, HomeAddress, PhoneNum, Gender, Tutor])
        print("Student Details Added")
#gathers students details in the systems abd checks if they match before deciding if the user is authorised or not
def ViewDetails():
    try:
        with open("Students.csv", mode='r') as file:
            reader = csv.reader(file)
            print("\nStudent details:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No student details found.")

def Menu():
    if LoginPage():
        while True:   
            print("Menu:")
            print("1) Enter Student Details.")
            print("2) View Student Details.")
            print("3) Log Out.")
            Option = input("Select Option: ")
            if Option == "1":
                EnterDetails()
            elif Option == "2":
                ViewDetails()
            elif Option == "3":
                print("Logged out.")
                break
            else:
                print("Invalid Option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    Menu()
