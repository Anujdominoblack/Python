def banner_text(text=" ",screen =80):
    if len(text)>screen-4:
        raise ValueError ("string is larger than the screen size")
    elif text=="*":
        print("*"*screen)
    else:
        center=text.center(screen-4)
        output="**{0}**".format(center)
        print(output)


banner_text("*")
banner_text()
banner_text(screen=50) # this is called keyword argument and we are specifying what we are using
