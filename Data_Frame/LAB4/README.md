<h1>LAB - S03-L004 - Dodawanie i usuwanie kolumn</h1>
<h3>1. Zaimportuj moduł pandas i nadaj mu standardowy alias. Do zmiennej fuel wczytaj zawartość pliku fuel.csv. Podczas wczytywania skorzystaj z dodatkowego argumentu low_memory=False, pobierz tylko następujące kolumny: 'Vehicle ID','Year','Make','Model','Class','Fuel Type','Combined MPG (FT1)'. Wyświetl nagłówek tak utworzonego Data Frame</h3>
<h3>2. Kolumna 'Combined MPG (FT1)' zawiera informację o tym ile mil można przejechać na jednym galonie paliwa. My chcemy zobaczyć ile kilometrów można przejechać na jednym litrze. 1 mila = 1.609 km. 1 galon = 3.78 litra. Dodaj do obiektu fuel nową kolumnę o nazwie 'Combined KPL', która wyzanczona będzie wzorem 'Combined MPG (FT1)' * 1.609 / 3.78</h3>
<h3>3. Upewnij się, że kolumna została dodana wyświetlając nagłówek obiektu fuel</h3>
<h3>4.Dodaj do obiektu fuel na 5-tej pozycji (liczymy od zera) kolumnę nazwaną 'liters per km', która dla każdego
samochodu wyznaczy spalanie w litrach na 100 km. Skorzystaj ze wzoru 100 / 'Combined KPL'</h3>
<h3>5. Upewnij się, że kolumna została dodana wyświetlając nagłówek obiektu fuel</h3>
<h3>6. Znasz dwie metody na usuwanie kolumn. Wybraną przez siebie metodą usuń kolumnę 'Combined MPG
(FT1)'</h3>
<h3>7. Upewnij się, że kolumna została usunięta wyświetlając nagłówek
</h3>
<h3>8.Korzystając z innej niż w pkt. 6 metody usuń również kolumnę Combined KPL</h3>
<h3>9. Upewnij się, że kolumna została usunięta wyświetlając nagłówek
</h3>

