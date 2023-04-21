def symmetrical_num(n):
    flag=0;
    if (n[::-1]==n):
        flag=1
    return flag

n=int(input("Nhap mot so bat ki: "))
check=symmetrical_num(n)

if check==1:
    print(n, "la so doi xung")
else:
    print(n, "khong phai so doi xung")
