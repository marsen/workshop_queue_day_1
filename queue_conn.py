from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueClient
from dotenv import load_dotenv
import os
 
load_dotenv()

queue_name = os.getenv("QUEUE_NAME")

account_url = os.getenv("ACCOUNT_URL")

default_credential = DefaultAzureCredential()
 
# 建立連線

queue_client = QueueClient(account_url, queue_name=queue_name ,credential=default_credential)