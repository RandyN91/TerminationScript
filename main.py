import bs4
import xlrd
import datetime
import time

file = open('report.html')
tablelist = []

excelfile = xlrd.open_workbook("Weekly CM Terminations.xlsx")
excelSheet = excelfile.sheet_by_index(0)

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

def listParsetime(input):
    t = time.strptime(input,'%m/%d/%y')
    return t

for i in dividedlist:
    print(int(i[1]),i[2],i[3],i[8])

print("---------")

for i in range(4,excelSheet.nrows):

    print(str(int(excelSheet.cell_value(i,2)))+" "+str(excelSheet.cell_value(i,3))+" "+str(excelSheet.cell_value(i,4))+" "+str(excelSheet.cell_value(i,5))+
          " "+str(datetime.datetime(*xlrd.xldate_as_tuple((excelSheet.cell_value(i,11)),excelfile.datemode))))

