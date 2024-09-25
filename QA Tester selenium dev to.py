from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# pemasangan WebDriver
driver = webdriver.Chrome(executable_path='D:\QE EP AUTO\piton\chromedriver.exe')

# Maksimalkan jendela setelah ChromeDriver terbuka
driver.maximize_window()

# Variabel untuk menghitung jumlah test case yang passed dan failed
test_cases_passed = 0
test_cases_failed = 0

# Test Case 1: Buka halaman website dan verifikasi halaman terbuka
try:
    # Buka halaman website
    driver.get("https://dev.to/enter")

    # Verifikasi bahwa halaman terbuka dengan memeriksa apakah elemen tertentu terlihat
    element = driver.find_element(By.XPATH, "//h1[@class='registration__title']")
    if element.is_displayed():
        print("Test Case 1: PASSED - Halaman terbuka dan elemen ditemukan.")
        test_cases_passed += 1
    else:
        print("Test Case 1: FAILED - Elemen tidak ditemukan.")
        test_cases_failed += 1
except Exception as e:
    print("Test Case 1: FAILED - Halaman tidak terbuka atau elemen tidak ditemukan:", e)
    test_cases_failed += 1

# Test Case 2: Klik tombol 'Continue with Apple'
try:
    # Tunggu beberapa detik agar elemen muncul (opsional, bisa menggunakan WebDriverWait untuk lebih robust)
    time.sleep(3)

    # Cari dan klik tombol 'Continue with Apple'
    apple_button = driver.find_element(By.XPATH, "//span[normalize-space()='Continue with Apple']")
    apple_button.click()
    print("Test Case 2: PASSED - Tombol 'Continue with Apple' berhasil diklik.")
    test_cases_passed += 1
except Exception as e:
    print("Test Case 2: FAILED - Gagal menemukan atau menekan tombol 'Continue with Apple':", e)
    test_cases_failed += 1
time.sleep(3)
driver.back()

# Test Case 3: Klik tombol 'Continue with Facebook'
try:
    # Tunggu beberapa detik agar elemen muncul (opsional, bisa menggunakan WebDriverWait untuk lebih robust)
    time.sleep(3)

    # Cari dan klik tombol 'Continue with Facebook'
    facebook_button = driver.find_element(By.XPATH, "//span[normalize-space()='Continue with Facebook']")
    facebook_button.click()
    print("Test Case 3: PASSED - Tombol 'Continue with Facebook' berhasil diklik.")
    test_cases_passed += 1
except Exception as e:
    print("Test Case 3: FAILED - Gagal menemukan atau menekan tombol 'Continue with Facebook':", e)
    test_cases_failed += 1
time.sleep(3)
driver.back()

# Test Case 4: Klik tombol 'Continue with Forem'
try:
    # Tunggu beberapa detik agar elemen muncul (opsional, bisa menggunakan WebDriverWait untuk lebih robust)
    time.sleep(3)

    # Cari dan klik tombol 'Continue with Forem'
    Forem_button = driver.find_element(By.XPATH, "//button[@class='flex w-100 p-3 radius-default items-center bg-base-inverted registration__button-container brand-forem']")
    Forem_button.click()
    print("Test Case 4: PASSED - Tombol 'Continue with Forem' berhasil diklik.")
    test_cases_passed += 1
except Exception as e:
    print("Test Case 4: FAILED - Gagal menemukan atau menekan tombol 'Continue with Forem':", e)
    test_cases_failed += 1
time.sleep(3)
driver.back()

# Test Case 5: Klik tombol 'Continue with GitHub'
try:
    # Tunggu beberapa detik agar elemen muncul (opsional, bisa menggunakan WebDriverWait untuk lebih robust)
    time.sleep(3)

    # Cari dan klik tombol 'Continue with GitHub'
    GitHub_button = driver.find_element(By.XPATH, "//span[normalize-space()='Continue with GitHub']")
    GitHub_button.click()
    print("Test Case 5: PASSED - Tombol 'Continue with GitHub' berhasil diklik.")
    test_cases_passed += 1
except Exception as e:
    print("Test Case 5: FAILED - Gagal menemukan atau menekan tombol 'Continue with GitHub':", e)
    test_cases_failed += 1
time.sleep(3)
driver.back()

# Test Case 6: Klik tombol 'Continue with Google'
try:
    # Tunggu beberapa detik agar elemen muncul (opsional, bisa menggunakan WebDriverWait untuk lebih robust)
    time.sleep(3)

    # Cari dan klik tombol 'Continue with Google'
    Google_button = driver.find_element(By.XPATH, "//span[normalize-space()='Continue with Google']")
    Google_button.click()
    print("Test Case 6: PASSED - Tombol 'Continue with Google' berhasil diklik.")
    test_cases_passed += 1
except Exception as e:
    print("Test Case 6: FAILED - Gagal menemukan atau menekan tombol 'Continue with Google':", e)
    test_cases_failed += 1
time.sleep(3)
driver.back()

# Test Case 7: Klik tombol 'Continue with Twitter'
try:
    # Tunggu beberapa detik agar elemen muncul (opsional, bisa menggunakan WebDriverWait untuk lebih robust)
    time.sleep(3)

    # Cari dan klik tombol 'Continue with Twitter'
    Twitter_button = driver.find_element(By.XPATH, "//span[normalize-space()='Continue with Twitter (X)']")
    Twitter_button.click()
    print("Test Case 7: PASSED - Tombol 'Continue with Twitter' berhasil diklik.")
    test_cases_passed += 1
except Exception as e:
    print("Test Case 7: FAILED - Gagal menemukan atau menekan tombol 'Continue with Twitter':", e)
    test_cases_failed += 1
time.sleep(3)
driver.back()

# Test Case 8: Klik tombol 'Forgot password?'
try:
    # Tunggu beberapa detik agar elemen muncul (opsional, bisa menggunakan WebDriverWait untuk lebih robust)
    time.sleep(3)

    # Cari dan klik tombol 'Forgot password?'
    Twitter_button = driver.find_element(By.XPATH, "//a[@class='m-0']")
    Twitter_button.click()
    print("Test Case 8: PASSED - Tombol 'Forgot password?' berhasil diklik.")
    test_cases_passed += 1
except Exception as e:
    print("Test Case 8: FAILED - Gagal menemukan atau menekan tombol 'Forgot password?':", e)
    test_cases_failed += 1
time.sleep(3)
driver.back()

# Test Case 9: Klik tombol 'privacy policy'
try:
    # Tunggu beberapa detik agar elemen muncul (opsional, bisa menggunakan WebDriverWait untuk lebih robust)
    time.sleep(3)

    # Cari dan klik tombol 'privacy policy'
    Twitter_button = driver.find_element(By.XPATH, "//a[normalize-space()='privacy policy']")
    Twitter_button.click()
    print("Test Case 9: PASSED - Tombol 'privacy policy' berhasil diklik.")
    test_cases_passed += 1
except Exception as e:
    print("Test Case 9: FAILED - Gagal menemukan atau menekan tombol 'privacy policy':", e)
    test_cases_failed += 1
time.sleep(3)
driver.back()

# Test Case 10: Klik tombol 'terms of use'
try:
    # Tunggu beberapa detik agar elemen muncul (opsional, bisa menggunakan WebDriverWait untuk lebih robust)
    time.sleep(3)

    # Cari dan klik tombol 'terms of use'
    Twitter_button = driver.find_element(By.XPATH, "//a[normalize-space()='terms of use']")
    Twitter_button.click()
    print("Test Case 10: PASSED - Tombol 'terms of use' berhasil diklik.")
    test_cases_passed += 1
except Exception as e:
    print("Test Case 10: FAILED - Gagal menemukan atau menekan tombol 'terms of use':", e)
    test_cases_failed += 1
time.sleep(3)
driver.back()

# Test Case 11: Klik tombol 'code of conduct'
try:
    # Tunggu beberapa detik agar elemen muncul (opsional, bisa menggunakan WebDriverWait untuk lebih robust)
    time.sleep(3)

    # Cari dan klik tombol 'code of conduct'
    Twitter_button = driver.find_element(By.XPATH, "//a[normalize-space()='code of conduct']")
    Twitter_button.click()
    print("Test Case 11: PASSED - Tombol 'code of conduct' berhasil diklik.")
    test_cases_passed += 1
except Exception as e:
    print("Test Case 11: FAILED - Gagal menemukan atau menekan tombol 'code of conduct':", e)
    test_cases_failed += 1
time.sleep(3)
driver.back()

# Test Case 12: Klik tombol 'create account'
try:
    # Tunggu beberapa detik agar elemen muncul (opsional, bisa menggunakan WebDriverWait untuk lebih robust)
    time.sleep(3)

    # Cari dan klik tombol 'create account'
    Twitter_button = driver.find_element(By.XPATH, "//div[@class='crayons-subtitle-3 color-grey-700 fw-normal align-center pb-6']//a[normalize-space()='Create account']")
    Twitter_button.click()
    print("Test Case 12: PASSED - Tombol 'create account' berhasil diklik.")
    test_cases_passed += 1
except Exception as e:
    print("Test Case 12: FAILED - Gagal menemukan atau menekan tombol 'create account':", e)
    test_cases_failed += 1
time.sleep(3)
driver.back()

# Test Case 13: Isi form login dengan email tanpa '@' dan verifikasi pesan kesalahan
try:
    time.sleep(3)

    # Isi email tanpa '@'
    email_input = driver.find_element(By.NAME, "user[email]")
    email_input.send_keys("syauqicom")

    # Coba submit form
    email_input.submit()

    # Tunggu sejenak untuk melihat validasi
    time.sleep(3)

    # Verifikasi apakah ada pesan kesalahan
    validation_message = email_input.get_attribute("validationMessage")
    if "@" in validation_message:
        print("Test Case 13: PASSED - Pesan kesalahan validasi muncul dibawah form: ", validation_message)
        test_cases_passed += 1
    else:
        print("Test Case 13: FAILED - Pesan kesalahan validasi tidak sesuai dibawah form.")
        test_cases_failed += 1
except Exception as e:
    print("Test Case 13: FAILED - Gagal mengisi form atau memverifikasi validasi karena browser atau driver tidak mendeteksi:", e)
    test_cases_failed += 1
time.sleep(3)
driver.back()

# Test Case 14: Input email dan password kosong, lalu verifikasi pesan kesalahan
try:
    time.sleep(3)
    # Kosongkan input email dan password
    email_input = driver.find_element(By.NAME, "user[email]")
    password_input = driver.find_element(By.NAME, "user[password]")
    email_input.clear()
    password_input.clear()

    # Coba submit form
    password_input.submit()
    time.sleep(3)

    # Verifikasi pesan kesalahan
    error_message_element = driver.find_element(By.CSS_SELECTOR, ".crayons-notice--danger.registration__error-notice")
    expected_error_message = (
        "Unable to login.\n"
        "If you haven't created an account, we recommend signing up with social authentication below. "
        "If you haven't received your confirmation email yet, click here to resend it.\n"
        "Contact us if you continue having trouble."
    )

    if error_message_element.is_displayed() and error_message_element.text == expected_error_message:
        print("Test Case 14: PASSED - Pesan kesalahan muncul seperti yang diharapkan ketika email password kosong.")
        test_cases_passed += 1
    else:
        print("Test Case 14: FAILED - Email password kosong pesan kesalahan tidak sesuai.")
        test_cases_failed += 1
except Exception as e:
    print("Test Case 14: FAILED - Gagal memverifikasi pesan kesalahan:", e)
    test_cases_failed += 1
time.sleep(3)
driver.back()

# Test Case 15: Input password tanpa email, lalu verifikasi pesan kesalahan
try:
    time.sleep(3)
    # Kosongkan input email hanya password
    email_input = driver.find_element(By.NAME, "user[email]")
    password_input = driver.find_element(By.NAME, "user[password]")
    email_input.clear()
    password_input.send_keys("admin#1234")

    # Coba submit form
    password_input.submit()
    time.sleep(3)

    # Verifikasi pesan kesalahan
    error_message_element = driver.find_element(By.CSS_SELECTOR, ".crayons-notice--danger.registration__error-notice")
    expected_error_message = (
        "Unable to login.\n"
        "If you haven't created an account, we recommend signing up with social authentication below. "
        "If you haven't received your confirmation email yet, click here to resend it.\n"
        "Contact us if you continue having trouble."
    )

    if error_message_element.is_displayed() and error_message_element.text == expected_error_message:
        print("Test Case 15: PASSED - Pesan kesalahan muncul seperti yang diharapkan ketika password tanpa email.")
        test_cases_passed += 1
    else:
        print("Test Case 15: FAILED - Password tanpa email pesan kesalahan tidak sesuai.")
        test_cases_failed += 1
except Exception as e:
    print("Test Case 15: FAILED - Gagal memverifikasi pesan kesalahan:", e)
    test_cases_failed += 1
time.sleep(3)
driver.back()

# Test Case 16: Input email tanpa password, lalu verifikasi pesan kesalahan
try:
    time.sleep(3)
    # Kosongkan input password hanya email
    email_input = driver.find_element(By.NAME, "user[email]")
    password_input = driver.find_element(By.NAME, "user[password]")
    email_input.send_keys("syauqi247@gmail.com")
    password_input.clear()

    # Coba submit form
    password_input.submit()
    time.sleep(3)

    # Verifikasi pesan kesalahan
    error_message_element = driver.find_element(By.CSS_SELECTOR, ".crayons-notice--danger.registration__error-notice")
    expected_error_message = (
        "Unable to login.\n"
        "If you haven't created an account, we recommend signing up with social authentication below. "
        "If you haven't received your confirmation email yet, click here to resend it.\n"
        "Contact us if you continue having trouble."
    )

    if error_message_element.is_displayed() and error_message_element.text == expected_error_message:
        print("Test Case 16: PASSED - Pesan kesalahan muncul seperti yang diharapkan ketika email tanpa password.")
        test_cases_passed += 1
    else:
        print("Test Case 16: FAILED - Email tanpa password pesan kesalahan tidak sesuai.")
        test_cases_failed += 1
except Exception as e:
    print("Test Case 16: FAILED - Gagal memverifikasi pesan kesalahan:", e)
    test_cases_failed += 1
time.sleep(3)
driver.back()

# Test Case 17: Input password email yang salah, lalu verifikasi pesan kesalahan
try:
    time.sleep(3)
    # input salah password dan email
    email_input = driver.find_element(By.NAME, "user[email]")
    password_input = driver.find_element(By.NAME, "user[password]")
    email_input.clear()
    email_input.send_keys("syauqi@gmail.com")
    password_input.send_keys("admin1234")

    # Coba submit form
    password_input.submit()
    time.sleep(3)

    # Verifikasi pesan kesalahan
    error_message_element = driver.find_element(By.CSS_SELECTOR, ".crayons-notice--danger.registration__error-notice")
    expected_error_message = (
        "Unable to login.\n"
        "If you haven't created an account, we recommend signing up with social authentication below. "
        "If you haven't received your confirmation email yet, click here to resend it.\n"
        "Contact us if you continue having trouble."
    )

    if error_message_element.is_displayed() and error_message_element.text == expected_error_message:
        print("Test Case 17: PASSED - Pesan kesalahan muncul seperti yang diharapkan ketika salah akun password.")
        test_cases_passed += 1
    else:
        print("Test Case 17: FAILED - Pesan kesalahan tidak sesuai setelah salah akun password.")
        test_cases_failed += 1
except Exception as e:
    print("Test Case 17: FAILED - Gagal memverifikasi pesan kesalahan:", e)
    test_cases_failed += 1
time.sleep(3)
driver.back()

# Test Case 18: Verifikasi apakah checkbox "Remember me" sudah dicentang secara otomatis
try:
    time.sleep(3)
    remember_me_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox' and @name='user[remember_me]']")
    if remember_me_checkbox.is_selected():
        print("Test Case 18: PASSED - Checkbox 'Remember me' sudah dicentang secara otomatis.")
        test_cases_passed += 1
    else:
        print("Test Case 18: FAILED - Checkbox 'Remember me' tidak dicentang secara otomatis.")
        test_cases_failed += 1
except Exception as e:
    print("Test Case 18: FAILED - Gagal memverifikasi status checkbox 'Remember me':", e)
    test_cases_failed += 1
time.sleep(3)

# Test Case 19: Login dengan email dan password yang benar
try:
    time.sleep(3)
    email_input = driver.find_element(By.NAME, "user[email]")
    password_input = driver.find_element(By.NAME, "user[password]")

    # Masukkan email dan password yang benar
    email_input.clear()
    email_input.send_keys("syauqi247@gmail.com")  # Email contoh ini
    password_input.clear()
    password_input.send_keys("admin#1234")  # Password untuk contoh

    # Submit form
    password_input.submit()
    time.sleep(3)

    # Verifikasi apakah login berhasil dengan memeriksa apakah halaman redirect setelah login
    profile_link = driver.find_element(By.XPATH, "//button[@id='member-menu-button']")
    if profile_link.is_displayed():
        print("Test Case 19: PASSED - Login berhasil dan halaman profil ditemukan.")
        test_cases_passed += 1
    else:
        print("Test Case 19: FAILED - Halaman profil tidak ditemukan setelah login.")
        test_cases_failed += 1
except Exception as e:
    print("Test Case 19: FAILED - Gagal login atau memverifikasi login:", e)
    test_cases_failed += 1
time.sleep(3)

# Tutup browser
driver.quit()

# Tampilkan hasil akhir
print("\nHasil Akhir Test Case:")
print(f"Total Test Case Passed: {test_cases_passed}")
print(f"Total Test Case Failed: {test_cases_failed}")