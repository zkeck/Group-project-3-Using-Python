from urllib.request import urlretrieve


URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)


#Counts total requests in the last 6 months
Six_month_count = 0

for line in open(local_file):
  if "May/1995" in line:
    Six_month_count += 1
  elif "Jun/1995" in line:
    Six_month_count += 1
  elif "Jul/1995" in line:
    Six_month_count += 1
  elif "Aug/1995" in line:
    Six_month_count += 1
  elif "Sep/1995" in line:
    Six_month_count += 1
  elif "Oct/1995" in line:
    Six_month_count += 1
 

#Counts total requests during the whole time period.
total_count = 0

for line in open(local_file):
  if "1994" in line or "1995" in line:
    total_count += 1 


print("Total requests made in the last 6 months:",Six_month_count)
print("Total requests made in the time period represented by the log:",total_count)



