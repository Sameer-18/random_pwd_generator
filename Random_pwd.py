import random
passlen=int(input("Enter the length of password"))
s="QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm01234567890!@#$%^&*()"
pwd="".join(random.sample(s,passlen))
print(pwd)
