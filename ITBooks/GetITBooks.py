import wget
from prettytable import PrettyTable
from pyquery import PyQuery as pq
import textwrap
from conf import config
from database.SqliteDb import SqliteDb


class GetITBooks():
    """
    Search and download some ITBookes that you need
    """

    def __init__(self):
        self.db = SqliteDb()
        self.result_field = None
        self.result = None
        self.page = 0

    def search_book(self, title=None, author=None):
        try:
            self.result = self.db.sql_search(title, author)
            self.result_field = PrettyTable(
                ['Id', 'Title', 'Author', 'Year', 'Pages', 'Category', 'Size'])
            if self.result:
                for index, book in enumerate(self.result):
                    index = '%02d' % (index + 1)
                    self.result_field.add_row([
                        index, book[1], book[3], book[5], book[6], book[10],
                        book[8]
                    ])
                print(self.result_field.get_string(start=0, end=5))
                message = "We got {0} entries in total. (if u don't know how to do next,just type 'help')".format(
                    len(self.result))
                print(message)
                self.get_command_param()

        except Exception as e:
            print(e)

    def get_next_page(self):
        self.page += 5
        if len(self.result) >= self.page:
            return self.result_field.get_string(
                start=self.page, end=self.page + 5)
        else:
            return None

    def get_command_param(self):
        while True:
            param = input('>')
            if param.lower() == 'next':
                next_page = self.get_next_page()
                if next_page:
                    print(next_page)
            if param.lower() == 'break':
                pass
            if param.lower().startswith('des'):
                try:
                    index = int(param.lower().split(' ')[1]) - 1
                    description = self.result[index][11]
                    des = self.get_description(description)
                    if des:
                        print(des)
                except:
                    pass
            if param.lower().startswith('get'):
                pass
            if param.lower() == 'help':
                info_field = PrettyTable(['Command', 'Details'])
                info_field.add_row(['next', 'show next page'])
                info_field.add_row(
                    ['break', 'break out, and search the other books'])
                info_field.add_row(['desc id', 'show book\'s description'])
                info_field.add_row(['get id', 'download'])
                info_field.add_row(['help', 'show all commands'])
                info_field.add_row(['quit', 'just like this command'])
                print(info_field)
            if param.lower() == 'quit':
                exit()

    def get_description(self, description):
        if description:
            des = pq(description)
            return textwrap.fill(des('.entry-content').text(), width=100)
        else:
            return 'No Description!'

    def download_book(self, url):
        pass


if __name__ == '__main__':
    g = GetITBooks()
    g.search_book(title='Mastering Python')
