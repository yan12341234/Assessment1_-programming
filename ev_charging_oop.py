import math
#-----------------------------
# USER CLASS
#-----------------------------
from abc import ABC, abstractmethod

class User(ABC):
    """Represent a user of the EV charging system."""
    def __init__(self, user_id, name, vehicle_no):

        self.__user_id  = ""
        self.__name = ""
        self.__vehicle_no = ""
        self.__active_session = None

        self.user_id = user_id
        self.name = name
        self.vehicle_no = vehicle_no

    # User ID
    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        if value.strip() != "":
            self.__user_id = value
        else:
            print("User ID is invalid")

    # Name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() != "":
            self.__name = value
        else:
            print("Name is invalid")

    # Vehicle Number
    @property
    def vehicle_no(self):
        return self.__vehicle_no

    @vehicle_no.setter
    def vehicle_no(self, value):
        if value.strip() != "":
            self.__vehicle_no = value
        else:
            print("Vehicle number is invalid")

    # Composition
    def start_charge(self, charging_session):
        self.__active_session = charging_session

    # Abstract Fee Calculation
    @abstractmethod
    def calculate_fee(self, gross_fee, charger_type):
        pass

#-------------------------
# STUDENT CLASS
#-------------------------
class StudentUser(User):
    """Represent a student user."""
    def __init__(self, user_id, name, vehicle_no, eco_pass, first_time_user, student_status):
        super().__init__(user_id, name, vehicle_no)

        self.__eco_pass = False
        self.__first_time_user = False
        self.__student_status = ""

        self.eco_pass = eco_pass
        self.first_time_user = first_time_user
        self.student_status = student_status

    # Eco-Pass
    @property
    def eco_pass(self):
        return self.__eco_pass

    @eco_pass.setter
    def eco_pass(self, value):
        if value == True or value == False:
            self.__eco_pass = value
        else:
            print("Eco-Pass must be True or False")

    # First-time User
    @property
    def first_time_user(self):
        return self.__first_time_user

    @first_time_user.setter
    def first_time_user(self, value):
        if value == True or value == False:
            self.__first_time_user = value
        else:
            print("First-time user must be True or False")

    # Student Status
    @property
    def student_status(self):
        return self.__student_status

    @student_status.setter
    def student_status(self, value):
        if value.strip() != "":
            self.__student_status = value
        else:
            print("Student status is invalid")

    # Polymorphism - Override calculate_fee()
    def calculate_fee(self, gross_fee, charger_type):

        # First-time User: 100% Waiver
        if self.__first_time_user:
            return 0

        # Student: 25% Discount for AC Charger
        if charger_type == "AC":
            return gross_fee * 0.75

        return gross_fee

#-------------------
# STAFF CLASS
#-------------------
class StaffUser(User):
    """Represent a staff user."""
    def __init__(self, user_id, name, vehicle_no, eco_pass, first_time_user, staff_status):
        super().__init__(user_id, name, vehicle_no)

        self.__eco_pass = False
        self.__first_time_user = False
        self.__staff_status = ""

        self.eco_pass = eco_pass
        self.first_time_user = first_time_user
        self.staff_status = staff_status

    # Eco-Pass
    @property
    def eco_pass(self):
        return self.__eco_pass

    @eco_pass.setter
    def eco_pass(self, value):
        if value == True or value == False:
            self.__eco_pass = value
        else:
            print("Eco-Pass must be True or False")

    # First-time User
    @property
    def first_time_user(self):
        return self.__first_time_user

    @first_time_user.setter
    def first_time_user(self, value):
        if value == True or value == False:
            self.__first_time_user = value
        else:
            print("First-time user must be True or False")

    # Staff Status
    @property
    def staff_status(self):
        return self.__staff_status

    @staff_status.setter
    def staff_status(self, value):
        if value.strip() != "":
            self.__staff_status = value
        else:
            print("Staff status is invalid")

    # Polymorphism - Override calculate_fee()
    def calculate_fee(self, gross_fee, charger_type):

        # First-Time User: 100% Waiver
        if self.__first_time_user:
            return 0

        # Staff: 50% Discount
        return gross_fee * 0.50

#----------------------------------
# CHARGING SESSION CLASS
#----------------------------------
class ChargingSession:
    """Represent one EV charging session."""
    def __init__(self, session_id, hours_charged, charging_time,
                 charger_type, idle_parking, battery_level):

        self.__session_id = ""
        self.__hours_charged = 0.0
        self.__charging_time = ""
        self.__charger_type = ""
        self.__idle_parking = False
        self.__battery_level = 0

        self.session_id = session_id
        self.hours_charged = hours_charged
        self.charging_time = charging_time
        self.charger_type = charger_type
        self.idle_parking = idle_parking
        self.battery_level = battery_level

    # Session ID
    @property
    def session_id(self):
        return self.__session_id

    @session_id.setter
    def session_id(self, value):
        if value.strip() != "":
            self.__session_id = value
        else:
            print("Session ID is invalid")

    # Hours Charged
    @property
    def hours_charged(self):
        return self.__hours_charged

    @hours_charged.setter
    def hours_charged(self, value):
        if value > 0:
            self.__hours_charged = value
        else:
            print("Hours charged must be greater than 0")

    # Charging Time
    @property
    def charging_time(self):
        return self.__charging_time

    @charging_time.setter
    def charging_time(self, time):
        if len(time) == 5 and time[2] == ":":
            hour = int(time[:2])
            minute = int(time[3:])
            if 0 <= hour <= 23 and 0 <= minute <= 59:
                self.__charging_time = time
            else:
               print("Charging time is invalid")
        else:
            print("Charging time must be in HH:MM format")

    # Charger Type
    @property
    def charger_type(self):
        return self.__charger_type

    @charger_type.setter
    def charger_type(self, value):
        value = value.upper()

        if value == "AC" or value == "DC":
            self.__charger_type = value
        else:
            print("Charger type must be AC or DC")

    # Idle Parking
    @property
    def idle_parking(self):
        return self.__idle_parking

    @idle_parking.setter
    def idle_parking(self, value):
        if value == True or value == False:
            self.__idle_parking = value
        else:
            print("Idle Parking must be True or False")

    @property
    def battery_level(self):
        return self.__battery_level

    @battery_level.setter
    def battery_level(self, value):
        if 0 <= value <= 100:
            self.__battery_level = value
        else:
            print("Battery level must be between 0 and 100")

    # Calculate Charging Fee
    def calculate_charging_fee(self):

        duration_hours = math.ceil(self.__hours_charged)

        if self.__charger_type == "AC":
            if duration_hours <= 2:
                gross_fee = duration_hours * 4

            elif duration_hours <= 4:
                gross_fee = duration_hours * 6

            elif duration_hours <= 6:
                gross_fee = duration_hours * 8

            else:
                gross_fee = duration_hours * 12

                if gross_fee > 80:
                    gross_fee = 80

        # DC
        else:
            if duration_hours <= 2:
                gross_fee = duration_hours * 10

            elif duration_hours <= 4:
                gross_fee = duration_hours * 15

            elif duration_hours <= 6:
                gross_fee = duration_hours * 20

            else:
                gross_fee = duration_hours * 30

                if gross_fee > 150:
                    gross_fee = 150

        return gross_fee

    #--------------------------------
    # GENERATE BILL
    #--------------------------------
    def generate_bill(self, user, lost_rfid):
        """Calculate final bill"""

        # Calculate gross charging fee
        gross_fee = self.calculate_charging_fee()

        # Polymorphism - user specific discount
        discounted_fee = user.calculate_fee(gross_fee, self.__charger_type)




    # Surcharge Calculation
        peak_hour_surcharge = 0
        idle_parking_surcharge = 0

        hour = int(self.__charging_time[:2])
        minute = int(self.__charging_time[3:])

        # Peak Hour: 12PM - 4PM
        if 12 <= hour < 16 or (hour == 16 and minute == 0):
            peak_hour_surcharge += 5

        # Idle Parking Surcharge
        if self.__idle_parking and self.__battery_level >= 100:
            idle_parking_surcharge += 15

        surcharge_fee = peak_hour_surcharge + idle_parking_surcharge


        # Lost RFID Replacement Fee
        replacement_fee = 0
        if lost_rfid:
            replacement_fee = 30

        # Eco-Pass Discount: RM2
        eco_pass_discount = 0
        if user.eco_pass:
            eco_pass_discount = 2

        # First-time User Waiver
        if user.first_time_user:
            discounted_fee = 0

        discount_fee = gross_fee - discounted_fee

    #-----------------------------------
    # FINAL BILL
    #-----------------------------------
        final_bill = (gross_fee + surcharge_fee + replacement_fee
                      - discount_fee - eco_pass_discount)

        if final_bill <= 0:
            final_bill = 0

        return {
            "gross_fee": gross_fee,
            "peak_hour_surcharge": peak_hour_surcharge,
            "idle_parking_surcharge": idle_parking_surcharge,
            "surcharge_fee": surcharge_fee,
            "replacement_fee": replacement_fee,
            "discount_fee": discount_fee,
            "eco_pass_discount": eco_pass_discount,
            "final_bill": final_bill
        }

#--------------------------
#MAIN PROGRAM
#--------------------------
# Student User
student = StudentUser(
    "S0001",
    "Mary",
    "ABC1105",
    False,
    False,
    "Active"
)

#Staff User
staff = StaffUser(
    "F0002",
    "John",
    "EFG5566",
    True,
    False,
    "Active"
)

#Charging Sessions
student_session = ChargingSession(
    "T0001",
    3.5,
    "13:00",
    "AC",
    False,
    80

)

staff_session = ChargingSession(
    "T0002",
    5,
    "08:30",
    "DC",
    True,
    100

)

# Start Charging Sessions
student.start_charge(student_session)
staff.start_charge(staff_session)

users = [
    (student, student_session, False),
    (staff, staff_session, True),
]

# Generate Bills
bills = []

for user, session, lost_rfid in users:
    bill = session.generate_bill(user, lost_rfid)
    bills.append((user, session, bill))

#-----------------------
# Display Bills
#-----------------------
for i, (user, session, bill) in enumerate(bills, 1):
    print("=========================================")
    print("  EV CHARGING BILL - SESSION {}".format(i))
    print("=========================================")
    if type(user).__name__ == "StudentUser":
        user_type = "Student"
    else:
        user_type = "Staff"
    print("Member Type:", user_type)
    print("User ID:", user.user_id)
    print("Name:", user.name)
    print("Vehicle Number:", user.vehicle_no)
    print("Charger Type:", session.charger_type)
    print("Hours Charged:", session.hours_charged)
    print("-----------------------------------------")
    print("Gross Fee                : RM {:.2f}".format(bill["gross_fee"]))
    print("Peak Hour Surcharge      : RM {:.2f}".format(bill["peak_hour_surcharge"]))
    print("Idle Parking Surcharge   : RM {:.2f}".format(bill["idle_parking_surcharge"]))
    print("RFID Replacement Fee     : RM {:.2f}".format(bill["replacement_fee"]))
    print("Discount Fee             : (RM {:.2f})".format(bill["discount_fee"]))
    print("Green Eco-Pass Discount  : (RM {:.2f})".format(bill["eco_pass_discount"]))
    print("-----------------------------------------")
    print("Net Payable              : RM {:.2f}".format(bill["final_bill"]))
    print("=========================================")
    print()


