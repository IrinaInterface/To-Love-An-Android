label vol1_ch1_d2:
    scene black
    with fade
    centered "{b}Volume 1 - Chapter 1 - Day 2{/b}\n{i}Tuesday 2nd January{/i}"

    scene bg bedroom_day
    show hareka neutral_v1_1
    with fade
    "I slowly wake up."
    "Hareka is waiting for me."
    show hareka neutral_talk_v1_1
    hareka "Good morning."
    show hareka neutral_v1_1
    mc "O-Oh... Good morning..."
    "I sit up, stretching my arms."
    show hareka neutral_talk_v1_1
    hareka "Did you sleep well?"
    show hareka neutral_v1_1
    menu vol1_ch1_d2_sleepstate:
        "Yes.":
            $ vol1_ch1_d2_sleepstate_sleptwell = True
            show hareka neutral_talk_v1_1
            hareka "Good."
            show hareka neutral_v1_1
        "No.":
            $ vol1_ch1_d2_sleepstate_sleptbad = True
            show hareka neutral_talk_v1_1
            hareka "Oh. That's a shame."
            show hareka neutral_v1_1
    show hareka neutral_talk_v1_1
    hareka "I'll make breakfast now."
    show hareka neutral_v1_1
    mc "O-Okay."
    hide hareka with moveoutleft
    "She leaves."
    "I stand up, doing a big stretch."
    mc "Ahh... Much better."
    "While waiting for her to return, I decide to make the bed."
    "Not like I have anything better to do..."
    "After that, I sit back down, and soon get lost in my thoughts."
    "I still kinda can't believe what happened... I really got kidnapped by the Government..."
    "Although she's being so nice to me... And for some reason I'm not that scared...?"
    show hareka neutral_v1_1 with moveinleft
    "She returns, carrying a tray with some buttered toast and apple juice."
    "She hands it to me."
    show hareka neutral_talk_v1_1
    hareka "Here."
    show hareka neutral_v1_1
    mc "Thanks..."