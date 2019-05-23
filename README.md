Projekt zawiera przypadki testujące stronę dedykowaną ćwiczeniom testów automatycznych: https://www.phptravels.net/.

**Uwaga do przypadku `test_password_change()` w pliku `test_account.py`:**
Przypadek, który przeszedł pozytywnie zmienia hasło z _demouser_ na _demouser123_, wobec czego `test_login()` z użyciem hasła _demouser_ nie będzie już działał.