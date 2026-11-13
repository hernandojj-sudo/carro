def on_forever():
    if input.light_level() < 200:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
    else:
        basic.clear_screen()
basic.forever(on_forever)
