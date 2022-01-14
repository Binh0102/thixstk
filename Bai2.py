def tongchuso(n):
    tong = 0;
    while (n > 0):
        tong = tong + n % 10;
        n = int(n / 10);
    return tong;
 
n = int(input("Nhập n = "));
print("Tổng các chữ số của", n , "là", tongchuso(n));

tendem=str(input("Nhập tên đệm: "));
print(tendem);

ten=(str(input("Nhập tên của mình: ")));
print("N = ",len(tendem),"+",len(ten),"=",len(tendem)+len(ten));