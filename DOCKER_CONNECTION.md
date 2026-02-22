# Подключение к PostgreSQL в Docker

## Статус контейнера
✅ Контейнер запущен: `check_grammar_db`
✅ База данных: `check_grammar`
✅ Порт: `5433` (внешний) → `5432` (внутренний)
✅ Функция search_word создана

## Параметры подключения

```
Host: localhost
Port: 5433
Database: check_grammar
Username: postgres
Password: postgres
```

## Подключение через VS Code (PostgreSQL Extension)

1. Установите расширение: **PostgreSQL** (от Chris Kolkman)
2. Нажмите `Ctrl+Shift+P` → "PostgreSQL: Add Connection"
3. Введите параметры:
   - Hostname: `localhost`
   - Username: `postgres`
   - Password: `postgres`
   - Port: `5433`
   - Database: `check_grammar`
   - Connection name: `check_grammar_docker`

## Команды Docker

```bash
# Запустить контейнер
docker start check_grammar_db

# Остановить контейнер
docker stop check_grammar_db

# Подключиться к БД через CLI
docker exec check_grammar_db psql -U postgres -d check_grammar

# Просмотр таблиц
docker exec check_grammar_db psql -U postgres -d check_grammar -c "\dt"

# Выполнить SQL-запрос
docker exec check_grammar_db psql -U postgres -d check_grammar -c "SELECT * FROM start_page_content LIMIT 5;"
```

## Проверка функции search_word

```bash
# Проверить наличие функции
docker exec check_grammar_db psql -U postgres -d check_grammar -c "\df search_word"

# Тестовый запрос
docker exec check_grammar_db psql -U postgres -d check_grammar -c "SELECT * FROM search_word('текст');"
```
