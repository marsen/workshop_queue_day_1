# LEARNING AZURE QUEUE

## SETUP

python3.10 -m pip install python-dotenv

## Create Connection  

```shell
python3.10 queue_conn.py
```

```shell
python3.10 queue_conn_2.py
```

## Create Queue

```shell
python3.10 queue_create.py  
```

### Exception

#### 嘗試創建的隊列已經存在

> Exception:  
Queue already exists  
RequestId:95423a02-0003-0052-2d8d-b1f4c6000000  
Time:2024-05-29 06:00:52+00:00  
ErrorCode:QueueAlreadyExists  

這個錯誤訊息表示你正在嘗試創建的隊列已經存在。在 Azure Storage 中，每個隊列的名稱必須是唯一的。

解決這個問題的方法有兩種：

如果你想使用一個已經存在的隊列，你可以直接使用它，而不需要再創建一個新的隊列。
如果你想創建一個新的隊列，你需要使用一個不同的名稱。

#### 隊列正在被刪除

> Exception:  
The specified queue is being deleted.  
RequestId:48e2cfe3-0003-001f-588e-b13b2a000000  
Time:2024-05-29T06:04:11.1975422Z  
ErrorCode:QueueBeingDeleted  
Content: <?xml version="1.0" encoding="utf-8"?><Error><Code>QueueBeingDeleted</Code><Message>The specified queue is being deleted.  
RequestId:48e2cfe3-0003-001f-588e-b13b2a000000  
Time:2024-05-29T06:04:11.1975422Z</Message></Error>  

這個錯誤訊息表示你正在嘗試創建的隊列正在被刪除。在 Azure Storage 中，  
當一個隊列被刪除時，其名稱不能立即被重用。  
你必須等待 Azure 完全刪除隊列後，才能使用相同的名稱創建新的隊列。  

解決這個問題的方法有兩種：

- 等待一段時間，直到 Azure 完全刪除隊列，然後再嘗試創建新的隊列。
- 使用一個不同的名稱來創建新的隊列。

你可以選擇最適合你的方法來解決這個問題。

## Send Message

```shell
python3.10 queue_msg_send.py
```

## Read Message

## Delete Message

(fin)
