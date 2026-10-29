class Patient:
    def __init__(self, name, bill_amount):
        self._name = name
        self._bill_amount = bill_amount

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_bill_amount(self):
        return self._bill_amount 

    def set_bill_amount(self, bill_amount):
            if bill_amount >= 0:
                self.__bill_amount = bill_amount
            else:
                raise ValueError("Bill amount cannot be negative! Try again.")

    def calculate_bill(self):
        return self.get_bill_amount()

class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85

regular_patient1 = Patient("Erikah Mya N. Zozobrado", 150433567897654)
regular_patient2 = Patient("Princess Sofia Roda", 1345678543)
regular_patient3 = Patient("LaVyrly D. Lucero", 154556)
regular_patient4 = Patient("Noreen Ysabelle C. Angangan", 9999999999999)
senior_patient1 = SeniorPatient("Eziah Aldrich M. Baylon", 1200657543)
senior_patient2 = SeniorPatient("Maria Avera Ardreya A. Carampil", 5657543000)
senior_patient3 = SeniorPatient("Neeron Ellebasy C. Nagnagna", 1000000070000)
philhealth_patient1 = PhilHealthPatient("Yoanna Glorien C. Cabatingan", 100455400)
philhealth_patient2 = PhilHealthPatient("Leoana Amabele B. Lumakin", 100545400)
philhealth_patient3 = PhilHealthPatient("Nagnagna C. Ellebasy Neeron", 9384376453782918237645637281982736456378291)

patients = [
    regular_patient1,
    regular_patient2,
    regular_patient3,
    senior_patient2,
    senior_patient3,
    philhealth_patient1,
    philhealth_patient2,
    philhealth_patient3
]


for patient in patients:
    print("Patient Name:", patient.get_name())
    print("Original Bill: PHP{:,.2f}".format(
        patient.get_bill_amount()
    ))
    print("Final Bill: PHP{:,.2f}".format(
        patient.calculate_bill()
    ))
    print("-" * 35)

