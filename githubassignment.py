#Task1
#  this shows a very simple requisition system that collects 
#staff information and also auto-generates a unique requisition ID.
#and after there is staff information and then it will print the information.
Requisition_ID_counter = 10000

def Staff_Info():
    global Requisition_ID_counter 
    
    Staff_Date = input("Enter staff date (dd/mm/yy): ")
    Staff_ID = input("Enter staff ID: ")
    Staff_Name = input("Enter Staff Name: ")
    
    
    
    Requisition_ID_counter += 1
    Requisition_ID = Requisition_ID_counter
    
    print("\nStaff Information")
    print(f"Staff Date: {Staff_Date}")
    print(f"Staff ID: {Staff_ID}")
    print(f"Staff Name: {Staff_Name}")
    print(f"Requisition ID: {Requisition_ID}")

    # It Returns the staff details 
    return Staff_Date, Staff_ID, Staff_Name, Requisition_ID

#Task2
# this Requisitions total function will handles creating a full requisition record.
# first, which can have staff information then it ask how many items 
#will be there to include in the requisition then there is a variable to store the cost.
def Requisitions_Total():
    
    Staff_Date, Staff_ID, Staff_Name, Requisition_ID = Staff_Info()
    
    num_items = int(input("How many requisition items? "))
    total = 0  

    # It is a Loop through all requisition items
    for i in range(num_items):
        item_name = input(f"Enter item {i+1} name: ")
        item_price = float(input(f"Enter {item_name} price: $"))
        total += item_price
    
    print(f"\nTotal Requisition Value: ${total}")
    # It returns all the details with total
    return Staff_Date, Staff_ID, Staff_Name, Requisition_ID, total

#Task3
# first, it Calls Requisitions total to get staff info, requisition ID, and total value.
# after that it Sets default requisition status as "Pending" and approval reference as "N/A".
# and then if the total requisition value is less than $500 then it automatically approves the request

def Requisition_Approval():
    
    Staff_Date, Staff_ID, Staff_Name, Requisition_ID, total = Requisitions_Total()
    
    status = "Pending"
    approval_ref = "N/A"
    
    if total < 500:
        status = "Approved"
        approval_ref = Staff_ID + str(Requisition_ID)[-3:]
    
    print(f"\nTotal: ${total}")
    print(f"Status: {status}")
    print(f"Approval Reference Number: {approval_ref}")
    
    return Staff_Date, Staff_ID, Staff_Name, Requisition_ID, total, status, approval_ref

#Task4
# In this we have to print the all  
def Display_Requisitions():
    Staff_Date, Staff_ID, Staff_Name, Requisition_ID, total, status, approval_ref = Requisition_Approval()
    
    print("\nPrinting Requisitions:")
    print(f"Date: {Staff_Date}")
    print(f"Requisition ID: {Requisition_ID}")
    print(f"Staff ID: {Staff_ID}")
    print(f"Staff Name: {Staff_Name}")
    print(f"Total: ${total}")
    print(f"Status: {status}")
    print(f"Approval Reference Number: {approval_ref}")

Display_Requisitions()





































