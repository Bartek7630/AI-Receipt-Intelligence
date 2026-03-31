import streamlit as st
import google.generativeai as genai
from PIL import Image
import json
import pandas as pd

st.set_page_config(page_title="Receipt Intelligence System", layout="wide")

API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-2.5-flash')

st.title("Receipt Intelligence System")
st.markdown("Automatyczna ekstrakcja danych z dokumentów księgowych przy użyciu modeli wizyjno-językowych.")

uploaded_file = st.file_uploader("Wgraj dokument (JPG/PNG)", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.image(img, use_container_width=True)

    if st.button("URUCHOM ANALIZĘ", type="primary"):
        with st.spinner("Przetwarzanie dokumentu..."):
            try:
                prompt = """
                Przeanalizuj załączony paragon. 
                Zwróć wynik wyłącznie jako poprawny plik JSON,
                zgodnie z poniższą strukturą. Zignoruj zwroty kaucji przy podliczaniu sumy, znajdź ostateczną kwotę do zapłaty.
                
                {
                    "sklep": "Nazwa sklepu",
                    "nip": "10 cyfr NIPu",
                    "data": "Data w formacie YYYY-MM-DD",
                    "suma": "Całkowita kwota do zapłaty (format X.YY)",
                    "waluta": "PLN",
                    "produkty": [
                        {"nazwa": "Dokładna nazwa produktu", "cena": "Cena (liczba w formacie X.YY)"}
                    ]
                }
                """
                
                response = model.generate_content(
                    [prompt, img],
                    generation_config={"response_mime_type": "application/json"}
                )
                
                surowy_tekst = response.text.strip()
                surowy_tekst = surowy_tekst.replace("```json", "").replace("```JSON", "").replace("```", "").strip()
                
                wynik_json = json.loads(surowy_tekst)
                
                try:
                    suma_str = str(wynik_json.get("suma", "0")).replace(",", ".").replace(" ", "").replace("PLN", "")
                    wynik_json["suma"] = f"{float(suma_str):.2f}"
                except ValueError:
                    pass 
                
                produkty = wynik_json.get("produkty", [])
                for prod in produkty:
                    try:
                        cena_str = str(prod.get("cena", "0")).replace(",", ".").replace(" ", "").replace("PLN", "")
                        prod["cena"] = f"{float(cena_str):.2f}"
                    except ValueError:
                        pass
                
                with col2:
                    st.success("Analiza zakończona pomyślnie.")
                    
                    json_string = json.dumps(wynik_json, indent=4, ensure_ascii=False)
                    st.download_button(
                        label="Pobierz dane jako JSON",
                        data=json_string,
                        file_name="dane_ksiegowe.json",
                        mime="application/json",
                        use_container_width=True
                    )
                    
                    st.subheader("Dane Nagłówkowe")
                    
                    c1, c2 = st.columns(2)
                    c1.metric("Sklep", wynik_json.get("sklep", "Brak"))
                    c1.metric("NIP", wynik_json.get("nip", "Brak"))
                    c2.metric("Do Zapłaty", f"{wynik_json.get('suma', 'Brak')} {wynik_json.get('waluta', 'PLN')}")
                    c2.metric("Data", wynik_json.get("data", "Brak"))
                    
                    st.subheader("Wykryte Pozycje")
                    if produkty:
                        df = pd.DataFrame(produkty)
                        st.table(df)
                    else:
                        st.warning("Nie udało się wyodrębnić listy produktów.")
                        
                    with st.expander("Surowy format JSON"):
                        st.json(wynik_json)

            except Exception as e:
                st.error(f"Wystąpił błąd podczas analizy dokumentu: {e}")
                st.info("Log debugowania:")
                st.code(response.text)
