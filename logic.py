def generate_response(user_message):
    # Lowercase the message to make matching case insensitive
    user_message = user_message.lower()

    # Respond based on what the user asked about
    if "festival" in user_message:
        return "Which festival would you like to know about? (e.g., Diwali, Holi, Eid, Navratri)"
    elif "diwali" in user_message:
        return get_festival_info("diwali")
    elif "holi" in user_message:
        return get_festival_info("holi")
    elif "eid" in user_message:
        return get_festival_info("eid")
    elif "navratri" in user_message:
        return get_festival_info("navratri")
    elif "dance" in user_message:
        return "What type of dance would you like to know about? (e.g., Bharatnatyam, Kathak, Odissi)"
    elif "bharatnatyam" in user_message:
        return get_dance_info("bharatnatyam")
    elif "kathak" in user_message:
        return get_dance_info("kathak")
    elif "odissi" in user_message:
        return get_dance_info("odissi")
    elif "food" in user_message:
        return "What type of food would you like to know about? (e.g., Biryani, Dosa, Samosa)"
    elif "biryani" in user_message:
        return get_food_info("biryani")
    elif "dosa" in user_message:
        return get_food_info("dosa")
    elif "samosa" in user_message:
        return get_food_info("samosa")
    elif "attire" in user_message:
        return "What type of attire would you like to know about? (e.g., Sari, Kurta, Sherwani)"
    elif "sari" in user_message:
        return get_attire_info("sari")
    elif "kurta" in user_message:
        return get_attire_info("kurta")
    elif "sherwani" in user_message:
        return get_attire_info("sherwani")
    elif "languages" in user_message:
        return "What language would you like to know about? (e.g., Hindi, Tamil, Bengali, Marathi, Gujarati)"
    elif "hindi" in user_message:
        return get_language_info("hindi")
    elif "marathi" in user_message:  # Ensure 'marathi' is case insensitive
        return get_language_info("marathi")
    elif "gujarati" in user_message:  # Ensure 'gujarati' is case insensitive
        return get_language_info("gujarati")
    elif "tamil" in user_message:
        return get_language_info("tamil")
    elif "bengali" in user_message:
        return get_language_info("bengali")
    else:
        return "Sorry, I didn't understand that. Can you please be more specific?"

def get_festival_info(festival):
    festival_data = {
        "diwali": "Diwali is the festival of lights, celebrated by Hindus, Sikhs, Jains, and Buddhists.\nIt signifies the victory of light over darkness.\nThe festival is celebrated to honor the return of Lord Rama to his kingdom in Ayodhya after 14 years of exile, during which he defeated the demon king Ravana.\nThe people of Ayodhya lit oil lamps (diyas) to welcome him back, symbolizing the triumph of light",
        "holi": "Holi is the festival of colors, celebrated by Hindus to mark the arrival of spring.\nThe festival is linked to the story of Prahlad, a devotee of Lord Vishnu, and the demoness Holika. It symbolizes the victory of devotion and righteousness over evil.\nOn the eve of Holi, people light bonfires (Holika Dahan) to symbolize the burning away of evil",
        "eid": "Eid is a Muslim festival marking the end of Ramadan, known for feasts and charity.\n It is celebrated at the end of Ramadan, the holy month of fasting\n Muslims who can afford it sacrifice an animal (usually a goat, sheep, or cow) and distribute the meat among family, friends, and the needy.",
        "navratri": "Navratri is a Hindu festival that celebrates the goddess Durga. It's a time for fasting, prayer, and dance.\nNavratri means nine nights in Sanskrit. The festival symbolizes the triumph of good over evil, as it celebrates Goddess Durga's victory over the demon Mahishasura."
    }
    return festival_data.get(festival, "Sorry, I don't have information on that festival.")

def get_dance_info(dance):
    dance_data = {
        "bharatnatyam": "Bharatanatyam is a classical dance form from Tamil Nadu, India, known for its intricate footwork, expressive hand gestures, and graceful movements. It tells stories from Hindu mythology and is performed to Carnatic music. The dance is a blend of devotion, storytelling, and emotion.",
        "kathak": "Kathak is a classical dance form from North India, renowned for its storytelling, intricate footwork, and spins. It combines expressions, rhythmic movements, and storytelling through gestures, often depicting themes from Hindu mythology. Kathak is performed to classical music, with an emphasis on rhythm and grace.",
        "odissi": "Odissi is a classical dance form from Odisha, famous for its graceful, fluid movements and temple-inspired poses. It emphasizes intricate footwork, expressive hand gestures, and elegant body postures, often depicting themes of devotion and mythology. The dance is performed to traditional Odissi music and rhythms."
    }
    return dance_data.get(dance, "Sorry, I don't have information on that dance style.")

def get_food_info(food):
    food_data = {
        "biryani": "Biryani is a flavorful and aromatic rice dish made with meat (such as chicken, mutton, or beef) or vegetables, often cooked with fragrant spices like saffron, cinnamon, and cardamom. It is a popular dish in India, Pakistan, and other South Asian countries, known for its rich taste and layered preparation. Biryani is typically served with raita, salad, or a boiled egg.",
        "dosa": "Dosa is a thin, crispy pancake made from a fermented batter of rice and lentils, popular in South India. It is typically served with a variety of chutneys and sambar (a spicy lentil soup). Dosa is a versatile dish, enjoyed as breakfast, snack, or main course, with variations like masala dosa, which is filled with spiced potatoes.",
        "samosa": "Samosa is a deep-fried pastry filled with a mixture of spiced potatoes, peas, and sometimes meat, often seasoned with cumin, coriander, and garam masala. It is a popular snack in India and other South Asian countries, typically served with chutneys like tamarind or mint. Samosas are enjoyed for their crispy texture and flavorful filling."
    }
    return food_data.get(food, "Sorry, I don't have information on that food item.")

def get_attire_info(attire):
    attire_data = {
        "sari": " A sari is a traditional Indian garment worn by women, consisting of a long piece of cloth draped elegantly around the body, typically paired with a blouse and petticoat. It is often worn during festivals, ceremonies, and weddings.",
        "kurta": "A kurta is a loose-fitting tunic worn by both men and women, usually paired with trousers, leggings, or traditional bottoms like churidars or salwars. It is a comfortable and versatile garment often worn for casual or formal occasions.",
        "sherwani": "A sherwani is a formal coat worn by men, typically with a close-fitting design and intricate embroidery. It is commonly worn during weddings, celebrations, or other grand events, often paired with a churidar or trousers."
    }
    return attire_data.get(attire, "Sorry, I don't have information on that attire.")

def get_language_info(language):
    language_data = {
        "hindi": "Hindi is one of the most widely spoken languages in India, written in the Devanagari script. It serves as a primary language of communication in various parts of India and is one of the official languages of the country.",
        "tamil": "Tamil is a Dravidian language spoken primarily in Tamil Nadu, India, and Sri Lanka. It has a rich literary history and is one of the longest-surviving classical languages in the world.",
        "bengali": "Bengali is spoken in the Indian state of West Bengal and Bangladesh, written in the Bengali script. It is the second-most spoken language in India and has a rich cultural and literary heritage.",
        "marathi": "Marathi is an Indo-Aryan language spoken predominantly in the state of Maharashtra, written in the Devanagari script. It has a rich literary tradition and is one of the 22 scheduled languages of India.",
        "gujarati": "Gujarati is an Indo-Aryan language spoken primarily in the state of Gujarat. It is written in the Gujarati script and is known for its extensive literature, including poetry, prose, and classical texts."
    }
    return language_data.get(language, "Sorry, I don't have information on that language.")
