#Laboratorio 3.1.1.11
income = float(input("Introduce el ingreso anual:"))
impuesto = 0

if income <= 85528:
    tax = income * 0.18 -556.02
else:
    tax = 14839.02 + (income-85528)*0.32 
tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
