from django.shortcuts import render_to_response
import openai, os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)

def chatbot(request):
    chatbot_response = None
    if api_key is not None and if request.method == 'POST'
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input

        responce = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 4000,
        n = 1,
        stop = None,
        temperature = 0.5,
    )
    return render(request,'form.html',{})