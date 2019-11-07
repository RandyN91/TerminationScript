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

del tablelist[:10]

def divide_chunks(l, n):

    for i in range(0, len(l), n):
        yield l[i:i + n]

n = 9

dividedlist = list(divide_chunks(tablelist, n))

for i in dividedlist:

 print(i)




'''
table_rows = soup.find_all('tr')
for tr in table_rows:

    ID = tr.find_all('nobr')

    print(ID)
'''
