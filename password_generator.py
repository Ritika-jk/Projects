import random
import string

pass_len = 10
charValues = string.ascii_letters + string.digits+ string.punctuation

result = " "
for i in range(pass_len):
    result += random.choice(charValues)

print (" Your Random Password is: ",result)    
