import bs4

file = open('report.html')
tablelist = []
soup = bs4.BeautifulSoup(file,features="lxml")
tables = soup.findChildren('table')
my_table = tables[1]
rows = my_table.findChildren(['th', 'tr'])

for row in rows:
        cells = row.findChildren('td')

        for cell in cells:

            value = str(cell.string).replace(u'\xa0', u'')

            tablelist.append(value)

del tablelist[:9]

#https://www.geeksforgeeks.org/iterate-over-a-list-in-python/

def divide_chunks(l, n):

    for i in range(0, len(l), 9):
        yield l[i:i + n]

dividedlist = list(divide_chunks(tablelist, 9))

for i in dividedlist:
    print(i)