# 專題API封裝Python庫 (當前實現Server 2.0 的 API 呼叫)

## Note: 該儲存庫由於仰賴[UV](https://github.com/astral-sh/uv)的設定，因此需使用UV安裝。Packagge name為laniustw_api_client**

```bash
pip install git+https://gitlab.com/LaniusTW_CSAI_114/LaniusTW_API_Client_Python.git@v4.3.0
```

### Example

```python
import laniustw_api_client
import laniustw_api_client.api as project_api
import uuid

laniustw_api_client.PROJECT_API_URL = r"https://www.example.com"
model_respond = project_api.chat_RAG("什麼是消費者", None)
print(model_respond.respond)
print(model_respond.result)

```

### Mapping

* **api.test**: ``/api/test``
* **api.chat_RAG**: ``/api/chat/RAG``
* **api.chat_Experience**: ``/api/chat/Experience``
* **api.integrate**: ``/api/Integrate``
