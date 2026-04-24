ParkEase: Integrated Parking & Vehicle Services Management System

Project Overview

ParkEase is a web-based system developed using Django to automate parking management operations.  
The system digitizes vehicle registration, parking fee calculation, receipt generation, sign-out processes, and revenue reporting.

It also includes additional modules for:
- Tyre  Services
- Battery Hire & Sales

 Objectives

- Improve record keeping
- Reduce revenue leakage
- Automate parking fee calculation
- Provide real-time reporting
- Support decision-making for management

System Features

 Parking Management
- Vehicle registration (driver name, plate, type, phone, NIN)
- Automatic parking fee calculation based on:
  - Vehicle type
  - Duration
  - Day/Night time
- Vehicle status tracking (Parked / Cleared)

 Receipt Management
- Automatic generation of unique receipt numbers
- Receipts linked to vehicles
- Printable receipts

---
 Sign-Out Process
- Records:
  - Receiver name
  - Phone number
  - Gender
  - NIN
  - Receipt number
- Validates receipt before sign-out
- Updates vehicle status to *cleared*


Reporting & Dashboard
- Total vehicles
- Today's revenue
- Available parking slots
- Daily revenue report (filter by date)
- Combined revenue:
  - Parking
    
Authentication System
- Staff registration
- Login & logout
- Role-based access (Admin, Attendant, Manager)

 Technologies Used

- Python (Django Framework)
- SQLite (Database)
- HTML, CSS, Bootstrap 5
- JavaScript (for UI interactions)
- xhtml2pdf (PDF export)

