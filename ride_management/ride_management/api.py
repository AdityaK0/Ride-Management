import frappe
from frappe.model.naming import make_autoname
import random


def createItemsData():
    createdItems = []
    itemDoctypeData = [

        {
            "item_code":"Wi-Fi Access",
            "item_group":"Services",
            "is_stock_item":0,
            "standard_rate": 500
        },
        {
            "item_code":"Travel Insurance",
            "item_group":"Services",
            "is_stock_item":0,
            "standard_rate": 1000
        },
        {
            "item_code":"Tourist Guides",
            "item_group":"Services",
            "is_stock_item":0,
            "standard_rate": 1500
        },

    ]

    for data in itemDoctypeData:
        itemNewDoc = frappe.get_doc({
            "doctype":"Item",
            "item_code":data[ "item_code"],
            "item_group":data["item_group"],
            "is_stock_item":data["is_stock_item"],
            "standard_rate": data["standard_rate"]
        })

        itemNewDoc.insert()
        itemNewDoc.save()
        createdItems.append(itemNewDoc)
    frappe.db.commit()    


    return f"{len(createdItems)} Items Created Successfully "


def createCustomerData():
    
    createdCustomers = []
    customerData = [
        {
            "customer_name":"Aditya",
            "customer_contact":"9327748938"
        },
        {
            "customer_name":"Addy"
        }
    ]

    for data in customerData:
        customerDocData = {
            "doctype":"Customer",
            "customer_name":data["customer_name"]
        }
        if "customer_contact" in data:
            customerDocData["custom_customer_mobile"] = data["customer_contact"]

        customerDoc = frappe.get_doc(customerDocData)
        customerDoc.insert()
        createdCustomers.append(customerDoc)


    frappe.db.commit()

    return f"{len(createdCustomers)} Customers created successfully"     



def createVehicleRideData():
    createdVehicleRides = []
    VehicleRideDoctypeData = [

              {
            "name": "VR-001",  
            "make": "Toyota",
            "type": "Sedan",
            "price_per_km": 10,
            "image": "https://imgd.aeplcdn.com/664x374/n/cw/ec/192443/camry-exterior-right-front-three-quarter-2.jpeg?isig=0&q=80"  
        },
        {
            "name": "VR-002",  
            "make": "Ford",
            "type": "SUV",
            "price_per_km": 15,
            "image": "https://www.ford.com/is/image/content/dam/brand_ford/en_us/brand/segment_landing/suvs/dm/25_FRD_EPD_F2A1615_Segment.tif?croppathe=1_4x3&wid=900" 
        },
        {
            "name": "VR-003",  
            "make": "Harley",
            "type": "Bike",
            "price_per_km": 5,
            "image": "https://imgd.aeplcdn.com/1056x594/n/tt7l79b_1795935.jpg?q=80"  
        }


    ]
    for data in VehicleRideDoctypeData:
        rideNewDoc = frappe.get_doc({
            "doctype":"Vehicle Ride",
            "name":data["name"],
            "make":data[ "make"],
            "type":data["type"],
            "price_per_km":data["price_per_km"],
            "image": data["image"]
        })

        rideNewDoc.insert()
        rideNewDoc.save()
        createdVehicleRides.append(rideNewDoc)
    frappe.db.commit()   

    return f"{len(createdVehicleRides) } Vehicle Rides Created Successfully"



def createRideBookingData():
    createdRideBookings = []
    BookingDoctypeData = [

    {
        "vehicle":"VR-001",
        "estimated_km":55,
        "customer":"Aditya",
        "booking_date": "2025-01-28",
        "return_date":"2025-02-03"
    },
    {
        "vehicle":"VR-002",
        "estimated_km":70,
        "customer":"Addy",
        "booking_date": "2025-01-27",
        "return_date":"2025-02-03"
    },
    {
        "vehicle":"VR-003",
        "estimated_km":90,
        "customer":"Aditya",
        "booking_date": "2025-01-29",
        "return_date":"2025-02-09"
    },
    

    ]
    for data in BookingDoctypeData:
        bookingNewDoc = frappe.get_doc({
            "doctype":"Ride Booking",
            "vehicle":data["vehicle"],
            "estimated_km":data["estimated_km"],
            "customer":data["customer"],
            "booking_date": data["booking_date"],
            "return_date":data["return_date"]
        })

        
        bookingNewDoc.append("services",{
            "service" : random.choice(["Wi-Fi Access","Travel Insurance","Tourist Guides"])
        })
        bookingNewDoc.insert()

        createdRideBookings.append(bookingNewDoc)
    frappe.db.commit()   

    return f"{len(createdRideBookings)} Vehicle Rides Created Successfully"




def createRecords():
    createItemsData()
    createCustomerData()
    createVehicleRideData()
    createRideBookingData()