
old_mails = [
'oldmail@mail.com',
'oldmail@mail.com'
]

new_mails = [
'newmail@mail.com',
'newmail@mail.com'
]

new_mails = list(set(new_mails))

diff = sorted(list(set(new_mails) - set(old_mails)))

with open("new_mails.txt", "w") as io:
    for iter in diff:
        io.write(iter+"\n")
