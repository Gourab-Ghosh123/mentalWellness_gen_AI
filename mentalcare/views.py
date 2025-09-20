from django.shortcuts import redirect, render
import random
from .models import ChatMessage
from django.contrib.auth.decorators import login_required 
import httpx
from .forms import MoodSliderform
from .models import MoodSlider
from datetime import timedelta , date


# Create your views here.


def home(request):

    #Chat on lading page
    chat = ChatMessage.objects.all() #All chats fetched haha

    #Mood Slider
    form = MoodSliderform()  # An empty form created
    today = date.today()

    # If the user is already logged-in  today's mood , then preload the slider value
    existing = None
    if request.user.is_authenticated:
        existing = MoodSlider.objects.filter(user = request.user , date = today).first()
        if existing :
            form = MoodSliderform(instance=existing)

    return render(request , 'index.html' , {'form' : form , 'chat' : chat})



#giving fake responses through strings for testing it a bit
'''@login_required
def chat_view(request):
    if request.method == "POST":
        user_message = request.POST.get("message") #Gets the message typed by the user in the place of the "message"

        #Fake AI responses(will be replacing with API later on....)
        ai_resposnses = [
            "I hear you 👂💙",
            "That sounds tough, but you’re strong 💪",
            "I’m glad you shared this 🫂",
            "✨ Remember to take a deep breath ✨",
            "Sending you positivity 🌸"
        ]
        response = random.choice(ai_resposnses)

        ChatMessage.objects.create(
            user = request.user,
            message =user_message,
            response = response
        )
        return redirect("chat")
    
    chats = ChatMessage.objects.filter(user=request.user).order_by("-timestamp")[:10]
    return render(request , "chat.html"  , {"chats" : chats})'''



#Okay now time for the real Caht responses , we aint using openai cuz I am broke lmao
#Instead we be using GPT4All , a locat bot which I installed on my system :P


#Update :- my pc sucks , lagged like hell , so we are back to integrating free API,s lol

#Its the Open Router api haha!

@login_required
def chat_view(request):
    ai_response = None
    user_message = None
    
    if request.method == "POST":
        user_message = request.POST.get("message")


        #Okay so now then let's call the Groq API then...
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization" : "Bearer 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" ,
            "Content-Type" : 'Application/json'
        }

        data = {
            "model" : "llama-3.1-8b-instant", # for empathy and smart replies
            "messages" : [
                {"role" : "system" , "content" : "You are a friendly and empathetic mental wellness assistant ."},
                {"role": "system", "content": "..."},
                {"role": "user", "content": "Hi!"},
                 {"role": "assistant", "content": "Hey! How are you feeling today?"},
                {"role" : "user" , "content" : user_message},
            ]
        }
        try :
            with httpx.Client(timeout=30.0) as client :
                response = client.post(url , headers=headers , json=data)
                result = response.json()
                ai_response =result["choices"][0]["message"]["content"]

                # Okay now saving the chat in DB...
                ChatMessage .objects.create(
                    user = request.user ,
                    message = user_message ,
                    response = ai_response
                )


        except Exception as e :
            ai_response = f"⚠️ Error : {str(e)}"
    
    # Fetches the last 10 recent chats
    chats = ChatMessage.objects.filter(user = request.user).order_by("timestamp")
        
    return render(request , "chat.html" , {"ai_response" : ai_response ,
                                         "user_message" : user_message,
                                         "chats" : chats
                                         })


@login_required
def clear_chat(request):
    if request.method == "POST":
        ChatMessage.objects.filter(user = request.user).delete()
    return redirect("chat")





#Mood Slider View....  
@login_required
def mood_slider_view(request):
    if request.method == "POST":
        mood_value = int(request.POST.get("mood"))
        MoodSlider.objects.create(user=request.user, mood_value=mood_value)

    moods = MoodSlider.objects.filter(user=request.user).order_by("-date")
    return render(request, "mood_slider.html", {"moods": moods})



def about_view(request):
    return render(request , "about.html")