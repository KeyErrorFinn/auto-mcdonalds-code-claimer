import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import os
from dotenv import load_dotenv


# Loads the .env file and gets the discord token
load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")

# Sets up the Selenium webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


# Function to make find_element simpler and faster to use
def febxp(xpath):
    return driver.find_element(By.XPATH, xpath)


# Logs into discord to retrieve the codes from the discord server
def discord_login():
    # Goes to discord login page
    driver.get("https://www.discord.com/login")

    # Uses token to log in faster
    driver.execute_script('''
        (function() {window.t = "'''+discord_token+'''";
        window.localStorage = document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage;window.setInterval(() => window.localStorage.token = `"${window.t}"`);
        window.location.reload();})();
    ''')
    time.sleep(4)


# Gets the code from the discord server
def get_code():
    # Goes to the main channel in the server
    driver.get("https://discord.com/channels/1136419235875258399/1136422264141774868")
    time.sleep(4)

    # Presses the generate button
    febxp('//*[@id="message-accessories-1169044279373611078"]/div[1]/div/div/button[1]').click()
    time.sleep(4)

    # Notes down the current time for the cooldown period
    current_time = datetime.datetime.now()
    print(current_time)
    time.sleep(2)

    # Returns the code generated
    try:
        mcd_code = driver.find_element(By.TAG_NAME, "code").text
        print(mcd_code)
    except:
        mcd_code = "none"
    time.sleep(1)
    return mcd_code


# Redeems the mcdonalds code on their website
def redeem_code(mcd_code):
    # Goes to mcdonalds page to redeem the code
    driver.get("https://www.mcdfoodforthoughts.com")
    time.sleep(4)
    febxp("/html/body/div[1]/main/div[2]/form/div/div/input").click()
    time.sleep(4)
    
    # Redirects the url to auto-input the data using the link
    mcd_code_parts = mcd_code.split("-")
    new_url = f"{driver.current_url}&AmountSpent1=13&AmountSpent2=48&CN1={mcd_code_parts[0]}&CN2={mcd_code_parts[1]}&CN3={mcd_code_parts[2]}"
    driver.get(new_url)
    time.sleep(4)
    febxp("/html/body/div[1]/main/div[2]/form/div/div[2]/input").click()
    time.sleep(4)

    # Function to deal with choice select options
    def choice_select():
        none_selected = True
        options = driver.find_elements(By.CLASS_NAME, "rbloption")
        for element in options:
            #/html/body/div[1]/main/div[2]/form/div/fieldset/div/div/div[3]/span/label/span
            span_elements = element.find_elements(By.TAG_NAME, "span")
            if span_elements[1].text in ["Dined in at restaurant", "Counter"]:
                try:
                    span_elements[0].find_element(By.TAG_NAME, "label").click()
                except Exception as e:
                    print(e)

                none_selected = False

        if none_selected:
            random_choice = random.randint(0, len(options)-1)
            options[random_choice].find_element(By.TAG_NAME, "label").click()

        time.sleep(random.randint(1, 3))
        driver.find_element(By.ID, "NextButton").click()

    # Function to deal with satisfaction select options
    def satisfaction_select():
        for element in driver.find_elements(By.TAG_NAME, "tr")[1:]:
            selected_answer = element.find_elements(By.CLASS_NAME, "inputtyperbloption")[random.randint(0, 2)]
            selected_answer.find_element(By.TAG_NAME, "label").click()
            time.sleep(random.randint(1, 4))
        
        time.sleep(random.randint(1, 3))
        driver.find_element(By.ID, "NextButton").click()

    # Function to deal with "yes or no" select options
    def yon_select():
        febxp("/html/body/div[1]/main/div[2]/form/div/table/tbody/tr/td[2]/label").click()

        time.sleep(random.randint(1, 3))
        driver.find_element(By.ID, "NextButton").click()

    # Runs through each page and decides the right selection to use
    while True:
        rbl_option = driver.find_elements(By.CLASS_NAME, "rbloption")
        input_type_rbl_option = driver.find_elements(By.CLASS_NAME, "inputtyperbloption")
        if rbl_option:
            input("about to preform: choiceSelect, continue?:")
            choice_select()
        elif len(input_type_rbl_option) <= 2 and input_type_rbl_option:
            input("about to preform: yonSelect, continue?:")
            yon_select()
        elif input_type_rbl_option:
            input("about to preform: satisfactionSelect, continue?:")
            satisfaction_select()
        else:
            ans = input("error, break? (y/n): ")
            if ans == "y":
                break
        
        time.sleep(4)

discord_login()
mcd_code = get_code()

# mcd_code = "C7HW-NBF9-TJKZ"
# mcd_code = "MD6W-6YFF-KXXL"
# mcd_code = "MLVW-NQFH-MKX9"
# mcd_code = "7XMW-4ZF9-9MKL"
# mcd_code = "CZTW-6YFH-7MT7"

if mcd_code == "none":
    print("Could not generate code!")
else:
    redeem_code(mcd_code)