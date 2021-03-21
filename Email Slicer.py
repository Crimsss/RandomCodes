# Email splicer
ind = 0
email = input("")
for i in range(0,len(email)):
    ind += 1
    if email[i] == "@":
        print("Your username is", email[0:ind-1], "and the domain is", email[ind:len(email)])
        break
    elif ind == len(email):
        print("Invalid email address")
        break
    else:
        continue
