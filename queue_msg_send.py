from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueClient, QueueMessage, BinaryBase64DecodePolicy, BinaryBase64EncodePolicy
from dotenv import load_dotenv
import os
 
load_dotenv()  

connect_str = os.getenv('CONNECTION_STRING') 
queue_name = os.getenv('QUEUE_NAME')
# 建立連線
queue_client = QueueClient.from_connection_string(
                            conn_str=connect_str,
                            queue_name=queue_name,
                            message_encode_policy = BinaryBase64EncodePolicy(),
                            message_decode_policy = BinaryBase64DecodePolicy()
                        )
# 寫入 Queue
queue_client.send_message(b"Mark:First message")
queue_client.send_message(b"Mark:Second message")
queue_client.send_message(b"Mark:Third message")

 
 