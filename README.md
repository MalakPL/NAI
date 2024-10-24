# Nim Game (A* Algorithm)

## Opis

**Nim** to klasyczna gra logiczna dla dwóch graczy. W tej implementacji, jeden z graczy to **AI**, które korzysta z **algorytmu A***, aby znaleźć optymalny ruch, prowadzący do wygranej.

Gracze wykonują ruchy naprzemiennie. Każdy ruch polega na wybraniu jednego stosu kamieni i usunięciu z niego dowolnej liczby kamieni (co najmniej jednego). Przegrywa ten, kto zmuszony jest wziąć ostatni kamień.

Algorytm **A*** w tej implementacji przeszukuje wszystkie możliwe stany gry i wybiera najlepszy ruch na podstawie heurystyki opartej na **suma Nim** (XOR wszystkich stosów), co pozwala AI minimalizować ryzyko porażki.

## Wymagania

Do uruchomienia tego programu potrzebujesz:
- **Python 3.7** lub nowszy

## Instalacja

Aby uruchomić projekt lokalnie, postępuj zgodnie z poniższymi krokami:

1. **Sklonuj repozytorium**:
   ```bash
   git clone https://github.com/MalakPL/NAI.git
   cd NAI
   python game.py
   ```

Przykład gry: 
```bash
python .\game.py  
Stosy: [3, 4, 5]

Player move (ex. 1,2): 3,1
Stosy: [3, 4, 4]

AI move...
Stosy: [3, 0, 4]

Player move (ex. 1,2): 1,2
Stosy: [1, 0, 4]

AI move...
Stosy: [1, 0, 0]

Player move (ex. 1,2): 1,1
Gracz 2 wygrywa!
```
