# Copyright (c) 2024, vaibhav and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
	def before_save(self):
		self.FullName()

	def FullName(self):
		if self.first_name:
			self.full_name = self.first_name + " " + self.last_name
		else:
			frappe.throw("First Name is required")
		

