import os 
x = input("Enter the file name: ")
try:
    os.rename(x, input("Enter the new file name: "))
    print("File is renamed")
except FileNotFoundError:
    print("File not found")