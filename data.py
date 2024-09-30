""" x = 3
y = float(3)
print(x,y)

```python
day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")

temp = 75
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
""" x_initialBill = int(input("What is the bill total?"))
x_tipValue = (input("how was the service?"))
if x_tipValue == "Bad": 
    print("0") 
    print((int(x_initialBill)) * (1 + (0.01 * 0)))
elif x_tipValue == "Okay":
    print("15") 
    print((int(x_initialBill)) * (1 + (0.01 * 15)))
    x = round(12.9999999999999)
elif x_tipValue == "Good":
    print("20") 
    print((int(x_initialBill)) * (1 + (0.01 * 20)))
elif x_tipValue == "Great":
    print("25") 
    print((int(x_initialBill)) * (1 + (0.01 * 25)))
else:
    print("choose another option") """

""" x_integer = input ("pick a number")
for x in range (int(x_integer)):
     if (x) > 0 and (int(x_integer)) % (x) == 0: 
        print((x)) """

#GCF
number_1 = int(input("pick a number"))
number_2 = int(input("pick another number"))
gcf = []
for x in range(int((number_1 + 1))):
    if x in range(int((number_2 + 1))) and (x) > 0:
        if number_1 % x == 0 and number_2 % x == 0:
            gcf.append(x)

print(max(gcf))



 



 