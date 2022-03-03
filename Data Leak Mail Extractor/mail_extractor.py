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


class XmlFormat:
    def __init__(self):
        self.xml_cleaned_lst = list()
        self.xml_formatter()

    def xml_formatter(self):
        with open("Inputs/Xml/raw_data.xml", "r") as io:
            data = io.read()

        for r in (("<></><></><></><></>", ""),
                  ("<>1</>", ""),
                  ("<>", "<Unknown>"),
                  ("</>", "</Unknown>"),
                  ("</NewDataSet></diffgr:diffgram></MMDataResult></MMDataResponse></soap:Body></soap:Envelope>", ""),
                  ("</Unknown></Unknown>", "</Unknown>")
                  ):
            data = data.replace(*r)

        if "diffgr:" or "msdata:" in data:
            print("SOAP Based XML Found")
            time.sleep(0.5)

        self.xml_cleaned_lst = re.split(
            "\<\sdiffgr:id=\"\d+\"\smsdata:rowOrder=\"\d+\"\>", data)

        """For Dumping
        with open("self.xml_cleaned_lst", "w") as io:
            io.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<data>\n")
        
            for i in self.xml_cleaned_list:
                io.write(i+"n")
            io.write("</data>")
        """

    def xml_finder(self, searchable, folder_name=None):
        if folder_name == None:
            folder_name = searchable

        count = 0
        output_lst = list()
        for i in self.xml_cleaned_lst:
            lst = re.findall(searchable, i)

            if len(lst) != 0:
                output_lst.append(i)
                count += 1

        print("\n{0} entry found about \"{1}\"".format(count, searchable))

        path = 'Outputs/Xml/'+folder_name.split(".")[0]
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)
        now = datetime.now().strftime("%Y-%-m-%d %H%:%M")

        with open(path+"/"+"["+str(count)+"] "+searchable+"("+now+")",  "w+") as io:
            io.write("\n{0} entry found about \"{1}\":".format(
                count, searchable))
            for i in output_lst:
                io.write("\n"+i.split("<Email>")[1].split("</Email>")[0])

    def xml_bulk_search(self):
        while True:
            inp = input(
                "ROOT/XML/BULK/: Enter a domain from /CustomerDomains:")
            if inp == "q":
                return

            with open("CustomerDomains/"+inp, "r") as io:
                data = io.read().splitlines()

            for i in data:
                self.xml_finder(i, inp)

    def xml_single_search(self):
        while True:
            inp = input("ROOT/XML/SINGLE/: Enter a Domain name:")
            if inp == "q":
                return
            self.xml_finder(inp)


class PasteBin:
    def __init__(self):
        self.regex = "[\w.+-]+@[\w-]+\.[\w.-]+"
        self.lst_overall = list()
        self.email_regex()

    def email_regex(self):
        list_of_files = glob.glob("Inputs/Bins/*.txt")
        for file in list_of_files:
            file_read = open(file, "r")
            for i in file_read.readlines():
                lst = re.findall(self.regex, i)
                self.lst_overall.append(lst)

    def bin_searcher(self, domain, folder_name=None):
        if folder_name == None:
            folder_name = domain
        count = 0
        output_bin_lst = list()
        path = "Outputs/Bin/"+folder_name.split(".")[0]
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)

        for mail in self.lst_overall:
            lst = re.findall(domain, mail[0])
            if len(lst) != 0:
                output_bin_lst.append(mail[0])
                count += 1

        now = datetime.now().strftime("%Y-%-m-%d %H%:%M")
        print("\n{0} entry found about \"{1}\"".format(count, domain))

        with open(path+"/"+domain+"("+now+") ["+str(count)+"] ", "w+") as io:
            io.write("\n{0} entry found about \"{1}\":".format(count, domain))
            for i in output_bin_lst:
                io.write("\n"+i)

    def bin_single_search(self):
        while True:
            inp = input("ROOT/BIN/SINGLE/: Enter a Domain name:")
            if inp == "q":
                return
            self.bin_searcher(inp)

    def bin_bulk_search(self):
        while True:
            inp = input(
                "ROOT/BIN/BULK/: Enter a domain from /CustomerDomains:")
            if inp == "q":
                return

            with open("CustomerDomains/"+inp, "r") as io:
                data = io.read().splitlines
            for i in data:
                self.bin_searcher(i, inp)


def main():
    print("Enter 'q' to return main menu or quit.\n")
    while True:
        formatter = input("ROOT/: type xml or bin to select format:")
        if formatter == "xml":
            print("Data is cleaning. Please wait...")
            xml = XmlFormat()
            while True:
                typer = input(
                    "ROOT/XML/: type bulk or single to select search mode:")
                if typer == "bulk":
                    xml.xml_bulk_search()
                elif typer == "single":
                    xml.xml_single_search()
                elif typer == "q":
                    break
                else:
                    print("Invalid choice")

        elif formatter == "bin":
            paste = PasteBin()
            while True:
                typer = input(
                    "ROOT/BIN/: type bulk or single to select search mode:")
                if typer == "bulk":
                    paste.bin_bulk_search()
                elif typer == "single":
                    paste.bin_single_search()
                elif typer == "q":
                    break
                else:
                    print("Invalid choice")

        elif formatter == "q":
            print("Bye..")
            time.sleep(0.5)
            break

        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
