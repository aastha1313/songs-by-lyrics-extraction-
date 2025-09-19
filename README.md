# songs-by-lyrics-extraction-

Here you go, Aastha! You can copy and paste this directly into a file named README.md in your GitHub repository:

# 🎵 Songs by Lyrics Extraction

This Python project automates the extraction of song titles and descriptions from [Chosic.com](https://www.chosic.com/find-song-by-lyrics/) based on a lyrics search query. The scraped data is stored in a PostgreSQL database for further use.

---

## 🚀 Features

- Automates browser interaction using Selenium
- Scrapes song titles and descriptions using XPath
- Stores results in a PostgreSQL table (`songs`)
- Ignores all other files except `main.py` using `.gitignore`

---

## 🛠️ Technologies Used

- Python 3.x
- Selenium WebDriver
- PostgreSQL
- psycopg2
- ChromeDriver (via `webdriver-manager`)

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/aastha1313/songs-by-lyrics-extraction-.git
cd songs-by-lyrics-extraction-

2. Create a virtual environment (optional)

python -m venv .venv
.\.venv\Scripts\activate  # On Windows

3. Install dependencies

pip install selenium psycopg2-binary webdriver-manager

4. Configure PostgreSQL

Update the connection details in main.py:

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="your_password",
    host="localhost",
    port="5432"
)

🧪 How to Run

python main.py

Follow the prompt to close the browser once scraping is complete.

🗃️ Database Schema

CREATE TABLE IF NOT EXISTS songs (
    id SERIAL PRIMARY KEY,
    title TEXT,
    description TEXT
);

📁 Project Structure

├── main.py               # Core scraping and database logic
├── .gitignore            # Ignores all files except main.py
├── README.md             # Project documentation

🙋‍♀️ Author

Aastha BhardwajPython Developer & Automation EnthusiastGitHub Profile

📄 License

This project is open-source and available under the MIT License.


Let me know if you'd like to add screenshots, sample output, or a badge for Python version or license. You're building a solid repo!
