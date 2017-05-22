import wget
from prettytable import PrettyTable
from colorama import init, Fore
from pyquery import PyQuery as pq
from future.builtins import input
import textwrap
from con.config import SEARCH_CONFIG
from ITBooks.database.SqliteDb import SqliteDb


class Console():
    """
    Let's start from here
    Search and download some ITBookes that you need
    """

    def __init__(self):
        self.db = SqliteDb()
        self.result_field = None
        self.result = []
        self.page = -5

    def search_book(self, title=None, author=None):
        # Get the full results
        for name in list(SEARCH_CONFIG.keys()):
            # list
            result = self.db.sql_search(name, title, author)
            if result:
                self.result += result
        # Show
        self.result_field = PrettyTable(
            ['Id', 'Title', 'Author', 'Year', 'Category', 'score'])
        if self.result:
            for index, book in enumerate(self.result):
                try:
                    index = '%02d' % (index + 1)
                    if book[-2] == 'allitebooks':
                        score = ''
                        self.result_field.add_row(
                            [index, book[1], book[3], book[5], book[10], ''])

                    if book[-2] == 'blah':
                        year = ''
                        self.result_field.add_row(
                            [index, book[1], book[3], year, book[4], book[6]])
                except Exception as e:
                    print(e)
                    continue
            init(autoreset=True)
            print(Fore.RED + self.get_next_page())
            message = "We got {0} entries in total. (if you don't know how to do next,just type 'help')".format(
                len(self.result))
            print(message)
            self.get_command_param()
        else:
            print("No result!")

    def get_next_page(self):
        self.page += 5
        if len(self.result) > self.page:
            return self.result_field.get_string(
                start=self.page, end=self.page + 5)
        else:
            return None

    def get_command_param(self):
        flag = True
        while flag:
            param = input('>')
            if param.lower() == 'next':
                next_page = self.get_next_page()
                if next_page:
                    init(autoreset=True)
                    print(Fore.RED + next_page)
            if param.lower() == 'break':
                flag = False
            if param.lower().startswith('des'):
                try:
                    index = int(param.lower().split(' ')[1]) - 1
                    if index >= (self.page) and index < (self.page + 5):
                        if self.result[index][-2] == "allitebooks":
                            description = self.result[index][11]
                            des = self.get_description(description)
                        if self.result[index][-2] == "blah":
                            des = self.result[index][5] if self.result[index][
                                5] else "No description."
                        init(autoreset=True)
                        print(Fore.MAGENTA + des)
                except:
                    print("if you don't know how to do next,just type 'help'")
            if param.lower().startswith('get'):
                try:
                    index = int(param.lower().split(' ')[1]) - 1
                    if self.result[index][-2] == "allitebooks":
                        url = self.result[index][12]
                        download_info = self.download_book(url)
                    if self.result[index][-2] == "blah":
                        url = [
                            self.result[index][7], self.result[index][8],
                            self.result[index][9]
                        ]
                        for each in url:
                            download_info = self.download_book(each)
                    print(download_info)
                except:
                    print("if you don't know how to do next,just type 'help'")
            if param.lower() == 'help':
                info_field = PrettyTable(['Command', 'Details'])
                info_field.add_row(['next', 'show next page'])
                info_field.add_row(
                    ['break', 'break out, and search the other books'])
                info_field.add_row(['des id', 'show book\'s description'])
                info_field.add_row(['get id', 'download'])
                info_field.add_row(['help', 'show all commands'])
                info_field.add_row(['quit', 'just like this command'])
                init(autoreset=True)
                print(Fore.YELLOW + info_field.get_string())
            if param.lower() == 'quit':
                exit()

    def get_description(self, description):
        if description:
            des = pq(description)
            return textwrap.fill(des('.entry-content').text(), width=100)
        else:
            return 'No Description!'

    def download_book(self, url):
        try:
            if url:
                download_info = wget.download(url)
                return download_info
            else:
                return "{0} is a invalid url.".format(url)
        except Exception as e:
            return "Download Failed."
