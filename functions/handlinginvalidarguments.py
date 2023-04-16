def banner_text(text):
    screen=80
    if len(text)>screen-4:
        raise ValueError("string size is more than the screen size")  #exception is raised of type value
    elif text=="*":
        print("*"*screen)
    else:
        centered=text.center(screen-4)
        output="**{0}**".format(centered)
        print(output)

banner_text("*")
banner_text("lets try this also")