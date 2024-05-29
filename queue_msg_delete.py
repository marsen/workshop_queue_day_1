import base64
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueClient
from dotenv import load_dotenv
import os
 
load_dotenv() 

connect_str = os.getenv('CONNECTION_STRING')
queue_name = os.getenv('QUEUE_NAME')

# 建立連線
queue_client = QueueClient.from_connection_string(connect_str, queue_name)
 
# 刪除 Queue
messages = queue_client.receive_messages(max_messages=5)
for msg_batch in messages.by_page():
    for msg in msg_batch:
        # "Process" the message
        content = base64.b64decode(msg.content).decode('utf-8')
        print(msg.id + " - " + content)
        # Let the service know we're finished with
        # the message and it can be safely deleted.
        queue_client.delete_message(msg)