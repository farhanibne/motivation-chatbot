
import random


motivational_messages = [
    

    "You are capable of amazing things!",
    
    "Believe you can and you're halfway there.",
    
    "Every day is a new opportunity to grow and improve.",
    
    "Don't let small minds convince you that your dreams are too big.",
    
    "You have the power to create the life you want.",
    
    "The only limit to our realization of tomorrow will be our doubts of today.",
    
    "Life isnt about getting and having, its about giving and being."
    
    "Whatever the mind of man can conceive and believe, it can achieve.",

    "Strive not to be a success, but rather to be of value.",

    "Two roads diverged in a wood, and I—I took the one less traveled by, And that has made all the difference.",

    "I attribute my success to this: I never gave or took any excuse.",

    "You miss 100% of the shots you don't take.",

    "I've missed more than 9000 shots in my career. I've lost almost 300 games. 26 times I've been trusted to take the game winning shot and missed. I've failed over and over and over again in my life. And that is why I succeed.",
    "The most difficult thing is the decision to act, the rest is merely tenacity.",

    "Every strike brings me closer to the next home run.",

    "Definiteness of purpose is the starting point of all achievement.",
    "We must balance conspicuous consumption with conscious capitalism.",

    "Life is what happens to you while you're busy making other plans.",

    "We become what we think about.",

    "Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did do, so throw off the bowlines, sail away from safe harbor, catch the trade winds in your sails.  Explore, Dream, Discover.",

    "Life is 10% what happens to me and 90% of how I react to it.",
    "The most common way people give up their power is by thinking they don't have any.",

    "The mind is everything. What you think you become.",

    "The best time to plant a tree was 20 years ago. The second best time is now.",

    "An unexamined life is not worth living.",

    "Eighty percent of success is showing up.",

    "Your time is limited, so don't waste it living someone else's life.",

    "Winning isn't everything, but wanting to win is.",

    "I am not a product of my circumstances. I am a product of my decisions.",

    "Every child is an artist.  The problem is how to remain an artist once he grows up.",

    "You can never cross the ocean until you have the courage to lose sight of the shore.",

    "I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.",

    "Either you run the day, or the day runs you.",

    "Whether you think you can or you think you can't, you're right.",

    "The two most important days in your life are the day you are born and the day you find out why.",

    "Whatever you can do, or dream you can, begin it.  Boldness has genius, power and magic in it.",

    "The best revenge is massive success.",

    "People often say that motivation doesn't last. Well, neither does bathing.  That's why we recommend it daily.",

    "Life shrinks or expands in proportion to one's courage.",

    "If you hear a voice within you say “you cannot paint,” then by all means paint and that voice will be silenced.",

    "There is only one way to avoid criticism: do nothing, say nothing, and be nothing.",

    "Ask and it will be given to you; search, and you will find; knock and the door will be opened for you.",

    "The only person you are destined to become is the person you decide to be.",

    "Go confidently in the direction of your dreams.  Live the life you have imagined.",

    "When I stand before God at the end of my life, I would hope that I would not have a single bit of talent left and could say, I used everything you gave me.",

    "Few things can help an individual more than to place responsibility on him, and to let him know that you trust him.",

    "Certain things catch your eye, but pursue only those that capture the heart.",

    "Believe you can and you're halfway there.",

    "Everything you've ever wanted is on the other side of fear.",

    "We can easily forgive a child who is afraid of the dark; the real tragedy of life is when men are afraid of the light.",

    "Teach thy tongue to say, “I do not know,” and thous shalt progress.",

    "Start where you are. Use what you have.  Do what you can.",

    "When I was 5 years old, my mother always told me that happiness was the key to life.  When I went to school, they asked me what I wanted to be when I grew up.  I wrote down 'happy'.  They told me I didn't understand the assignment, and I told them they didn't understand life.",

    "Fall seven times and stand up eight.",

    "When one door of happiness closes, another opens, but often we look so long at the closed door that we do not see the one that has been opened for us.",

    "Everything has beauty, but not everyone can see.",

    "How wonderful it is that nobody need wait a single moment before starting to improve the world.",

    "When I let go of what I am, I become what I might be.",

    "Life is not measured by the number of breaths we take, but by the moments that take our breath away.",

    "Happiness is not something readymade.  It comes from your own actions.",
    "If you're offered a seat on a rocket ship, don't ask what seat! Just get on.",

    "First, have a definite, clear practical ideal; a goal, an objective. Second, have the necessary means to achieve your ends; wisdom, money, materials, and methods. Third, adjust all your means to that end.",

    "If the wind will not serve, take to the oars.",

    "You can't fall if you don't climb.  But there's no joy in living your whole life on the ground.",

    "We must believe that we are gifted for something, and that this thing, at whatever cost, must be attained.",

    "Too many of us are not living our dreams because we are living our fears.",

    "Challenges are what make life interesting and overcoming them is what makes life meaningful.",

    "If you want to lift yourself up, lift up someone else.",
    "I have been impressed with the urgency of doing. Knowing is not enough; we must apply. Being willing is not enough; we must do.",

    "Limitations live only in our minds.  But if we use our imaginations, our possibilities become limitless.",

    "You take your life in your own hands, and what happens? A terrible thing, no one to blame.",

    "What's money? A man is a success if he gets up in the morning and goes to bed at night and in between does what he wants to do.",

    "I didn't fail the test. I just found 100 ways to do it wrong.",

    "In order to succeed, your desire for success should be greater than your fear of failure.",

    "A person who never made a mistake never tried anything new.",

    "The person who says it cannot be done should not interrupt the person who is doing it.",

    "There are no traffic jams along the extra mile.",

    "It is never too late to be what you might have been.",

    "You become what you believe.",
    "I would rather die of passion than of boredom.",

    "A truly rich man is one whose children run into his arms when his hands are empty.",

    "It is not what you do for your children, but what you have taught them to do for themselves, that will make them successful human beings.",

    "If you want your children to turn out well, spend twice as much time with them, and half as much money.",

    "Build your own dreams, or someone else will hire you to build theirs.",

    "The battles that count aren't the ones for gold medals. The struggles within yourself-the invisible battles inside all of us-that's where it's at.",

    "Education costs money.  But then so does ignorance.",

    "I have learned over the years that when one's mind is made up, this diminishes fear.",

    "It does not matter how slowly you go as long as you do not stop.",

    "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",

    "Remember that not getting what you want is sometimes a wonderful stroke of luck.",
    "You can't use up creativity.  The more you use, the more you have.",

    "Dream big and dare to fail.",

    "Our lives begin to end the day we become silent about things that matter.",

    "Do what you can, where you are, with what you have.",

    "If you do what you've always done, you'll get what you've always gotten.",

    "Dreaming, after all, is a form of planning.",

    "It's your place in the world; it's your life. Go on and do all you can with it, and make it the life you want to live.",

    "You may be disappointed if you fail, but you are doomed if you don't try.",

    "Remember no one can make you feel inferior without your consent.",

    "Life is what we make it, always has been, always will be.",

    "The question isn't who is going to let me; it's who is going to stop me.",

    "When everything seems to be going against you, remember that the airplane takes off against the wind, not with it.",

    "It's not the years in your life that count. It's the life in your years.",

    "Change your thoughts and you change your world.",

    "Either write something worth reading or do something worth writing.",

    "Nothing is impossible, the word itself says, “I'm possible!”",

    "The only way to do great work is to love what you do.",
    "If you can dream it, you can achieve it."
]


def generate_motivational_message():
    return random.choice(motivational_messages)


while True:

    user_input = input("You: ")


    if user_input.lower() == "motivate me" or user_input.lower() == "motivate me please" or user_input.lower() == "motivate"  :

        message = generate_motivational_message()
        print("Chatbot: " + message)
    else:

        print("Chatbot: I don't understand. Please type 'motivate me' to get a motivational message. As you know i can only do that 😅.")



