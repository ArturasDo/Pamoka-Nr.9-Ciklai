# Converter: kilometers into miles
print(" ")
print ("It's a converter, that converts kilometers into miles")

while True:
    print(" ")
    km = input("Please enter number of kilometers: ")
    km = float(km.replace(",", "."))
    miles = km * 0.621371
    print("Result: " + str(km) + " kilometers = " + str(miles) + " miles.")
#ka reiskia pavyzdyje sekantis print su{} skliausteliais:
    print("{0} kilometers is {1} miles.".format(km, miles))
    z = input("Would you like to continue (Y/N)?")
    f = z.lower()
    if f != "y":
        print("End of job.")
        break
