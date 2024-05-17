# str = string 'text'
# int = integer '1 2  3  4 5' number, 1.2 or 5.8, entero
# float4 for virgule number
name = input("What is your name ? ") #Name
age = int(input("What is your age ? "))

if age < 18:
    print("You cannot drink you are too young !")
else: 
    print(f"{name} can buy alcohol") # you open in the print something writing inside