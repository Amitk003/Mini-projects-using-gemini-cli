
import streamlit as st
from forex_python.converter import CurrencyRates

def main():
    st.title("Currency Converter")

    c = CurrencyRates()
    currencies = ['USD'] + list(c.get_rates('USD').keys())

    amount = st.number_input("Enter amount", value=1.00)
    from_currency = st.selectbox("From", currencies)
    to_currency = st.selectbox("To", currencies)

    if st.button("Convert"):
        result = c.convert(from_currency, to_currency, amount)
        st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")

if __name__ == '__main__':
    main()
