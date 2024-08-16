import frappe
from frappe.model.document import Document

class AirplaneTicketWebForm(Document):
    def onload(self):
        if frappe.request.args.get('flight'):
            flight = frappe.request.args.get('flight')
            self.flight = flight