init python:
    tak = Character("Takawa", who_color="#50c878")
    yumi = Character("Miss Yumi", who_color="#50c878")
    commentary = False

    style.say_dialogue.size = 20

init:
    $ mods["sisterhood"] = "Katawa Shoujo: Sisterhood"
    $ mods_with_menus["sisterhood"] = True

define replays = [
    (_("Act 1"), [
        (_("Chapter 1"), [
            (_("Chapter 1"), "script-c1.en_chapter1", _("Yap yap yap")),
            (_("Bundle of Hisao"), "a1_monday.bundle_of_hisao", _("Hisao is told about Yamaku Academy, where he will likely spend the rest of his high school days."))
        ]),])]