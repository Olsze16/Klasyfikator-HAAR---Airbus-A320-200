# Klasyfikator HAAR - Airbus A320-200

<p align="center">
  <img src="/support_files/putlogo.png?raw=true" alt="PUT logo"/>
</p>

<p align="center">
<strong>[LO4] Tworzenie klasyfikatora HAAR</strong><br>realizacja na modelu: Airbus A320-200
</p>
<p align ="right">
Autorzy: Kamil Olszewski,<br>Daniel Świątek
</p>

<h2> Opis projektu</h2>
Niniejszy projekt zawiera pliki, oraz kody źródłowe potrzebne do wykonania klasyfikatora HAAR'o podobnego na przykładzie modelu: Airbus A320-200.

Projekt został wykonany w związku z realizacją zajęć laboratoryjnych w trybie zdalnym z przedmiotu Informatyka IV - Symulacja Komputerowa, pod patronatem mgr. inż. Przemysława Siwka.

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

Powyżej przedstawione obrazy zostały zapisane w katalogu głównym projektu. Na podstawie tych obrazów zostały stworzone wzory stucznie pozytywne, które w późniejszym etapie zostały wykorzystane do procesu uczenia maszynowego.

Aby wygenerować wzory pozytywne, należy skorzystać z gotowej funkcji biblioteki opencv - [opencv_createsamples](https://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html). W tym przypadku stworzono 600 pozytywnych wzorców, które zapisano w katalogu <strong>[./info](https://github.com/Olsze16/Klasyfikator-HAAR---Airbus-A320-200/tree/master/info)</strong> wraz z plikiem tekstowym, który jest generowany jako element wyjściowy funkcji. Aby tego dokonać, w terminalu OS Ubuntu należało wpisać odpowiedni fragment kodu:

    opencv_createsamples -img luft3.png -bg negatives.txt -info info/info3.lst -pngoutput info -bgcolor 0 -bgtresh 8 -maxxangle 0.3 -maxyangle 0.3 -maxzangle 0.3 -num 200 -w 50 -h 25

Jako argumenty funkcji, zdefiniowano kolejno:
<ul>
<li><strong>-img</strong> - lokalizacja wzorca do uczenia,</li>
<li> <strong>-bg</strong> - lokalizacja pliku tekstowego, który przechowuje informację o wzorcach negatywnych, </li>
<li> <strong>-info</strong> - lokalizacja do zapisu pliku tekstowego z wzorcami pozytywnymi </li>
<li> <strong>-pngoutput</strong> - lokalizacja do zapisu wzorców pozytywnych </li>
<li> <strong>-bgcolor, -bgtrash, -max?angle, -num, -w, -h</strong> - parametry do wygenerowania pozytywnych wzorców. Szczegółowe informacje zawarte są w bibliotecę opencv.  </li>
</ul>

Dla każdego obrazu modelu 3D należało stworzyć po 200 pozytywnych wzorców, co łącznie wygenerowało 600 pozytywnych zdjęć dostępnych w katalogu [./info](https://github.com/Olsze16/Klasyfikator-HAAR---Airbus-A320-200/tree/master/info). Poniższe zrzuty ekranu przedstawiają przykładowo wygenerowane wzorce pozytywne:

<p align="center">
  <img src="/info/0001_0026_0034_0085_0042.jpg?raw=true" alt="Wzorzec pozytywny do uczenia"/>
  <img src="/info/0004_0026_0035_0098_0049.jpg?raw=true" alt="Wzorzec do uczenia"/>
</p>
<p align="center"><em>Pic. 6/7. Wygenerowane przykładowe wzorce pozytywne</em></p>


Po wygenerowaniu 600 pozytywnych wzorców, należało stworzyć wektor, który przechowa informację o lokalizacji pozytywnych wzorców i będzie podawany jako argument do wywołania funkcji uczenia maszynowego. Aby wygenerować wektor należało skorzystać z podstawowej funkcji biblioteki opencv - <strong>opencv_createsamples</strong>. Aby tego dokonać, w terminalu OS Ubuntu wpisano poniżej załączony fragment kodu:

    opencv_createsamples -info info/info1.lst -num 600 -w 50 -h 25 -vec pozytywne.vec

gdzie:

<ul>
<li><strong>-info</strong> - lokalizacja pliku tekstowego przechowującego dane o lokalizacji wzorców pozytywnych,</li>
<li> <strong>-num</strong> - liczba wzorców pozytywnych, </li>
<li> <strong>-w, -h</strong> - szerokość i wysokość modelu na wzorcu (proporcje),</li>
<li> <strong>-vec</strong> - lokalizacja do zapisania pliku z rozszerzeniem .vec (wektora).</li>
</ul>

W ten sposób utworzono plik .vec, który w następnym etapie zostanie użyty jako argument wejściowy do procesu uczenia maszynowego. Plik wektora (pozytywne.vec) powinien być zlokalizowany w katalogu głównym projektu.






<h3> Konfiguracja i uruchomienie uczenia maszynowego</h3>

Po przygotowaniu wyżej opisanych plików i katalogów, można było przystąpić do czasochłonnego procesu uczenia maszynowego. Aby rozpocząć uczenie maszynowe, należało skorzystać z funkcji dostępnej w bibliotece opencv- `opencv_traincascade`. Poniżej przestawiono fragment kodu, który użyto w niniejszym projekcie:

    opencv_traincascade -data ./data -vec pozytywne.vec -bg negatives.txt -numPos 600 -numNeg 3000 -numStages 13 -featuretype HAAR -minHitRate 0.996 -maxFalseAlarmRate 0.5 -w 50 -h 25

Jako argumenty funkcji, zdefiniowano kolejno:
<ul>
<li><strong>-data</strong> - wskazanie na katalog, w którym miejscu zostaną zapisane elementy wyjściowe funkcji (klasyfikator)</li>
<li> <strong>-vec</strong> - lokalizacja wcześniej przygotowanego pliku wektora z wzorcami pozytywnymi, </li>
<li> <strong>-bg</strong> - lokalizcja wcześniej przygotowanego pliku z informacją o lokalizacji wzorców negatywnych, </li>
<li> <strong>-numPos, -numNeg</strong> - odpowiednio: liczba wzorców pozytywnych, liczba wzorców negatywnych, </li>
<li> <strong>-numStages</strong> - liczba kroków do wykonania przez uczenie maszynowe opencv,  </li>
<li> <strong>-featuretype</strong> - typ uczenia maszynowego,  </li>
<li> <strong>-minHitRate</strong> - minimalna wartość HitRate dopuszczalna w procesie uczenia, </li>
<li> <strong>-maxFalseAlarmRate</strong> - maksymalna wartość False Alarm w procesie uczenia,  </li><li> <strong>-w, -h</strong> - szerokość i wysokość modelu na wzorcu (proporcje),</li>
</ul>

W przypadku opisywanego projektu, funkcja traincascade została uruchomiona w terminalu OS Ubuntu. Po kilkunastu godzinach pracy otrzymano pliki, które zostały zapisane w katalogu [./data](https://github.com/Olsze16/Klasyfikator-HAAR---Airbus-A320-200/tree/master/data). Sam klasyfikator (gotowy do użycia) został zapisany jako plik w formacie .xml - [cascade30.xml](https://github.com/Olsze16/Klasyfikator-HAAR---Airbus-A320-200/tree/master/data/cascade30.xml)


<h3> Rezultat</h3>

Aby sprawdzić poprawność działania klasyfikatora HAAR, skorzystaliśmy z gotowego kodu (Python) udostępnionego w ramach przeprowadzenia zajęć wykładowych przez Pana dr. Konrada Urbańskiego. Kod został zapisany w katalogu głównym projektu pod nazwą [testHAAR.py](https://github.com/Olsze16/Klasyfikator-HAAR---Airbus-A320-200/tree/master/testHAAR.py).

Jako zdjęcie testowe użyliśmy zrzutu ekranu z uczonym modelem 3D obiektu Airbus-A320-200. Klasyfikator poprawnie wskazał lokalizację obiektu, a program za pomocą użycia gotowych funkcji z biblioteki opencv narysował prostokąt na lokalizacji wykrytego obiektu. Poniżej załączono zrzut ekranu przedstawiający poprawnie działający program:


<p align="center">
  <img src="/support_files/result.jpg?raw=true" alt="HAAR result"/>
</p>
<p align="center"><em>Pic. 8. Rezultat uruchomionego programu z klasyfikatorem HAAR</em></p>


<h2> Literatura </h2>

<ol>
<li><strong>PRZEMYSŁAW SIWEK</strong> Materiały do zajęc laboratoryjnych - Tworzenie klasyfikatorów HAAR'o podobnych - Informatyka IV - Symulacja komputerowa
[online]. Pobrano: http://zsep.cie.put.poznan.pl/. </li>
<li><strong>DR KONRAD URBAŃSKI</strong> Materiały do zajęc wykładowych - klasyfikatory HAAR - Informatyka IV - Symulacja komputerowa
[online].  Pobrano: http://zsep.cie.put.poznan.pl/. </li>
<li> <strong>Logo PUT Poznań</strong>
[online]. Pobrano: http://put.poznan.pl/.</li>
<li><strong>Computational Vision at Caltech - Caltech 101</strong> [online]. Pobrano: 
http://www.vision.caltech.edu/Image_Datasets/Caltech101/.</li>
<li><strong>Sketchfab 3D Models</strong> [online]. Pobrano: 
https://sketchfab.com/search?q=aircraft&sort_by=-pertinence&type=models.</li>
<li><strong>Pythonprogramming.net HAAR cascade lesson</strong> [online] Pobrano: https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/</li>
<li><strong>Biblioteka opencv - HAAR cascade</strong> [online] Pobrano: https://docs.opencv.org/3.4/d7/d8b/tutorial_py_face_detection.html</li>
</ol>




