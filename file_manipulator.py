import sys

def reverse(file1,file2):
    content = ""
    with open(file1) as f:
        content = f.read()

    with open(file2,"w") as f:
        length = len(content)
        for i in range(-1,-1*length-1,-1):
            f.write(content[i])

def copy(file1,file2):
    content = ""
    with open(file1) as f:
        content = f.read()

    with open(file2,"w") as f:
        f.write(content)

def duplicate_contents(file,n):
    content = ""
    with open(file) as f:
        content = f.read()
    
    with open(file,"w") as f:
        for i in range(5):
            f.write(content) 

def isSubstring(string1,string2):
    return True if string1.find(string2) != -1 else False

def replace_string(file,string,newstring):
    content = ""
    with open(file) as f:
        content = f.read()
    
    with open(file,"w") as f:
        f.write(content.replace(string,newstring))

def main():
    if sys.argv[1] == "reverse":
        reverse(sys.argv[2],sys.argv[3])
    elif sys.argv[1] == "copy":
        copy(sys.argv[2],sys.argv[3])
    elif sys.argv[1] == "duplicate_contents":
        duplicate_contents(sys.argv[2],sys.argv[3])
    elif sys.argv[1] == "replace_string":
        replace_string(sys.argv[2],sys.argv[3],sys.argv[4])

if __name__ == "__main__":
    main()
