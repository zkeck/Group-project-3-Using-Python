from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

Six_month_count = 0
total_count = 0
for line in open(local_file):
  
  total_count += 1
  #get the month
  if line[0] == 'r':
    if line[19:23] == '1995':
      if line[15:18] == 'Oct' or line[15:18] == "Sep" or line[15:18] == "Aug" or line[15:18] == "Jul" or line[15:18] == "Jun" or line[15:18] == "May":
        print(line[12:23])
        Six_month_count += 1
      #elif line[15:18] == "May":
       # if int(line[12:14]) >= 11: 
        #  print(line[12:23])
         # Six_month_count += 1
 
  elif line[0] == 'l':
    if line[19:23] == '1995':
      if line[15:18] == 'Oct' or line[15:18] == "Sep" or line[15:18] == "Aug" or line[15:18] == "Jul" or line[15:18] == "Jun" or line[15:18] == "May":
        print(line[12:23])
        Six_month_count += 1
      #elif line[15:18] == "May":
        #if int(line[12:14]) >= 11: 
          #print(line[12:23])
          #Six_month_count += 1
        
 

print(total_count)
print(Six_month_count)


