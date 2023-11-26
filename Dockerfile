FROM python:3.11-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /src

# poetryのインストール
RUN pip install poetry

# 依存関係ファイルのコピー
COPY pyproject.toml* poetry.lock* ./

# 必要な依存関係のインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# python-multipart のインストール
RUN pip install python-multipart

# poetry設定と依存関係のインストール
RUN poetry config virtualenvs.in-project true 
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

# アプリケーションのコピーと実行
COPY . /src
WORKDIR /src
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
