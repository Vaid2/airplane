# Copyright (c) 2024, vaibhav and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random
import string
from frappe.model.document import Document

class AirplaneTicket(Document):
	def before_save(self):
		self.Total_Amount()
		self.submit_data()
		# self.capacity_control()
		# self.seat_number()

	def Total_Amount(self):
		self.total_amount = self.flight_price
		unique_add_ons = set()
		for add_on in self.add_ons:
			if add_on.item not in unique_add_ons:
				self.total_amount += add_on.amount
				unique_add_ons.add(add_on.item)
            	#unique_add_ons.add(add_on.item)
		        #total_amount = add_ons + flight_price

	def submit_data(self):
		if self.status != "Boarded":
			frappe.throw("Airplane Ticket cannot be submitted unless status is 'Boarded'")

	
	 

	def seat_number(self):
		random_number = random.randint(1,50)
		random_letter = random.choice(string.ascii_uppercase)
		self.seat = f"{random_number}{random_letter}"
		return self.seat


	def onload(self):
		self.default_flight()


	def default_flight(self):
		if frappe.request.args.get("flight"):
			flight = frappe.request.args.get("flight")
			self.flight = flight
	

	def capacity_control(self):
		if self.flight and self.seat:
			flight = frappe.get_doc('Flight',self.flight)
			airplane_capacity = flight.airplane_capacity
			booked_tickets = frappe.db.count('Airplane Ticket', filters={'flight':self.flight,'docstatus':1})
			if booked_tickets + self.seat > airplane_capacity:
				frappe.throw("seats are full")
    #ModuleNotFoundError: No module named 'frappe.core.doctype.flight'
		