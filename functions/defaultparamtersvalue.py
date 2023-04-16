def banner_text(text,screen=80):  # default paramter is passed
    if len(text)>screen-4:
        raise ValueError ("string is larger than the screen size")
    elif text=="*":
        print("*"*screen)
    else:
        center=text.center(screen-4)
        output="**{0}**".format(center)
        print(output)

banner_text("*",60)
banner_text(" its been a loong time")  #if we dont pass the second parameter then the defaullt value is considered
