classes_held = 20
classes_attended =int(input("How many classes have you attended"))
attendance_percent= (classes_attended/classes_held)*100
medical_cause= "Yes"
no_cause = "No"
if attendance_percent >100 or attendance_percent < 0:
    print("invalid class attendance")
elif attendance_percent>= 75:
    print("You have an attendance of:",attendance_percent, "% and will therefore  to sit for exams")
elif attendance_percent<75:
    medical_input=input("Do you have a medical cause? Yes or No ")
    if medical_input == medical_cause:
        print("You have an attendance of:",attendance_percent, "% and but can still sit for exams")
    else:
        print("You have an attendance of:",attendance_percent, "% and will therefore not be able to sit for exams")