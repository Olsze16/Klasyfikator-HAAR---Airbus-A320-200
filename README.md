# Klasyfikator HAAR - Airbus A320-200

<p align="center">
  <img src="/support_files/putlogo.png?raw=true" alt="PUT logo"/>
</p>

<p align="center">
<strong>[LO4] Tworzenie klasyfikatora HAAR</strong><br>realizacja na modelu: Airbus A320-200
</p>

<h2> Opis projektu</h2>
Niniejszy projekt zawiera pliki, oraz kody źródłowe potrzebne do wykonania klasyfikatora HAAR'o podobnego na przykładzie modelu: Airbus A320-200.

Projekt został wykonany w związku z realizacją zajęć laboratoryjnych w trybie zdalnym z przedmiotu Informatyka IV - Symulacja Komputerowa, pod patronatem Pana mgr. inż. Przemysława Siwka.

Celem projektu jest poznanie możliwości biblioteki OpenCV 3.4 do tworzenia klasyfikatorw HAAR'o podobnych, poprzez nabycie umiejętności w zakresie:
<ul>
<li> obsługi biblioteki OpenCV </li>
<li> tworzenia zbiorów uczących dla algorytmów integracji maszynowej </li>
<li> tworzenia klasyfikatorów HAAR'o podobnych </li>
</ul>

Ponadto, celem projektu jest kształtowanie właściwych postaw ugruntowania świadomości ważności i rozumienia pozatechnicznych aspektów i skutków działalności inżyniera i związaną z tym odpowiedzialność za podejmowane decyzje.

<h2> Przebieg realizacji projektu </h2>
<h3> Tworzenie wzorców negatywnych</h3>

Jednym z procesów przygotowania do uczenia maszynowego HAAR jest przygotowanie zbioru zdjęć negatywnych. Aby przygotować takowy zbirór, ze [strony internetowej](http://www.vision.caltech.edu/Image_Datasets/Caltech101 "download images") pobrano losowy zbiór zdjęć różnych kategorii, który zapisano w katalogu <strong>[./101_ObjectCategories](https://github.com/Olsze16/Klasyfikator-HAAR---Airbus-A320-200/tree/master/101_ObjectCategories)</strong>.

Do realizacji niniejszego projektu, z wyżej wymienionego katalogu losowo wybrano 3000 zdjęć, które następnie skonwertowano w odcienie szarości i przeskalowano do wartości 150x150 [px]. Losowo wybrane wzorce zostały zapisane w katalogu <strong>[./negatiive](https://github.com/Olsze16/Klasyfikator-HAAR---Airbus-A320-200/tree/master/negative).</strong>

Poniżej przedstawiono przykładowe, skonwertowane wzorce negatywne:
<p align="center">
  <img src="/negative/image2.jpg?raw=true" alt="Negative example 1"/>
  <img src="/negative/image10.jpg?raw=true" alt="Negative example 2"/>
</p>
<p align="center"><em>Pic. 1/2. Przykładowe wzorce negatywne</em></p>

W powyższym repozytorium załączono [kod źródłowy(HAAR.py)](https://github.com/Olsze16/Klasyfikator-HAAR---Airbus-A320-200/tree/master/HAAR.py) programu w języku Python, który dokonuje losowania dowolnych zdjęć z katalogu <strong>[./101_ObjectCategories](https://github.com/Olsze16/Klasyfikator-HAAR---Airbus-A320-200/tree/master/101_ObjectCategories)</strong>, odpowiednio je konwertuje i zapisuje do katalogu <strong>[./negatiive](https://github.com/Olsze16/Klasyfikator-HAAR---Airbus-A320-200/tree/master/negative).</strong>

Liczbę potrzebnych do wygenerowania negatwynych wzorów należy zmienić poprzez zmianę argumentu pętli while:

    while pic_num<3001: $- wygenerowanie 3000 wzorców
    while pic_num<2001: $- wygenerowanie 2000 wzorców

Aby zakończyć proces generowania negatwynych wzorców, należało stworzyć plik .txt, który przechowuje lokalizację wszystkich negatywnych wzorców porzebnych do uczenia maszynowego. Aby tego dokonać, w terminalu OS Ubuntu należało wpisać odpowiednią komendę:

    find ./negative -iname "*.jpg" > negatives.txt

<h3> Tworzenie wzorców pozytywnych (sztucznych)</h3>

Kolejnym procesem przygotowania do uczenia maszynowego HAAR jest przygotowanie zbioru zdjęć sztucznie pozytwynych. Aby przygotować takowy zbiór, należy zdefiniować obiekt uczenia maszynowego. W niniejszym przypadku obiektem jest samolot Airbus-A320-200, którego model 3D pobrano ze strony [sketchfab](https://sketchfab.com/3d-models/airbus-a320-200-lufthansa-d78fe1ede1f7483cb9fd7734d055b417 "Airbus-A320-200 3D Model").

Na podstawie modelu 3D, stworzono trzy obrazy obiekty w formacie .png (z usnięciem tła). Konwersję usuwania tła wykonano poprzez skorzystanie z gotowego narzędzia online, dostępnego pod linkiem: [https://www.remove.bg/](https://www.remove.bg/). Poniższe zrzuty przedstawiają wygenerowane obrazy w formacie .png.

<p align="center">
  <img src="/luft1.png?raw=true" alt="Wzorzec do uczenia"/>
  <img src="/luft2.png?raw=true" alt="Wzorzec do uczenia"/>
  <img src="/luft3.png?raw=true" alt="Wzorzec do uczenia"/>
</p>
<p align="center"><em>Pic. 3/4/5. Wygenerowane obrazy obiektu w formacie .png</em></p>


<h3> Konfiguracja uczenia mszynowego</h3>

<h3> Rezultat</h3>

<h2> Podsumowanie </h2>


