import random

question_pool = [
    "What about St. Edwards hall makes you feel at home?",
    "How are you feeling this week?",
    "What are some things that Steds could improve?",
    "What's something you learned this week?",
    "What was a high point for you this week?",
    "What was a low point for you this week?",
    "What's a message you would like to share with your younger self?",
    "What do you struggle with the most right now?",
    "What's your favorite part of being at Notre Dame?",
    "What's something most people don't know about you?",
    "What's your favorite way to build community within the dorm?",
    "What does St. Edwards hall mean to you?",
    "What do you think others should know about this week?",
    "How do you like to relax on the weekends?",
    "Why did you decide to go to Notre Dame?",
    "Are you having a good week?",
    "Do you feel at home in Steds?",
    "Are you traveling for spring break?",
    "Did you spend time outside today?",
    "Have you reached out to friends or family at home this week?",
    "Did you go to all of your classes this week?",
    "Are you feeling worried about midterms this week?",
    "Have you thought about what you're thankful for today?",
    "Have you explored any new places on campus this week?",
    "Have you maintained your relationships with neighbors and roommates this week?",
    "Do you plan to attend any campus events this weekend?",
    "Have you encountered any difficulties this week?",
    "Have you taken time to visit the chapel this week?",
    "Have you checked in with Fr. Ralph this week?",
    "Which floor is the best?",
    "What's the best dining hall?",
    "What's your favorite ND sport to watch?",
    "How do you feel this week?",
    "What do you feel you need the most right now?",
    "How much sleep do you usually get every night?",
    "How is your stress level this week?",
    "How often do you call your family?",
    "How connected do you feel to the dorm community?",
    "How often do you work out?",
    "What do you struggle with the most?",
    "What kind of person are you?",
    "What element best describes you?",
    "How many times did you skip class this week?",
    "How many meals do you usually eat in a day?"
]

def choose_one():
    return random.choice(question_pool)