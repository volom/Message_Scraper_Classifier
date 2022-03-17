import os
import time

# set your list of groups
lst_groups = []

def run():
    while True:
        for group in lst_groups:
            os.system(f"""python {os.getcwd()}//Telegram_Message_Scraper_base//m_scraper_groups.py "{group}" """)
            print(f"launched process of {group} group")
            time.sleep(10)

if __name__ == "__main__":
    run()    