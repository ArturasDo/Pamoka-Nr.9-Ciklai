print(" ")
print("It's a FizzBuzz Homework: you should enter one figure between 1 and 100")
print("and program will print the numbers from '1' in sequence under the rule:")
print("if number is devisable with 3, it will prints 'fizz' instead of number.")
print("If the number is divisable with 5, it prints 'buzz'. If the number is")
print("devisable with both 3 and 5, it prints 'fizzbuzz'.")
print("If you want to finish, enter 'cancel'")

while True:
    print(" ")
    x = input("Enter the number between 1 and 100: ")
    if x == "cancel":
        print("Thank you for your time.")
        exit()
    elif int(x) < 1:
        print("Your number is less than 1")
        continue
    elif int(x) > 100:
        print("Your number is bigger than 100")
        continue

    i = int(1)
    y = int(x)
    while i <= y:
        if (i % 3) == 0 and (i % 5) == 0:   #dalybos likutis = 0
            print("fizzbuzz")
            i = i + 1
            continue
        elif (i % 5) == 0:
            print("buzz")
            i = i + 1
            continue
        elif (i % 3) == 0:
            print("fizz")
            i = i + 1
            continue
        else:
        print(i)
        i = i + 1

#klausimai: kodel pavyzdyje kintamoji num neauginama?
#Pavyzdys:
'''print("Welcome to the fizzbuzz game!")

end = input("Please enter a number between 1 and 100: ")
end = int(end)  # convert string into number

for num in range(1, end+1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)'''