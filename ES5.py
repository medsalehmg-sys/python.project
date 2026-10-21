# code :
# creation prixTHx the price before tax :
# except
# we use try/
try:
  prixTH=int(input("Enter the price before tax"))
  prixTTC=prixTH+prixTH*0.2
  print(prixTTC)
  break
except ValueError:
  print("Warning ?,you should to Enter a number")

