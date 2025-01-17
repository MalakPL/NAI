# Wirtualne Piano: Granie za pomocą gestów

## Opis projektu
Wirtualne Piano, aplikacja wykorzystująca kamerę internetową oraz bibliotekę MediaPipe do rozpoznawania dłoni i gestów w czasie rzeczywistym. Dzięki mapowaniu pozycji końcówek palców na klawisze pianina projekt umożliwia generowanie dźwięków MIDI. Dodatkowo aplikacja zawiera kod umożliwiający nagrywanie obrazu oraz wciśniętych klawiszy z podłączonego urządzenia MIDI, co może być wykorzystane do analizy, treningu lub tworzenia danych do uczenia maszynowego.

## Funkcjonalności
Rozpoznawanie dłoni i końcówek palców w czasie rzeczywistym za pomocą MediaPipe.
Mapowanie pozycji końcówek palców na klawisze pianina (wektor 128 stanów).
Generowanie dźwięków MIDI odpowiadających aktywnym klawiszom.
Wizualizacja aktywnych klawiszy na obrazie z kamery.
Możliwość nagrywania obrazu z kamery oraz danych o wciśniętych klawiszach z podłączonego urządzenia MIDI.
Solidna podstawa do stworzenia wirtualnego pianina sterowanego gestami.
Macierz odległości dla każdej z dłoni, co pomaga w detekcji gestów lub jako features do modelu AI.

Autor: Karol Szmajda

### Demo
![Demo Video](x.gif)
