from sympy import *
from cmath import sqrt

x = symbols('x')

def derivative_function(f):
    return diff(f, x)

user_input = input("Parašykite funkcija: ")
f = parse_expr(user_input)

derivative_f = derivative_function(f)
print("Funkcijos išvestinė: ", derivative_f)

x0 = float(input("Įveskite x0 reikšmę: "))

result = derivative_f.subs(x, x0)
print("Išvestinės reikšmė taške x0: ", result)

try:
    elasticity = abs(derivative_f.subs(x, x0)*x0/f.subs(x,x0))
    print("Elastiškumas pakeitus vienu procentu turimam taške x0: %g" % elasticity)
except Exception as e:    
    print("Nepavykos suskaičiuoti elastiškumo")


try:

    percentage_change = ((derivative_f.subs(x, x0)/f.subs(x,x0))*100)
    print("Procentinis funkcijos kitimo greitis procentais: %g%%" % percentage_change)
except Exception as e:

    print("Nepavykos suskaičiuoti elastiškumo")

