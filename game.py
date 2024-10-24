"""
Gra Nim

Zasady gry:
1. Gra polega na naprzemiennym usuwaniu kamieni z jednego z kilku stosów.
2. Każdy gracz w swojej turze wybiera jeden stos i usuwa z niego dowolną liczbę kamieni (nie więcej niż jest dostępnych w stosie).
3. Gra kończy się, gdy wszystkie stosy są puste. Gracz, który ostatni wykona ruch, przegrywa.

Autor: Karol Szmajda

Instrukcja przygotowania środowiska:
- Aby uruchomić grę, potrzebujesz zainstalowanego Pythona w wersji 3.x.
- Aby uruchomić grę, wpisz `python game.py` w terminalu.

"""


import heapq

class Node:
    def __init__(self, state, cost, priority, parent=None):
        """
        Reprezentacja węzła w algorytmie A*.

        Parametry:
        - state: aktualny stan stosów
        - cost: koszt dojścia do tego węzła
        - priority: priorytet (f = g + h)
        - parent: wskaźnik na poprzedni węzeł (stan gry)
        """
        self.state = state
        self.cost = cost
        self.priority = priority
        self.parent = parent

    def __lt__(self, other):
        return self.priority < other.priority


class NimGame:
    """
    Klasa reprezentująca grę Nim.
    """

    def __init__(self, piles=(3, 4, 5)):
        """
        Inicjalizacja gry Nim z określoną liczbą stosów.

        Parametry:
        - piles: krotka określająca liczbę kamieni w każdym stosie
        """
        self.piles = list(piles)
        self.current_player = 1

    def display_piles(self):
        """ Wyświetla aktualny stan stosów. """
        print(f"Stosy: {self.piles}\r\n")

    def possible_moves(self):
        """ Zwraca wszystkie możliwe ruchy z bieżącego stanu gry. """
        moves = []
        for i, pile in enumerate(self.piles):
            for j in range(1, pile + 1):
                moves.append((i, j))  # (stos, liczba kamieni do usunięcia)
        return moves

    def make_move(self, pile, stones):
        """ Wykonuje ruch, usuwając kamienie z wybranego stosu. """
        if 0 <= pile < len(self.piles) and 0 < stones <= self.piles[pile]:
            self.piles[pile] -= stones
            return True
        else:
            return False

    def is_game_over(self):
        """ Sprawdza, czy gra się zakończyła (wszystkie stosy są puste). """
        return all(pile == 0 for pile in self.piles)

    def nim_sum(self, piles):
        """ 
        Oblicza sumę Nim (XOR) wszystkich stosów.
        
        Parametry:
        - piles: lista liczby kamieni w stosach

        Zwraca:
        - Wynik operacji XOR na stosach.
        """
        result = 0
        for pile in piles:
            result ^= pile
        return result

    def heuristic(self, piles):
        """
        Funkcja heurystyczna dla gry Nim.

        Parametry:
        - piles: lista stosów

        Zwraca:
        - Heurystyka, oceniająca stan gry na podstawie sumy Nim oraz liczby kamieni.
        """
        # Obliczamy sumę Nim
        nim_result = self.nim_sum(piles)

        # Jeśli suma Nim wynosi 0, jest to stan niekorzystny dla bieżącego gracza
        if nim_result == 0:
            return float('inf')  # Bardzo niekorzystna pozycja

        # W przeciwnym razie, im mniej kamieni, tym lepsza pozycja
        return sum(piles)  # Im mniej kamieni, tym bliżej końca gry

    def generate_successors(self, piles):
        """ Generuje wszystkie możliwe stany po wykonaniu ruchu. """
        successors = []
        for i, pile in enumerate(piles):
            for j in range(1, pile + 1):
                new_piles = piles[:]
                new_piles[i] -= j
                successors.append(new_piles)
        return successors

    def a_star_move(self):
        """ Implementacja algorytmu A* dla AI. """
        pq = []
        heapq.heapify(pq)

        initial_state = self.piles[:]

        initial_node = Node(state=initial_state, cost=0, priority=self.heuristic(initial_state))
        heapq.heappush(pq, initial_node)

        best_node = None
        last_node = None
        best_f_score = float('inf')

        while pq:
            current_node = heapq.heappop(pq)

            successors = self.generate_successors(current_node.state)
            for successor in successors:
                g_score = current_node.cost + 1  # Koszt ruchu
                h_score = self.heuristic(successor)
                f_score = g_score + h_score  # f(x) = g(x) + h(x)

                new_node = Node(state=successor, cost=g_score, priority=f_score, parent=current_node)

                if f_score < best_f_score:
                    best_f_score = f_score
                    best_node = new_node

                last_node = new_node
                
                heapq.heappush(pq, new_node)


        if best_node is not None:
            current = best_node
            path = []

            while current:
                path.append(current.state)
                current = current.parent

            path.reverse()

            best_move = path[1]
            self.piles = best_move
            return True

        # FIX
        self.piles = last_node.state
        
        return False

    def switch_player(self):
        """ Zmienia aktualnego gracza. """
        self.current_player = 1 if self.current_player == 2 else 2


if __name__ == "__main__":
    game = NimGame(piles=[4, 3, 5])

    while not game.is_game_over():
        game.display_piles()
        if game.current_player == 1:
            move = input("Player 1 move (ex. 1,2): ")
            try:
                pile, stones = map(int, move.split(","))
                if not game.make_move(pile - 1, stones):
                    print("Nieprawidłowy ruch! Spróbuj ponownie.")
                else:
                    game.switch_player()
            except ValueError:
                print("Nieprawidłowy format! Użyj formatu: stos,kamienie")
        else:
            print("AI move...")
            game.a_star_move()
            game.switch_player()

    print(f"Gracz {game.current_player} wygrywa!")
