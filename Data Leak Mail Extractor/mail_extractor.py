"""
Name: Data Leak Email Extractor
Author : Ramazan Emre Erkan
Compatibility: Python3.0+
"""

from datetime import datetime
import re
import pathlib
import glob
import time


class Exctractor:
    def __init__(self):
        self.regex = "[\w.+-]+@[\w-]+\.[\w.-]+"
        self.lst_overall = list()
        self.email_regex()

    def email_regex(self):
        list_of_files = glob.glob("Inputs/*")
        if list_of_files:
            for file in list_of_files:
                if file != "Inputs/test_data.txt":
                    file_read = open(file, "r")
                    print("\n\"{}\" found.\n".format(file))
                    for i in file_read.readlines():
                        lst = re.findall(self.regex, i)        
                        self.lst_overall.append(lst)
                else:
                    continue
        else:
            print("No document found.")

    def searcher(self, domain, folder_name=None):
        if folder_name == None:
            folder_name = domain
        count = 0
        output_lst = list()
        now = datetime.now().strftime("%Y-%-m-%d %H.%M.%S")
        path = "Outputs/"+folder_name.split(".")[0]+" ("+now+")"
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)

        for mail_list in self.lst_overall:
            if type(mail_list) is list:
                for mail in mail_list:        
                        splitted = mail.split("@")
                        if re.findall(domain, splitted[1]):
                            output_lst.append(mail)
                            count += 1        

        print("\n{0} entry found about \"{1}\"\n".format(count, domain))
        with open(path+"/"+domain+"["+str(count)+"].txt", "w+") as io:
            io.write("{0} entry found about \"{1}\":\n".format(count, domain))
            for i in list(set(output_lst)):
                io.write("\n"+i)

    def single_search(self):
        while True:
            inp = input("SINGLE/: Enter a single Domain name:")
            if inp == "q":
                return
            self.searcher(inp)

    def bulk_search(self):
        while True:
            inp = input(
                "BULK/: Enter a domain from /CustomerDomains:")
            if inp == "q":
                return

            with open("CustomerDomains/"+inp, "r") as io:
                data = io.read().splitlines()
            for i in data:
                self.searcher(i, inp)

def main():
    while True:
        print("Enter 'q' to return main menu or quit.\n")
        formatter = input("/: type bulk or single to select search mode:")
        if formatter == "q":
            print("Bye..")
            time.sleep(0.5)
            break

        elif formatter == "bulk" or formatter == "single":            
            obj = Exctractor()                                   
            if formatter == "bulk":
                obj.bulk_search()
            elif formatter == "single":            
                obj.single_search()                                   
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
