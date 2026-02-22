import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.chat_models.gigachat import GigaChat

load_dotenv()

GIGACHAT_API_KEY = os.getenv('GIGACHAT_API_KEY')

def check_grammar_gigachat(text: str, language: str = 'ru') -> str:
    """
    Проверка грамматики текста через GigaChat
    
    Args:
        text: Исходный текст
        language: Язык текста (ru, en, zh, es)
    
    Returns:
        Исправленный текст
    """
    if not GIGACHAT_API_KEY:
        return text + " !"
    
    try:
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
        
    except Exception as e:
        print(f"Ошибка GigaChat: {e}")
        return text + " !"

def process_text(text: str, language: str = 'ru') -> str:
    """
    Обработка текста с помощью GigaChat
    """
    return check_grammar_gigachat(text, language)

def rephrase_text_gigachat(text: str, language: str = 'ru') -> str:
    """
    Перефразирование текста с подбором синонимов через GigaChat
    
    Args:
        text: Исходный текст
        language: Язык текста (ru, en, zh, es)
    
    Returns:
        Перефразированный текст
    """
    if not GIGACHAT_API_KEY:
        return text + " (перефразировано)"
    
    try:
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
            SystemMessage(content=f"Ты - эксперт по перефразированию текста на {lang_names.get(language, 'русском')} языке. Перефразируй текст, подбери синонимы к словам, сохраняя общий смысл. Верни только перефразированный текст без комментариев."),
            HumanMessage(content=text)
        ]
        
        response = chat.invoke(messages)
        return response.content
        
    except Exception as e:
        print(f"Ошибка GigaChat: {e}")
        return text + " (перефразировано)"

if __name__ == "__main__":
    input_text = input("Введите текст для обработки: ")
    result = process_text(input_text)
    print(result)