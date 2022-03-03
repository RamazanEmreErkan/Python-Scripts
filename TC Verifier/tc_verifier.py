"""
Name : TC Verifier
Author : Ramazan Emre Erkan
Usage : Just run the file and follow the instructions.
Compatibility: Python3.0+
"""
import re

class verifier:

    def __init__(self, tc):
        self.tc = tc

    def verify(self):

        if len(self.tc) != 11:
            print("TC kimlik numarasi 11 haneli olmalidir.")
            return False

        elif not self.tc.isdigit():
            print("TC Kimlik numarasi sadece sayilardan oluşmalidir.")
            return False

        elif int(self.tc[0]) == 0:
            return False

        else:
            digits = [int(i) for i in str(self.tc)]

        if not ((sum(digits[:9][-1::-2]) * 7) - (sum(digits[:8][-1::-2]))) % 10 == digits[9]:
            print("10. Hane denkleme göre uyumsuz")
            return False

        elif not sum(digits[:10]) % 10 == digits[10]:
            print("11. Hane denkleme göre uyumsuz")
            return False

        else:
            return True


def main():

    while True:
        inp = input("\nEnter an TCKN: ")

        if inp == "q":
            return

        lst = [i for i in re.split((" |,|:|-"), inp) if i != ""]
               
        for i in lst:
            obj = verifier(i)
            result = obj.verify()
            if result is True:
                print("\n TCKN [{}] is valid".format(i))


main()
