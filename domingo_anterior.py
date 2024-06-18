import datetime
from datetime import timedelta

data = datetime.datetime.now()
print("Data antes do while", data )
while data.weekday() != 6:
    data = data - timedelta(days=1) 
print("Data depois do while:",data)
