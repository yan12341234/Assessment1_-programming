#Task 2
import math

next_vehicle = "Y" # Yes= Y

while next_vehicle == "Y":

    # user input
    user_id = input("User ID: ")
    vehicle_no = input("Vehicle Number: ")
    print("\nMember Type: ")
    print("1. Staff")
    print("2. Student")
    print("3. Public")

    # member type
    member_choice = input("Enter choice(1/2/3): ")

    while member_choice not in ["1", "2", "3"]:
        print("Invalid choice. Please try again.")
        member_choice = input("Enter choice(1/2/3): ")

    if member_choice == "1":
        member_type = "Staff"
    elif member_choice == "2":
        member_type = "Student"
    else:
        member_type = "Public"

    # charger type: AC or DC
    print("\nCharger Type:")
    print("1. AC Fast Charger (7kW)")
    print("2. DC Ultra-Fast Charger (50kW)")

    charger_choice = input("Enter choice(1/2): ")

    while charger_choice not in ["1", "2"]:
        print("Invalid choice. Please try again.")
        charger_choice = input("Enter choice(1/2): ")

    if charger_choice == "1":
        charger_type = "AC"
    else:
        charger_type = "DC"


    hours_charged = float(input("\nHours Charged: "))
    while hours_charged <= 0:
        print("Invalid input. Please try again.")
        hours_charged = float(input("\nHours Charged: "))


    charging_time = input("Charging Time (HH:MM, 24-hours format): ")
    while len(charging_time) != 5 or charging_time[2] != ":":
        print("Invalid input. Please enter time in HH:MM format.")
        charging_time = input("Charging Time (HH:MM, 24-hours format): ")

    #--------------------------------
    # SPECIAL CONDITIONS
    #--------------------------------
    # Y = Yes; N = No
    print("\nSpecial Conditions:")
    first_time_user = input("First-time User (Y/N): ").upper()
    while first_time_user not in ["Y", "N"]:
        print("Invalid Input. Please enter Y or N.")
        first_time_user = input("First-time User (Y/N): ").upper()

    green_ecopass = input("Green Eco-Pass Holder (Y/N): ").upper()
    while green_ecopass not in ["Y", "N"]:
        print("Invalid Input. Please enter Y or N.")
        green_ecopass = input("Green Eco-Pass Holder (Y/N): ").upper()

    idle_parking = input("Idle Parking (Y/N): ").upper()
    while idle_parking not in ["Y", "N"]:
        print("Invalid Input. Please enter Y or N.")
        idle_parking = input("Idle Parking (Y/N): ").upper()

    lost_rfid = input("Lost RFID (Y/N): ").upper()
    while lost_rfid not in ["Y", "N"]:
        print("Invalid Input. Please enter Y or N.")
        lost_rfid = input("Lost RFID (Y/N): ").upper()

    # initial fees
    discount_fee = 0
    eco_discount = 0
    surcharge_fee = 0
    replacement_fee = 0

    #---------------------------------
    # CHARGING FEE CALCULATION
    #---------------------------------
    # calculate duration in hours
    duration_hours = math.ceil(hours_charged)

    # AC charging rate
    if charger_type == "AC":
        if duration_hours <= 2:
            gross_fee = duration_hours * 4

        elif duration_hours <= 4:
            gross_fee = duration_hours * 6

        elif duration_hours <= 6:
            gross_fee = duration_hours * 8

        else:
            gross_fee = duration_hours * 12

            if gross_fee > 80:  # AC max charging rate
                gross_fee = 80

    # DC charging rate
    elif charger_type == "DC":
        if duration_hours <= 2:
            gross_fee = duration_hours * 10

        elif duration_hours <= 4:
            gross_fee = duration_hours * 15

        elif duration_hours <= 6:
            gross_fee = duration_hours * 20

        else:
            gross_fee = duration_hours * 30

            if gross_fee > 150:  # DC max charging rate
                gross_fee = 150
    else:
        print("Invalid Charger Type. Please try again.")
        continue

    #--------------------------------
    # DISCOUNT & WAIVER CALCULATION
    #--------------------------------
    # 100% waiver for first-time user
    if first_time_user == "Y":
        discount_fee = gross_fee

    # 50% discount for staff
    elif member_type == "Staff":
        discount_fee = gross_fee * 0.5

    # 25% discount for student
    elif member_type == "Student" and charger_type == "AC":
        discount_fee = gross_fee * 0.25

    # discount for green eco-pass holder
    if green_ecopass == "Y":
        eco_discount = 2

    # avoid discount fee exceed gross fee
    if discount_fee > gross_fee:
        discount_fee = gross_fee

    #---------------------------------
    # SURCHARGES
    #---------------------------------
    hour = int(charging_time[:2])
    minute = int(charging_time[3:])

    # peak hour surcharges: 12pm-4pm
    if 12 <= hour < 16 or (hour == 16 and minute == 0):
        surcharge_fee += 5

    # idle parking
    if idle_parking == "Y":
        surcharge_fee = surcharge_fee + 15

    # lost RFID card replacement fee
    if lost_rfid == "Y":
        replacement_fee = 30

    #-------------------------------
    #  FINAL BILL CALCULATION
    #-------------------------------
    final_bill = (gross_fee + surcharge_fee + replacement_fee - discount_fee - eco_discount)

    if final_bill < 0:
        final_bill = 0

    #---------------------------------
    # FORMATTED BILL OUTPUT DISPLAY
    #---------------------------------
    print()
    print("=========================================================")
    print("        Taylor's Smart Campus EV Charging Bill")
    print("=========================================================")
    print(f"User ID: {user_id}")
    print(f"Vehicle Number: {vehicle_no}")
    print(f"Member Type: {member_type}")
    print(f"Charger Type: {charger_type}")
    print(f"Hours Charged: {duration_hours}")
    print("---------------------------------------------------------")
    print(f"Gross Fee: RM {gross_fee:.2f}")
    print(f"Surcharge Fee: RM {surcharge_fee:.2f}")
    print(f"RFID Card Replacement Fee: RM {replacement_fee:.2f}")
    print(f"Discount Fee: (RM {discount_fee:.2f})")
    print(f"Eco-Pass Discount: (RM {eco_discount:.2f})")
    print(f"---------------------------------------------------------")
    print(f"Net Payable: RM {final_bill:.2f}")
    print("=========================================================")

    #-----------------------
    # CONTINUOUS LOOP
    #-----------------------
    next_vehicle = input("Process another Vehicle? (Y/N): ").upper()
    while next_vehicle not in ["Y", "N"]:
        print("Invalid Input. Please enter 'Y' or 'N'.")
        next_vehicle = input("Process another Vehicle? (Y/N): ").upper()

print("EV Charging System Closed. Thank you.")





