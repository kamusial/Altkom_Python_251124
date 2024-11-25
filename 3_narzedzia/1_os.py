import os
import time

print(os.environ['PATH'])
print(os.environ['OS'])

print(os.getcwd())
# os.chdir(r'C:\Users\Student\Desktop')
os.chdir('C:\\Users\\Student\\Desktop')
print(os.getcwd())

try:
    os.mkdir('test')
except FileExistsError:
    pass
time.sleep(2)
os.rename('test', 'test2')
time.sleep(2)
os.rmdir('test2')
time.sleep(2)
os.system('cmd /c "cd C:/Users/Student/Desktop/Altkom_Python_251124 && dir >> text.txt"')
os.system('cmd /c "dir"')
data = os.walk('C:/Users/Student/Desktop')
print(list(data))

with open('C://Users//Student//Desktop//Altkom_Python_251124//text.txt', 'r') as f:
    content = f.readlines()
print(content)