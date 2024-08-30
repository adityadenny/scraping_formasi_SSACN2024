from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Inisialisasi WebDriver
driver = webdriver.Chrome()

# Akses halaman web yang ingin di-scrape
url = 'https://sscasn.bkn.go.id/#/daftarFormasi'
driver.get(url)

# Tunggu halaman untuk load sepenuhnya (disesuaikan)
driver.implicitly_wait(10)  # Tunggu hingga 10 detik

# Isi filter sesuai dengan pilihan yang diinginkan
jenjang_input = driver.find_element(By.XPATH, '//input[@placeholder="--- Pilih Jenjang Pendidikan ---"]')
jenjang_input.send_keys('S-1/Sarjana')

program_studi_input = driver.find_element(By.XPATH, '//input[@placeholder="--- Pilih Program Studi ---"]')
program_studi_input.send_keys('S-1 TEKNIK INFORMATIKA')

instansi_input = driver.find_element(By.XPATH, '//input[@placeholder="--- Pilih Instansi ---"]')
instansi_input.send_keys('Badan Kepegawaian Negara')

jenis_pengadaan_input = driver.find_element(By.XPATH, '//input[@placeholder="--- Pilih Jenis Pengadaan ---"]')
jenis_pengadaan_input.send_keys('CPNS')

# Klik tombol "CARI"
tombol_cari = driver.find_element(By.XPATH, '//a[contains(@class, "bg-primary") and contains(text(), "CARI")]')
tombol_cari.click()

# Tunggu beberapa saat untuk memastikan data muncul
time.sleep(10)  # Disesuaikan

# Coba temukan tabel
tables = driver.find_elements(By.XPATH, '//table')

if len(tables) > 0:
    table = tables[0]
    print("Tabel ditemukan, mulai scraping data...")
    
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

    print("Data berhasil disimpan ke data_formasi.xlsx")
else:
    print("Tabel tidak ditemukan.")

# Tutup browser
driver.quit()