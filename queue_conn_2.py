from azure.storage.queue import QueueClient 
from dotenv import load_dotenv
import os

# load env
load_dotenv()

connect_str = os.getenv("CONNECTION_STRING")
queue_name = os.getenv("QUEUE_NAME") 
# 建立連線
queue_client = QueueClient.from_connection_string(connect_str, queue_name)