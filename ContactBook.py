import time
print("This is a contact book programme made in python.")
time.sleep(1)
print("Pay me $1 to append more than 3 contacts")
time.sleep(1)
names = []
phoneNumbers = []
print("Enter the number of contacts you need to save")

for i in range(3):
     name_of_contact = input("Name: ")
     phone_number_of_contact = input("Phonenumber: ")
     names.append(name_of_contact)
     phoneNumbers.append(phone_number_of_contact)

print("Do you wanna see you contacts?")
y_n = input("(y/n): ")
if y_n == 'y':
     print("Okay here are the contacts you had saved: ")
     print(names)
     print(phoneNumbers)
else:
     print("Okay")