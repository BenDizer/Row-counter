#
from github import Github


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

g = Github("")
Row_Counter = 0
 # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
repo = g.get_user().get_repo("DigBicks")
def pars(path):
    Row_Counter = 0
    for cont in repo.get_contents(path):
        print(cont.name)
        print(cont.type)
        if cont.type == "file":
            try:
                for line in cont.decoded_content:
                    if format(line, 'x').__str__() == "a":
                        Row_Counter = Row_Counter + 1
            except AssertionError:
                Row_Counter = Row_Counter

        if cont.type == "dir":
            pars(cont.path)
    print(Row_Counter)
pars("")


#contentF = repo.get_contents("/")
#for content_file in contentF:
 #   print(content_file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
