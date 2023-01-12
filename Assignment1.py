#Program 1.1: Remove atleast 2 chars from input string and print it reverse
input_string = input("Input:")
deleted_string = input_string[0:-2]
print("deleted_string:",deleted_string)
reversed_string = deleted_string [::-1]
print("output:", reversed_string)



#Program 1.2: Perform any four Arthmetic operations
ip1 = int(input("Input 1:"))
ip2 = int(input("Input 2:"))
print ("Sum: ", ip1+ip2)
print ("Sub:", ip1-ip2)
print ("Mul:", ip1*ip2)
print ("Division:", ip1%ip2)



#Program 2: Replace python word with pythons in an input string
input_string = input("Input:")
print ("Input:", input_string)
output_string = input_string.replace("python", "pythons")
print(f"Output:{output_string}")



#Program 3: Grading based on score
ip=int(input('Marks:'))
if(ip>=90 and ip<=100):
    print("Grade: A")
elif(ip>=80 and ip<=89):
    print("Grade : B")
elif(ip>=70 and ip<=79):
    print("Grade: C")
elif(ip>=60 and ip<=69):
    print("Grade: D")
elif(ip<=59):
    print("Grade: F")

