## ITBooks

### What is ITBooks?
The project uses scrapy to crawl data from some websites such as allitebooks,digilibraries,etc ,and stores it in sqlite3.
You can search and download some books that you need.

**Data source**

- [allitebooks](http://www.allitebooks.com/)  √
- [taiwanebook](http://taiwanebook.ncl.edu.tw/zh-tw)
- [blah](http://blah.me/)
- [digilibraries](http://digilibraries.com/)

Run `pip install -r requirements.txt`

### Usage:
```
  abook.py search <title> <author>
  abook.py title <title>
  abook.py author <author>
```
#### Search
![search](docs/search.png)
#### Command
![command](docs/command.png)
#### download
![command](docs/download.png)
Enjoy reading time !
### TODO:
- Add more websites
- Batch download
### How to update?
[Update the data](docs/crawl.md)