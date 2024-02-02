label start:
    scene black
    with fade
    "Welcome to \"[config.name] [config.version]\"!"
    "First of all, what is your name?"
    $ player_name = renpy.input("My name is...", default='Alex')
    $ player_name = player_name.strip()
    menu vol1_chslct:
        "Please choose a Chapter."
        "Chapter 1.":
            jump vol1_ch1_dayslct
    menu vol1_ch1_dayslct:
        "{b}Current Chapter: 1{/b}\nPlease choose a Day."
        "Day 1.":
            jump vol1_ch1_d1
        "Day 2.":
            jump vol1_ch1_d2
        "Go back.":
            jump vol1_chslct