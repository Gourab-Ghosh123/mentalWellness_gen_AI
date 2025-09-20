from django.shortcuts import render
import requests
# Create your views here.


def mood_suggestions(request):
    suggestions = None
    if request.method == "POST":
        user_text = request.POST.get("feeling" , "").lower()
        # First Let's call the Zenquotes API for quotes
        quote_resp = requests.get("https://zenquotes.io/api/random")
        if quote_resp.status_code == 200:
            quote_data = quote_resp.json()
            quote = f"{quote_data[0]['q']} - {quote_data[0]['a']}"
        else:
            quote = "Keep going bud , trust me you are really ... Really doing GReaatt!!!"



        # Now let's create a dictionary for songs based on the user's mood
        mood_songs = {
            "sad" :{"Title" : "Weightless - Marconi Union","youtube" : "UfcAVejslrU"},
            "stressed" : {"Title" : "Weightless - Marconi Union","youtube" : "UfcAVejslrU"},
            "happy" : {"Title" : "Weightless - Marconi Union","youtube" : "UfcAVejslrU"},
            "default" : {"Title" : "Weightless - Marconi Union","youtube" : "UfcAVejslrU"}
        }
        if "sad" in user_text:
            song = mood_songs["sad"]
        elif "stressed" in user_text:
            song = mood_songs["stressed"]
        elif "happy" in user_text:
            song = mood_songs["happy"]
        else:
            song = mood_songs["default"]

        # Now let's create a dictionary for exercises based on the user's mood
        mood_exercises = {
            "sad" : "10 minutes of Yoga and Deep Breathing",
            "stressed" : "15 minutes of Cardio",
            "happy" : "A quick 5-minute walk to keep the vibes going",
            "default" : "10 minutes of Meditation"
        }
        remedies = {
            "sad" : "Let's watch the latest series that was out on Netflix you love with a cup of chilled cappucino! ˙✧˖°☕ ༘ ⋆｡˚",
            "stressed" : "Let's go on a walk to that  river bank you love and listen to the sound of flowing water! 🌊",
            "happy" : "Let's call up a friend and share what made you happy today! 📞",
            "default" : "Let's read a chapter from that book you love with a cup of hot chocolate! 📖"
        }

        mood = "default"
        if "sad" in user_text:
            mood = "sad"
        elif "stress" in user_text or "anxious" in user_text:
            mood = "stressed"
        elif  "happy" in user_text or "excited" in user_text:
            mood = "happy"

        #Collect Suggestions
        suggestions = {
            "song_title" : song["Title"],
            "youtube" : song["youtube"],
            "quote" : quote,
            "exercise" : mood_exercises[mood],
            "remedy" : remedies[mood]
        }
    return render(request , "mood_suggestions.html" , {"suggestions" : suggestions})
