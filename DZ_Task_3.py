# Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.



import math 
 
print("Введите целое положительное число ") 
number = int(input()) 
palindrom_from_number = 0 
 
numbers = [] 
while number > 0:   #перевод числа в лист для сравнения 
    remainder = number % 10 
    numbers.append(remainder) 
    number = math.trunc(number / 10) 
 
while numbers != palindrom_from_number:  # условие :Если перевернутое число не равно исходному,  
                                         #то они складываются и проверяются на палиндром еще раз 
     
    palindrom_from_number = [] 
    size_number = len(numbers) 
    i = 1 
 
    while i < size_number+1: 
        palindrom_from_number.append(numbers[size_number -i]) 
        i = i + 1 
    if numbers == palindrom_from_number: 
 
        print(palindrom_from_number, "число - Палиндром") 
    else: 
         
        print(palindrom_from_number,"число не Палиндром") 
        i =0 
        number = [] 
        while i < size_number: 
            sum_numbers = numbers[i] + palindrom_from_number[i] 
            number.append(sum_numbers) 
            i = i +1 
        numbers = number










# while Copy_Namber != res:
#     Namber = Copy_Namber + res
#     print (Namber)
#     if Namber == res:
#         print ("Palindrom")


    

    