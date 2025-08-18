import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random
from db_utils import save_price_to_db

def human_typing(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.25))

def get_amazon_price(isbn):
    print(f"→ Searching Amazon for ISBN: {isbn}")
    options = uc.ChromeOptions()
    options.headless = False

    driver = uc.Chrome(options=options)

    try:
        driver.get("https://www.amazon.com")
        time.sleep(4)

        # Handling "Continue Shopping"
        try:
            continue_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue shopping')]"))
            )
            print("'Continue Shopping' prompt found. Clicking...")
            continue_button.click()
            time.sleep(3)
        except:
            print("No 'Continue Shopping' prompt or already handled.")

        # Searching ISBN
        search = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search.clear()
        human_typing(search, isbn)
        search.send_keys(Keys.RETURN)
        time.sleep(4)

        price = None
        try:
            price_element = WebDriverWait(driver, 8).until(
                EC.presence_of_element_located((By.XPATH, "(//span[@class='a-price']//span[@class='a-offscreen'])[1]"))
            )
            price = driver.execute_script("return arguments[0].textContent;", price_element).strip().replace("$", "")
        except Exception as e:
            print("⚠️ Fallback price not found:", e)

        if price:
            print(f"Amazon price found: ${price}")
            save_price_to_db(isbn, "amazon", "new", float(price))
        else:
            print("Price was empty or not found after all attempts.")

    except Exception as e:
        print(f"Amazon price extraction failed: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    isbn_list = [
    "9780131103627",  # The C Programming Language
    "9780321573513",  # Calculus (Stewart)
    "9780134685991",  # Computer Networking (Kurose & Ross)
    "9781492078005",  # Python for Data Analysis
    "9781266141094",  # Principles of Economics (Mankiw)
    "9780134093413",  # Operating System Concepts (Silberschatz)
    "9781119701730",  # Organic Chemistry (Klein)
    "9780135166307",  # AI: A Modern Approach
    "9780132350884",  # Clean Code
    "9780135957059",  # Software Engineering (Sommerville)
    "9781260458350",  # The Art of Public Speaking
    "9780135183786",  # Introduction to Algorithms (CLRS)
    "9780393885384",  # Norton Anthology of English Lit
    "9781259911457",  # Campbell Biology
    "9780321982384",  # Linear Algebra (Lay)
    "9780201616224",  # The Pragmatic Programmer
    "9781119565028",  # Physics for Sci & Eng (Serway)
    "9780190906989",  # International Relations (Goldstein)
    "9781455751472",  # Robbins & Cotran Pathologic Basis of Disease
    "9781118808560",  # Myers' Psychology
    "9780135179192",  # Electrical Eng (Hambley)
    "9780073523323",  # Macroeconomics (McConnell)
    "9780134757599",  # C++ Primer (Lippman)
    "9781449355739",  # Fluent Python
    "9780321877587",  # Fundamentals of Database Systems
    "9781337671021",  # Business Statistics
    "9780134076437",  # Artificial Intelligence (2nd edition)
    "9781118018174",  # Strategic Management
    "9781284080193",  # Medical Terminology
    "9780321503028",  # Computer Architecture (Hennessy)
    "9781285763880",  # Anatomy & Physiology
    "9780470458365",  # Visualizing Nutrition
    "9780133594149",  # Chemistry (Zumdahl)
    "9780321839554",  # Programming in Python 3
    "9780132836495",  # Digital Design (Morris Mano)
    "9781284101850",  # Health Info Mgmt Tech
    "9780321914336",  # Essentials of Genetics
    "9781284065800",  # Pathophysiology
    "9781118841475",  # Business Communication
    "9780321856711",  # Engineering Economy
    "9780321993720",  # Statistics (McClave)
    "9781119285421",  # Evidence Based Practice
    "9780134092669",  # Modern Operating Systems
    "9780133943030",  # Computer Security
    "9780321920429",  # Microbiology
    "9781305580343",  # Economics (Cowen & Tabarrok)
    "9781118703414",  # Advanced Accounting
    "9780077862564",  # Intermediate Accounting
    "9780135178027",  # Software Dev Principles
    "9780136042593",  # Systems Analysis and Design
    "9781284080193",  # Medical Law and Ethics
]

    for isbn in isbn_list:
        get_amazon_price(isbn)
