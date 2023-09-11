import unittest
import os
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestKesbangpol(unittest.TestCase):

    url = "https://pelayanan.kesbangpol.bandung.go.id"

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_penelitianpage(self):

        print("=====================================")
        print("[Test] Penelitian page")
        # Test name: penelitian-page
        # Step # | name | target | value
        # 1 | open | / | 
        self.driver.get(self.url)
        # 2 | setWindowSize | 1382x736 | 
        self.driver.set_window_size(1382, 736)
        # 3 | runScript | window.scrollTo(0,535) | 
        self.driver.execute_script("window.scrollTo(0,535)")
        # 4 | click | linkText=Penelitian | 
        self.driver.find_element(By.LINK_TEXT, "Penelitian").click()

        expected_url = self.url + "/penelitian"
        current_url = self.driver.current_url
        self.assertEqual(current_url, expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}")
        self.driver.close()

    def test_pklmagangkknpage(self):

        print("=====================================")
        print("[Test] PKL/Magang/KKN page")
        # Test name: pkl-magang-kkn-page
        # Step # | name | target | value
        # 1 | open | / | 
        self.driver.get(self.url)
        # 2 | setWindowSize | 1050x700 | 
        self.driver.set_window_size(1050, 700)
        # 3 | runScript | window.scrollTo(0,496) | 
        self.driver.execute_script("window.scrollTo(0,496)")
        # 4 | click | linkText=PKL/Magang/KKN | 
        self.driver.find_element(By.LINK_TEXT, "PKL/Magang/KKN").click()

        expected_url = self.url + "/magang"
        current_url = self.driver.current_url
        self.assertEqual(current_url, expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}")
        self.driver.close()

    def test_datawawancaraobservasipage(self):

        print("=====================================")
        print("[Test] Data/Wawancara/Observasi page")
        # Test name: data-wawancara-observasi-page
        # Step # | name | target | value
        # 1 | open | / | 
        self.driver.get(self.url)
        # 2 | setWindowSize | 1050x700 | 
        self.driver.set_window_size(1050, 700)
        # 3 | runScript | window.scrollTo(0,429) | 
        self.driver.execute_script("window.scrollTo(0,429)")
        # 4 | click | linkText=Data/Wawancara | 
        self.driver.find_element(By.LINK_TEXT, "Data/Wawancara").click()

        expected_url = self.url + "/wawancara"
        current_url = self.driver.current_url
        self.assertEqual(current_url, expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}")
        self.driver.close()

    def test_faqpage(self):

        print("=====================================")
        print("[Test] FAQ page")
        # Test name: faq-page
        # Step # | name | target | value
        # 1 | open | / | 
        self.driver.get(self.url)
        # 2 | setWindowSize | 1050x700 | 
        self.driver.set_window_size(1050, 700)
        # 3 | click | id=popover-trigger-:r6: | 
        self.driver.find_element(By.ID, "popover-trigger-:r6:").click()

        expected_url = self.url + "/faq"
        current_url = self.driver.current_url
        self.assertEqual(current_url, expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}")
        self.driver.close()

    def test_datawawancaraobservasiform(self):

        print("=====================================")
        print("[Test] Data/Wawancara/Observasi form")

        self.driver.get(self.url)
        self.driver.set_window_size(1050, 700)
        self.driver.execute_script("window.scrollTo(0,403)")
        self.driver.find_element(By.LINK_TEXT, "Data/Wawancara").click()
        self.driver.execute_script("window.scrollTo(0,407)")
        self.driver.find_element(By.ID, "nama").click()
        self.driver.find_element(By.ID, "nama").send_keys("Jane Doe")
        self.driver.find_element(By.ID, "alamat").click()
        self.driver.find_element(By.ID, "alamat").send_keys("Jl. Mawar No. 01")
        self.driver.find_element(By.ID, "jenis_no_identitas").click()
        dropdown = self.driver.find_element(By.ID, "jenis_no_identitas")
        dropdown.find_element(By.XPATH, "//option[. = 'NPM']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".css-16t6c2g").click()
        self.driver.find_element(By.ID, "no_identitas").click()
        self.driver.find_element(By.ID, "no_identitas").send_keys("223163300")
        self.driver.find_element(By.ID, "tujuan_dinas").click()
        self.driver.find_element(By.ID, "tujuan_dinas").send_keys("Badan Kesatuan Bangsa dan Politik")
        self.driver.find_element(By.CSS_SELECTOR, ".css-16t6c2g").click()
        self.driver.find_element(By.CSS_SELECTOR, ".chakra-form-control:nth-child(16) > .chakra-text").click()
        self.driver.find_element(By.ID, "judul_data").click()
        self.driver.find_element(By.ID, "judul_data").send_keys("Efektifitas Penghimpunan Dana Zakat Profesi ASN di Baznas Kota Bandung")
        self.driver.find_element(By.ID, "anggota").click()
        self.driver.find_element(By.ID, "anggota").send_keys("-")
        self.driver.find_element(By.CSS_SELECTOR, ".chakra-form-control:nth-child(18)").click()
        self.driver.find_element(By.ID, "jabatan").click()
        dropdown = self.driver.find_element(By.ID, "jabatan")
        dropdown.find_element(By.XPATH, "//option[. = 'Ketua Peneliti']").click()
        self.driver.find_element(By.ID, "nama_kampus").click()
        self.driver.find_element(By.ID, "nama_kampus").send_keys("University of India")
        self.driver.find_element(By.ID, "no_surat_kampus").click()
        self.driver.find_element(By.ID, "no_surat_kampus").send_keys("01")
        self.driver.find_element(By.ID, "tanggal_surat_kampus").click()
        self.driver.find_element(By.ID, "tanggal_surat_kampus").send_keys("11-09-2023")
        self.driver.find_element(By.ID, "no_hp").click()
        self.driver.find_element(By.ID, "no_hp").send_keys("081234567890")

        current_directory = os.path.dirname(os.path.abspath(__file__))
        relative_path = "avatar.png"
        image_path = os.path.join(current_directory, relative_path)
        self.driver.find_element(By.ID, "attach_ktp").send_keys(image_path)
        self.driver.find_element(By.ID, "attach_suratKampus").send_keys(image_path)
        self.driver.find_element(By.ID, "attach_ktm").send_keys(image_path)
        self.driver.find_element(By.ID, "attach_vaksin").send_keys(image_path)
        self.driver.find_element(By.ID, "attach_pasFoto").send_keys(image_path)
        self.driver.close()

    def test_penelitianform(self):

        print("=====================================")
        print("[Test] Penelitian form")
        
        self.driver.get(self.url)
        self.driver.set_window_size(1050, 700)
        self.driver.execute_script("window.scrollTo(0,403)")
        self.driver.find_element(By.LINK_TEXT, "Penelitian").click()
        self.driver.execute_script("window.scrollTo(0,407)")
        self.driver.find_element(By.ID, "nama").click()
        self.driver.find_element(By.ID, "nama").send_keys("Jane Doe")
        self.driver.find_element(By.ID, "alamat").click()
        self.driver.find_element(By.ID, "alamat").send_keys("Jl. Mawar No. 01")
        self.driver.find_element(By.ID, "jenis_no_identitas").click()
        dropdown = self.driver.find_element(By.ID, "jenis_no_identitas")
        dropdown.find_element(By.XPATH, "//option[. = 'NPM']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".css-16t6c2g").click()
        self.driver.find_element(By.ID, "no_identitas").click()
        self.driver.find_element(By.ID, "no_identitas").send_keys("223163300")
        self.driver.find_element(By.ID, "tujuan_dinas").click()
        self.driver.find_element(By.ID, "tujuan_dinas").send_keys("Badan Kesatuan Bangsa dan Politik")
        self.driver.find_element(By.ID, "anggota").click()
        self.driver.find_element(By.ID, "anggota").send_keys("-")
        self.driver.find_element(By.CSS_SELECTOR, ".chakra-form-control:nth-child(18)").click()
        self.driver.find_element(By.ID, "jabatan").click()
        dropdown = self.driver.find_element(By.ID, "jabatan")
        dropdown.find_element(By.XPATH, "//option[. = 'Ketua Peneliti']").click()
        self.driver.find_element(By.ID, "nama_kampus").click()
        self.driver.find_element(By.ID, "nama_kampus").send_keys("University of India")
        self.driver.find_element(By.ID, "no_surat_kampus").click()
        self.driver.find_element(By.ID, "no_surat_kampus").send_keys("01")
        self.driver.find_element(By.ID, "tanggal_surat_kampus").click()
        self.driver.find_element(By.ID, "tanggal_surat_kampus").send_keys("11-09-2023")
        self.driver.find_element(By.ID, "judul_penelitian").click()
        self.driver.find_element(By.ID, "judul_penelitian").send_keys("Penelitian di Badan Kesatuan Bangsa dan Politik")
        self.driver.find_element(By.ID, "no_hp").click()
        self.driver.find_element(By.ID, "no_hp").send_keys("081234567890")

        current_directory = os.path.dirname(os.path.abspath(__file__))
        relative_path = "avatar.png"
        image_path = os.path.join(current_directory, relative_path)
        self.driver.find_element(By.ID, "attach_ktp").send_keys(image_path)
        self.driver.find_element(By.ID, "attach_suratKampus").send_keys(image_path)
        self.driver.find_element(By.ID, "attach_ktm").send_keys(image_path)
        self.driver.find_element(By.ID, "attach_vaksin").send_keys(image_path)
        self.driver.find_element(By.ID, "attach_pasFoto").send_keys(image_path)
        self.driver.find_element(By.ID, "attach_proposal").send_keys(image_path)
        self.driver.find_element(By.ID, "attach_notaris").send_keys(image_path)
        self.driver.close()

    def test_kknform(self):

        print("=====================================")
        print("[Test] PKL/Magang/KKN form")
        self.driver.get("https://pelayanan.kesbangpol.bandung.go.id/")
        self.driver.set_window_size(1050, 700)
        self.driver.find_element(By.LINK_TEXT, "PKL/Magang/KKN").click()
        self.driver.execute_script("window.scrollTo(0,401)")
        self.driver.find_element(By.ID, "nama").click()
        self.driver.find_element(By.ID, "nama").send_keys("Jane Doe")
        self.driver.find_element(By.CSS_SELECTOR, ".chakra-form-control:nth-child(14) > .chakra-text:nth-child(3)").click()
        self.driver.find_element(By.ID, "alamat").click()
        self.driver.find_element(By.ID, "alamat").send_keys(" Jl. Wastukencana No. 01 RT. 001/001")
        self.driver.find_element(By.ID, "jenis_no_identitas").click()
        dropdown = self.driver.find_element(By.ID, "jenis_no_identitas")
        dropdown.find_element(By.XPATH, "//option[. = 'NPM']").click()
        self.driver.find_element(By.ID, "no_identitas").click()
        self.driver.find_element(By.ID, "no_identitas").send_keys("211475511")
        self.driver.find_element(By.ID, "anggota").click()
        self.driver.find_element(By.ID, "anggota").send_keys("-")
        self.driver.find_element(By.ID, "jabatan").click()
        dropdown = self.driver.find_element(By.ID, "jabatan")
        dropdown.find_element(By.XPATH, "//option[. = 'Ketua Kelompok']").click()
        self.driver.find_element(By.ID, "nama_kampus").click()
        self.driver.find_element(By.ID, "nama_kampus").send_keys("University of India")
        self.driver.find_element(By.ID, "no_surat_kampus").click()
        self.driver.find_element(By.ID, "no_surat_kampus").send_keys("1")
        self.driver.find_element(By.ID, "tanggal_surat_kampus").click()
        self.driver.find_element(By.ID, "tanggal_surat_kampus").send_keys("11-09-2023")
        self.driver.find_element(By.ID, "no_hp").click()
        self.driver.find_element(By.ID, "no_hp").send_keys("081234567890")
        self.driver.find_element(By.ID, "nama_dinas_terkait").click()
        self.driver.find_element(By.ID, "nama_dinas_terkait").send_keys("Badan Kesatuan Bangsa dan Politik Kota Bandung")
        self.driver.find_element(By.ID, "no_surat_dinas").click()
        self.driver.find_element(By.ID, "no_surat_dinas").send_keys("1")
        self.driver.find_element(By.ID, "tanggal_surat_dinas").click()
        self.driver.find_element(By.ID, "tanggal_surat_dinas").send_keys("11-09-2023")
        self.driver.find_element(By.ID, "tanggal_mulai").click()
        self.driver.find_element(By.ID, "tanggal_mulai").send_keys("11-09-2023")
        self.driver.find_element(By.ID, "tanggal_akhir").click()
        self.driver.find_element(By.ID, "tanggal_akhir").send_keys("11-09-2023")
        self.driver.find_element(By.CSS_SELECTOR, ".css-6gshi5").click()

        current_directory = os.path.dirname(os.path.abspath(__file__))
        relative_path = "avatar.png"
        image_path = os.path.join(current_directory, relative_path)
        self.driver.find_element(By.ID, "attach_ktp").send_keys(image_path)
        self.driver.find_element(By.ID, "attach_suratKampus").send_keys(image_path)
        self.driver.find_element(By.ID, "attach_ktm").send_keys(image_path)
        self.driver.find_element(By.ID, "attach_vaksin").send_keys(image_path)
        self.driver.find_element(By.ID, "attach_pasFoto").send_keys(image_path)
        self.driver.find_element(By.ID, "attach_suratDinas").send_keys(image_path)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()