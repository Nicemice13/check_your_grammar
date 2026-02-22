from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Content
from user_page.gigachat_text_processing import check_grammar_gigachat, rephrase_text_gigachat

def start_page(request):
    context = {}
    if request.user.is_authenticated:
        search_query = request.GET.get('search', '')
        if search_query:
            context['contents'] = Content.objects.filter(user=request.user, corrected_text__icontains=search_query)
        else:
            context['contents'] = Content.objects.filter(user=request.user)[:10]
        context['search_query'] = search_query
    return render(request, 'start_page/index.html', context)

@login_required
@require_http_methods(["POST"])
def check_text(request):
    original_text = request.POST.get('original_text', '')
    language = request.POST.get('language') or 'ru'
    
    # Проверка текста через GigaChat
    checked_text = check_grammar_gigachat(original_text, language)
    
    return HttpResponse(checked_text)

@login_required
@require_http_methods(["POST"])
def rephrase_text(request):
    original_text = request.POST.get('original_text', '')
    language = request.POST.get('language') or 'ru'
    
    # Перефразирование текста через GigaChat
    rephrased_text = rephrase_text_gigachat(original_text, language)
    
    return HttpResponse(rephrased_text)

@login_required
@require_http_methods(["POST"])
def save_content(request):
    language = request.POST.get('language')
    corrected_text = request.POST.get('corrected_text')
    
    content = Content.objects.create(
        user=request.user,
        language=language,
        corrected_text=corrected_text
    )
    
    return render(request, 'start_page/content_item.html', {'content': content})

@login_required
@require_http_methods(["GET"])
def search_history(request):
    search_query = request.GET.get('search', '')
    contents = Content.objects.filter(user=request.user, corrected_text__icontains=search_query) if search_query else Content.objects.filter(user=request.user)[:10]
    return render(request, 'start_page/history_list.html', {'contents': contents})