import os
while True:
    os.system("pip install --upgrade pip")
    os.system("clear")
    name = input("Library name you want to download :  ")
    os.system(f"pip install {name}")
    print("")
    print("Complate")
    input("")
