x = 3
y = float(3)
print(x,y)

day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")

    x = "test"
print(f"hello {x}")
temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold')

number=input("pick a number")
if number == "8": 
    print ("even")
else:
    print ("odd")

#tip calculator

initialBill = input ("What is the bill total?")
tipValue = input ("how was the service?")
if "service" == "bad":
    print ('0%')
elif "service" == "okay":
    print ("15%")
elif "service" == "good":
    print ('20%')
elif "sevice" == "great":
    print ("25%")