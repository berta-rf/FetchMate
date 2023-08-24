# Import model
from app import db, Question, app



# Array of quiz questions
questions = [
    # 1. shedding
    {
        "question": "How do you feel about sharing your space with some extra fur?",
        "options": {
            "a": "No shedding at all, please!",
            "b": "I'd prefer almost no hair, my vacuum's on a diet.",
            "c": "I'd rather keep it to minimal shedding.",
            "d": "I don't mind some shedding.",
            "e": "I'm cool with any shedding.",
            "f": "I'm happy to resemble a fur coat ",
        },
        "param": "shedding",
    },
    # 2. barking
    {
        "question": "How do you vibe with canine vocalizations?",
        "options": {
            "a": "Silence is golden with a dog.",
            "b": "Rare barks, please!",
            "c": "I prefer a quieter, more chill companion.",
            "d": "A little barking is okay.",
            "e": "I don't mind a good bark-concert now and then.",
            "f": "My landlord said no dogs allowed so silence is an absolute must!",
        },
        "param": "barking",
    },
    # 3. playfulness
    {
        "question": "What level of daily activity are you excited to share with your future pup?",
        "options": {
            "a": "Couch potato mode, please! Let's set a new record for belly rubs.",
            "b": "A calm companion is more my thing.",
            "c": "I'm up for playtime, but not too intense. A leisurely game of fetch, perhaps?",
            "d": "I enjoy a good balance of play and relaxation. Couch Olympics, anyone?",
            "e": "Bring on the adventures! I'm an active soul.",
            "f": "I'm looking for a lazy, cuddle buddy",
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
            "f": "I'm after a dog that doesn't require training at all, does that exist?",
        },
        "param": "trainability",
    },
    # 5. protectiveness
    {
        "question": "How do you envision your pup's role when it comes to guarding your kingdom?",
        "options": {
            "a": "I'm looking for a friend who's friendly to all.",
            "b": "I prefer a more easygoing, less protective pal.",
            "c": "A friendly attitude with a bit of caution. Barking at strangers but making friends at the park.",
            "d": "I'm looking for a good balance of protector & friendliness. Diplomat by day, security chief by night.",
            "e": "I'd appreciate a watchful protector by my side. A loyal guardian who moonlights as a cuddle buddy.",
            "f": "I'm happy to be the protector for a scaredy cat",
        },
        "param": "protectiveness",
    },
    # 6. walking frequency
    {
        "question": "How often are you excited to lace up those trainers and hit the park?",
        "options": {
            "a": "I'd prefer minimal outdoor time, I prefer indoor coziness.",
            "b": "Occasional walks suit me fine.",
            "c": "I'm more of a leisurely walker.",
            "d": "Regular, daily walks make for a great routine.",
            "e": "Twice a day runs are my thing!",
            "f": "I'd rather a window watcher than a walker",
        },
        "param": "energy",
    },
    # 7. drooling
    {
        "question": "How do you feel about a dog's drooling habits?",
        "options": {
            "a": "I'm okay with drool, but not a swimming pool's worth.",
            "b": "Some drool is fine, but I don't want to be a raincoat-wearing dog owner.",
            "c": "I'd prefer a breed that doesn't drool excessively.",
            "d": "I'm looking for a dog that keeps the wet kisses to a minimum.",
            "e": "I'd rather have a breed that doesn't drool at all, but I don't think that exists.",
            "f": "I'm a bit of a clean freak so absolutely no drool",
        },
        "param": "drooling",
    },
    # 8. Good with other dogs
    {
        "question": "Do you see your puppy pal enjoying the company of other furry friends?",
        "options": {
            "a": "Absolutely! I'd love a breed that's a social butterfly and enjoys playdates.",
            "b": "My dog should get along with other dogs, but a few close pals are enough.",
            "c": "I'd prefer a breed that's friendly but doesn't mind some me-time too.",
            "d": "I'm looking for a breed that's content with human companionship and occasional dog interactions.",
            "e": "I'm seeking a breed that prefers human attention over canine camaraderie.",
            "f": "I'm a bit of a diva, so I want a dog that is all about me",
        },
        "param": "good_with_other_dogs",
    }
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
            answer_6=question_obj["options"]["f"],
        )

        db.session.add(new_question)

    # Commit queries
    db.session.commit()

