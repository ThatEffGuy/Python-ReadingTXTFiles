#read and print the contents of marks file
#  filename.read() will read the contents of the file
print("Marks")
with open("marks.txt","r") as f:
    print (f.read())
#end with
input("\npress enter to continue")

#reading a line at a time
#   filename.readline() will read one line at a time
print("\nMarks one line at a time")
with open("marks.txt","r") as f:
    print (f.readline())
    print (f.readline())
    print (f.readline())
#end with
input("\npress enter to continue")

#reading a line at a time
#use a for loop to read each line in file (for line in f:)
print("\nMarks one line at a time using a FOR loop")
with open("marks.txt","r") as f:
    for line in f:
        print (int(line))
    #end for
#end with
input("\npress enter to continue")

#use a for loop to read each line in file (for line in f:)
print("\nRead Marks one line at a time and write to a list")
markList = []   # empty list
with open("marks.txt","r") as f:
    for line in f:
        markList.append(int(line))  # append int value
    #end for
    print(markList)
#end with
for index in range(len(markList)):
    print (markList[index])
#end for 
input("\npress enter to continue")
