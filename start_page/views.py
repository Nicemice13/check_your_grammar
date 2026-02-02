from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Content

def start_page(request):
    context = {}
    if request.user.is_authenticated:
        context['contents'] = Content.objects.filter(user=request.user)[:10]
    return render(request, 'start_page/index.html', context)

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