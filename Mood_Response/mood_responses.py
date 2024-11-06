# Custom Module for Mood Responses

def mood_response(mood):
    if mood == "happy":
        return "It's great to see you happy!"
    elif mood == "nervous":
        return "Take a deep breath 3 times."
    elif mood == "sad":
        return "I'm sorry to hear that. I hope you feel better soon."
    elif mood == "excited":
        return "That's awesome! What has you feeling so excited?"
    elif mood == "relaxed":
        return "Great! Relaxation is key."
    elif mood == "angry":
        return "Calm down! Please don't hit me."
    else:
        return "I don't recognize that mood."