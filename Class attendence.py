held = int(input("Enter the number of classes held: "))
attended = int(input("Enter the number of classes attended: "))

attendance_percentage = (attended / held) * 10

print("Percentage of classes attended:", attendance_percentage)

if attendance_percentage < 75:
    print("Sorry you fail")
else:
    print("Allow to sit in exam")