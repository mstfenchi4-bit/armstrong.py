#Armstrong Number-------------
#153=1*1*1+5*5*5+3*3*3=1+125+27
number=int(input("Enter a number:"))
original=number
digits=len(str(number))
total=0
temp=number
while temp>0:
    digit = temp%10
    total = total + digit **digits
    temp=temp//10
if total == original:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number.")

#Factor
def print_factors(number):
    print("Facgtors of ",number,"are:")
    for i in range(1,number+1):
        if number % i==0:
            print(i)
num=int(input("Enter a number:"))
print_factors(num)

#Roman
def romanToInt(romanInput):
    roman ={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    total=0
    for i in range(len(romanInput)):
        current=roman[romanInput[i]]
        if i+1<len(romanInput):
            next_value=roman[romanInput[i+1]]
            if current<next_value:
                total=total+current
            else:
                total= total+current
        else:
            total=total+current
    return total
user_input=input("Enter a Roman Number:")
answer=romanToInt(user_input)
print("Integer value:",answer)