import math
from datetime import datetime 

today = datetime.now()

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

#the formula of the volume of a tire 
v = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10 ** 10

print(f"\nThe approximate volume is {v:.2f} liters.\n")

#function to ask if the person want to buy and record it
def want_to():
    want_to_buy = input("Do you want to buy that tire?"
        "\nEnter 'y' for yes and 'n' for no: ").lower()
    if want_to_buy  == "y":
        phone_number = input("\nPlease Enter your phone number: ")
        print("Order made", file=volume_file)
        print(f"***Phone Number: {phone_number}\n", file=volume_file)
        print("Thank you")
    elif want_to_buy == "n":
        print("Order rejected", file=volume_file)
        print("No worries")
        print("Thank you")
        print(file=volume_file)
    else:
        print("invalid input")
        print("error", file=volume_file)

measurement = f"{width}/{aspect_ratio}R{diameter}" #convert the measurement of the tire from int to string

#opening the file;
#the "at" attribute allow to append in the file
with open("volumes.txt", "at") as volume_file:
    print(f"{today:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {v:.2f}",file=volume_file) #print statement with the comma follow by the file name in allow to print in the file.
    if measurement == "205/60R15":
        print(f"A '{measurement}' tire price is: R2359")
        print(f"A '{measurement}' tire price is: R2359", file=volume_file)
        want_to()
    elif measurement == "155/70R13":
        print(f"A '{measurement}' tire price is : R799")
        print(f"A '{measurement}' tire price is : R799", file=volume_file)
        want_to()
    elif measurement == "165/65R14":
        print(f"A '{measurement}' tire price is: R999")
        print(f"A '{measurement}' tire price is: R999", file=volume_file)
        want_to()
    elif measurement == "155/80R12":
        print(f"A '{measurement}' tire price is: R1099")
        print(f"A '{measurement}' tire price is: R1099", file=volume_file)
        want_to()
    else:
        print("Sorry we do not have that size in stock")
        print("order not in stock\n", file=volume_file)
        print()