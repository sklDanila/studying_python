try:
    number = int(input("Enter number: "))
    print("Entered number:", number)
except:
    print("Error")
finally:
    print("Block try good end")
print("Close program")


try:
    number = int(input("Enter number: "))
    print("Entered number:", number)
except ValueError as e:  # information about exception
    print("Information about exception", e)
print("Close program")
