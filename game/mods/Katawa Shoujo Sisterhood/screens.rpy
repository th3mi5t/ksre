screen sisterhood():
    tag menu
    style_prefix "sisterhood"

    if main_menu:
        add "main_menu_bg"

    add "blind"

    frame:
        style_suffix "interface"

        has vbox

        text _("Mods > Katawa Shoujo: Sisterhood"):
            bold True
            size bold_size

        frame:
            has vbox

            vbox:
                textbutton _("Start") action Start("sisterhood_start")
            
            vbox:
                style_prefix "check"

                textbutton _("Commentary") action ToggleVariable("commentary", True, False)

            vbox:
                textbutton _("About") action ShowMenu("pxt_about")

        textbutton _("Return"):
            style "return_button"
            action ShowMenu("mods")

screen sisterhood_about():
    tag menu
    style_prefix "sisterhood_about"

    if main_menu:
        add "main_menu_bg"

    add "blind"

    frame:
        style_suffix "interface"
        xsize 1200

        has vbox

        text _("Mods > sisterhood > About"):
            bold True
            size bold_size

        frame:
            has vbox

            vbox:

                text _("A faithful port of the Sisterhood fanfic written by Guest Poster on KSRenai. \n")


                text _("Port by th3mi5t.\n")

        textbutton _("Return"):
            style "return_button"
            action ShowMenu("pxt")
