Twoim zadaniem jest stworzenie prostego systemu konfiguracyjnego dla aplikacji, który będzie wykorzystywał wzorce
projektowe: Singleton, Fabrykę Abstrakcyjną oraz Budowniczego. System ma pozwalać na łatwą zmianę i dostęp do
ustawień aplikacji.

1. Singleton: Użyj wzorca Singleton do stworzenia klasy Configuration, która przechowuje ustawienia aplikacji
w formie słownika. Klasa ta powinna zapewniać globalny punkt dostępu do konfiguracji.
2. Fabryka Abstrakcyjna: Stwórz fabrykę abstrakcyjną ConfigFactory z metodą create_config(), która
zwraca instancję Configuration. Następnie, implementuj konkretne fabryki dla różnych środowisk (np.
deweloperskiego, testowego i produkcyjnego), które dostosowują konfigurację do danych warunków.
3. Budowniczy: Zaimplementuj wzorzec Budowniczego, aby umożliwić stopniowe tworzenie skomplikowanych
obiektów konfiguracyjnych. Budowniczy powinien dostarczać metody do definiowania poszczególnych ustawień
konfiguracyjnych, np. połączenia z bazą danych, ścieżek dostępu, itp.
4. W zadaniu umieść plik test_flow.py który będzie zawierał kod testujący poprawność działania systemu
konfiguracyjnego. Kod ten ma sprawdzać, czy konfiguracja jest poprawnie tworzona i dostosowywana do różnych
środowisk. Nie muszą to być testy jednostkowe, ale kod, który demonstruje działanie systemu.
