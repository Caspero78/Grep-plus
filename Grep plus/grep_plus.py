# Definiujemy funkcję grep_plus, która przyjmuje cztery argumenty: napis file, napis searched_string, liczbę number_before_line i liczbę number_after_line
# Funkcja ta ma za zadanie znaleźć linię w pliku, która zawiera podany ciąg znaków, i wyświetlić ją wraz z określoną liczbą linii przed i po niej
def grep_plus(file, searched_string, number_before_line, number_after_line):
    # Próbujemy wykonać następujący blok kodu
    try:
        # Otwieramy plik o nazwie file w trybie odczytu i przypisujemy go do zmiennej file
        with open(file, 'r') as file:
            # Tworzymy listę lines, która zawiera wszystkie linie z pliku
            lines = file.readlines()

            # Dla każdej pary (i, line), gdzie i jest liczbą od 0 do długości listy lines, a line jest elementem listy lines o indeksie i
            for i, line in enumerate(lines):
                # Jeśli napis searched_string znajduje się w napisie line
                if searched_string in line:
                    # Jeśli zmienna i jest mniejsza od zmiennej number_before_line i długość listy lines pomniejszona o i i 1 jest mniejsza od zmiennej number_after_line
                    if i < number_before_line and len(lines) - i - 1 < number_after_line:
                        # Wyświetlamy komunikat o błędzie, że podano za dużą liczbę linii do wyświetlenia przed i po znalezionej linii
                        print("BŁĄD: Podano za dużą liczbe linii do wyświetlenia przed i po znalezionej linii.\n")
                        # Przerywamy działanie funkcji i zwracamy wartość None
                        return
                    # W przeciwnym razie, jeśli zmienna i jest mniejsza od zmiennej number_before_line
                    elif i < number_before_line:
                        # Wyświetlamy komunikat o błędzie, że podano za dużą liczbę linii do wyświetlenia przed znalezioną linią
                        print("BŁĄD: Podano za dużą liczbe lini do wyswietlenia przed znalezioną linią.\n")
                        # Przerywamy działanie funkcji i zwracamy wartość None
                        return
                    # W przeciwnym razie, jeśli długość listy lines pomniejszona o i i 1 jest mniejsza od zmiennej number_after_line
                    elif len(lines) - 1 - i < number_after_line:
                        # Wyświetlamy komunikat o błędzie, że podano za dużą liczbę linii do wyświetlenia po znalezionej linii
                        print("BŁĄD: Podano za dużą liczbe lini do wyswietlenia po znalezionej lini.\n")
                        # Przerywamy działanie funkcji i zwracamy wartość None
                        return

                    # Wyświetlamy napis z informacją o linii z szukanym ciągiem, podając jej numer i zawartość
                    print(f"Linia z szukanym ciągiem: \nNumer lini: {i + 1}, zawartość lini: \"{line.strip()}\"")
                    # Wyświetlamy napis z informacją o liniach przed znalezioną linią
                    print("\nLinie przed znalezioną linią:")

                    # Tworzymy zmienną max_before_line i przypisujemy jej wartość zmiennej i pomniejszoną o zmienną number_before_line
                    max_before_line = i - number_before_line
                    # Tworzymy zmienną max_after_line i przypisujemy jej wartość zmiennej i powiększoną o zmienną number_after_line
                    max_after_line = i + number_after_line

                    # Jeśli zmienna number_before_line jest równa 0
                    if(number_before_line == 0):
                        # Wyświetlamy napis, że nie wybrano linii do wyświetlenia
                        print("- Nie wybrano lini do wyświetlenia")
                    # W przeciwnym razie
                    else:
                        # Dla każdej liczby j od zmiennej max_before_line do zmiennej i
                        for j in range(max_before_line, i):
                            # Wyświetlamy napis z informacją o linii, podając jej numer i zawartość
                            print(f"- Numer lini: {j + 1}, zawartość lini: \"{lines[j].strip()}\"")

                    # Wyświetlamy napis z informacją o liniach po znalezionej lini
                    print("\nLinie po znalezionej lini:")
                    # Jeśli zmienna number_after_line jest równa 0
                    if(number_after_line == 0):
                        # Wyświetlamy napis, że nie wybrano linii do wyświetlenia
                        print("- Nie wybrano lini do wyświetlenia")
                    # W przeciwnym razie
                    else:
                        # Dla każdej liczby j od zmiennej i + 1 do zmiennej max_after_line + 1
                        for j in range(i + 1, max_after_line + 1):
                            # Wyświetlamy napis z informacją o linii, podając jej numer i zawartość
                            print(f"- Numer lini: {j + 1}, zawartość lini: \"{lines[j].strip()}\"")

                    # Przerywamy pętlę for, ponieważ znaleźliśmy linię z szukanym ciągiem
                    break
            # Jeśli pętla for się zakończyła, a nie znaleźliśmy linii z szukanym ciągiem
            else:
                # Wyświetlamy napis, że nie znaleziono linii zawierającej ciąg znaków
                print(f"Nie znaleziono linii zawierającej ciąg znaków: {searched_string}")

    # Jeśli wystąpi błąd FileNotFoundError, czyli gdy plik o nazwie file nie istnieje
    except FileNotFoundError:
        # Wyświetlamy napis, że plik nie istnieje
        print(f"Plik {file} nie istnieje.")

# Wywołujemy funkcję grep_plus z argumentami: 'plik.txt', 'asd', 2, 2
grep_plus('plik.txt', 'asd', 2, 2)