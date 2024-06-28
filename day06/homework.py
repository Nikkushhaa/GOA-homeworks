#1) მომხმარებელს შემოატანინეთ 4 სხავდასხვა რიცხვი და ამ ოთხივე რიცხვზე მოახდინეთ არითმეტიკური ოპერაციები. +,-,*,//,**
#2) დაწერეთ პროგრამა სადაც შემოიტანთ თქვენი ოჯახის წევრების ასაკს და გამოიტანეთ ის თუ რამდენი წლის იქნებიან 20 წლის შემდეგ.
#3) შექმენით ცვლადები სადაც შეინახავთ თქვენს თავზე ინფორმაციას (სახელი, გვარი, ასაკი, ქვეყანა, ქალაქი, საყვარელი ფერი, საყვარელი მანქანა, საყვარელი საჭმელი, საყვარელი სპორტი და ა.შ) შემდეგ შემოტანილი მნიშვნელობებით ააწყვეტ ერთი დიდი წინადადება.
#4)დაწერეთ მარტივი პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს თავისი სახელი და შემდეგ დაბეჭდოს მისალოცი შეტყობინება მათი სახელის გამოყენებით.


# დავალება N1

num1 = int(input('Enter first num: '))
num2 = int(input('Enter second num: '))
num3 = int(input('Enter third num: '))
num4 = int(input('Enter forth num: '))

print(num1 + num2 + num3 + num4)
print(num1 - num2 - num3 - num4)
print(num1 * num2 * num3 * num4)
print(num1 // num2 // num3 // num4)

#---------------------------------------------------------------------------

# დავალება N2

mom_age = int(input(" enter mom age: "))

after_20_years = mom_age + 20

print(" mom age after 20 years, will be  ", after_20_years) 


dad_age = int(input(" enter dad age: "))

after_30_years = dad_age + 30

print(" dad age after 30 years, will be  ", after_30_years) 



#-----------------------------------------------------------------------------

# დავალება N3 

name = input("enter ur name: ")
last_name = input("enter ur last name: ")
age  = input("enter ur age: ")
country  = input("enter ur country name : ")
car  = input("enter ur fav car: ")
sport = input("enter ur fav sport: ")

print(" hello my name is " + name + "my last name is " + last_name + "my age is "+ age + " my country name is " + country + "my fav car is " + car + " my fav sport is " + sport)


#-------------------------------------------------------------------------------
# დავალება N4

name = input("enter ur name: ")
print(name + " Happy Birthday <3333")
