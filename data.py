""" x = 3
y = float(3)
print(x,y)

day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")

input ("What is the temperature?")
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold')

number=input("pick a number")
if int(number) % 2 == 0: 
    print ("even")
else:
    print ("odd") """

#tip calculator
initialBill = input ("What is the bill total?")
tipValue = input ("how was the service?")
initialBill = 1
if tipValue == "bad":
    input('0%') 
    print(1+ (0.01 * 0))
elif tipValue == "okay":
    input("15%") 
    print(1 + (0.01 * 15))
elif tipValue == "good":
    input('20%') 
    print(1 + (0.01 * 20))
elif tipValue == "great":
    input("25%") 
    print(1 + (0.01 * 25))
else:
    print("choose another option")