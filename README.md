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
<h3> Tworzenie zdjęc negatywnych</h3>

Jednym z procesów przygotowania do uczenia maszynowego HAAR jest przygotowanie zbioru zdjęć negatywnych. Aby przygotować takowy zbirór, ze [strony internetowej](http://www.vision.caltech.edu/Image_Datasets/Caltech101 "download images") pobrano losowy zbiór zdjęć różnych kategorii, który zapisano w katalogu <strong>./101_ObjectCategories</strong>.

Do realizacji niniejszego projektu, z wyżej wymienionego katalogu losowo wybrano 3000 zdjęć, które następnie skonwertowano w odcienie szarości i przeskalowano do wartości 150x150 [px]. Losowo wybrane wzorce zostały zapisane w katalogu <strong>./negative</strong>.

<h3> Tworzenie zdjęć pozytywnych</h3>

<h3> Konfiguracja uczenia mszynowego</h3>

<h3> Rezultat</h3>

<h2> Podsumowanie </h2>


