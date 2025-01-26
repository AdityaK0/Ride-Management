# Copyright (c) 2025, ADITYA and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class RideBooking(Document):
    
    def before_save(self):
        self.update_total_amount()


    def update_total_amount(self):
        price_per_km = self.price_per_km
        estimated_km = self.estimated_km or 1
        # print(price_per_km,estimated_km)
        
        total_service_amount = 0
        if len(self.services) > 0:
            for service in self.services:
                total_service_amount += service.amount or 0  

        total_amount = (price_per_km * estimated_km) + total_service_amount

        self.total_amount = total_amount
        # print(self.total_amount)



