from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Lokasi chromedriver
chromedriver_path = '/opt/homebrew/bin/chromedriver'

# Inisialisasi Service
service = Service(chromedriver_path)

# Inisialisasi WebDriver dengan service
driver = webdriver.Chrome(service=service)

# Akses halaman
url = 'https://sscasn.bkn.go.id/#/daftarFormasi'
driver.get(url)

# Tunggu halaman untuk load sepenuhnya
time.sleep(5)  # Menunggu elemen menjadi visible

# Tunggu hingga elemen input untuk Jenjang Pendidikan tersedia
wait = WebDriverWait(driver, 20)

# Isi Jenjang Pendidikan
jenjang_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="--- Pilih Jenjang Pendidikan ---"]')))
jenjang_field.click()
time.sleep(1)  # Delay untuk menunggu dropdown muncul
jenjang_field.send_keys('S-1/Sarjana')
jenjang_field.send_keys('\ue007')  # Simbol Enter

# Isi Program Studi
program_studi_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="--- Pilih Program Studi ---"]')))
program_studi_field.click()
time.sleep(1)
program_studi_field.send_keys('TEKNIK INFORMATIKA')
program_studi_field.send_keys('\ue007')

# Isi Jenis Pengadaan
jenis_pengadaan_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="--- Pilih Jenis Pengadaan ---"]')))
jenis_pengadaan_field.click()
time.sleep(1)
jenis_pengadaan_field.send_keys('CPNS')
jenis_pengadaan_field.send_keys('\ue007')

# Klik tombol CARI
cari_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="button" and @class="ant-btn css-3rel02 ant-btn-default ant-btn-icon-only ant-input-search-button"]')))
cari_button.click()

# Tunggu hasil pencarian muncul
time.sleep(5)

# Pilih Formasi "Umum"
formasi_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "ant-select-selector")]')))
formasi_dropdown.click()
time.sleep(1)

formasi_umum_option = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "ant-select-item-option-content") and text()="UMUM"]')))
formasi_umum_option.click()

# Tunggu tabel muncul setelah memilih formasi
table = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="ant-table-container"]//table')))

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
