products = {
    "P001": {"name": "Keyboard" ,"price":500 ,"stock":10},
    "P002": {"name": "Mouse" ,"price":250 ,"stock":20},
    "P003": {"name": "Monitor" ,"price":3500 ,"stock":5},
}

while True:
    print("Inventor System")
    print("1.Show Products\n2.Search Product\n3.Revecive Product\n4.Deliver Product\n5.Exit")
    choice = int(input("Select Menu : "))
    if choice == 1:
        print("แสดงสินค้าทั้งหมด : ")
        print("ชื่อรายการสินค้า : ",products["P001"]["name"],"\nจำนนวนราคา/ต่อชิ้น : ",products["P001"]["price"],"\nจำนวนสินค้าคงเหลือ : ",products["P001"]["stock"],"\n")
        print("ชื่อรายการสินค้า : ",products["P002"]["name"],"\nจำนนวนราคา/ต่อชิ้น : ",products["P002"]["price"],"\nจำนวนสินค้าคงเหลือ : ",products["P002"]["stock"],"\n")
        print("ชื่อรายการสินค้า : ",products["P003"]["name"],"\nจำนนวนราคา/ต่อชิ้น : ",products["P003"]["price"],"\nจำนวนสินค้าคงเหลือ : ",products["P003"]["stock"],"\n")

    elif choice == 2:
        search = input("กรอกรหัสสินค้าที่ต้องการค้นหา : ")
        search = search.upper()
        # คำสั่ง in เอาไว้ตรวจสอบว่ามี key อยู่ในนั้นหรือเปล่า
        while search not in products: # การใช้ not in ลดการเขียนมือซ้ำ ๆ
            print(f"ไม่มีรหัสสินค้าที่คุณต้องการหา : {search} ครับกรุณากรอสินค้าใหม่")
            search = input("กรอกรหัสสินค้าที่ต้องการค้นหา : ")

        if search in products: # ตรวจสอบว่าพบสินค้ามั้ย โดยการใช้ in
            print("พบสินค้า")
            if  search == "P001": #ค้นหาค่า key
                print(f"ชื่อรายการสินค้า : {products['P001']['name']} \nจำนนวนราคา/ต่อชิ้น : {products['P001']['price']} บาท \nจำนวนสินค้าคงเหลือ : {products['P001']['stock']} ชิ้น ")

            elif search == "P003":  # ค้นหาค่า key
                print(
                    f"ชื่อรายการสินค้า : {products['P002']['name']} \nจำนนวนราคา/ต่อชิ้น : {products['P002']['price']} บาท \nจำนวนสินค้าคงเหลือ : {products['P002']['stock']} ชิ้น ")

            elif search == "P003": #ค้นหาค่า key
                print(f"ชื่อรายการสินค้า : {products['P003']['name']} \nจำนนวนราคา/ต่อชิ้น : {products['P003']['price']} บาท \nจำนวนสินค้าคงเหลือ : {products['P003']['stock']} ชิ้น ")

    elif choice == 3:
        print("การเพิ่มสต๊อกสินค้า")
        search_receive = (input("กรุณากรอกรหัสสินค้า : "))
        search_receive = search_receive.upper()

        while search_receive not in products:
            print(f"ไม่มีรหัสสินค้าที่คุณต้องการหา : {search_receive} ครับกรุณากรอสินค้าใหม่")
            search_receive = input("กรอกรหัสสินค้าที่ต้องการค้นหา : ")

        if search_receive in products: # ตรวจสอบว่าพบสินค้ามั้ย โดยการใช้ in
            if  search_receive == "P001": #ค้นหาค่า key
                update_stock = int(input("กรอกจำนวนสินค้าที่เพิ่มเข้ามา : "))
                products["P001"]["stock"] += update_stock
            elif search_receive == "P002":  # ค้นหาค่า key
                update_stock = int(input("กรอกจำนวนสินค้าที่เพิ่มเข้ามา : "))
                products["P002"]["stock"] += update_stock
            elif search_receive == "P003": #ค้นหาค่า key
                update_stock = int(input("กรอกจำนวนสินค้าที่เพิ่มเข้ามา : "))
                products["P003"]["stock"] += update_stock

    elif choice == 4:
        print("การลดสต๊อกสินค้า")
        search_receive = (input("กรุณากรอกรหัสสินค้า : "))
        search_receive = search_receive.upper()

        while search_receive not in products:
            print(f"ไม่มีรหัสสินค้าที่คุณต้องการหา : {search_receive} ครับกรุณากรอสินค้าใหม่")
            search_receive = input("กรอกรหัสสินค้าที่ต้องการค้นหา : ")

        if search_receive in products:  # ตรวจสอบว่าพบสินค้ามั้ย โดยการใช้ in
            if search_receive == "P001":  # ค้นหาค่า key
                update_stock = int(input("กรอกจำนวนสินค้าที่เพิ่มเข้ามา : "))
                products["P001"]["stock"] -= update_stock
            elif search_receive == "P002":  # ค้นหาค่า key
                update_stock = int(input("กรอกจำนวนสินค้าที่เพิ่มเข้ามา : "))
                products["P002"]["stock"] -= update_stock
            elif search_receive == "P003":  # ค้นหาค่า key
                update_stock = int(input("กรอกจำนวนสินค้าที่เพิ่มเข้ามา : "))
                products["P003"]["stock"] -= update_stock

    elif choice == 5:
        break