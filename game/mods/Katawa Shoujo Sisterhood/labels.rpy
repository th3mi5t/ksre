label sisterhood:
    show screen sisterhood
    call screen sisterhood

    return

label sisterhood_start:
    stop music fadeout 1.0

    scene black
    with config.game_main_transition
    pause 2.0

    call en_chapter1

    return