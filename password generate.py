import strings
import random
#characters to generte password form
alphabets=list(string.ascii_letters)
digits=list(string.digits)
special_characters=list("!@$%^&*()")
characters=list(string.ascii-letters+string.digits+string+"@$%^&*()")
def generate_random_password():
length=int(input("enter the password length :"))
#numbe ros character types
alphabets_count=int(input("enter the alphabets count in password :"))
digits_count=int(input("enter the digits count on the password :"))
special_character_count=int(input("enter the special character count in password :")
character_count=alphabets_count+digits_count+special_character_count
#check the tatal length with the character count
#print not valid if the sum is greater then length
if character_count>length:
print("character total count is greater then the password length")
return
#intializing the password
password=[]
#picking the random alphabets
for i in range(alphabets_count):
password.append(random.choice(alphabets))
#pickking random digits
for i in range(digits_count):
password.append(random.choice(digits))
#picking special characters
for i in range(special_character_count):
password.append(random.choice(special_characters))
#if the total cahracters count is less than the password length
if characters_count<length:
random.shuffle(characters)
for i in range(lenth_characters_count)
password.append(random.choice(characters))
#shuffling the resultant password
random.shuffle(password)
#converting the list to arrays
print(""join(password))
generate_random_password()