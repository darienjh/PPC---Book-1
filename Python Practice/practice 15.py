#darien hayes
#10/1/2014
#pracitce 15

count = 1
password = "changeme"
guess = input("Enter Password: ")
while guess != password:
    count+=1
    guess = input("Enter Password: ")
if password == "changeme":
    print("Accepted")
else:
    print("Denied")
print("Attempts tried:",count)

#yes
#no
#no
#figuring how to make it count
