# Tokopedia-Review-Scraper
## 📘 Deskripsi Proyek
Scraping ulasan, rating, serta nama produk dari halaman review Fantech Official Store di Tokopedia menggunakan Selenium, BeautifulSoup4, dan webdriver-manager.
## 🚀 Cara Menjalankan Proyek
- clone repo
  ```
  git clone https://github.com/Ardhan807/Tokopedia-Review-Scraper.git
  cd tokopedia-review-scraper
  ```

- istall dependencies
  ```
  pip install -r requirements.txt
  ```
  
- jalankan script scrape
  ```
  python scrape.py
  ```

- jalankan script see (melihat data csv)
  ```
  python see.ipynb
  ```
## 📁 Output Format
```
| Kolom        | Deskripsi                        |
| ------------ | -------------------------------- |
| review       | Isi ulasan pelanggan             |
| rating       | Jumlah bintang (1–5)             |
| produk       | Nama produk yang diulas          |
```
## ⚠ Catatan Penting
- Scraping Tokopedia bisa berubah karena perubahan struktur HTML.
- Dianjurkan menambahkan delay agar tidak dianggap bot.
- Gunakan hanya untuk keperluan analisis secara pribadi, bukan komersial.
