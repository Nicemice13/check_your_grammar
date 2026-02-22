"""
Тестовый файл для работы с GigaChat API
Документация: https://developers.sber.ru/docs/ru/gigachain/tools/python/langchain-gigachat
"""

import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.chat_models.gigachat import GigaChat

# Загрузка переменных окружения
load_dotenv()

GIGACHAT_API_KEY = os.getenv('GIGACHAT_API_KEY')

if not GIGACHAT_API_KEY:
    raise ValueError("Не найден GIGACHAT_API_KEY в .env файле")

def test_gigachat_basic():
    """Базовый тест GigaChat API"""

    # Инициализация модели
    chat = GigaChat(
        credentials=GIGACHAT_API_KEY,
        verify_ssl_certs=False,
        scope="GIGACHAT_API_PERS"
    )

    # Простой запрос
    messages = [
        SystemMessage(content="Ты - помощник для проверки грамматики."),
        HumanMessage(content="Привет! Как дела?")
    ]

    response = chat.invoke(messages)
    print("Ответ GigaChat:", response.content)
    return response.content


def test_grammar_check(text: str):
    """Проверка грамматики текста через GigaChat"""

    chat = GigaChat(
        credentials=GIGACHAT_API_KEY,
        verify_ssl_certs=False,
        scope="GIGACHAT_API_PERS"
    )

    messages = [
        SystemMessage(content="Ты - эксперт по проверке грамматики. Исправь ошибки в тексте и верни только исправленный вариант."),
        HumanMessage(content=text)
    ]

    response = chat.invoke(messages)
    print(f"Исходный текст: {text}")
    print(f"Исправленный текст: {response.content}")
    return response.content


def test_multilingual_check(text: str, language: str):
    """Проверка грамматики с указанием языка"""

    chat = GigaChat(
        credentials=GIGACHAT_API_KEY,
        verify_ssl_certs=False,
        scope="GIGACHAT_API_PERS"
    )

    lang_names = {
        'ru': 'русском',
        'en': 'английском',
        'zh': 'китайском',
        'es': 'испанском'
    }

    messages = [
        SystemMessage(content=f"Ты - эксперт по проверке грамматики на {lang_names.get(language, 'русском')} языке. Исправь все грамматические, орфографические и пунктуационные ошибки. Верни только исправленный текст без комментариев."),
        HumanMessage(content=text)
    ]

    response = chat.invoke(messages)
    return response.content


if __name__ == "__main__":
    print("=== Тест 1: Базовая проверка ===")
    try:
        test_gigachat_basic()
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\n=== Тест 2: Проверка грамматики ===")
    try:
        test_text = "Я пошол в магазин и купил молоко."
        test_grammar_check(test_text)
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\n=== Тест 3: Мультиязычная проверка ===")
    try:
        test_text_en = "I goed to the store yesterday."
        result = test_multilingual_check(test_text_en, 'en')
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")
