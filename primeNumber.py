"""

  Ý tưởng:
    - Nhập số n, ép kiểu thành số nguyên
    - Viết một hàm check_SNT(), hàm này sẽ trả về rrue nếu một số là SNT, ngược lại trả về false
    - Dùng vòng lặp để lặp từ 1 đến n, mỗi lần lặp sẽ sử dụng hàm check_SNT() để kiểm tra và tính tổng.
    
"""

n = int(input())

def check_SNT(n):
    flag = True
 
    if (n < 2):
        flag = False
        
    elif (n == 2):
        flag = True
        
    elif (n % 2 == 0):
        flag = False
        
    else:
        for i in range(3, n, 2):
            if (n % i == 0):
                flag = False
 
    return flag
 
tong = 0
for i in range(1, n):
    if (check_SNT(i)):
        print(i)
        tong += i

print("Tong  so nguyen to la:", tong)
