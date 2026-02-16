import streamlit as st
import sqlite3 as sql
from streamlit_option_menu import option_menu
import pandas as pd
import time


def init_db():
    conn = sql.connect('stock.db')
    print("Connected to database successfully")

    cursor = conn.cursor()
    print("Cursor create successfully")

    cursor.execute("""CREATE TABLE IF NOT EXISTS PRODUCT
                      (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT,
                      category TEXT,
                      stock_count INTEGER,
                      price REAL
                      )""")
    print("Table created successfully")

    conn.commit()
    conn.close()


init_db()


# --- 1. Veritabanı Fonksiyonları ---
# (Veri ekle, sil, getir komutları burada)

def Add_Product(name, category, stock_count, price):
    conn = sql.connect('stock.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO PRODUCT (name, category, stock_count, price) VALUES (?, ?, ?, ?)",
                   (name, category, stock_count, price))

    conn.commit()
    conn.close()
    st.success(f"✅ {name} başarıyla eklendi!")
    time.sleep(1.5)  # 1.5 saniye bekle, kullanıcı mesajı görsün
    st.rerun()  # Sonra ekle


def Delete_Product(name):
    conn = sql.connect('stock.db')
    cursor = conn.cursor()
    # Seçilen isme sahip ürünü sil
    cursor.execute("DELETE FROM PRODUCT WHERE name = ?", (name,))
    conn.commit()
    conn.close()
    st.success(f"❌ {name} silindi!")
    time.sleep(1.5)  # 1.5 saniye bekle, kullanıcı mesajı görsün
    st.rerun()  # Sonra sil


def Update_Product(name, new_stock, new_price):
    conn = sql.connect('stock.db')
    cursor = conn.cursor()
    # Seçilen ismin stok ve fiyatını değiştir
    cursor.execute("UPDATE PRODUCT SET stock_count = ?, price = ? WHERE name = ?",
                   (new_stock, new_price, name))
    conn.commit()
    conn.close()
    st.success(f"🔄 {name} güncellendi!")
    time.sleep(1.5)  # 1.5 saniye bekle, kullanıcı mesajı görsün
    st.rerun()  # Sonra yenile


def Get_Product():
    conn = sql.connect('stock.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PRODUCT")
    data = cursor.fetchall()  # Tüm veriyi çek
    conn.close()
    return data


# --- 2. Sayfa Düzeni ---

with st.sidebar:
    selected = option_menu("Main Menu", ['Get Product', 'Add Product', 'Delete Product', 'Update Product'],
                           icons=['arrow-down-left-circle', 'plus-circle', 'dash-circle', 'r-circle'], menu_icon="cast",
                           default_index=0)

if selected == "Get Product":
    st.header("Ürün Listesi")
    data = Get_Product()
    if data:
        df = pd.DataFrame(data, columns=["ID", "Name", "Category", "Stock Count", "Price"])
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.warning("Henüz hiç ürün eklenmemiş.")


if selected == "Add Product":
    st.header("Yeni Ürün Ekle")
    productName = st.text_input("Enter product name")
    productCategory = st.selectbox("Select category", ("Technology", "Clothing", "Food"))
    productStockCount = st.number_input("Enter product stock count", min_value=0)
    productPrice = st.number_input("Enter product price", min_value=0.0)

    if st.button("Add Product"):
        if productName:
            Add_Product(productName, productCategory, productStockCount, productPrice)


if selected == "Delete Product":
    st.header("Ürün Sil")

    data = Get_Product()

    if data:
        # data listesinden sadece İsimleri (1. indeks) alıp bir liste yapıyoruz
        list_of_products = [x[1] for x in data]

        selected_product = st.selectbox("Silinecek Ürünü Seç", list_of_products)

        # Butonu kırmızı yapmak için type="primary"
        if st.button("Sil", type="primary"):
            Delete_Product(selected_product)
    else:
        st.warning("Silinecek ürün yok.")

# --- 4. GÜNCELLEME (UPDATE) ---
if selected == "Update Product":
    st.header("Ürün Güncelle")

    data = Get_Product()

    if data:
        list_of_products = [x[1] for x in data]
        selected_product_name = st.selectbox("Güncellenecek Ürünü Seç", list_of_products)

        # Seçilen isme ait verileri 'data' listesinin içinden bulup çekiyoruz.
        # x[1] ismi temsil ediyor. Eşleşen satırı buluyoruz.
        current_product_info = None
        for row in data:
            if row[1] == selected_product_name:
                current_product_info = row
                break

        if current_product_info:
            # Veritabanından gelen sıraya göre: (id, name, category, stock, price)
            current_stock = current_product_info[3]
            current_price = current_product_info[4]

            st.write("---")
            st.info(
                f"Seçilen Ürün: **{selected_product_name}** | Mevcut Stok: **{current_stock}** | Mevcut Fiyat: **{current_price} TL**")

            col1, col2 = st.columns(2)

            with col1:
                # Hem başlıkta gösteriyoruz hem de kutunun içine varsayılan değer (value) olarak yazıyoruz.
                new_stock = st.number_input(
                    f"Yeni Stok Adedi (Şu an: {current_stock})",
                    min_value=0,
                    value=current_stock  # Kutunun içinde "0" yerine mevcut stok yazar
                )

            with col2:
                new_price = st.number_input(
                    f"Yeni Fiyat (Şu an: {current_price})",
                    min_value=0.0,
                    value=current_price  # Kutunun içinde "0" yerine mevcut fiyat yazar
                )

            if st.button("Güncelle"):
                Update_Product(selected_product_name, new_stock, new_price)

    else:
        st.warning("Güncellenecek ürün yok.")