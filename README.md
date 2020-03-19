# TerminationScript

Problem : 
IT Security is responsible for confirming that terminated users have had their accounts disabled by Desktop teams as per a Weekly Termination Report and if accounts are still active we investigate if attempts were made to login after termination. 
 This is typically a manual process since SAP provides terminations in an outdated HTML formatted page and the analyst has to query each system to diff the dates and status.

Solution : 
I wrote a Script in Python which uses Beautiful Soup to Scrape the page, extracting the table into a 2 Dimensional List. Then iterates though it, querying Active Directory to confirm if the account is disabled via status code. If it isnt, it queries the Last Login Timestamp and diffs this to see if the User tried to login after their term date and warrants more investigation. 

Script then packaged in Windows Executable and distributed to the Analysts. 

![Image description](https://lh3.googleusercontent.com/7NXSezs4EL5UlJmp3X3eu83xGTByf3BLPYkRAtib_NGQp1kuzTveP0h2fGl5sJoICrRtvhdrk-Hcw2sArkAh7ZlrhyOZGh32nuluK8SRZfyrr3oXLUIbI0BF9C3JUX0HyrQqDuiSHnu_JzLDLkgUaN7-gxyevcpXGXMcrNGNsc2UhP9gv0kCvWC1eNpd1eiNrxiiPy1PYxEaJLXoSl3rUjO5I894t5RhAd5nM-zKxO1CTxgzRdi0QeTs22CSh4J3rz31Qzlcu1p9SXpxT7AMqNbYL0FvwHbZeRPqzoFbTqcjvMLUzkR6xSdYLedoAuMlg1G5-TB_WSEywasfcCjTehs130oITwL6B00KcRIkZabYl9WGbeM-gZuTSzPeMX4n5LVTeqlJEMAs4kW95xLqthWb23XZZXSY0jqbJ-20C3CDbRSTE-8wUhhiGQlZ4gtmO2qSkhXUqza6S3dUOEQ9IY_atZGaeKxPTuM__NGE5oN-NQcZzCdUyDK1ANGzIceDbelpqeVjxDP23IC5BCGimo-A-7YYw0l-JF-89_8CMHHMS9sHTUYDTQi0c4ipMF5GPOgWoTd9y4d3eAkcznlM_FpyJFFAo_vQOD3sew0w3yPpRW4h9zqH_isHHDFqpg3g8jyy3YS3D899zQC_8wt55A5hcO2Zp_lYkB7FoE3YHHrJXmqBA1L9ETW2PnOSd_w=w1160-h760-no)

Authors : https://github.com/grepcoffee and myself 
