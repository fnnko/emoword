from django.shortcuts import render, get_object_or_404
from .models import Emotion, Message

import random

def start_view(request):
    return render(request, 'words/start.html')

def emotion_select_view(request):
    emotions = Emotion.objects.all()

    context = {'emotions': emotions}
    return render(request, 'words/emotions.html', context)

def message_view(request, emotion_id):
    emotion = get_object_or_404(Emotion, id=emotion_id)
    quotes = Message.objects.filter(emotion=emotion)
    quote = random.choice(quotes) if quotes else None

    context = {'emotion':emotion, 'quote': quote }
    return render(request, 'words/quote.html', context)