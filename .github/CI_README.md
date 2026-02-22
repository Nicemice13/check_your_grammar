# CI/CD для Check Your Grammar

## GitHub Actions

Автоматический CI запускается при:
- Push в ветки `main` или `master`
- Создании Pull Request

## Что проверяет CI:

1. ✅ Установка зависимостей из `requirements.txt`
2. ✅ Применение миграций Django
3. ✅ Запуск тестов
4. ✅ PostgreSQL 16 в качестве тестовой БД

## Статус сборки

Проверить статус можно в разделе **Actions** вашего GitHub репозитория.

## Локальный запуск тестов

```bash
# Активировать виртуальное окружение
source venv/bin/activate

# Запустить тесты
python manage.py test

# Проверить миграции
python manage.py makemigrations --check --dry-run
```

## Добавление бейджа статуса

Добавьте в README.md:

```markdown
![CI](https://github.com/YOUR_USERNAME/check_your_grammar/workflows/CI/badge.svg)
```

Замените `YOUR_USERNAME` на ваше имя пользователя GitHub.
