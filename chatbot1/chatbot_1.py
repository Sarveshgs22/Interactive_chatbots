import pickle

class people:

    def __str__(self):
        return self.name

    def get_details(self):
        # getting the name
        name_input = input("Hi , Enter your Name : ")
        name = ""
        for i in name_input.lower().split():
            if i not in ["my", "name", "is", "i", "am", 'the']:
                name = name + i + " "
        self.name = name

        # getting the mail id
        print("Hi {}, What is your Mail Id : ".format(name), end='')
        email_input = input()
        email = ""
        flag = 0
        if '.' in email_input and '@' in email_input:
            for i in email_input.split():
                if i not in ['My', 'Email', 'email', 'the', 'is', 'Is', 'ID', 'id', 'Email Id', 'EMAIl']:
                    email = email + i + " "
        else:
            print("please enter a Valid Email {}".format(name))
            flag = 1

        if flag == 0:
            print("Nice, so your email is : {}".format(email))
            self.email=email
        else:
            self.email = email

        # getting the mobile no
        mobile_input = input("your mobile number, please : ")
        if len(mobile_input) == 10 and mobile_input.isdigit():
            mobile = mobile_input
            print("Thanks for the Input")
        else:
            print("Please Enter a Valid Mobile Number")
        self.phone_no=mobile


person = people()
person.get_details()
import pandas as pd
df = pd.DataFrame({'Name':[person.name],'Email':[person.email],'Phone_no':[person.phone_no]})
df.to_csv('details.csv')
print(df)

