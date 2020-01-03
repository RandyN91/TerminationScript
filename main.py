import bs4
import pyad
from datetime import  datetime as dt
import time

from pyad import pyadutils, adquery

htmlfile = open(input("\nPlease Enter the HR Report Path : "))

file = open("AD_ScriptOutput_"+dt.now().strftime("%d-%m-%Y_%I-%M-%S_%p") +".txt", "w")

tablelist = []

print("\nThis Script will cycle through all accounts in the HTML HR Report, "
       "\ncheck if accounts are disabled, then  check if accounts have logged  "
      "\nin past termination. Limit : 50 accounts on first HTML Table on page. "
       "\nIf more than 50 please do the rest manually. This is a bug because of "
       "\nthe way the script scrapes the page and old HTML format.\n")

def accountStatus(input):
    if input == 514:
        return "Disabled"
    if input == 512:
        return "*Enabled* - > Check this ASAP "
    if input == 66048:
        return "Enabled, password never expires"
    if input == 66050:
        return "Disabled, password never expires"

def parseHTML(input):
 soup = bs4.BeautifulSoup(input,features="lxml")
 tables = soup.findChildren('table')

 my_table = tables[1]

 rows = my_table.findChildren(['th', 'tr'])

 for row in rows:
        cells = row.findChildren('td')
        for cell in cells:
            value = str(cell.string).replace(u'\xa0', u'')
            tablelist.append(value)
 return tablelist

parseHTML(htmlfile)

del tablelist[:9]

def divide_chunks(l, n):
    # https://www.geeksforgeeks.org/iterate-over-a-list-in-python/
    # this cuts the list of elements from the HTML table and extracts the rows since table data spans 9 columns
    for i in range(0, len(l), 9):
        yield l[i:i + n]

dividedlist = list(divide_chunks(tablelist, 9))

#print(dividedlist)

def adsearching(input):

  for i in input:
   try:
    q = pyad.adquery.ADQuery()
    usrid = i[1]
    nusrid = str("employeeID =" +usrid)
    q.execute_query(
        attributes=["mailNickname", "employeeID", "lastLogonTimeStamp","userAccountControl"],
        where_clause= nusrid,
        base_dn="DC=jetblue,DC=com"
    )

# add another AD function to show all user accounts if they are enabled / disabled

    for row in q.get_results():

        EmployeeID = (row['employeeID'])
        LastLogon = (pyadutils.convert_datetime(row['lastLogonTimeStamp']))
        Name = (row['mailNickname'])
        LastLogonDate = LastLogon.strftime('%m/%d/%Y')
        ActStatus = (row['userAccountControl'])
        #print(type(LastLogonDate))
        #print(Name, EmployeeID, LastLogonDate)


        for i in dividedlist:

         if EmployeeID in i:

          timediff = dt.strptime(LastLogonDate, '%m/%d/%Y') - dt.strptime(i[7],'%m/%d/%Y')

          if timediff.days > 0:
           print("User " + Name + " Was Terminated on "+str(i[7])+" and last logged in on "+LastLogonDate+" which is "+str(timediff.days)+" days after his termination")
           file.write("\nUser " + Name + " Was Terminated on " + str(i[7]) + " and last logged in on " + LastLogonDate + " which is " + str(timediff.days) + " days after his termination.")
        for i in dividedlist:

            try:
                if EmployeeID in i:
                    print("User " + Name + " account is " + accountStatus(ActStatus))
                    file.write("\nUser " + Name + " account is " + accountStatus(ActStatus))
            except Exception as e:
                print("Error " + e + " account likely doesnt exist or was deleted")

   except Exception as e :
     print("Error "+str(e)+" in user "+Name+" Check HTML and AD Manually")
     file.write("\nError "+str(e)+" in user "+Name+" Check HTML and AD Manually")
     pass
#Script Terminal Output

print("Output : \n")

adsearching(dividedlist)

file.close()

print("\nScript Complete. Close window to generate file. File output will be saved in working directory.")

time.sleep(200)
