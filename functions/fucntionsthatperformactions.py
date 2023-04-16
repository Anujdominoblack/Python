def banner_text(text):
    screen=80
    if len(text)>screen-4:
        print("this is too long")
    elif text=="*":
        print("*"*screen)
    else:
        centered=text.center(screen-4)
        output="**{0}**".format(centered)
        print(output)

banner_text("*")
banner_text("im just checking it")