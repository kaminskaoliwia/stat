# Funkcja gęstości prawdopodobieństwa średnicy D pewnego elementu schodzącego
# z linii produkcyjnej podanej w milimetrach dana jest wzorem:
# P(D=d)={3/4⋅(1−(d−100)2) dla 99≤ d ≤101 
# 0 w pozostałych przypadkach
# Jakie jest prawdopodobieństwo, że losowo wybrany element będzie miał 
# nie więcej niż 99.5 mm średnicy.

import sympy as sp
from scipy.stats import poisson, norm

# Zmienna jako symbol
d = sp.symbols('d')

# Funkcja gęstości prawdopodobieństwa
pdf = (3/4) * (1 - (d - 100)**2)

# Obliczenie całki
probability = sp.integrate(pdf, (d, 99, 99.5))

probability = round(probability, 4)
print(probability)

# Oczekiwana liczba defektów kabla wynosi 0.02 defektów na metr długości kabla.
# Jakie jest prawdopodobieństwo, że 7. defekt 
# zostanie znaleziony na nie mniej niż 250 metrze sprawdzanego kabla?

# Rozklad Poissona

lambda1 = 0.02
kabel = 250
k1 = lambda1*kabel # ilosc zdarzen

probability1 = (poisson.cdf(6, k1))
probability1 = round(probability1, 4)
print(probability1)

# Wzrost pewnej grupy ludzi podany w centymetrach jest dany rozkładem normalnym o wartości oczekiwanej 164
# i odchyleniu standardowym 5.
# Jakie jest prawdopodobieństwo, że losowo wybrana osoba z tej grupy będzie miała więcej niż 153, ale mniej niż 165 cm wzrostu?

wo2 = 164
sd2 = 5

# co najmniej 153, najwyżej 165
probability2 = norm.cdf(165, wo2, sd2) - norm.cdf(153, wo2, sd2)

probability2 = round(probability2, 4)
print(probability2)