
from math import comb
from scipy.stats import binom, poisson

# Badania kliniczne wykazały, że prawdopodobieństwo wystąpienia komplikacji po wykonaniu pewnej operacji wynosi 5%.
#Oblicz prawdopodobieństwo, że w pewnym szpitalu więcej niż 6, ale mniej niż 13 operacji zakończy się sukcesem zanim po raz 3
# pojawią się pooperacyjne komplikacje.

# Rozkład ujemny dwumianowy (Pascala)

p = 0.95  # sukces
q = 1 - p  #porażka
r = 3  # liczba porażek

# Zakres sukcesów
k_values = range(7, 13)

probability = sum(comb(k + r - 1, r - 1) * (p ** k) * (q ** r) for k in k_values)
probability = round(probability, 4)

print(probability)

# W urnie znajdują się kule białe (9) i czarne (6).
# Losujemy kulę 7 razy, za każdym razem wrzucając ją z powrotem do urny.
# Jakie jest prawdopodobieństwo, że biała kula zostanie wyciągnięta nie mniej niż 4 razy?

# Rozkład dwumianowy Bernoulliego

p1 = 0.6 # prawdopodobienstwo wyciagniecia bialej kuli
n1 = 7 # liczba prób
k1 = 4 # minimalna liczba sukcesow

# obliczamy warunek przeciwny i odejmujemy od 1
probability1 = 1 - binom.cdf(k1 - 1, n1, p1)
probability1 = round(probability1, 4)

print(probability1)

# Rzucamy dwoma sześciennymi kostkami do gry.
# Oblicz prawdopodobieństwo, że suma wyrzuconych 
# oczek przyjmie wartość nie więcej niż 4 lub nie mniej niż 7.

# musimy obliczyc prawdopodobienstwo, że wylosuje 1-3 oraz 7-12 i dodajemy te prawdopodobienstwa

n3 = 36
probability3 = sum(1 for x in range(1,7) for y in range(1,7) if (x+y) <= 4 or (x+y) >= 7)/n3
probability3 = round(probability3, 4)
print(probability3)

# Średnia liczba telefonów do działu obsługi klienta pewnej firmy wynosi 12
# na godzinę.
# Oblicz prawdopodobieństwo, że w ciągu godziny wykonanych zostanie mniej niż 15 telefonów.

# Rozkład Poissona

k4 = 14 # mniej niż 15
lambda4 = 12

probability4 = poisson.cdf(k4, lambda4)
probability4 = round(probability4, 4)
print(probability4)