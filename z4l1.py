def znajdz_min_wartosc(tablica):
    min_value = tablica[0]
    for i in range(1, len(tablica)):
        if tablica[i] < min_value:
            min_value = tablica[i]
    return min_value