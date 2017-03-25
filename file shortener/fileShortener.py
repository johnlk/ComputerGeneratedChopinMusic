#file = open("../midi conversion/unadulterated.txt", "r")

def cleanStringArr(arr):
	if len(arr) < 1 :
		return ""
	if len(arr) == 1 and arr[0] == "\n" :
		return ""
	for x in range(len(arr)):
		if x < len(arr) and not arr[x]:
		    arr = arr[:x] + arr[x+1:]
		    x = x - 1
	return ' '.join(arr)


file = open("./test.txt", "r")

fileText = ""

for line in file:
	fileText += line
	print(cleanStringArr(line.split(' ')))

file.close()


#writing to a new file the condensed text
file = open("./test.txt", 'w')
if len(fileText) > 0:
	file.write(fileText)
	print("fileChanged Successfully")
file.close()

