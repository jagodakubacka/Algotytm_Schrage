s = []  # Moment rozpoczęcia
c = []  # Moment zakończeni
r = []  # Termin dostępności
p = []  # Czas wykonania
q = []  # Czas dostarczenia

A = []  # Tablica poomocnicza do odczytu danych
n = 0

N = []  # Tablica zadń oraz r
P = []  # Tablica zadń oraz p
G_0 = []  # Tablica zadń oraz q
G = []  # Tablica gotowych zadań


C = []  # Tablica momentów wykonań
D = []  # Tablica momentów dostarczeń


def wczytaj(plik):
    f = open(plik, "r")
    global n
    for i in f:
        A.append(i)  # Przypisanie danych z pliku
    n = int(A[0])
    for x in range(len(A)):
        if x > 0:
            B = A[x].split()
            r.append(int(B[0]))  # Termin dostępności
            p.append(int(B[1]))  # Czas wykonania
            q.append(int(B[2]))  # Czas dostarczenia

    for x in range(n):
        a = (r[x], x)
        N.append(a)

    for x in range(n):
        a = (q[x], x)
        G_0.append(a)

    for x in range(n):
        a = (p[x], x)
        P.append(a)

# te wszystkie tablice zostały utworzone, aby móc dostac się bez problemu do r,p,q

# Stworzenie zbioru N -> rosnące r
def Sort_N():
    N.sort()

# Stworzenie zbioru N -> malejące q
def Sort_G():
    G.sort(reverse=True)


def Schrage():
    Sort_N()
    Pi = []
    C_max = 0 # Maksymalny z terminów dostarczenia zadń
    t = 0
    while len(G) != 0 or len(N) != 0:
        while len(N) != 0 and N[0][0] <= t:  # N[0][0] to r pierwszego elementu (o ineksie 0)
            x = N[0][1]  # index zadania o najmniejszym r
            e = (G_0[x][0], x)  # x -> ineks zadanie o najmniejszym r; G_0[x][0] -> q tego zadania
            G.append(e)  # Dodanie powyższego elementu do zbioru zadan gotowych
            N.pop(0)  # Usunięcie elementu ze zbioru zadań niegotowych
        if len(G) == 0:
            t = N[0][0]
        else:
            Sort_G()  # Sortowanie G -> Malejące Q
            e = G[0][1]  # index zadania o największym q (jest to element o indeksie 0)
            G.pop(0)  # Usuwanie 1 elementu
            Pi.append(e)  # kolejność wykonywanych zadań
            t = t + P[e][0]  # Aktualizacja czasu
            C.append(t)  # moment zakończenia wykonywania zadania i
            D.append(t + G_0[e][0])  # moment dostarczenia zadania i
            D_max = max(C_max, t + G_0[e][0])  # Wyznaczenie maksymalnego terminu dostarczenia
    return D_max


def main():
    wczytaj("SCHRAGE1.DAT")
    print(Schrage())


main()
