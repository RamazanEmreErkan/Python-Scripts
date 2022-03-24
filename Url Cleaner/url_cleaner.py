"""
Name : Url Cleaner
Definition: Cleans safe urls to make them works.
Author : Ramazan Emre Erkan
Usage : Just run the file and follow the instructions.
Compatibility: Python3.0+
"""
import urllib.parse


def cleaner(urls):
    out_lst = list()

    for r in (("hxxp", "http"), ("hxxps", "https"), ("[.]", "."), ("\"", ""), ("\n", ""), ("“", ""), ("”", ""), ("(Obfuscated)", ""), ("%20", ""), (",", "")):
        urls = urls.replace(*r)

    for i in urls.split(" "):
        i = urllib.parse.unquote(i)
        if i.startswith("http") or i.startswith("https"):
            out_lst.append(i)

    return list(set(out_lst))


def main():
    print("\n{Type 'q' to terminate program.}")
    while True:
        inp = input("\nEnter an URL: ")
        if inp == "q":
            return
        out_lst = cleaner(inp)
        counter = 1
        if out_lst:
            for i in out_lst:
                print("\n\t [{}]-> {}".format(counter, i), sep="")
                counter += 1
        else:
            print("\n\t!!!URL can not be found!!!")


if __name__ == '__main__':
    main()
