# 專題API封裝Python庫
**Note: 該儲存庫可直接使用pip安裝。Packagge name為laniustw_api_client**
```bash
pip install git+https://gitlab.com/LaniusTW_CSAI_114/LaniusTW_API_Client_Python.git
```
### Example
```python
import laniustw_api_client
import laniustw_api_client.api as project_api
import uuid
# Note: Example 的 URL 不是永久的
laniustw_api_client.PROJECT_API_URL = r"https://www.example.com"
respond = project_api.chat_RAG("什麼是消費者", None)
print(respond.json())

```
### Mapping
* **api.test**: ``/api/test``
* **api.speech_recogn**: ``/api/speech_recognition``
* **api.image_recognition**: ``/api/Image_recognition``
* **api.chat_RAG**: ``/api/chat/RAG``
* **api.chat_Recommendation**: ``/api/chat/Recommendation``
* **api.chat_Experience**: ``/api/chat/Experience``
