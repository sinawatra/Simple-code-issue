a = int(input("Enter the grade: "))
if a > 85 and a <= 100:
    print('Student Grade A')
if a > 60 and a <= 85:
    print('Student Grade B')
if a > 40 and a < 60:
    print('Student Grade C')
if a < 40:
    print('Student Fail')