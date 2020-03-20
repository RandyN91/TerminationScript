# TerminationScript

Problem : 
IT Security is responsible for confirming that terminated users have had their accounts disabled by Desktop teams as per a Weekly Termination Report and if accounts are still active we investigate if attempts were made to login after termination. 
 This is typically a manual process since SAP provides terminations in an outdated HTML formatted page and the analyst has to query each system to diff the dates and status.

Solution : 
I wrote a Script in Python which uses Beautiful Soup to Scrape the page, extracting the table into a 2 Dimensional List. Then iterates though it, querying Active Directory to confirm if the account is disabled via status code. If it isnt, it queries the Last Login Timestamp and diffs this to see if the User tried to login after their term date and warrants more investigation. 

Script then packaged in Windows Executable and distributed to the Analysts. 

![Image description](https://lh3.googleusercontent.com/bsxzs1ePRkNVHn1Indkpl3xCGwxQes37IJ0Q1qtbEujqGdK0Gp0Ivv51gmR2HIdvntGL0TaoFMCWKbJtx2SVT780wyXZUOh4sqVVoVyrxew7kHX1sTLLfDrgL6R1dVv8ULB1jm2h34aYvTLpVbZlqeW2Xo4bYaNZTpSQuoJ9u7EYc-PnjTjdRO3I6aWS8vYmKQPcSpH-51NnqRRAt325gRfIkY4KXfwLEZ6_vuEU7QjAY8xEKqbd7LfuqxyJlgwFFan2hpOru60dadq7aZWUgK4zWzIxOzPV5ws-97orLElxhwMkVyRv2PxM9BZZYYOFTqxEwFldjonPHCZVLJ-C30dwUhwEkVq8upNshDO6ZrZ2xG9LqmSegWMyEOvmQu9Kkoarja9pt169S6F1QEKZdATbPr-9YG2kM1krYV5XdGJrL4ozwze3Eqf49CQ9dM_Yi2t9r0M9QR7f0jsrBkTrLBe_Mvd676GhDEsMS5A6XGYrn-SfVdizAZ7YdeCdH0sggtFOIt3K3YT53OhfrhZunlBYlkmJQpCNAqJS1KUOgX301tQ9LxDAqZyGDzKPniBUB6kq-eLcCE8bC1mJau96TNhTlMTovKJW7lWJIlMWhimsj2qyu9UdfYgAGFrBS0PRgXQ-SBc-_OSGplr9KilrNwjXPtubtcY8I8U3J5aLtk9YY1WVoLXRTvewVhPI-7M=w1160-h760-no)

Authors : https://github.com/grepcoffee and myself 
