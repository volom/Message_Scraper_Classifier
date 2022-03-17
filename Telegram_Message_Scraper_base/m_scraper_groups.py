from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import PeerUser
from csv_saver import *
from auth_info import *
import re
import pandas as pd
import sys

sys.path.append("../Message_Scraper_Classifier")

from DS_Model.ds_model_predict import *

chats = []
last_date = None

# set the limit of members amount
chunk_size = 100000

# set limit of messages amount
while True:
    try:
        limit_msg = 10000
        break
    except:
        print("Enter integer...")
        continue

groups = [] 
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)

print('Fetching Messages...')

group_title = sys.argv[1]

channel_entity=client.get_entity(group_title)
try:
    client.get_participants(group_title, limit=None, filter=None, aggressive=False) #!!!!! 
except:
    pass
posts = client(GetHistoryRequest(
    peer=channel_entity,
    limit=limit_msg,
    offset_date=None,
    offset_id=0,
    max_id=0,
    min_id=0,
    add_offset=0,
    hash=0))

post_msg = posts.messages

# save the results
all_msg = []

for m in post_msg:
    try:
        msg_lst = []
        msg = str(m.message).replace('\t', ' ').replace("\n", "{ENTER}")
        msg_sent = pd.read_csv("messages_group_db.csv", sep="\t")
        msg_sent = list(msg_sent.iloc[:, 2])

        if bool(re.search(r"[a-zA-Z|а-яА-Я]", msg)) and msg not in msg_sent:
            try:
                if client.get_entity(PeerUser(int(m.from_id.user_id))).username is None:
                    from_ = m.from_id.user_id
                else:
                    from_ = client.get_entity(PeerUser(int(m.from_id.user_id))).username
            except:
                from_ = ""
            msg_lst.append(group_title)    
            msg_lst.append(from_)
            msg_lst.append(msg)
            msg_lst.append(m.date)
            msg_lst.append(predict_label(msg))
            msg_lst.append("ds_model")
            all_msg.append(msg_lst)
    except:
        pass

all_msg = all_msg[::-1]

csv_save_group(all_msg)
