from azure.storage.queue import QueueClient 
from dotenv import load_dotenv
import os

# load env
load_dotenv()

queue_name = os.getenv("QUEUE_NAME") 

connect_str = os.getenv("CONNECTION_STRING")

# 建立連線

queue_client = QueueClient.from_connection_string(connect_str, queue_name)