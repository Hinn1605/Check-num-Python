try:
    a=int(input('Nhap so thu nhat: '))
    b=int(input('Nhap so thu hai: '))

    while a>b:
        print('\nSo thu nhat khong duoc lon hon so thu hai!')
        a=int(input('Nhap so thu nhat: '))
        b=int(input('Nhap so thu hai: '))
    else:
        dem=0
        # Sử dụng for duyệt các giá trị từ a đến b rồi kiểm tra điều kiện
        for i in range(a, b+1):
            if (i%2==0) and (i%3==0):
                dem+=1
                print(i, end=" ")
                break
        else:
            if dem==0:
                print('Khong co so nao chia het cho ca 2 va 3')
            else:
                print('Tren day la cac so chia het cho ca 2 va 3')
except:
    print('ERROR: Dinh dang dau vao khong hop le!')
