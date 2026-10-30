print("เกมตอบคำถาม")
correct_answer = ['A', 'B', 'C', 'B', 'B']
answer = []
score_now = 0

print("ประเทศไทยมีกี่จังหวัด ?")
print("A. 77 จังหวัด\nB. 78 จังหวัด\nC. 76 จังหวัด\nD. 56 จังหวัด")
chose = input("เลือกคำตอบ : ").upper()
answer.append(chose)
print(" ")

print("เมืองหลวงของประเทศไทย ?")
print("A. ตาก\nB. กรุงเทพ\nC. เชียงใหม่\nD. ขอนแก่น")
chose = input("เลือกคำตอบ : ").upper()
answer.append(chose)
print(" ")

print("ดาวเคราะห์อยู่ใกล้ดวงอาทิตย์มากที่สุด ?")
print("A. โลก\nB. ดาวศูกร์\nC. ดาวพุธ\nD. ดาวอังคาร")
chose = input("เลือกคำตอบ : ").upper()
answer.append(chose)
print(" ")

print("ประเทศใดมีประชากรมากที่สุดในโลก ?")
print("A. จีน\nB. อินเดีย\nC. ญี่ปุุ่น\nD. อินเดีย")
chose = input("เลือกคำตอบ : ").upper()
answer.append(chose)
print(" ")

print("มนุษย์มีกระดูกกี่ชิ้นเมื่อโตเต็มวัย ?")
print("A. 406\nB. 206\nC. 106\nD. 306")
chose = input("เลือกคำตอบ : ").upper()
answer.append(chose)
print(" ")

for check, point in zip(correct_answer, answer):
    if check == point:
        get_point = int(1)
    else:
        get_point = int(0)

    score_now += get_point

print("คุณได้คะเเนน", score_now)
