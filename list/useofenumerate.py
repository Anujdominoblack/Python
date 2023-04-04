current_choice ="-"
computer_parts=[]
valid=[]
available_parts=["mouse","mouse pat","cpu","monitor","keyboard"]
for i in range(1,len(available_parts)+1):
    valid.append(str(i))
print(valid)
while current_choice !="0":
    if current_choice in valid :
        index=int(current_choice)-1
        chosen_part=available_parts[index]
        computer_parts.append(chosen_part)
    else:
        for number,part in enumerate(available_parts):
            print("{0} :{1}".format(number+1,part))
    current_choice=input()
print(computer_parts)
