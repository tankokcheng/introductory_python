name = input("Enter patient's name: ")

temperature = input("Enter patient's temperature: ")

diff_from_369 = float(temperature) - 36.9

print(name +"'s temperature is " + str(diff_from_369) + " degree from 36.9 degree celsius")

#Using String formatting:
print("{}'s temperature is {:.2f} degree from 36.9 degree celsius".format(name, diff_from_369))