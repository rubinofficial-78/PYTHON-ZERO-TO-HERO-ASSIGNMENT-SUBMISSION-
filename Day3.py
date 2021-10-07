#Python LetsUpgrade Assignment
#Getting the altitude from the User
altitude = int(input("Enter the altitude : "))
if altitude == 1000 :
    print("Safe to Land");
elif ((altitude < 1000) or (altitude < 5000)) :
    print("Bring down to 1000")
else :
    print("Turn Around")
