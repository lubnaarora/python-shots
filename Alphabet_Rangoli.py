
import string

Size = int(raw_input())

mid = Size - 1

#upper triangle
for i in range(Size - 1, 0 ,-1):
	row = ['-'] * ( 2*Size - 1)
	for j in range(Size - i):
		row[mid -j] = row[mid + j] = string.ascii_lowercase[j + i]
	print '-'.join(row)
	
#lower triangle
for i in range(0,Size):
	row = ['-']*(2*Size - 1)
	for j in range(0,Size - i):
		row[mid-j] = row[mid+j] = string.ascii_lowercase[j+i]
	print '-'.join(row)
