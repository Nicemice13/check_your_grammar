# Инструкция по активации CI/CD

## ✅ Изменения закоммичены локально

Коммит: `Add CI/CD with GitHub Actions`

## Следующий шаг: Push на GitHub

```bash
git push origin main
```

## После push:

1. Перейдите на GitHub: `https://github.com/YOUR_USERNAME/check_your_grammar`
2. Откройте вкладку **Actions**
3. Вы увидите запущенный workflow "CI"

## Если workflow не запустился:

1. Проверьте название ветки (должна быть `main` или `master`)
2. Убедитесь, что в настройках репозитория включены Actions:
   - Settings → Actions → General → Allow all actions

## Проверка статуса локально:

```bash
# Проверить, что файлы добавлены
git log --name-only -1

# Должны быть:
# .github/workflows/ci.yml
# .github/CI_README.md
# Check_your_grammar/settings.py
# requirements.txt
# .gitignore
```
