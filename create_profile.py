my_file = open("credentials.txt", "w") # Open .txt file with permission to write to it

enter_email = input("Enter the email you want to use:") # Have the user enter their email address for profile
enter_password = input("Enter the password you want to use:") # Have the user enter a password for their profile
confirm_password = input("Confirm your password:") # Have the user confirm the password they are using

my_file.write(enter_email + "\n") # Write the email entered to the .txt file
if(enter_password == confirm_password): # Check if the passwords matched each other, if they do write them to the .txt file
    my_file.write(enter_password)

if(my_file != my_file.closed): # Check if the file is closed, if not close the file
    my_file.close() 