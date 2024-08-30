from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Inisialisasi WebDriver (pastikan ChromeDriver berada di PATH atau masukkan path lengkapnya)
driver = webdriver.Chrome()

# Akses halaman web yang ingin di-scrape
url = 'https://ssacn.bkn.go.id/#/daftarFormasi'
driver.get(url)

# Tunggu halaman untuk load sepenuhnya (disesuaikan)
driver.implicitly_wait(10)  # Tunggu hingga 10 detik

# Contoh interaksi dengan dropdown (jika diperlukan, sesuaikan dengan form yang ada di halaman)
# driver.find_element(By.XPATH, '//input[@aria-labelledby="select2-jenjang-label"]').send_keys('S-1/Sarjana')
# driver.find_element(By.XPATH, '//input[@aria-labelledby="select2-program_studi-label"]').send_keys('S-1 TEKNIK INFORMATIKA')
# driver.find_element(By.XPATH, '//input[@aria-labelledby="select2-pengadaan-label"]').send_keys('CPNS')

# Klik tombol Cari (sesuaikan dengan tombol yang ada di halaman)
# driver.find_element(By.XPATH, '//button[text()="CARI"]').click()

# Tunggu hasil pencarian muncul
driver.implicitly_wait(10)

# Temukan tabel yang berisi data formasi
table = driver.find_element(By.XPATH, '//table')  # Sesuaikan dengan path tabel yang ada di halaman

# Ambil semua baris dalam tabel
rows = table.find_elements(By.TAG_NAME, "tr")

# Ambil header dari tabel
headers = [header.text for header in rows[0].find_elements(By.TAG_NAME, "th")]

# Ambil data dari tiap baris
data = []
for row in rows[1:]:
    cols = row.find_elements(By.TAG_NAME, "td")
    data.append([col.text for col in cols])

# Simpan data ke dalam DataFrame dan ekspor ke Excel
df = pd.DataFrame(data, columns=headers)
df.to_excel('data_formasi.xlsx', index=False)

# Tutup browser
driver.quit()

print("Data berhasil disimpan ke data_formasi.xlsx")
