import streamlit as st

def calculate_profit(sales_price, product_cost, ad_cost, desi):
    # Komisyon oranı (örnek: %18)
    commission_rate = 18 / 100
    commission_fee = sales_price * commission_rate
    
    # Kargo ücreti belirleme (TEX - Trendyol Ekspres)
    if sales_price <= 149.99:
        shipping_fee = 27.08 * 1.2  # KDV dahil
    elif sales_price <= 249.99:
        shipping_fee = 51.66 * 1.2
    else:
        shipping_fee = 62.49 * 1.2  # Örnek bir üst sınır koyduk
    
    # Net kâr hesaplama
    net_profit = sales_price - (product_cost + ad_cost + commission_fee + shipping_fee)
    profit_margin = (net_profit / sales_price) * 100 if sales_price > 0 else 0
    
    return net_profit, profit_margin

# Streamlit arayüzü
def main():
    st.title("Pazaryeri Kâr Hesaplama")
    
    sales_price = st.number_input("Satış Fiyatı (TL)", min_value=0.0, step=0.01)
    product_cost = st.number_input("Ürün Maliyeti (TL)", min_value=0.0, step=0.01)
    ad_cost = st.number_input("Reklam Maliyeti (TL)", min_value=0.0, step=0.01)
    desi = st.number_input("Ürün Desi Bilgisi", min_value=0.0, step=0.1)
    
    if st.button("Hesapla"):
        net_profit, profit_margin = calculate_profit(sales_price, product_cost, ad_cost, desi)
        
        st.subheader("Sonuçlar")
        st.write(f"**Net Kâr:** {net_profit:.2f} TL")
        st.write(f"**Kâr Marjı:** {profit_margin:.2f} %")

if __name__ == "__main__":
    main()

