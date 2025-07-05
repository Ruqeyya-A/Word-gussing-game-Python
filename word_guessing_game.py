import csv
import random
import os
all_categories = {
    '🥑 Fruits': {
        'grape': 'I am small, purple, and grow in bunches on vines.',
        'lemon': 'I’m yellow, sour, and often used in drinks or cleaning.',
        'mango': 'I’m tropical, sweet, and sometimes called the "king of fruits".',
        'peach': 'I’m fuzzy, juicy, and have a large pit in the center.',
        'pear': 'I’m bell-shaped, sweet, and come in green or red varieties.',
        'kiwi': 'I’m small, brown, fuzzy on the outside, and green inside with tiny black seeds.',
        'melon': 'I’m large, juicy, and can be watermelons or cantaloupes.',
        'blackberry': 'I’m a dark purple berry that grows on thorny bushes.',
        'raspberry': 'I’m a delicate red berry with a hollow core.',
        'watermelon': 'I’m 92% water, have black seeds, and are perfect for summer.'
    },
    '⚙️ Technology': {
        'app': 'Short for "application"; I run on your phone or computer.',
        'code': 'I’m a set of instructions that tell a computer what to do.',
        'data': 'I’m information stored and processed by computers.',
        'cookie': 'I’m a small piece of data stored by websites to remember you.',
        'domain': 'I’m the address of a website (e.g., google.com).',
        'encryption': 'I scramble data to keep it secure from hackers.',
        'artificial': 'Often paired with "intelligence"; I mimic human thinking.',
        'cybersecurity': 'I protect computers and networks from digital attacks.',
        'machinelearning': 'I allow computers to learn from data without explicit programming.',
        'algorithm': 'I’m a step-by-step procedure for calculations.',
        'javascript': 'I’m a programming language used for web interactivity.',
        'framework': 'I’m a reusable structure for building software applications.'
    },
    '🎊 Adjectives': {
        'happy': 'The opposite of sad; a feeling of joy.',
        'quick': 'Moving fast or done in a short time.',
        'brave': 'Showing courage in the face of danger.',
        'browser': 'A software used to access the internet (e.g., Chrome).',
        'mysterious': 'Difficult or impossible to understand.',
        'nervous': 'Feeling anxious or worried.',
        'flabbergasted': 'Extremely surprised or shocked.',
        'clever': 'Quick to understand or learn.',
        'jealous': 'Feeling envy toward someone else’s achievements.'
    },
    '🔮 Mythology': {
        'zeus': 'King of the gods, ruler of Mount Olympus, and god of thunder.',
        'athena': 'Goddess of wisdom, warfare, and crafts; born from Zeus’s head.',
        'persephone': 'Queen of the Underworld; spends half the year with Hades.'
    },
    '🎼 Music': {
        'note': 'A single sound of a particular pitch and duration.',
        'song': 'A musical composition with vocals.',
        'harmony': 'Multiple notes played together to create chords.',
        'chord': 'Three or more musical notes played simultaneously.',
        'choir': 'A group of singers performing together.'
    },
    '🐩 Animals': {
        'cat': 'A small, furry pet that purrs and loves to nap.',
        'lion': 'Known as the "king of the jungle"; has a majestic mane.',
        'frog': 'Amphibian that jumps and says "ribbit".',
        'whale': 'The largest mammal in the ocean; sings complex songs.',
        'zebra': 'African animal with black-and-white stripes.',
        'panda': 'A bear from China that eats bamboo.',
        'koala': 'Australian marsupial that sleeps 20 hours a day.',
        'giraffe': 'Tallest land animal with a long neck.',
        'hippopotamus': 'Large African mammal that spends time in water.',
        'chameleon': 'Lizard that changes color to blend in.',
        'kangaroo': 'Australian marsupial that hops and carries babies in a pouch.'
    },
    '🗺️ Countries': {
        'japan': 'Known for sushi, anime, and Mount Fuji.',
        'italy': 'Famous for pizza, pasta, and the Colosseum.',
        'brazil': 'Home to the Amazon rainforest and Carnival.',
        'canada': 'Known for maple syrup, hockey, and politeness.',
        'egypt': 'Land of pyramids, pharaohs, and the Nile River.',
        'thailand': 'Famous for its temples, beaches, and spicy food.',
        'argentina': 'Known for tango dancing and beef.',
        'switzerland': 'Famous for chocolate, watches, and the Alps.',
        'madagascar': 'Island nation with unique wildlife like lemurs.',
        'philippines': 'An archipelago known for its beaches and friendly people.'
    }
}
category = 0
word = 0
hint = 0
attempts = 10
score = 0
level = 1
def get_random_word_and_category():
    global hint
    category = random.choice(list(all_categories.keys()))
    word = random.choice(list(all_categories[category].keys()))
    hint = all_categories[category][word]
    return word, category



def word_diff():
    global level, word
    if level in [1, 2]:
        return [diff for diff in all_categories if len(diff) < 5]
    elif level in [3, 4]:
        print("Medium")
pool = word_diff()
def play_again():
    while True:
        ask = input("Play again (y/n)? ")
        if ask == 'y':
            game()
        else:
            print('Goodbye!')
            return False
        break


def game():
    global score, attempts, hint, level, pool
    word, category = get_random_word_and_category()
    print(f"Random word: '{word}' from category: {category}")
    word_arr = list(word)
    underscores_arr = ["_"] * len(word_arr)
    print(word_arr)
    print(hint)
    print("📐 LEVEL: ", level,            "\t\t\t\t📌 Score: ", score, "\t\t\t\t🎯 Attempts: ", attempts)
    while attempts > 0 and "_" in underscores_arr:
        print(" ".join(underscores_arr))

        guess = input("Guess a letter: ")

        if guess in word_arr:
            for n, letter in enumerate(word_arr):
                if letter == guess:
                    underscores_arr[n] = guess
                    score += 1
        elif guess == word:
            underscores_arr = list(word)
            print(" ".join(underscores_arr))
            break
        elif guess not in word_arr:
            print("Wrong guess. Try again!")
            attempts -= 1
    if "_" not in underscores_arr:
        print("You found the word!")
        level += 1
        play_again()



game()
word_diff()