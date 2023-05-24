# n=int(input("nhan so duong: "))
# def tongcacchuso(a):
#     temp=0
#     while a>0:
#         temp=temp+a%10
#         a=a//10   #chia lay phan nguyen
#     return temp
# while n>=10:
#     x=tongcacchuso(n)
#     n=n-x
# print(n)

n=input("Nhap so n:")
while int(n) > 9:
    for i in n:
        x=0
        x=x+int(i)
        n=int(n)-x
        n=str(n)
print(n)