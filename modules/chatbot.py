# modules/chatbot.py

def respond(user_input):
    user_input = user_input.lower()
    if "ahoj" in user_input or "čau" in user_input:
        return "Ahoj! Jak ti mohu pomoci s rozpoznáním mincí?"
    elif "pomoc" in user_input:
        return "Jsem tu, abych pomohl s rozpoznáváním mincí. Nahraj obrázek mince a já se na ni podívám!"
    elif "děkuji" in user_input:
        return "Není zač! 🙂"
    else:
        return "Omlouvám se, nerozumím. Můžeš to říct jinak?"
