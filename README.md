# 專題API封裝Python庫 (當前實現Server 3.0 的 API 呼叫)

## Note: Packagge name為laniustw_api_client
* 從 git 的安裝
```bash
pip install git+https://gitlab.com/LaniusTW_CSAI_114/LaniusTW_API_Client_Python.git@v5.0.0
```
* 從 gitlab pypi 安裝(需指定index-url)
```
--index-url https://gitlab.com/api/v4/projects/61310914/packages/pypi/simple
```
### Example

```python
import laniustw_api_client
import laniustw_api_client.api as project_api
import uuid

laniustw_api_client.PROJECT_API_URL = r"https://www.example.com"
respond = project_api.chat_boot(question="你好，哪裡有賣牛肉?", token=TOKEN)
respond.response.raise_for_status()
print(respond.result)
print(respond.result.result)

```

### Mapping

* **api.test**: ``/api/test``
* **api.chat_professional**: ``/api/chat/professional``
* **api.chat_experience**: ``/api/chat/experience``
* **api.integrate**: ``/api/integrate``
* **api.chat_boot**: ``/api/chat/boot``
