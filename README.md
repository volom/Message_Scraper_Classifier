Fetching messages from Telegram chats and classifying its text using the Data Science model

❕ This project solves the problem: selection of participants from chats corresponding to your pattern, which will be created after manually labeling a pre-loaded certain number of messages and based on which the machine learning model will be trained for further automatic labeling.

--------------------------------------------------------------

🗒🗒🗒 Instruction

1. Put your credentials for telegram API from https://my.telegram.org/ to auth_info.py
2. Put chat name (one or multiple) into variable lst_groups in *ru_scraper.py*
3. Run *run_scraper.py*. The code is taken from here - https://github.com/volom/Telegram_Message_Scraper
4. Make manual labeling using labeling_manual.py. Just run it
5. Select Data Science model with highest accuracy score using DS_Model/*DS_Model_Selection_Classification.ipynb*. The script is taken from here - https://github.com/volom/DS_ModelSelection
6. Paste the appropriate model into *ds_model_train.py* or leave the one it already contains. Run the script.
7. Congrats!🎉🎉🎉 From this step, you can run run_scraper.py which will fill your database with automated labeling
8. After the next runnings you can use labeling_auto_check.py to review the predicted label and change it as you want. 🤖 The model will be retrained automatically 🤖

--------------------------------------------------------------

ℹ️ℹ️ℹ️ Additional info

🏷 0️⃣ - suitable 1️⃣ - non suitable

🧠 More messages -> more accuracy of label prediction

🔭 You can select Data Science model at your sole

🔤 The script uses only text from messages regardless of other options available: forwards, mentions, attachments etc.

❗️ some scripts use bash command in os.system(). Depending on your OS or environment settings you may probably need to change commands. Bash commands are used in *run_scraper.py*, *labeling_auto_check.py*, *labeling_manual.py*
