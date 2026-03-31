# 🧾 AI Receipt Intelligence System

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)
[![Gemini API](https://img.shields.io/badge/AI-Google%20Gemini%202.5%20Flash-orange.svg)](https://aistudio.google.com/)

Nowoczesna aplikacja webowa (End-to-End) do automatycznej ekstrakcji i ustrukturyzowania danych z dokumentów księgowych i paragonów. 

## Główne funkcjonalności

* **Rozumienie Kontekstowe (Zero-Regex):** Zamiast szukać słów kluczowych, system "patrzy" na zdjęcie i rozumie jego strukturę. Bez problemu radzi sobie z pogniecionymi, krzywymi paragonami oraz "rozstrzelonym" tekstem (np. paragony z Biedronki).
* **Ekstrakcja Danych Biznesowych:** Automatycznie wyciąga kluczowe dla księgowości informacje:
  * Nazwa sklepu
  * Numer NIP (identyfikator podatkowy)
  * Data transakcji
  * Ostateczna kwota do zapłaty (z pominięciem kaucji i podsumowań VAT)
  * Pełna, zdekodowana lista zakupionych produktów wraz z ich cenami.
* **Standaryzacja Danych:** Automatyczne formatowanie kwot do standardu finansowego (dwa miejsca po przecinku, kropka zamiast przecinka).
* **Eksport do JSON:** Możliwość pobrania czystego pliku `.json` gotowego do integracji z systemami ERP lub oprogramowaniem księgowym.
* **Interaktywny UI:** Czysty i responsywny interfejs użytkownika zbudowany w bibliotece Streamlit.

## Stack Technologiczny

* **Język:** Python
* **Frontend / Framework:** Streamlit
* **AI / VLM:** Google Generative AI (Model: `gemini-2.5-flash`)
* **Przetwarzanie danych:** Pandas, JSON, PIL (Pillow)
