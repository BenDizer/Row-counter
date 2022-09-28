#
from github import Github

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

g = Github("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")

 # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
for repo in g.get_user().get_repos():
    print(repo.name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
