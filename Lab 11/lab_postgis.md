# Baza danych przestrzennych/PostGIS
Przestrzenna baza danych to baza danych zoptymalizowana pod kątem przechowywania i wykonywania zapytań dotyczących danych reprezentujących obiekty geometryczne. Większość baz danych przestrzennych umożliwia reprezentację prostych obiektów geometrycznych, takich jak punkty, linie i wielokąty. Niektóre bazy danych przestrzennych obsługują bardziej złożone struktury, takie jak obiekty 3D, pokrycia topologiczne, sieci liniowe itp.

Open Geospatial Consortium (OGC) opracowało specyfikację Simple Features (po raz pierwszy wydaną w 1997 r.) i wyznaczył standardy dodawania przestrzennej funkcjonalności do systemów baz danych. Standard SQL/MM Spatial ISO/IEC jest częścią standardu multimedialnego SQL/MM i rozszerza standard Simple Features.

### Przykładowa baza danych
Na zajęciach użyjemy bazy danych opisującej Nowy York [(data)](http://s3.cleverelephant.ca/postgis-workshop-2018.zip).

Zbiór ten zawiera publicznie dostępne informacje na temat:
- Bloki
- dzielnice
- ulice
- pod ziemią
- dane populacyjne.
	
### Utwórz bazę danych przestrzennych
Użytkownik i hasło do lokalnej bazy danych to *postgres*

1. Stwórz bazę danych przy pomocy psql lub PgAdmina z ustawieniami \([pomoc](https://www.postgresqltutorial.com/connect-to-postgresql-database/)\):
	- Baza danych: lab11_nyc
	- Właściciel: postgres


2. Otwórz w terminalu lab11_nyc

3. Dodaj rozszerzenie przestrzenne do tej bazy danych za pomocą zapytania:
``` sql
CREATE EXTENSION postgis;

```
4. Potwierdź, że PostGIS jest zainstalowany, uruchamiając funkcję PostGIS:

``` sql
select postgis_full_version();
```

Spodziewany wynik:
```
POSTGIS="3.1.1 3.1.1" [EXTENSION] PGSQL="120" GEOS="3.9.1-CAPI-1.14.1" PROJ="7.1.1" LIBXML="2.9.9" LIBJSON="0.12" LIBPROTOBUF="1.2.1" WAGYU="0.5.0 (inter)"
```

### Importuj dane przestrzenne do bazy danych

#### Ubuntu
1. 
```
export PGPASSWORD= haslo_do_bazy
```

2. Wczytanie pojedynczego pliku kształtu:
```
shp2pgsql \
  -D \
  -I \
  -s 26918 \
  nyc_census_blocks.shp \
  nyc_census_blocks \
  | psql -h localhost -d mydatabase -U postgres -p <port>
```

## Wyświetl dane geometryczne

### QGIS

QGIS to system informacji geograficznej o otwartym kodzie źródłowym. Projekt narodził się w maju 2002 roku i powstał jako projekt na SourceForge w czerwcu tego samego roku. Ciężko pracowaliśmy, aby oprogramowanie GIS (które jest tradycyjnie drogim oprogramowaniem własnościowym) było dostępne dla każdego, kto ma dostęp do komputera osobistego. QGIS działa obecnie na większości platform Unix, Windows i macOS. QGIS jest rozwijany przy użyciu zestawu narzędzi Qt (https://www.qt.io) i C++. Oznacza to, że QGIS jest zgryźliwy i ma przyjemny, łatwy w użyciu graficzny interfejs użytkownika (GUI).

QGIS ma być przyjaznym dla użytkownika systemem GIS, zapewniającym wspólne funkcje i cechy. Pierwotnym celem projektu było dostarczenie przeglądarki danych GIS. QGIS osiągnął punkt ewolucji, w którym jest używany do codziennych potrzeb przeglądania danych GIS, do przechwytywania danych, do zaawansowanej analizy GIS oraz do prezentacji w postaci wyrafinowanych map, atlasów i raportów. QGIS obsługuje bogactwo formatów danych rastrowych i wektorowych, a obsługa nowych formatów jest łatwa do dodania dzięki architekturze wtyczek.


## Ćwiczenia:

1. Ile rekordów znajduje się w tabeli nyc_streets?
2. Ile ulic w Nowym Jorku ma nazwy zaczynające się na „B”, „Q” i „M”?
3. Jaka jest populacja miasta Nowy Jork?
4. Jaka jest populacja Bronxu, Manhattanu i Queens?
5. Ile dzielnic ("neighborhoods") znajduje się w każdej gminie (borough)?

![terminal1](./1.PNG)
![terminal2](./2.PNG)
![qgis](./3.PNG)

## Odpowiedzi na ćwiczenia:
1. 19091
2. 2102
3. 8,17503e+06
4. 5,2016e+06e
5. Staten Island (24), The Bronx (24), Brooklyn (23), Queens (30), Manhattan (28)

# Materiały uzupełniające
1. [PostGIS workshops](https://postgis.net/workshops/postgis-intro/index.html)
2. [Qgis](https://qgis.org/pl/site/)