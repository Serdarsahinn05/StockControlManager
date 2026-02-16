# Stock Control System (Stok Takip Uygulaması) 📦

Python ve Streamlit kullanılarak geliştirilmiş, SQLite veritabanı tabanlı basit ve etkili bir stok yönetim sistemi. Bu uygulama ile ürünlerinizi ekleyebilir, güncelleyebilir, silebilir ve anlık stok durumunu takip edebilirsiniz.

## 🚀 Özellikler

Uygulama temel **CRUD** (Create, Read, Update, Delete) işlemlerini içerir:

* **📊 Ürün Listeleme (Get Product):** Veritabanındaki tüm ürünleri tablo halinde görüntüler.
* **➕ Ürün Ekleme (Add Product):** İsim, kategori, stok adedi ve fiyat bilgisiyle yeni ürün girişi.
* **❌ Ürün Silme (Delete Product):** Seçilen ürünü veritabanından kalıcı olarak siler.
* **🔄 Ürün Güncelleme (Update Product):** Mevcut ürünlerin stok adedini ve fiyatını günceller.

## 🛠️ Teknolojiler

* **Python 3.x**
* **Streamlit:** Modern web arayüzü için.
* **SQLite:** Verileri yerel olarak saklamak için (Kurulum gerektirmez).
* **Pandas:** Verileri tablo formatında işlemek ve göstermek için.
* **Streamlit Option Menu:** Yan menü navigasyonu için.

## 💻 Kurulum ve Çalıştırma

Projeyi bilgisayarınızda çalıştırmak için adımları izleyin:

1.  **Projeyi Klonlayın:**
    ```bash
    git clone [https://github.com/KULLANICI_ADIN/StockControlSystem.git](https://github.com/KULLANICI_ADIN/StockControlSystem.git)
    cd StockControlSystem
    ```

2.  **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Uygulamayı Başlatın:**
    ```bash
    streamlit run stock_manager.py
    ```


> **Not:** Uygulama ilk kez çalıştırıldığında `stock.db` adında bir veritabanı dosyası otomatik olarak oluşturulacaktır.

## 📷 Ekran Görüntüleri
<img width="2561" height="1468" alt="stock1" src="https://github.com/user-attachments/assets/cf13977d-fb00-4e80-81f4-8c30b9a5d5d4" />
<img width="2561" height="1468" alt="stock2" src="https://github.com/user-attachments/assets/bf139784-dc40-472c-8f55-9591dc1627b5" />
<img width="2561" height="1468" alt="stock3" src="https://github.com/user-attachments/assets/08a59fc2-6163-4bc5-9ad8-b0ff4eaadc69" />
<img width="2561" height="1468" alt="stock4" src="https://github.com/user-attachments/assets/fcd19ff2-ec67-497c-8f15-76e679dd29cf" />


## 📂 Proje Yapısı

* `stock_manager.py`: Uygulamanın ana kaynak kodu.
* `stock.db`: SQLite veritabanı dosyası (Otomatik oluşur).
* `requirements.txt`: Gerekli kütüphane listesi.

## 📝 Lisans
Bu proje eğitim amaçlı geliştirilmiştir ve açık kaynaklıdır.

---
**Geliştirici:** [GitHub Profiliniz](https://github.com/KULLANICI_ADIN)
