FROM: 使用官方的 Python 3.10 映像作為基礎。這提供了 Python 執行環境。
WORKDIR: 設定容器內的工作目錄為 /app。
COPY requirements.txt: 將 requirements.txt 複製到工作目錄。
RUN pip install: 使用 pip 安裝 requirements.txt 中列出的所有 Python 依賴項。 --no-cache-dir 參數用於減少映像大小。
COPY . .: 將專案的其餘程式碼複製到工作目錄。
CMD: 設定容器啟動時要執行的命令。 在這裡，它運行 main.py。

## 如何構建和運行 Docker 映像

**建立 Docker 映像：**

在包含 Dockerfile 的目錄中，執行以下命令：

```bash
docker build -t q-estimation .
```

- `-t q-estimation` 標記映像，使其命名為 `q-estimation`。
- `.` 表示 Dockerfile 所在的當前目錄。

**運行 Docker 容器：**

```bash
docker run q-estimation
```

這將運行新建立的映像，並執行 `main.py`。

## 額外說明

- `.dockerignore` 檔案： 為了減少映像大小，您可以使用 `.dockerignore` 檔案來排除不需要複製到容器中的檔案和目錄（例如，`.git` 目錄、`__pycache__` 目錄等）。
- 環境變數： 您可以使用 `ENV` 指令在 Dockerfile 中設定環境變數，或者在運行容器時使用 `-e` 參數設定。
- 卷： 如果您需要將容器內部的檔案與主機上的檔案同步，可以使用 Docker 卷。
- 多階段建置： 對於更複雜的專案，您可以使用多階段建置來優化映像大小。 例如，您可以在一個階段安裝依賴項，然後將程式碼複製到另一個階段，只包含執行所需的檔案。
- 網路： 如果您的 `main.py` 需要網路連線，Docker 容器預設可以使用網路。 您可以使用 `--network` 參數來設定網路模式。

## Docker Push 和 Pull

- **docker push**:
  - 用於將 Docker 映像上傳到 Docker 註冊中心（例如 Docker Hub、Amazon ECR、Google Container Registry 等）。
  - 在使用 `docker push` 之前，您需要先登錄到 Docker 註冊中心。您可以使用 `docker login` 指令進行登錄。
  - 基本語法：`docker push <映像名稱>:<標籤>`。例如，`docker push my-image:latest`。
  - 映像名稱通常由註冊中心 URL、使用者名稱和映像名稱組成。例如，`docker push docker.io/myusername/my-image:latest`。
  - 如果沒有指定標籤，則預設使用 `latest` 標籤。
- **docker pull**:
  - 用於從 Docker 註冊中心下載 Docker 映像。
  - 基本語法：`docker pull <映像名稱>:<標籤>`。例如，`docker pull ubuntu:latest`。
  - 如果沒有指定標籤，則預設使用 `latest` 標籤。
  - 下載的映像將儲存在本地 Docker 映像庫中，您可以使用 `docker images` 指令查看。
