
class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_bill_amount(self):
        return self.bill_amount

    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount

    def calculate_bill(self):
        return self.bill_amount

    def display_patient_type(self):
        print("Patient Type: Regular Patient")


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.bill_amount * 0.80

    def display_patient_type(self):
        print("Patient Type: Senior Citizen")


class PhilhealthPatient(Patient):
    def calculate_bill(self):
        return self.bill_amount * 0.85

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")


print("Hospital Billing System")
print("------------------------------")

patient1 = Patient("Juan Dela Cruz", 15000)

print("\nPatient Name: ", patient1.get_name())
patient1.display_patient_type()
print(f"Original Bill: ₱{patient1.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{patient1.calculate_bill():,.2f}")

patient2 = SeniorPatient("Maria Santos", 15000)

print("\nPatient Name: ", patient2.get_name())
patient2.display_patient_type()
print(f"Original Bill: ₱{patient2.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{patient2.calculate_bill():,.2f}")

patient3 = PhilhealthPatient("Pedro Reyes", 15000)

print("\nPatient Name: ", patient3.get_name())
patient3.display_patient_type()
print(f"Original Bill: ₱{patient3.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{patient3.calculate_bill():,.2f}")

