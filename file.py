from datetime import datetime

students = {
    "B101": "Jayappratha",
    "B102": "Kavin",
    "B103": "Anitha",
    "B104": "Rohit",
    "B105": "Priya"
}


attendance = {}

CUTOFF_HOUR = 11
CUTOFF_MINUTE = 00


def show_menu():
    print("\n========== BIOMETRIC ATTENDANCE SYSTEM ==========")
    print("1. Scan Biometric (Mark Intime)")
    print("2. View Attendance Report")
    print("3. Exit")
    print("=================================================")

def scan_biometric():
    bio_id = input("\nEnter Biometric ID: ").strip()
    if bio_id in students:
        name = students[bio_id]
        mark_intime(bio_id, name)
    else:
        print("❌ Invalid Biometric ID! Try again.")

def mark_intime(bio_id, name):
    now = datetime.now()
    current_time = now.strftime("%H:%M")  


    if now.hour < CUTOFF_HOUR or (now.hour == CUTOFF_HOUR and now.minute <= CUTOFF_MINUTE):
        status = "Present"
    else:   
        status = "Absent"


    if bio_id in attendance:
        print(f"\n⚠ {name} already marked intime at {attendance[bio_id]['Intime']} — {attendance[bio_id]['Status']}")
    else:
        attendance[bio_id] = {'Name': name, 'Intime': current_time, 'Status': status}
        print("\n✅ Attendance Recorded Successfully!")
        print(f"Name   : {name}")
        print(f"Intime : {current_time}")
        print(f"Status : {status}")
        print("Thank you!\n")

def update_absent_status():
    """Mark Absent for students who didn’t scan before cutoff"""
    now = datetime.now()
    if now.hour > CUTOFF_HOUR or (now.hour == CUTOFF_HOUR and now.minute > CUTOFF_MINUTE):
        for bio_id, name in students.items():
            if bio_id not in attendance:
                attendance[bio_id] = {'Name': name, 'Intime': '-', 'Status': 'Absent'}

def view_attendance():
    update_absent_status()

    if not attendance:
        print("\n📄 No attendance marked yet!")
        return

    today_date = datetime.now().strftime("%d-%b-%Y")
    print(f"\n========= TODAY'S ATTENDANCE REPORT ({today_date}) =========")
    print("{:<10} {:<15} {:<10} {:<15}".format("Bio ID", "Name", "Intime", "Status"))
    print("------------------------------------------------------------")

    present_count = 0
    absent_count = 0

    for bio_id, data in attendance.items():
        intime = data.get('Intime', '-')
        status = data.get('Status', 'Absent')
        if status == 'Present':
            present_count += 1
        else:
            absent_count += 1

        print("{:<10} {:<15} {:<10} {:<15}".format(bio_id, data['Name'], intime, status))

    print("------------------------------------------------------------")
    print(f"Total Present: {present_count} | Total Absent: {absent_count}")
    print("============================================================")


while True:
    show_menu()
    option = input("Enter your choice (1-3): ")

    if option == '1':
        scan_biometric()
    elif option == '2':
        view_attendance()
    elif option == '3':
        print("\n👋 Exiting the system. Have a great day!")
        break
    else:
        print("❌ Invalid option! Please choose 1–3.")