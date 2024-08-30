from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Inisialisasi WebDriver
driver = webdriver.Chrome(executable_path='/opt/homebrew/bin/chromedriver')

# Akses halaman
url = 'https://sscasn.bkn.go.id/#/daftarFormasi'
driver.get(url)

# Tunggu halaman untuk load sepenuhnya
time.sleep(5)  # Menunggu elemen menjadi visible

# Isi Jenjang Pendidikan
jenjang_field = driver.find_element(By.XPATH, '//div[contains(@class, "css-1d8n9bt")]//input')
jenjang_field.click()
time.sleep(1)  # Delay untuk menunggu dropdown muncul
jenjang_field.send_keys('S-1/Sarjana')
jenjang_field.send_keys('\ue007')  # Simbol Enter

# Isi Program Studi
program_studi_field = driver.find_element(By.XPATH, '//div[contains(@class, "css-1d8n9bt")]//input')
program_studi_field.click()
time.sleep(1)
program_studi_field.send_keys('TEKNIK INFORMATIKA')
program_studi_field.send_keys('\ue007')

# Isi Jenis Pengadaan
jenis_pengadaan_field = driver.find_element(By.XPATH, '//div[contains(@class, "css-1d8n9bt")]//input')
jenis_pengadaan_field.click()
time.sleep(1)
jenis_pengadaan_field.send_keys('CPNS')
jenis_pengadaan_field.send_keys('\ue007')

# Klik tombol CARI
cari_button = driver.find_element(By.XPATH, '//button[contains(text(), "CARI")]')
cari_button.click()

# Tunggu hasil pencarian muncul
time.sleep(5)

# Temukan tabel
table = driver.find_element(By.XPATH, '//table')

# Ambil semua baris dalam tabel
rows = table.find_elements(By.TAG_NAME, "tr")

# Ambil header
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
