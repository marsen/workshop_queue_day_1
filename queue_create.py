from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueClient
from dotenv import load_dotenv
import os
 
load_dotenv()

try:
    # queue 命名
    queue_name = os.getenv("QUEUE_NAME")
    account_url = os.getenv("ACCOUNT_URL")
    default_credential = DefaultAzureCredential()
 

    # 建立連線
    queue_client = QueueClient(account_url, queue_name=queue_name ,credential=default_credential)
     
    # 建立 queue
    queue_client.create_queue()
    print("Creating queue: " + queue_name)
    
except Exception as e:
    print('Exception:')
    print(e)