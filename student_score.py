cardinal_student = int(input("กรอกจำนวนนักเรียน : "))
student = []
cardinal_student +=1
i = 1
for i in range(1,cardinal_student):
    student_score = int(input(f"นักเรียนคนที่ {i} ได้คะเเนน : "))
    student.append(student_score)

past = 0
no_past = 0

for a in range(len(student)):
    if student[a] >= 50:
        past += 1
    elif student[a]<50:
        no_past += 1


print(f"มีนักเรียนผ่านจำนวน {past} คน")
print(f"มีนักเรียนผ่านจำนวน {no_past} คน")


