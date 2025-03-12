
#definiowanie macierzy
ar1 = np.array([[5,3,6,4],[1,7,4,1],[9,2,8,5]])

#macierz zerowa
ar2 = np.zeros_like(ar1)

#macierz zawierajaca liczby od 0 do 100 z krokiem 20
ar3 = np.arange(0, 101, 20)

#transpozycja
ar4 = np.atleast_2d(ar3).T

#iloczyn
ar5 = ar3*ar4

#zmienienie wymiaru
ar6 = np.reshape(ar5,(12,3))

#Korzystajac z funkcji np.zeros() zdefiniuj macierz
#zerowa o wymiarach 7x5. Dodaj 10 do wszystkich elementow
#macierzy, dodaj do kolumne 1,2,3,2,1,4. Odejmij od wierszy
#3,2,1,0,1,2,3

ar7 = np.zeros((7,5))
ar7+=10
ar7+=[1,2,3,2,1]
ar7-=np.array([3,2,1,0,1,2,3]).reshape(-1,1)

#reshape zmienie ksztalt tablicy na kolumnowy

#tworzenie wykresu
fig, ax = plt.subplots(figsize=(10, 10))
#fig - obszar na ktorym mozna umieszczac elementy
#tj wykresy, paski kolorow (okno do rysowania)
#ax - obszar na ktorym rysujemy konkretny wykres
#figsize - tworzy figure i osie, szer i wys w calach

im = plt.imshow(ar7, cmap="viridis")
#im - zmienna do ktorej przypisywany jest obiekt
#funkcja uzywana min do wysw heatmaps, mapuje argument kolorem

cbar = plt.colorbar(im, ax=ax)
#cbar - przypisanie wyniki do zmiennej, mozna modyfikowac pasek kolorow
#ax - parametr okreslajacy os wykresu

ax.set_title("Rozkład wartości macierzy ar7")
plt.show()

#Zdefiniuj macierz zerowa o wymiarach 10x10
#Dodaj 1 do elementow znajdujacych sie w trzeciej kolumnnie macierzy. 
#Dodaj 1 do elementow znajdujacych sie w trzeciem od konca wierszu macierzy.
# Dodaj 3 do elementow, ktore jednoczesnie znajduja sie w 2-6 wierszu i 5-9 kolumnie macierzy.
ar8 = np.zeros((10,10))
ar8[:,2]+=1
ar8[-3,:]+=1
ar8[1:6,4:9]+=3

#wykres
fig, ax = plt.subplots(figsize=(12,10))
sns.heatmap(ar8,cmap="viridis", ax=ax)
plt.title("Rozkład wartości w macierzy ar8")
plt.show()

ar9 = np.full((5,3),6)
ar10 = np.full((5,3),11)
#full - wypelnia dana liczba w konkretnnych wymiarach

ar11 = np.hstack((ar9,ar10))
print(ar11)
#hstack - laczenie wzdluz osi kolumn

ar12 = np.vstack((ar9,ar10))
print(ar12)
#vstack - laczenie wzdloz wierszy

x = np.linspace(0,2*np.pi, 100)
#linspace - generuje rowno rozmieszczone wartosci w przedziale
#0 - pierwszy argument przedzialu
#2pi - koncowa wartosc
#100 - ilosc punktow

y = x**2*np.sin(x)

df1 = pd.DataFrame({"X":x,"Y":y})
#pd - funkcja biblioteki pandas, tworzenie struktury danych
#wewnatrz podajemy slownik

print("Początek DataFrame:")
print(df1.head())
print("Koniec DataFrame:")
print(df1.tail())
#automatycznie head zwraca 5 pierwszych, a tail 5 ostatnich
#wierszy, chyba ze podamy argument

print("Statystyczne podsumowanie:")
print(df1.describe())

#wykresy

fig, axes = plt.subplots(nrows=2,ncols=1,figsize=(15,10))
#plt.subplots - bibl Matplotiv do tworzenia wielu wykresow w 1 obsz
#obszar ma wym 2x1

axes[0].plot(df1["X"],df1["Y"],label = "y = x^2*sin(x)",
            color="blue", linestyle="-",linewidth=2)
#0 odnosi sie do pierwszego wykresu, X,Y to nazwy kolumn z ktorych
#pobieramy dane, label to etykieta/legenda tego wykresu

axes[0].set_title("Wykres liniowy")
axes[0].set_xlabel("X")
axes[0].set_ylabel("Y")
axes[0].legend()
axes[0].grid(True)
#dostosowanie parametrow

#drugi wykres
sns.lineplot(x="X", y="Y", data=df1, ax=axes[1], label="y = x^2 * sin(x)",
color="green", linewidth=2)
axes[1].set_title("Wykres seaborn")
axes[1].set_xlabel("X")
axes[1].set_ylabel("Y")
axes[1].legend()
axes[1].grid(True)

plt.subplots_adjust(hspace=0.4)
#hspace - odstep miedzy wykresami
plt.show() 