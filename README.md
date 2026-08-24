# Family Manager

Backend для мобильного приложения, которое снимает с семьи координационную и ментальную нагрузку: собирает дела из разных источников, помогает распределить их справедливо и показывает вклад каждого.

## Что уже заложено

- FastAPI API с OpenAPI-документацией: `http://localhost:8000/docs`;
- PostgreSQL, SQLAlchemy и Alembic;
- доменные сущности: семья, участник, задача и приглашение;
- API-контракты для пяти первых экранов;
- изолированный LLM-слой с адаптерами OpenAI и GigaChat;
- первый AI-flow: из текста письма, OCR или транскрипта получается черновик задачи.

Пока реализован только health-check и рабочий AI-contract. Остальные product endpoints намеренно описаны в OpenAPI, но не подключены к репозиториям/сервисам и возвращают `501` до следующего этапа.

## Структура

```text
app/
  api/v1/endpoints/      # HTTP-контракты пяти экранов и AI
  core/                  # конфигурация
  db/                    # сессии и SQLAlchemy base
  models/                # PostgreSQL-модели
  schemas/               # Pydantic request/response модели
  services/              # продуктовая логика
  integrations/llm/      # взаимозаменяемые OpenAI/GigaChat адаптеры
migrations/              # Alembic-миграции
tests/
```

## Быстрый старт

```bash
cp .env.example .env
docker compose up --build
```

Проверка API:

```bash
curl http://localhost:8000/api/v1/health
```

Локальная разработка без Docker:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

## Миграции

После первого запуска PostgreSQL создайте стартовую миграцию и примените её:

```bash
alembic revision --autogenerate -m "initial schema"
alembic upgrade head
```

## LLM

В `.env` выберите один провайдер:

```dotenv
LLM_PROVIDER=openai
OPENAI_API_KEY=...
# или
LLM_PROVIDER=gigachat
GIGACHAT_AUTH_KEY=...
```

`app/services` не зависит от SDK провайдера: адаптеры отвечают только за авторизацию и запрос к модели. Следующими flows логично добавить `fair_assignment`, `adaptive_reminders` и `conflict_mediation` по той же схеме.

## Первые API-контракты

| Экран | Контракт |
| --- | --- |
| Онбординг | `POST /api/v1/families` |
| Сегодняшние дела | `GET /api/v1/tasks/today?family_id=...` |
| Добавление задачи | `POST /api/v1/tasks` |
| Вклад участников | `GET /api/v1/statistics/workload?family_id=...` |
| Приглашение | `POST /api/v1/invitations` |
| Парсинг входящих данных | `POST /api/v1/ai/extract-task` |
