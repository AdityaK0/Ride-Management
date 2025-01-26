# Ride Management App

## Overview
This README provides a step-by-step guide for the custom app "Ride Management" built in Frappe Framework. The app contains several custom Doctypes, scripts, and configurations to handle customer creation, item setup, vehicle rides, ride add-ons, and ride bookings.

## Task Breakdown

### 1. Create Customers
- **Customer 1**:
  - Fields: Customer Name, Mobile Number
- **Customer 2**:
  - Fields: Customer Name only

### 2. Create Items
- **Item 1**:
  - **Item Code**: Wi-Fi Access
  - **Item Group**: Service
  - **Maintain Stock**: 0 (False)
  - **Standard Selling Rate**: 500
- **Item 2**:
  - **Item Code**: Travel Insurance
  - **Item Group**: Service
  - **Maintain Stock**: 0 (False)
  - **Standard Selling Rate**: 1000
- **Item 3**:
  - **Item Code**: Tourist Guides
  - **Item Group**: Service
  - **Maintain Stock**: 0 (False)
  - **Standard Selling Rate**: 1500

### 3. Create a "Vehicle Ride" DocType
- **Fields**:
  - **Make**: Data (In List View)
  - **Type**: Data (In List View)
  - **Price Per Km**: Currency (In List View)
  - **Image**: Attach Image
- **Additional Details**:
  - Set the naming rule to "Set By User."
  - Display the "Image" field on the sidebar.
  - Add 3 demo Vehicle Rides.

### 4. Create a "Ride Add On" DocType
- **Fields**:
  - **Service**: Link to Item DocType (In List View)
  - **Amount**: Currency (Fetched from "Item" field: Standard Selling Rate) (In List View)
- **Additional Details**:
  - Make this a child table with an editable grid.

### 5. Create a "Ride Booking" DocType
- **Fields**:
  - **Vehicle**: Link to "Vehicle Ride" (In List View)
  - **Make**: Fetch from the "Vehicle Ride" field: Make
  - **Type**: Fetch from the "Vehicle Ride" field: Type
  - **Price Per Km**: Fetch from "Vehicle Ride" field: Price Per Km
  - **Estimated Km**: Float
  - **Services**: Table (Option: "Ride Add On")
  - **Total Amount**: Currency (Read Only) – Calculated as: `(Price Per Km * Estimated Km) + (Total Amount from Services Table)`
  - **Customer**: Link to "Customer"
  - **Customer Name**: Fetch from the "Customer" field: Customer Name (In List View)
  - **Phone Number**: Fetch if empty from the "Customer" field: Mobile No
  - **Booking Date**: Date (In List View)
  - **Return Date**: Date (In List View)
- **Additional Details**:
  - Set a naming rule to "Naming Series" which includes the Vehicle field at the start, the current year in the middle, and 4 digits at the end.
  - Add 3 Ride Bookings.

### 6. Export Default Items
- Export all the data entries in fixtures using the following command:
  ```bash
  bench export-fixtures
  ```

### 7. Upload Ride Management App to GitHub
- Create a repository on GitHub.
- Initialize a Git repository locally and push the app:
  ```bash
  git init
  git remote add origin https://github.com/<username>/Ride-Management.git
  git add .
  git commit -m "Initial Commit"
  git push -u origin main
  ```

## Custom Script for Record Creation
To automate the creation of required Doctype records, a custom script has been created. This script can be executed using the following command:
```bash
bench --site <site_name> execute ride_management.api.createRecords
```

### Example Script Logic
The script includes logic to:
- Create customers.
- Add items with predefined properties.
- Add demo vehicle rides.
- Add ride bookings with services.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<username>/Ride-Management.git
   ```
2. Install the app on your site:
   ```bash
   bench --site <site_name> install-app ride_management
   ```
3. Migrate the database:
   ```bash
   bench --site <site_name> migrate
   ```
4. Execute the record creation script if needed.

## Notes
- Ensure the app is installed on a Frappe site before running scripts or creating records.
- Fixtures are exported to preserve default items, doctypes, and custom configurations.

