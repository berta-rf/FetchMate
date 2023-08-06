# Import model
from app import db, Question, app


# Array of quiz questions
questions = [
    # 1. shedding
    {
        "question": "How do you feel about sharing your space with some extra fur?",
        "options": {
            "a": "I'm cool with any shedding.",
            "b": "I don't mind some shedding.",
            "c": "I'd rather keep it to minimal shedding.",
            "d": "I'd prefer almost no hair, my vacuum's on a diet.",
            "e": "No shedding at all, please!",
        },
        "param": "shedding",
    },
    # 2. barking
    {
        "question": "How do you vibe with canine vocalizations?",
        "options": {
            "a": "I don't mind a good bark-concert now and then.",
            "b": "A little barking is okay.",
            "c": "I prefer a quieter, more chill companion.",
            "d": "Rare barks, please!",
            "e": "Silence is golden with a dog.",
        },
        "param": "barking",
    },
    # 3. playfulness
    {
        "question": "What level of daily activity are you excited to share with your future pup?",
        "options": {
            "a": "Bring on the adventures! I'm an active soul.",
            "b": "I enjoy a good balance of play and relaxation. Couch Olympics, anyone?",
            "c": "I'm up for playtime, but not too intense. A leisurely game of fetch, perhaps?",
            "d": "A calm companion is more my thing.",
            "e": "Couch potato mode, please! Let's set a new record for belly rubs.",
        },
        "param": "playfulness",
    },
    # 4. trainability
    {
        "question": "How patient are you with the training process?",
        "options": {
            "a": "I'm ready to put in the work for a clever and obedient friend.",
            "b": "I'm happy to train, but maybe not every day.",
            "c": "I'm willing to train, but prefer quick learners.",
            "d": "Training? Maybe a little. Just enough to master the basics.",
            "e": "I'd rather avoid training challenges. Canine college dropout here!",
        },
        "param": "trainability",
    },
    # # 5. size
    # {
    #     "question": "What size of canine companion best fits your lifestyle?",
    #     "options": {
    #         "a": "The bigger, the better! Let's go large.",
    #         "b": "A big dog but not so big that it will be taking me for walks.",
    #         "c": "A medium-sized amigo is just right. Not too big, not too small, just fur-tastic!",
    #         "d": "A smaller sidekick suits me just fine.",
    #         "e": "Miniature is my choice. Compact cuteness is where it's at.",
    #     },
    #     "param": "?",
    # },
    # 6. protectiveness
    {
        "question": "How do you envision your pup's role when it comes to guarding your kingdom?",
        "options": {
            "a": "I'd appreciate a watchful protector by my side. A loyal guardian who moonlights as a cuddle buddy.",
            "b": "I'm looking for a good balance of protector and friendliness. Diplomat by day, security chief by night.",
            "c": "A friendly attitude with a bit of caution. Barking at strangers but making friends at the park.",
            "d": "I prefer a more easygoing, less protective pal.",
            "e": "I'm looking for a friend who's friendly to all.",
        },
        "param": "protectiveness",
    },
    # # 7. life expectancy
    # {
    #     "question": "How many years of companionship are you aiming for?",
    #     "options": {
    #         "a": "I'm in it for the long haul. We're growing old and wrinkly together!",
    #         "b": "A healthy lifespan is important to me. Quality and quantity, that's the goal.",
    #         "c": "A moderate lifespan suits my plans.",
    #         "d": "I'm looking for a shorter-term commitment. A brief but beautiful chapter in my life story.",
    #         "e": "Any time together is precious.",
    #     },
    #     "param": "?"
    # },
    #
    # 8. walking frequency
    {
        "question": "How often are you excited to lace up those trainers and hit the park?",
        "options": {
            "a": "Twice a day runs are my thing!",
            "b": "Regular, daily walks make for a great routine.",
            "c": "I'm more of a leisurely walker.",
            "d": "Occasional walks suit me fine.",
            "e": "I'd prefer minimal outdoor time, I prefer indoor coziness.",
        },
        "param": "energy",
    },
]

with app.app_context():

    # Insert each question
    for question_obj in questions:

        new_question = Question(
            question_text=question_obj["question"],
            param=question_obj["param"],
            answer_1=question_obj["options"]["a"],
            answer_2=question_obj["options"]["b"],
            answer_3=question_obj["options"]["c"],
            answer_4=question_obj["options"]["d"],
            answer_5=question_obj["options"]["e"],
        )

        db.session.add(new_question)

    # Commit queries
    db.session.commit()
