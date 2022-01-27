print('Welcome')
key = input('Please, give me a new password\n-->')
print('New password saved')
security = input('Can you tell me you password?\n-->')
if security == key:
    print('The pasword is correct!')
else:
    print('The password is wrong :(')