label vol1_ch1_d1:
    scene black
    with fade
    centered "{b}Volume 1 - Chapter 1 - Day 1{/b}\n{i}Monday 1st January{/i}"

    scene bg bedroom_day
    with fade
    "I slowly open my eyes."
    "Sitting up, I look around in sleepy confusion."
    "This... isn't my room..."
    "I should be panicking... right?"
    "Why do I feel so calm?"
    "The click of a lock snapped me out of my thoughts."
    show hareka neutral_v1_1 with moveinleft
    "A girl enters."
    show hareka neutral_talk_v1_1
    hareka_unk "Oh. You're finally awake."
    show hareka neutral_v1_1
    "I nod."
    show hareka neutral_talk_v1_1
    hareka_unk "I suppose I should explain the situation."
    hareka "My name is Hareka Kiratani. I am an Arbiter working for the Government. I have been assigned to take you in due to a perceived threat which I am unable to disclose to you right now."
    show hareka neutral_v1_1
    "That's... a surprisingly thorough explanation."
    "Why do I feel so..."
    show hareka neutral_talk_v1_1
    hareka "I just need to double check against our records..."
    hareka "What is your name?"
    mc "Uhm... [player_name]..."
    show hareka neutral_v1_1
    if player_name == "Hareka":
        show hareka neutral_talk_v1_1
        hareka "[player_name]...?"
        hareka "Your name... is the same as mine."
        hareka "How interesting."
    if player_name == "hareka":
        show hareka neutral_talk_v1_1
        hareka "[player_name]...?"
        hareka "Your name... is the same as mine."
        hareka "How interesting."
    else:
        pass
    show hareka neutral_talk_v1_1
    hareka "[player_name]... Yes, that sounds correct. Thank you."
    hareka "Are you hungry, [player_name]? You've been knocked out for quite some time."
    show hareka neutral_v1_1
    mc "Y-Yes..."
    show hareka neutral_talk_v1_1
    hareka "Okay. I will make you some food."
    show hareka neutral_v1_1
    show hareka at left with move
    "She heads to the door, then turns back to me."
    show hareka neutral_talk_v1_1
    hareka "What would you like? I can only make simple things for now, since I'm new to cooking."
    hareka "The options would be buttered toast, a ham sandwich, or a microwaved pasta dish."
    show hareka neutral_v1_1
    menu vol1_ch1_d1_lunchslct:
        "The toast.":
            $ vol1_ch1_d1_lunchslct_toast = True
            show hareka neutral_talk_v1_1
            hareka "Okay, I will make you the toast."
            show hareka neutral_v1_1
            hide hareka with moveoutleft
            "Hareka leaves."
        "The sandwich.":
            $ vol1_ch1_d1_lunchslct_sandwich = True
            show hareka neutral_talk_v1_1
            hareka "Okay, I will make you the sandwich."
            show hareka neutral_v1_1
            hide hareka with moveoutleft
            "Hareka leaves."
        "The pasta.":
            $ vol1_ch1_d1_lunchslct_pasta = True
            show hareka neutral_talk_v1_1
            hareka "Okay, I will make you the pasta."
            show hareka neutral_v1_1
            hide hareka with moveoutleft
            "Hareka leaves."
    "I await patiently for her return."
    "{i}A few minutes later...{/i}"
    show hareka neutral_v1_1 with moveinleft
    "Hareka returns."
    show hareka neutral_talk_v1_1
    hareka "Here."
    show hareka neutral_v1_1
    if vol1_ch1_d1_lunchslct_toast:
        "She hands me a plate of evenly buttered toast."
    if vol1_ch1_d1_lunchslct_sandwich:
        "She hands me a plate with two fluffy-looking ham sandwiches."
    if vol1_ch1_d1_lunchslct_pasta:
        "She hands me a plate of steamy pasta."
    "I thank her and dig in."
    "It has been a while since I've eaten, so it's rather enjoyable."
    "When done, she takes the plate from me."
    show hareka neutral_talk_v1_1
    hareka "Did you enjoy it?"
    show hareka neutral_v1_1
    "I nod."
    show hareka neutral_talk_v1_1
    hareka "Good. I will wash this plate now."
    show hareka neutral_v1_1
    hide hareka with moveoutleft
    "She leaves once more."
    "I stand up, stretching. Lying down for so long has made me stiff."
    "I decide to look around the room."
    "It's plainly decorated, with beige colours and simple furniture."
    "Surprisingly though, it feels quite homey to me."
    "I really should be panicking, right? I mean, I got kidnapped by this strange girl..."
    "Yet somehow... I'm not scared at all."
    show hareka neutral_v1_1 with moveinleft
    "Soon enough, she returns."
    show hareka neutral_talk_v1_1
    hareka "Oh, you're moving around. Good. Your mobility seems fine."
    show hareka neutral_v1_1
    mc "Of course it is..."
    show hareka neutral_talk_v1_1
    hareka "What would you like to do? I am allowed to give you certain activities to keep you occupied."
    hareka "You can either read, play with LEGOs, or do some colouring."
    hareka "It's your choice."
    show hareka neutral_v1_1
    menu vol1_ch1_d1_activityslct:
        "Read.":
            $ vol1_ch1_d1_activityslct_read = True
            $ hareka_mana -= 25
            show hareka neutral_talk_v1_1
            hareka "Okay."
            show hareka neutral_v1_1
            "She waves her hand, and a pile of books appear on the bed."
            "Woaaaah..."
            show hareka neutral_talk_v1_1
            hareka "Take your pick."
            show hareka neutral_v1_1
            "I sift through the books, before ultimately deciding on one titled \"An Unforgettable Getaway\"."
            "I sit down and begin to read."
        "Play with the LEGO.":
            $ vol1_ch1_d1_activityslct_lego = True
            $ hareka_mana -= 75
            show hareka neutral_talk_v1_1
            hareka "Okay."
            show hareka neutral_v1_1
            "She waves her hand, and a box of LEGOs appears on the floor by the bed."
            "Woaaaah..."
            show hareka neutral_talk_v1_1
            hareka "You can build whatever you'd like."
            show hareka neutral_v1_1
            "I open the box and begin getting some pieces out."
            "This should keep me entertained for a while..."
            "Time to start building."
        "Do colouring.":
            $ vol1_ch1_d1_activityslct_colour = True
            $ hareka_mana -= 10
            show hareka neutral_talk_v1_1
            hareka "Okay."
            show hareka neutral_v1_1
            "She waves her hand, and a colouring book with coloured pencils appears on the bed."
            "Woaaaah..."
            show hareka neutral_talk_v1_1
            hareka "There should be enough there to keep you satisfied for a while."
            show hareka neutral_v1_1
            "I nod, sitting on the bed and flipping through the book."
            "There's some really cool looking designs here..."
            "I think this'll be fun."
            "I grab the pencils and begin to colour."
    scene bg bedroom_evening
    show hareka neutral_v1_1
    with dissolve
    "{i}A few hours later...{/i}"
    show hareka neutral_talk_v1_1
    hareka "It is time for dinner."
    show hareka neutral_v1_1
    "I look up at her."
    "It does look like the sun is setting outside..."
    "I'd been totally absorbed the entire time, and Hareka had been watching me closely."
    if vol1_ch1_d1_activityslct_read:
        "I fold the page where I am and close the book, putting it to one side."
    if vol1_ch1_d1_activityslct_lego:
        "I quickly tidy the LEGO pieces, fitting them neatly into the box, then put the box aside."
    if vol1_ch1_d1_activityslct_colour:
        "I close the colouring book and tidy the pencils, placing them both to one side."
    show hareka neutral_talk_v1_1
    hareka "I will go prepare dinner now."
    show hareka neutral_v1_1
    mc "Okay..."
    hide hareka with moveoutleft
    "She leaves again."
    "I await patiently for her return."
    scene bg bedroom_night
    with dissolve
    "{i}Fifteen minutes later...{/i}"
    show hareka neutral_v1_1 with moveinleft
    "She returns, carrying a tray with a bowl of soup, bread on the side, and water."
    show hareka neutral_talk_v1_1
    hareka "Here."
    show hareka neutral_v1_1
    "She hands me the tray."
    "I thank her and dig into the meal."
    "It's... delicious."
    "I enjoy it."
    "When finished, I hand the tray to Hareka."
    show hareka neutral_talk_v1_1
    hareka "I will wash the plates."
    show hareka neutral_v1_1
    "I nodded."
    show hareka neutral_talk_v1_1
    hareka "There are pajamas in the wardrobe. Get changed."
    show hareka neutral_v1_1
    hide hareka with moveoutleft
    "She leaves once more."
    "I head to the wardrobe and, sure enough, a set of fluffy-looking pajamas are waiting for me."
    "I get changed."
    "They're lovely and warm..."
    show hareka neutral_v1_1 with moveinleft
    "Hareka returns."
    show hareka neutral_talk_v1_1
    hareka "Do they fit you?"
    show hareka neutral_v1_1
    mc "Uhm, yes."
    show hareka neutral_talk_v1_1
    hareka "Good."
    show hareka neutral_v1_1
    "I head to get into bed, but she stops me."
    show hareka neutral_talk_v1_1
    hareka "Wait."
    hareka "You need to brush your teeth and wash your face first."
    show hareka neutral_v1_1
    mc "Ohh..."
    "It totally slipped my mind."
    show hareka neutral_talk_v1_1
    hareka "Follow me."
    show hareka neutral_v1_1
    "She grabs my hand and leads me out of the bedroom."

    scene bg bathroom
    show hareka neutral_v1_1
    with fade
    "We cross the hallway and enter the bathroom."
    "This is the first time I've been out of the bedroom..."
    show hareka neutral_talk_v1_1
    hareka "There's a toothbrush and washcloth there. Go on."
    show hareka neutral_v1_1
    show hareka at left with move
    "I head to the sink and brush my teeth, then wash my face."
    "Hareka keeps a close eye on me."
    show hareka neutral_talk_v1_1
    hareka "Alright, that's enough."
    show hareka neutral_v1_1
    show hareka at center with move
    "She turns off the water."
    show hareka neutral_talk_v1_1
    hareka "There, all clean."
    show hareka neutral_v1_1
    "I nod."
    "She grabs a towel and pats it around my face, drying me."
    "I smile as appreciation."
    show hareka neutral_talk_v1_1
    hareka "Let's go. It's bedtime for you."
    show hareka neutral_v1_1
    "I nod, following her once more."

    scene bg bedroom_night
    show hareka neutral_v1_1
    with fade
    "We return to the bedroom."
    show hareka neutral_talk_v1_1
    hareka "Right. Bedtime."
    show hareka neutral_v1_1
    "I obey, getting into bed."
    "It's nice and warm."
    "Hareka sits down at the desk."
    menu vol1_ch1_d1_enddayask:
        "Ask where she'll sleep.":
            show hareka neutral_talk_v1_1
            hareka "That is not your concern."
            hareka "Go to sleep."
        "Don't ask.":
            pass
    "I snuggle into bed and close my eyes."
    scene black
    with Fade(2.0)
    hareka "Goodnight, [player_name]."

    menu vol1_ch1_d1_completemenu:
        "Day complete!\nWould you like to restart the day, move onto the next day, or return to the menu?"
        "Restart the day.":
            centered "{b}{i}Restarting...{/b}{/i}"
            pause 1.5
            jump vol1_ch1_d1
        "Move on.":
            centered "{b}{i}Loading next day...{/b}{/i}"
            pause 1.5
            jump vol1_ch1_d2
        "Return to menu.":
            centered "{b}{i}Returning to menu...{/b}{/i}"
            pause 1.5
            jump vol1_ch1_dayslct