
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

    def add_requisition(self, items):
        self.items = items
        self.total = sum(cost for item, cost in items)
        return self.total

    def approve_requisition(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = (
                self.staff_id + str(self.requisition_id)[-3:]
            )
        else:
            self.status = "Pending"

        return self.status

