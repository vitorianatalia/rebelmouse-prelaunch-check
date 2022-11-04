# Rebelmouse Pre-Launch URLs Check
 
 ### Initial Report File:
   
   Run a screaming frog report of the old website and export it normally (internal links only) 
   ![image](https://user-images.githubusercontent.com/54844059/199789785-4ffd606f-8e94-4c30-8354-ab138bf5433a.png)
 
 ### How to run it:
 This script takes in 5 parameters:
   python status_code.py <file_name> <csv_delimiter> <old_domain> <new_domain> <base_user> <base_password>
   

  <file_name>: name of the screaming frog report
  
  <csv_delimiter>: delimiter used in this CSV report
  
  <old_domain>: the URL of the current CMS of the client
  
  <new_domain>: the URL of rebelmouse runner were the migration is being set
  
  <base_user>: base auth login
  
  <base_password>: base auth password
  
### Output:
  output.cvs -> A copy of all URLs with Content Type text/html, plus 2 new columns at the end with the status code 200 in Rebelmouse site and their respective URLs
