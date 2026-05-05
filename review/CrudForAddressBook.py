# A simple crud based console app for the address book
# Ops : delete , add , update , create
### Dated : May 5th , 2026
contactsbook = dict()

ID = 0
def GetId() :
   # Function to create the global id.
   global ID
   ID += 1
   return ID

def validcontact(contact):
   # This is to check if the number is a valid contact of 10 digits length
   if (type(contact) != int):
      return False
   elif (len(str(contact)) != 10):
      return False
   
   return True
   


def createcontact():
    # Function to save the contact
    name = input("Enter name of the person to be saved ")
    contact = int(input("Enter the number of the contact "))
    if (validcontact(contact)) :
        id = GetId()
        contactsbook[id] = [name , contact]
    else :
       print("Please enter a valid contact number. So redo the creation of contact.")
       createcontact()

def readcontacts():
   
   # Function to show all contacts
   if not contactsbook:
      print(" No contacts found ")
      return

   for id, details in contactsbook.items():
      print("ID : ", id, "Name : ", details[0], "Contact : ", details[1])

def fetchcontact():
    # This is the function to return the contact that was searched . It returns the first matched contact on the basis of the name.
    name = input("Please enter the name of the contact to be found : ")
    found = 0 # found flag by default 0 .as not found
    for id , details in contactsbook.items():
        if (details[0] == name) :
            print(f"This is the contact that was found with the entered name :\nID : {id} | Name : {details[0]} | Contact Number : {details[1]}")
            found = 1
        else :
            found = 0
    if (found == 0):
       print ("Not found.")
    
    
      
    
      

def updatecontact():
   # Function to update an existing contact
   id = int(input("Enter contact id to update "))
   if id in contactsbook:
      name = input("Enter new name ")
      contact = int(input("Enter new number "))
      contactsbook[id] = [name, contact]
      print("Contact updated ")
   else:
      print("Contact not found")

def deletecontact():
   # Function to delete a contact
   id = int(input("Enter contact id to delete "))
   if id in contactsbook:
      del contactsbook[id]
      print("Contact deleted")
   else:
      print("Contact not found")

def menu():
   while True:
      print("1. Add Contact")
      print("2. View Contacts")
      print("3. Update Contact")
      print("4. Delete Contact")
      print("5. Fetch the saved contact by name")
      print("0. Exit")

      choice = input("Enter your choice: ")

      if choice == "1":
         createcontact()
      elif choice == "2":
         readcontacts()
      elif choice == "3":
         updatecontact()
      elif choice == "4":
         deletecontact()
      elif choice == "5":
         fetchcontact()
      elif choice == "0":
         break
      else:
         print("Invalid choice")

menu()


