        for mail_list in self.lst_overall:
            if mail_list:
                print(type(mail_list))                
                if type(mail_list) is list:
                    for mails in mail_list:
                    # print("mail type:{}, len{}".format(type(mail),len(mail)))                    
                        splitted = mails.split("@")
                        lst = re.findall(domain, splitted[0])
                        if lst:
                            for mail in lst:
                                output_bin_lst.append(mail)
                                count += 1


######

from typing import List


lst = [["emre@gmail.com", "erkan@gmail.com"], "remre98@gmail.com"]

if type(lst) is list:
    print("yes")

out = list()
for j in lst:
    if type(j) is list:
        for i in j:
            splitted = (i.split("@")[0], i.split("@")[1])
            print(splitted)
import re

for i in lst:
    print(re.findall("[\w.+-]+@[\w-]+\.[\w.-]+", i))