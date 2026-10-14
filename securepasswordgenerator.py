import random
#this lets use random-functions.

print('your password: ')
#gives a visual for the user's randomly generated password

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()£?'
#here I listed every single character that could be used on a keyboard in most passwords


password = ''
#here I created a blank string variable so we can fill it with a random password
for x in range(16):
    #this creates a for-loop which means we consistently run this code.
    password += random.choice(chars)
    #we've defined the password variable and then as it's in a loop it will generate random characters up to 16 until the loop breaks which has been defined at 16 characters.

print(password)