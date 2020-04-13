# TerminationScript

Problem : 
IT Security is responsible for confirming that terminated users have had their accounts disabled by Desktop teams as per a Weekly Termination Report and if accounts are still active we investigate if attempts were made to login after termination. 
 This is typically a manual process since SAP provides terminations in an outdated HTML formatted page and the analyst has to query each system to diff the dates and status.

Solution : 
I wrote a Script in Python which uses Beautiful Soup to Scrape the SAP term report page, extracting the table into a 2 Dimensional List. Then iterates though it, querying Active Directory to confirm if the account is disabled via status code. It also queries the Last Login Timestamp and diffs this to see if the User tried to login after their planned term date and warrants more investigation (i.e if their account was not disabled on time and they noticed and tried to log in. then open a DLP incident to investigate)

Script then packaged in Windows Executable and distributed to the Analysts. 

![Image description](https://www.roamingviews.com/wp-content/uploads/2020/04/term1.jpg)
![Image description](https://www.roamingviews.com/wp-content/uploads/2020/04/term2.jpg)
Authors : https://github.com/grepcoffee and myself 
