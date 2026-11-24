
# Software Development Assessment 2
# Requisition Management System

class Requisition:

    counter = 10000
    requisitions = []

    def __init__(self, date, staff_id, staff_name):
        Requisition.counter += 1

        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = Requisition.counter
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"

        Requisition.requisitions.append(self)

    # Calculate the total cost
    def add_requisition(self, items):
        self.items = items
        self.total = sum(cost for item, cost in items)
        return self.total

    # Automatically approve requests below $500
    def approve_requisition(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = (
                self.staff_id + str(self.requisition_id)[-3:]
            )
        else:
            self.status = "Pending"
            self.approval_reference = "Not available"

        return self.status

    # Manager response to pending requests
    def respond_requisition(self, decision):
        if self.status == "Pending":

            if decision == "Approved":
                self.status = "Approved"
                self.approval_reference = (
                    self.staff_id + str(self.requisition_id)[-3:]
                )

            elif decision == "Not approved":
                self.status = "Not approved"
                self.approval_reference = "Not available"

        return self.status

    # Display all requisitions
    @classmethod
    def display_requisitions(cls):
        for req in cls.requisitions:
            print("Date:", req.date)
            print("Requisition ID:", req.requisition_id)
            print("Staff ID:", req.staff_id)
            print("Staff Name:", req.staff_name)
            print(f"Total: ${req.total:.2f}")
            print("Status:", req.status)
            print("Approval Reference Number:",
                  req.approval_reference)
            print()

    # Calculate and display statistics
    @classmethod
    def requisition_statistics(cls):
        total = len(cls.requisitions)

        approved = sum(
            r.status == "Approved" for r in cls.requisitions
        )

        pending = sum(
            r.status == "Pending" for r in cls.requisitions
        )

        not_approved = sum(
            r.status == "Not approved" for r in cls.requisitions
        )

        print("Displaying the Requisition Statistics")
        print("The total number of requisitions submitted:", total)
        print("The total number of approved requisitions:", approved)
        print("The total number of pending requisitions:", pending)
        print("The total number of not approved requisitions:",
              not_approved)

        return total, approved, pending, not_approved


# Testing the program
if __name__ == "__main__":

    r1 = Requisition("03/04/2024", "FN19", "John Paul")
    r1.add_requisition([("Keyboard", 150), ("Monitor", 300)])
    r1.approve_requisition()

    r2 = Requisition("05/04/2024", "FN20", "Tracy Brown")
    r2.add_requisition([("Laptop", 1000)])
    r2.approve_requisition()

    r3 = Requisition("07/05/2024", "FN15", "Emma Wellington")
    r3.add_requisition([("Computer", 3500)])
    r3.approve_requisition()

    r4 = Requisition("03/05/2024", "FN02", "Catlin White")
    r4.add_requisition([("Printer", 400), ("Paper", 90)])
    r4.approve_requisition()

    r5 = Requisition("10/05/2024", "FN25", "James Smith")
    r5.add_requisition([("Office Chair", 500)])
    r5.approve_requisition()

    print("BEFORE MANAGER RESPONSE")
    print("-----------------------")

    Requisition.display_requisitions()
    Requisition.requisition_statistics()

    # Manager decisions
    r2.respond_requisition("Approved")
    r3.respond_requisition("Not approved")

    # Requisition 5 remains pending

    print("\nAFTER MANAGER RESPONSE")
    print("-----------------------")

    Requisition.display_requisitions()
    Requisition.requisition_statistics()


