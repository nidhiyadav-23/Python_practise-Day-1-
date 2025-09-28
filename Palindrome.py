num=12121
original_num=num
rev=0
while num > 0:
    digit=num % 10
    rev=rev * 10 + digit
    num= num // 10
if original_num == rev:
    print("Number is Palindrome")
