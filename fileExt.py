filename = str(input("Enter the filename alon with extention and path : "))
count = 0
ext = ''
for ch in filename:
	if(ch=='.'):
		count = 1
		continue
	if(count):
		ext = ext + ch

if(ext=="py"):
        print("The extension of the file is : 'python'")
