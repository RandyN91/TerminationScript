import bs4
import pyad
from datetime import  datetime as dt
import time

# to compile to EXE run "python -m auto_py_to_exe" in terminal (need library)

from pyad import pyadutils, adquery

htmlfile = open(input("\nPlease Enter the HR Report Path (.html extension only) : "))

file = open("AD_ScriptOutput_"+dt.now().strftime("%d-%m-%Y_%I-%M-%S_%p") +".txt", "w")

tablelist = []

print("\nThis Script will cycle through all accounts in the HTML HR Report, "
       "\ncheck if accounts are disabled, then  check if accounts have logged  "
      "\nin past their termination. \n\nPlease report bugs to randy.naraine@jetblue.com\n")

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

 for tables in tables:
  #iterate table objects

  rows = tables.findChildren(['th', 'tr'])

  for row in rows:
        cells = row.findChildren('td')
        for cell in cells:
            value = str(cell.string).replace(u'\xa0', u'')
            tablelist.append(value)
 return tablelist

parseHTML(htmlfile)

# after all possible cells from all tables are in one list, we remove the first few cells which include the report name,date etc

del tablelist[:13]

def divide_chunks(l, n):
    # this now cuts the list of elements from the HTML table and extracts the rows in chunks of 9 elements,
    # since table data spans 9 columns and the data is static.

    for i in range(0, len(l), 9):
        yield l[i:i + n]

dividedlist = list(divide_chunks(tablelist, 9))

#dividedlist is a list where each item is a list of 9 elements , essentially the rows we just extracted

def ADsearch(input):
#This reads the dividedlist and extracts the Users ID then queries AD to return the last login, account status
# and if the account had attempted login after the termination date. Warranting further investigation.

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
     print("Error "+str(e)+" in user "+str(Name)+" Check HTML and AD Manually")
     file.write("\nError "+str(e)+" in user "+str(Name)+" Check HTML and AD Manually")
     pass
#Script Terminal Output

print("Output : \n")

ADsearch(dividedlist)

file.close()

print("\nScript Complete. Close window to generate file. File output will be saved in working directory.")
print("\nThis window will close in 200 Seconds....")
time.sleep(200)