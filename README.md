# CS2 Demo Analytics MVP Backend

Минимальный backend для хранения метаданных CS2 демо-файлов в SQLite и выдачи списка импортов через API.

## Функциональность
- SQLite БД: `data/db/demos.sqlite3`
- Таблица `demos`:
  - `id` — INTEGER PRIMARY KEY AUTOINCREMENT
  - `filename` — TEXT NOT NULL
  - `date_added` — TEXT NOT NULL (UTC ISO-8601)
- CLI импорт: `import_demo.py`
- API (FastAPI):
  - `GET /health`
  - `GET /demos`

## Быстрый старт (Windows)

### 1. Клонирование
```powershell
git clone https://github.com/nnp08599-bot/CS2-.git
cd CS2-
```

### 2. Установка зависимостей
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Импорт `.dem`
```powershell
python import_demo.py C:\path\to\match.dem
```

### 4. Запуск API
```powershell
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 5. Проверка
- Health: `http://127.0.0.1:8000/health`
- Demos: `http://127.0.0.1:8000/demos`

Пример ответа `GET /demos`:
```json
[
  {
    "id": 1,
    "filename": "match.dem",
    "date_added": "2026-01-01T12:00:00+00:00"
  }
]
```
