# 🚀 Wiralownia - Wzorce Wiralowych Postów

Kompletna biblioteka wzorców i promptów do tworzenia angażujących treści dla mediów społecznościowych.

## 📚 Co znajdziesz w tym repozytorium?

### 20 Typów Postów Wiralowych

Każdy wzorzec zawiera:
- ✅ Szczegółowy opis i strukturę
- ✅ Gotowy prompt do użycia
- ✅ Przykłady zastosowania
- ✅ Rekomendacje platform
- ✅ Czynniki zwiększające wiralność

### Kategorie wzorców:

- 📖 **Storytelling** - posty oparte na narracji
- 🎓 **Edukacyjne** - tutoriale, FAQ, obalanie mitów
- 🎮 **Interaktywne** - ankiety, quizy, wyzwania
- 😂 **Rozrywkowe** - memy i treści relatable
- 💼 **Social Proof** - case studies, rekomendacje
- 🎨 **Wizualno-Edukacyjne** - karuzele, infografiki
- 💬 **Angażujące** - kontrowersje, dyskusje
- ⭐ **Inspiracyjne** - transformacje, przed/po
- 🎬 **Autentyczne** - za kulisami, osobiste historie
- 📚 **Zasoby** - listy narzędzi, rekomendacje
- 📊 **Data-driven** - statystyki, liczby
- 🔮 **Thought Leadership** - trendy, przewidywania

## 📖 Dokumentacja

### Podstawowe pliki:

1. **[WZORCE-POSTOW.md](WZORCE-POSTOW.md)** - Pełna dokumentacja
   - Szczegółowe prompty dla wszystkich 20 typów
   - Przykłady użycia
   - Wskazówki optymalizacji
   - Checklisty publikacji
   - Najlepsze praktyki

2. **[QUICK-REFERENCE.md](QUICK-REFERENCE.md)** - Szybki przewodnik
   - Tabele porównawcze
   - Power words do hooków
   - Optymalizacja per platforma
   - Dobór typu do celu

3. **[post-types.json](post-types.json)** - Struktura danych
   - Format JSON dla programowego dostępu
   - Wszystkie 20 wzorców ze strukturą
   - Idealne do integracji z aplikacjami i narzędziami AI

### Narzędzia:

4. **[browser.py](browser.py)** - Interaktywna przeglądarka CLI
   - Przeglądaj wzorce w terminalu
   - Szukaj po kategoriach, platformach
   - Wyświetlaj szczegóły i prompty
   - Tryb interaktywny lub CLI commands

5. **[example_usage.py](example_usage.py)** - Przykłady programowe
   - Jak załadować i używać danych JSON
   - Filtrowanie po kategoriach i platformach
   - Generowanie customowych promptów
   - Statystyki biblioteki

## 🚀 Jak używać?

### Metoda 1: Przeglądarka CLI (Rekomendowane)

```bash
# Tryb interaktywny
python3 browser.py

# Lista wszystkich wzorców
python3 browser.py list

# Szukaj wzorców
python3 browser.py search instagram
python3 browser.py search educational

# Pokaż szczegóły konkretnego wzorca
python3 browser.py show tutorial
python3 browser.py show meme-relatable

# Pokaż kategorie lub platformy
python3 browser.py categories
python3 browser.py platforms
```

### Metoda 2: Programowy dostęp (Python)

```python
# Zobacz example_usage.py dla pełnych przykładów
import json

with open('post-types.json', 'r') as f:
    data = json.load(f)

# Znajdź konkretny typ posta
tutorial = next(pt for pt in data['postTypes'] if pt['id'] == 'tutorial')
print(tutorial['prompt'])
```

### Metoda 3: Manualna (Dokumentacja)

#### Krok 1: Wybierz typ posta
Przejrzyj [QUICK-REFERENCE.md](QUICK-REFERENCE.md) i wybierz wzorzec odpowiedni do twojego celu i platformy.

#### Krok 2: Użyj prompta
Skopiuj gotowy prompt z [WZORCE-POSTOW.md](WZORCE-POSTOW.md) i wypełnij zmienne.

#### Krok 3: Personalizuj
Dostosuj treść do swojego głosu i marki.

#### Krok 4: Publikuj i mierz
Śledź metryki i optymalizuj!

## 💡 Przykład użycia

### Przykład 1: Przeglądanie w CLI

```bash
# Uruchom interaktywną przeglądarkę
python3 browser.py

# Lub użyj bezpośrednich komend
python3 browser.py search "instagram"
python3 browser.py show tutorial
```

### Przykład 2: Integracja z kodem

```python
import json

# Załaduj dane
with open('post-types.json', 'r') as f:
    data = json.load(f)

# Znajdź wzorzec dla LinkedIn
linkedin_posts = [
    pt for pt in data['postTypes'] 
    if 'LinkedIn' in pt['bestFor']
]

# Wygeneruj prompt
tutorial = next(pt for pt in data['postTypes'] if pt['id'] == 'tutorial')
prompt = tutorial['prompt'].replace('[TEMAT]', 'Marketing w AI')
print(prompt)
```

### Przykład 3: Tworzenie posta krok po kroku

Chcesz stworzyć post edukacyjny na LinkedIn?

1. **Uruchom przeglądarkę:**
   ```bash
   python3 browser.py
   ```

2. **Wybierz opcję "3" (Szukaj)** i wpisz "educational"

3. **Wybierz "Tutorial"** z wyników

4. **Skopiuj prompt** i wypełnij zmienne:
   - `[TEMAT]` → "zwiększanie zasięgów organicznych"
   - `[LICZBA]` → "5"
   - `[POZIOM]` → "ŚREDNIO-ZAAWANSOWANY"

5. **Gotowe!** Masz strukturę posta gotową do wypełnienia treścią

## 🎯 Dla kogo?

- 📱 Social Media Managerów
- ✍️ Content Creatorów
- 🎨 Marketerów
- 💼 Przedsiębiorców
- 🤖 Twórców narzędzi AI do content creation

## 📊 Statystyki

- **20** gotowych wzorców postów
- **12** kategorii treści
- **8** platform społecznościowych
- **Setki** przykładów i wskazówek

## 🔄 Aktualizacje

Repozytorium będzie regularnie aktualizowane o nowe wzorce i trendy.

## 📝 Licencja

Otwarte do użytku. Korzystaj, modyfikuj, dziel się!

## 🤝 Wkład

Sugestie nowych wzorców i ulepszenia mile widziane!

---

**Wersja:** 1.0  
**Ostatnia aktualizacja:** 2025-11-23  
**Język:** Polski