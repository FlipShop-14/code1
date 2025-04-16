counter = 1

#Task 1
def staff_info():
    global counter 
    date = input("Enter the date (DD/MM/YYYY): ")
    staff_name = input("Enter your name: ")
    staff_id = input("Enter your staff ID: ")

    #My Requistion ID generator
    random_id = counter + 1000
    counter += 1  

    #Made data into a dictionary to extract later
    return{
        "date": date,
        "staff_name": staff_name,
        "staff_id": staff_id,
        "random_id": random_id
    }
    
#staff_data = staff_info()
#print(staff_data)

#task 2
def requisition_totals(staff_data):
    #Collection item price and name
    item = input("Enter the name of the item ")
    cost = float(input(f"enter a price for {item} "))

    item2 = input("Enter the name of the item ")
    cost2 = float(input(f"enter a price for {item2} "))

    item3 = input("Enter the name of the item ")
    cost3 = float(input(f"enter a price for {item3} "))
        
    #print(f"{item} $ {cost}")
    #print(f"{item2} $ {cost2}")
    #print(f"{item3} $ {cost3}")

    total_cost = cost + cost2 + cost3
    return total_cost
    #Print(total_cost)
#total_price = requisition_totals(staff_data)        

#task 3
def requisition_approval(total_price, staff_data):
    if total_price < 500:
        status = "Approved"
        #The [-3] takes the first 3 didgits off the random_id
        approval_ref = f"{staff_data['staff_id']}{str(staff_data['random_id'])[-3:]}"

    else:
        status = "Pending"
        approval_ref = ""
    return status, approval_ref
    #print(status, approval_ref)
#staff_approval = requisition_approval(total_price, staff_data)       

#Task 4 
def display_requisitions(staff_data, total_price, staff_approval):
    status, approval_ref = staff_approval #Collection status and approval ref from task 3
    #Printing relevent information
    print("Printing Requisitions:")
    print(f"Date: {staff_data['date']}")
    print(f"Staff Name: {staff_data['staff_name']}")
    print(f"Staff ID: {staff_data['staff_id']}")
    print(f"Total Requisition Amount: ${total_price}")
    print(f"Status: {status}")
    print(f"Approval refrence: {approval_ref}")

    


#Calling in functions
staff_data = staff_info()
total_price = requisition_totals(staff_data)   
staff_approval = requisition_approval(total_price, staff_data)
display_requisitions(staff_data, total_price, staff_approval)
