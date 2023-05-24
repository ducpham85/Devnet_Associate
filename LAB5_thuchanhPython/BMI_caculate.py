def tinh_BMI(a,b):
    BMI=a/(b**2)
    if BMI<18.5:
        print("Thieu can")
    elif BMI<23:
        print("Binh thuong")
    elif BMI <25:
        print("Thua Can")
    else:
        print("Beo phi")
for i in range(1,6):
    print("nhap thong tin nguoi thu ",i)
    weight=input("Nhap can nang: ")
    height=input("Nhap chieu cao: ")
    # print("chieu cao: ",height)
    # print("can nang: ",weight)
    tinh_BMI(float(weight),float(height))


