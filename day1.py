#Functions
def calculate_minutes_saved(current_minutes, new_minutes):
    return current_minutes - new_minutes


def calculate_hours_saved(minutes_saved_per_week):
    return minutes_saved_per_week / 60

# Variables
# Variables
try:
    current_minutes = float(input("Current minutes per transaction: "))
    new_minutes = float(input("New minutes per transaction: "))
    transactions_per_week = float(input("Transactions per week: "))
    hourly_cost = float(input("Employee hourly cost: "))
except ValueError:
    print("\nInvalid input. Please enter numbers only.")
    raise SystemExit

#Calculations
if new_minutes >= current_minutes:
    print("\nNo process improvement detected.")
    print("The new process takes the same amount of time or longer.")
else:  
    minutes_saved = calculate_minutes_saved(current_minutes, new_minutes)
    minutes_saved_per_week = minutes_saved * transactions_per_week
    hours_saved_per_week = calculate_hours_saved(minutes_saved_per_week)
    weekly_labor_savings = hours_saved_per_week * hourly_cost
    annual_labor_savings = weekly_labor_savings * 52
    percent_reduction = (minutes_saved / current_minutes) * 100

    #Outputs
    print("\nPROCESS IMPROVEMENT ANALYSIS")
    print("----------------------------")
    print(f"Minutes saved per transaction: {minutes_saved:.1f}")
    print(f"Hours saved per week: {hours_saved_per_week:.1f}")
    print(f"Weekly labor savings: ${weekly_labor_savings:,.2f}")
    print(f"Annual labor savings: ${annual_labor_savings:,.2f}")
    print(f"Process time reduction: {percent_reduction:.1f}%")