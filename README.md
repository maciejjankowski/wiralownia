# 🚀 Wiralownia - Wzorce Wiralowych Postów z piszemywirale.pl

Kompletna biblioteka 127 wzorców wiralowych postów bezpośrednio z piszemywirale.pl, z szczegółowymi wyjaśnieniami psychologicznymi i algorytmicznymi.

## 📚 Co znajdziesz w tym repozytorium?

### 127 Wzorców Postów z piszemywirale.pl

Każdy wzorzec zawiera:
- ✅ **Typ posta** - szczegółowy opis wzorca i jego siły
- ✅ **Dlaczego działa** - wyjaśnienie psychologiczne i algorytmiczne
- ✅ ID i numer dla łatwego odnajdywania

Wszystkie wzorce pochodzą bezpośrednio z serwisu piszemywirale.pl i zawierają profesjonalne analizy dotyczące:
- **Psychologii** - dlaczego użytkownicy reagują na ten typ treści
- **Algorytmu** - jak platformy (zwłaszcza LinkedIn) promują te posty

## 📖 Pliki w repozytorium

### 1. [post-types.json](post-types.json)
Struktura JSON zawierająca wszystkie 127 wzorców - idealna do:
- Integracji z aplikacjami
- Programowego dostępu
- Budowania narzędzi AI
- Automatyzacji tworzenia treści

### 2. [browser.py](browser.py)
Interaktywna przeglądarka CLI umożliwiająca:
- Przeglądanie wszystkich wzorców
- Wyszukiwanie po słowach kluczowych
- Wyświetlanie szczegółowych informacji
- Tryb interaktywny lub komendy CLI

### 3. [example_usage.py](example_usage.py)
Przykłady programowego dostępu pokazujące:
- Jak załadować i używać danych JSON
- Wyszukiwanie wzorców
- Filtrowanie po słowach kluczowych
- Statystyki biblioteki

## 🚀 Jak używać?

### Metoda 1: Przeglądarka CLI (Rekomendowane)

```bash
# Tryb interaktywny
python3 browser.py

# Lista wszystkich wzorców
python3 browser.py list

# Szukaj wzorców po słowie kluczowym
python3 browser.py search humor
python3 browser.py search vulnerability
python3 browser.py search algorytm

# Pokaż szczegóły konkretnego wzorca (po numerze)
python3 browser.py show 1
python3 browser.py show 42

# Statystyki
python3 browser.py stats
```

### Metoda 2: Programowy dostęp (Python)

```python
import json

# Załaduj wzorce
with open('post-types.json', 'r') as f:
    data = json.load(f)

# Znajdź wzorzec po numerze
wzorzec = next(w for w in data['postTypes'] if w['number'] == 1)
print(wzorzec['type'])
print(wzorzec['why'])

# Szukaj wzorców zawierających słowo
humor_posts = [w for w in data['postTypes'] 
               if 'humor' in w['type'].lower() or 'humor' in w['why'].lower()]
print(f"Znaleziono {len(humor_posts)} wzorców z humorem")
```

### Metoda 3: Bezpośredni dostęp do JSON

Możesz bezpośrednio przeglądać plik `post-types.json` w dowolnym edytorze lub narzędziu obsługującym JSON.

## 💡 Przykłady wzorców

### Wzorzec #1: Historia relatable
Post oparty na krótkiej, autentycznej i często humorystycznej historii z życia prywatnego lub zawodowego. Jego siła tkwi w uniwersalności i relatywności.

**Dlaczego działa:** Efekt lustra i zasada podobieństwa. Generuje wysoki wskaźnik zaangażowania (reakcje, komentarze) w krótkim czasie.

### Wzorzec #2: Vulnerable confession
Posty zaczynające się od odważnego, osobistego wyznania błędu, słabości lub trudnego doświadczenia.

**Dlaczego działa:** Buduje natychmiastowe zaufanie poprzez podatność na zranienie. Osobiste historie zatrzymują użytkowników na dłużej (zwiększają 'dwell time').

### Wzorzec #3: Dekonstrukcja mitów
Posty kwestionujące popularne hasła, mity lub stereotypy biznesowe.

**Dlaczego działa:** Wywołuje dysonans poznawczy. Generuje zaangażowaną dyskusję w komentarzach, często z polaryzacją opinii.

## 🎯 Dla kogo?

- 📱 Social Media Managerów
- ✍️ Content Creatorów  
- 🎨 Marketerów (szczególnie na LinkedIn)
- 💼 Przedsiębiorców i freelancerów
- 🤖 Twórców narzędzi AI do content creation
- 📊 Analityków mediów społecznościowych

## 📊 Statystyki

- **127** profesjonalnych wzorców z piszemywirale.pl
- **100%** z wyjaśnieniami psychologicznymi
- **100%** z analizą algorytmiczną
- **Polski** język
- **LinkedIn** jako główna platforma (ale wzorce działają też na innych platformach)

## 🔍 Przykłady wyszukiwania

```bash
# Znajdź wzorce o humorze
python3 browser.py search humor

# Znajdź wzorce wykorzystujące vulnerability
python3 browser.py search vulnerability

# Znajdź wzorce edukacyjne
python3 browser.py search edukacyjny

# Znajdź wzorce o storytelling
python3 browser.py search historia

# Znajdź wzorce o algorytmie
python3 browser.py search algorytm
```

## 🔄 Źródło

Wszystkie wzorce pochodzą bezpośrednio z **piszemywirale.pl** - profesjonalnego serwisu poświęconego tworzeniu wiralowych treści w polskim internecie, ze szczególnym naciskiem na LinkedIn.

## 📝 Format danych

```json
{
  "postTypes": [
    {
      "id": "wzorzec-1",
      "number": 1,
      "type": "Opis typu posta i jego siły...",
      "why": "Wyjaśnienie psychologiczne i algorytmiczne..."
    }
  ],
  "metadata": {
    "version": "2.0",
    "source": "piszemywirale.pl",
    "totalTypes": 127,
    "language": "pl"
  }
}
```

## 🤝 Aktualizacje

Biblioteka zawiera oryginalne wzorce z piszemywirale.pl. Przy aktualizacjach zawartości serwisu, repozytorium będzie odpowiednio uaktualniane.

---

**Wersja:** 2.0  
**Źródło:** piszemywirale.pl  
**Ostatnia aktualizacja:** 2025-11-24  
**Język:** Polski
