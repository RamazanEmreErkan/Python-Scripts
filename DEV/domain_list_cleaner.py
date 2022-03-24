domain = input("Enter an domain filename:")
with open(domain, "r") as rf:
    data = rf.readlines()
    print("len of data: ", len(data))
out = sorted(list(set([i.strip() for i in data])))

print("len of out: ",len(out))
with open(domain+"1", "w") as wf:
    wf.writelines(i+"\n" for i in out)