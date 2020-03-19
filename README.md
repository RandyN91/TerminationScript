# TerminationScript

Problem : 
IT Security is responsible for confirming that terminated users have had their accounts disabled by Desktop teams as per a Weekly Termination Report and if accounts are still active we investigate if attempts were made to login after termination. 
 This is typically a manual process since SAP provides terminations in an outdated HTML formatted page and the analyst has to query each system to diff the dates and status.

Solution : 
I wrote a Script in Python which uses Beautiful Soup to Scrape the page, extracting the table into a 2 Dimensional List. Then iterates though it, querying Active Directory to confirm if the account is disabled via status code. If it isnt, it queries the Last Login Timestamp and diffs this to see if the User tried to login after their term date and warrants more investigation. 

Script then packaged in Windows Executable and distributed to the Analysts. 

![Image description](https://lh3.googleusercontent.com/Mk4Wiaol11g-PiUYmcPTb630fsnirFzeIRRzlNM7oHWzTI20-xQgtyZHoKVq8trsOROzvL1HPwYKTP3tEA2KviFLXVQBCdDrninxJJlLU1LSLIldo5YUdNHbzT24u35SVjMo8ymQ2GOwoxMN6RB93ObD6kQrqYgj6_XQSXMm18mWEj8rOqZZ2irlb3AYC1Tayal4XJl9SzPZBpa2AmWa7ts-ZKTLbNZPCikwigwxJMpAEJy2wYyW76D194GPMkVcEagveEE4-GvzZ2JtGPNuTXIUTDyvFG0HRid_HYN76_2B4aKtaQaV2Sju3p3F2hU9N-BQb6i0GTFVCECJNFQlaJ_8r3UD0RNcf9i42HO8KqYQeH5ClQ_wK2gpvDbuanOgkuB45QEpEzf6mOaNj3un9W3UM64rrgfQEoNytUFuCRqxSdNrEVZDw3Ks35Nc6gRcTaLpx6GXJQKKoTILGkEKXbxNv8fMJ5B9NF530pQb0fdmCEcHMf_TmLytpo-jL6-bfJcm80rMtlXnv2GlwVgz3LqsL4yAoh88zhRIv3bFNAWQp-EvEYSev7TXCLoUtrObqiWahw8ltLzjhQ1Aa3kvrQEv4w1TBZQ2EU3J0lLKxd_4KqYkwNTX1KK-2mZ8TyomUgagEhXjA3K4ERduDgnUM9cfMYef1Xz4b9_L_p9fPkw8Kvc6yqRUkn2-wQ3m0hg=w1160-h760-no)

Authors : https://github.com/grepcoffee and myself 
