#Task 2
import math

next_vehicle = "Y"  # Y = Yes

while next_vehicle == "Y":

    #------------------
    # USER INPUT
    #------------------
    user_id = input("User ID: ")
    vehicle_no = input("Vehicle Number: ")
    print("\nMember Type: ")
    print("1. Staff")
    print("2. Student")
    print("3. Public")

    # Member Type
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

    # Charger Type
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

    # Charging Details
    hours_charged = float(input("\nHours Charged: "))
    while hours_charged <= 0:
        print("Invalid input. Please try again.")
        hours_charged = float(input("\nHours Charged: "))


    charging_time = input("Charging Time (HH:MM, 24-hours format): ")
    while len(charging_time) != 5 or charging_time[2] != ":":
        print("Invalid input. Please enter time in HH:MM format.")
        charging_time = input("Charging Time (HH:MM, 24-hours format): ")

    # Battery
    battery_level = float(input("Battery Level (%): "))
    while battery_level < 0 or battery_level > 100:
        print("Invalid input. Please enter a value between 0 and 100.")
        battery_level = float(input("Battery Level (%): "))


    #--------------------------------
    # SPECIAL CONDITIONS
    #--------------------------------
    # Y = Yes; N = No
    print("\nSpecial Conditions:")

    first_time_user = input("First-time User (Y/N): ").upper()
    while first_time_user not in ["Y", "N"]:
        print("Invalid Input. Please enter Y or N.")
        first_time_user = input("First-time User (Y/N): ").upper()

    eco_pass = input("Green Eco-Pass Holder (Y/N): ").upper()
    while eco_pass not in ["Y", "N"]:
        print("Invalid Input. Please enter Y or N.")
        eco_pass = input("Green Eco-Pass Holder (Y/N): ").upper()

    idle_parking = input("Idle Parking (Y/N): ").upper()
    while idle_parking not in ["Y", "N"]:
        print("Invalid Input. Please enter Y or N.")
        idle_parking = input("Idle Parking (Y/N): ").upper()

    lost_rfid = input("Lost RFID (Y/N): ").upper()
    while lost_rfid not in ["Y", "N"]:
        print("Invalid Input. Please enter Y or N.")
        lost_rfid = input("Lost RFID (Y/N): ").upper()


    # Initial Fees
    discount_fee = 0
    eco_pass_discount = 0
    surcharge_fee = 0
    replacement_fee = 0

    #---------------------------------
    # CHARGING FEE CALCULATION
    #---------------------------------
    # Calculate Charging Duration
    duration_hours = math.ceil(hours_charged)

    # AC Charging Fee
    if charger_type == "AC":
        if duration_hours <= 2:
            gross_fee = duration_hours * 4

        elif duration_hours <= 4:
            gross_fee = duration_hours * 6

        elif duration_hours <= 6:
            gross_fee = duration_hours * 8

        else:
            gross_fee = duration_hours * 12

            if gross_fee > 80:  # AC maximum fee
                gross_fee = 80

    # DC Charging Fee
    elif charger_type == "DC":
        if duration_hours <= 2:
            gross_fee = duration_hours * 10

        elif duration_hours <= 4:
            gross_fee = duration_hours * 15

        elif duration_hours <= 6:
            gross_fee = duration_hours * 20

        else:
            gross_fee = duration_hours * 30

            if gross_fee > 150:     # DC maximum fee
                gross_fee = 150


    #--------------------------------
    # DISCOUNT & WAIVER CALCULATION
    #--------------------------------
    # 100% Waiver for First-time User
    if first_time_user == "Y":
        discount_fee = gross_fee

    # Staff Discount
    elif member_type == "Staff":
        discount_fee = gross_fee * 0.5

    # Student Discount
    elif member_type == "Student" and charger_type == "AC":
        discount_fee = gross_fee * 0.25

    # Green Eco-Pass Holder
    if eco_pass == "Y":
        eco_pass_discount = 2

    # Ensure Discount Fee Does Not Exceed Gross Fee
    if discount_fee > gross_fee:
        discount_fee = gross_fee

    #---------------------------------
    # SURCHARGES CALCULATION
    #---------------------------------
    hour = int(charging_time[:2])
    minute = int(charging_time[3:])

    # Peak Hour Surcharge: 12PM - 4PM
    if 12 <= hour < 16 or (hour == 16 and minute == 0):
        surcharge_fee += 5

    # Idle Parking
    if idle_parking == "Y" and battery_level >= 100:
        surcharge_fee += 15

    # RFID Replacement Fee
    if lost_rfid == "Y":
        replacement_fee = 30

    #-------------------------------
    #  FINAL BILL CALCULATION
    #-------------------------------
    final_bill = (gross_fee + surcharge_fee + replacement_fee - discount_fee - eco_pass_discount)

    if final_bill < 0:
        final_bill = 0

    #---------------------------------
    #  BILL OUTPUT
    #---------------------------------
    print()
    print("=======================================================")
    print("        Taylor's Smart Campus EV Charging Bill         ")
    print("=======================================================")
    print(f"User ID: {user_id}")
    print(f"Vehicle Number: {vehicle_no}")
    print(f"Member Type: {member_type}")
    print(f"Charger Type: {charger_type}")
    print(f"Hours Charged: {duration_hours}")
    print("-------------------------------------------------------")
    print(f"Gross Fee                      : RM {gross_fee:.2f}")
    print(f"Surcharge Fee                  : RM {surcharge_fee:.2f}")
    print(f"RFID Card Replacement Fee      : RM {replacement_fee:.2f}")
    print(f"Discount Fee                   : (RM {discount_fee:.2f})")
    print(f"Eco-Pass Discount              : (RM {eco_pass_discount:.2f})")
    print("-------------------------------------------------------")
    print(f"Net Payable                    : RM {final_bill:.2f}")
    print("=======================================================")

    #-----------------------
    # CONTINUOUS LOOP
    #-----------------------
    next_vehicle = input("Process another Vehicle? (Y/N): ").upper()
    while next_vehicle not in ["Y", "N"]:
        print("Invalid Input. Please enter 'Y' or 'N'.")
        next_vehicle = input("\nProcess another Vehicle? (Y/N): ").upper()

    if next_vehicle == "Y":
        print()

print("EV Charging System Closed. Thank you.")





