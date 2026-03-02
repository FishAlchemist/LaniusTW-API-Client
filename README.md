> [!NOTE]  
> 該Repo，由於相關的遠端依賴已關閉或刪除，所以目前是無法運行的，僅供閱覽。

# LaniusTW API Client (當前實現API 4.0版本的呼叫)

這是一個基於 Python 開發的 HTTP API Client (v6.1.1)，用於連接 LaniusTW API Server 進行各種 AI 對話與辨識功能。

## 功能介紹

- **健康檢查**：驗證 API Server 連線狀態。
- **語音辨識**：上傳音訊檔案至伺服器進行語音轉文字處理。
- **圖像辨識**：上傳圖片至伺服器進行影像辨識處理。
- **對話互動**：支援多角色對話模式，包括 Expert、Salesperson、Clerk 等不同對話場景。

## Tech Stack

- **HTTP 通訊**：`httpx`
- **資料模型**：`laniustw-model`
- **資料驗證**：`pydantic`
- **版本管理**：`packaging`
- **程式碼品質檢測**：`ruff`
- **套件依賴管理**：`uv`

## 安裝方式

```bash
pip install git+https://github.com/FishAlchemist/LaniusTW-API-Client.git
```

## 使用範例

```python
import laniustw_api_client
import laniustw_api_client.api as project_api

# 設定 API 伺服器網址
laniustw_api_client.PROJECT_API_URL = r"https://www.example.com"

# 進行健康檢查
respond = project_api.health_check(token="YOUR_TOKEN")
respond.response.raise_for_status()
print(respond.result)

# 專家對話
respond = project_api.chat_expert(
    question="你好，哪裡有賣牛肉?",
    identifier=None,
    token="YOUR_TOKEN"
)
respond.response.raise_for_status()
print(respond.result)

```

## API 端點映射

| 函數                | 端點                    |
| ------------------- | ----------------------- |
| `health_check`      | `/api/health`           |
| `speech_recogn`     | `/api/speech-recogn`    |
| `image_recognition` | `/api/image-recogn`     |
| `chat_expert`       | `/api/chat/expert`      |
| `chat_salesperson`  | `/api/chat/salesperson` |
| `chat_clerk`        | `/api/chat/clerk`       |

## 系統架構

本系列專案由三個獨立模組組成：

- **[Laniustw-Project-Demo] Desktop GUI**
  - **定位**：基於 CustomTkinter 開發的桌面圖形客戶端。
  - **職責**：提供直觀的操作介面，透過 HTTP API Library 與後端進行互動。
  - **Repository**: [GitHub Link](https://github.com/FishAlchemist/Laniustw-Project-Demo)

- **LaniusTW API Client** (本倉庫)
  - **定位**：與 Server 通訊的封裝，避免在 GUI 部分額外關注和 Server 的通訊細節。
  - **職責**：標準化 HTTP 請求流程、處理序列化與錯誤機制，供 GUI 使用。
  - **Repository**: [GitHub Link](https://github.com/FishAlchemist/LaniusTW-API-Client)

- **[Laniustw-Project-API-Server] Core Server**
  - **定位**：系統運算與資料中心。
  - **職責**：處理業務邏輯，並對外提供 API 接口。
  - **Repository**: [GitHub Link](https://github.com/FishAlchemist/Laniustw-Project-API-Server)

**運作機制：**
使用者在 **Desktop GUI** 觸發動作 → 呼叫 **API Library** 的方法 → 發送請求至 **Core Server** 執行邏輯並回傳結果。
