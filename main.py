import psycopg2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 🗄️ Setup PostgreSQL connection and create table if not exists
def setup_db():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="12345",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS songs (
            id SERIAL PRIMARY KEY,
            title TEXT,
            description TEXT
        )
    """)
    conn.commit()
    return conn, cursor

# 🌐 Setup Selenium WebDriver
def setup_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# 🔍 Perform search on Chosic
def search_lyrics(driver, query):
    driver.get("https://www.chosic.com/find-song-by-lyrics/")
    search_bar = driver.find_element(By.XPATH, '//*[@id="search-word"]')
    search_bar.send_keys(query)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='content']/div/article/div[1]/div[2]/button"))
    ).click()
    time.sleep(10)

# 📥 Scrape song titles and descriptions using XPath and insert into DB
def scrape_songs(driver, cursor, conn, max_items=20):
    for i in range(1, max_items + 1):
        title_xpath = f'/html/body/div[1]/div[1]/div/div[3]/article/div[2]/div/div/div/div/div[5]/div[2]/div/div/div[1]/div[{i}]/div[1]/div[1]/div/span'
        desc_xpath = f'/html/body/div[1]/div[1]/div/div[3]/article/div[2]/div/div/div/div/div[5]/div[2]/div/div/div[1]/div[{i}]/div[1]/div[3]/div[2]/div[3]'

        try:
            song_name = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, title_xpath))
            ).text.strip()
        except:
            print(f"{i}. Song title not found.")
            continue

        try:
            song_desc = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, desc_xpath))
            ).text.strip()
        except:
            print(f"{i}. Description not found.")
            continue

        print(f"{i}. {song_name} - {song_desc}")

        # Insert into PostgreSQL
        cursor.execute(
            "INSERT INTO songs (title, description) VALUES (%s, %s)",
            (song_name, song_desc)
        )
        conn.commit()

# 🚀 Main function
def main():
    conn, cursor = setup_db()
    driver = setup_driver()

    try:
        search_lyrics(driver, 'search')  # Replace 'search' with any lyrics
        scrape_songs(driver, cursor, conn)
    finally:
        input("Press Enter to close the browser...")
        driver.quit()
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()