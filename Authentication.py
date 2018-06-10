
# coding: utf-8

# In[3]:


print("-----------------------------------")
print("rock, paper, scissors account setup")
print("-----------------------------------")
while True:
    username = input("Pick a username:  ")
    password = input("Pick a password:  ")
    password_confirm = input("Please confirm your password:  ")
    
    if password != password_confirm:
        print("Your passwords don't match. Please Try again")
        
    if password == password_confirm:
        print("Your account has been set up.")
        text_file = open("accounts.csv", "a")
        text_file.write(",")
        text_file.write(username)
        text_file.write(",")
        text_file.write(password)
        text_file.close()
        break

