def ktthuannghich(n):
    str1 = str(n);
    str2 = str1[::-1];
    if (str1 == str2):
        return True;
    else:
        return False;

n = int(input("Nhập số nguyên dương n = "));
if(ktthuannghich(n)==True):
    print(n , "là số thuận nghịch");
else: print(n, "không phải là số thuận nghịch");

hoten=str(input("Nhập họ và tên: "));
print(hoten);

ho=str(input("Nhập họ: "));
tendem=str(input("Nhập tên đệm: "));
ten=str(input("Nhập tên: "));
print("N = ",len(ho),len(tendem),len(ten));

