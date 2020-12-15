# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the
# file, and print out the results to the screen. I have a .txt file for you, if you want to use it!
#
# Extra:
#
# Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt
# file, and count how many of each “category” of each image there are. This text file is actually a list
# of files corresponding to the SUN database scene recognition database, and lists the file directory
# hierarchy for the images. Once you take a look at the first line or two of the file, it will be 
# clear which part represents the scene category. To do this, you’re going to have to remember a bit 
# about string parsing in Python 3. I talked a little bit about it in this post.

def fileToList(filename):
    with open(filename, "r") as open_file:
        line = open_file.readline()
        linelist = []
        while line:
            linelist.append(line.strip())
            #print(line)
            line = open_file.readline()
        return linelist

def count(list):
    for item in set(list):
        print("Count of", item + " is", list.count(item))
        
def stripString(list):
    striplist = []
    i = 0
    for item in list:
        string = str(list[i])
        striplist.append(string[0:-20])
        i += 1
    return striplist

if __name__ == "__main__":
    print("First part: \n") 
    count(fileToList("nameslist.txt"))
    print("Extra part: \n")
    count(stripString(fileToList("Training_01.txt")))
