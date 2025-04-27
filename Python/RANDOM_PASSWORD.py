
#---------------------------------RANDOM PASSWORD GENERATOR------------------------------------------

import random
import string
charValues=string.ascii_letters + string.digits + string.punctuation

#----- METHOD 1-----
# password=""
# for i in range (12):
#     password+=(random.choice(charValues))
# print(password)

#------METHOD 2-------
# LIST COMPREHENSION

password="".join([random.choice(charValues) for i in range (12)])
print("YOUR PASSWORD IS :",password)
