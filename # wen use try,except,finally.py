# wen use try,except,finally
try:
    # we try to to open the file :
    file=open("Goodmorning.txt")
    # readlines the goodmorning.txt file :
    print(file.readlines())
    file.close()
except FileNotFoundError :
    print("the file doesn't excist")
finally:
    print("finishing")