
import math

#zadanie 1
r = 5
area = 3.14*r*r

tekst1 = "Pole kola o promieniu {:.2f} cm wynosi {:.2f} cm^2.".format(r, area)
print(tekst1)

#zadanie 2
lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse euismod augue in pretium faucibus. Curabitur ultrices luctus dui, nec malesuada urna viverra vitae."
words = len(lorem_ipsum.split())

sentences = lorem_ipsum.count(".")

#zadanie 3
ls = [1, 7.8, "d", 9, "e", 2, 3.162, 7, 4.55, "f", 0, 2.5]

sum_of_numbers = 0
for element in ls:
    if isinstance(element, (int, float)):
        sum_of_numbers += element

tekst = "Suma liczb wchodzących w skład listy wynosi {:.3f}".format(sum_of_numbers)
print(tekst)

#zadanie 4
shopping_list = {'Jabłko': 5,
'Ogórek': 2,
'Cebula': 3,
'Sałata': 1,
'Gruszka': 7,
'Ziemniak': 15,
'Arbuz': 1}

tekst = "Lista zakupów"
print(tekst)
for key, value in shopping_list.items():
    print(key, value)

n_fruits = 0
for key in shopping_list:
    if key == 'Jabłko' or key =='Gruszka' or key =='Arbuz':
        n_fruits+=shopping_list[key]
    
#zadanie 5
def compute_pi_leibniz(n):
    approx_pi = 0
    for k in range(n):
        approx_pi += 1 / ((4*k + 1) * (4*k + 3))
        
    approx_pi *= 8
    return approx_pi

def compute_pi_euler(n):
    approx_pi = 0
    for k in range(1,n):
        approx_pi+=1/(k**2)
    approx_pi*=6
    approx_pi = math.sqrt(approx_pi)
    return approx_pi

def compute_pi(n,schema):
    if schema == 'Leibniz':
        return compute_pi_leibniz(n)
    if schema == 'Euler':
        return compute_pi_euler(n)
    
tekst = compute_pi(100,"Leibniz")
print(tekst)

tekst1 = compute_pi(40,"Euler")
print(tekst1)

#zadanie 6
def bisection_root_search(x, epsilon=0.001):
    a = 0
    b = max(1, x)
    d = (a + b) / 2
    while abs(d**2 - x) > epsilon:
        if d**2 > x:
            b = d
        else:
            a = d
            d = (a + b) / 2
    return d

sqrt_25 = bisection_root_search(25)
sqrt_125 = bisection_root_search(125)
print("Pierwiastek z 25 wynosi w przybliżeniu {:.4f}.".format(sqrt_25))
print("Pierwiastek z 125 wynosi w przybliżeniu {:.4f}.".format(sqrt_125)) 
