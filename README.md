# 🧾 AI Receipt Intelligence System

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)
[![Gemini API](https://img.shields.io/badge/AI-Google%20Gemini%202.5%20Flash-orange.svg)](https://aistudio.google.com/)

A modern, end-to-end web application for automatically extracting and structuring data from receipts and accounting documents.

## Key Features

* **Context-Based Understanding (Zero-Regex):** Instead of searching for keywords, the system "looks" at the image and understands its structure. It handles crumpled, skewed receipts and "scattered" text layouts (e.g. receipts from Polish discount grocery chains) without issues.
* **Business Data Extraction:** Automatically extracts information critical for accounting:
  * Store name
  * Tax ID number (NIP)
  * Transaction date
  * Final amount due (excluding deposits and VAT summary lines)
  * Full, decoded list of purchased items with their prices
* **Data Standardization:** Automatically formats amounts to a consistent financial standard (two decimal places, period instead of comma).
* **JSON Export:** Download a clean `.json` file ready for integration with ERP systems or accounting software.
* **Interactive UI:** Clean, responsive user interface built with Streamlit.

## Tech Stack

* **Language:** Python
* **Frontend / Framework:** Streamlit
* **AI / VLM:** Google Generative AI (Model: `gemini-2.5-flash`)
* **Data Processing:** Pandas, JSON, PIL (Pillow)
