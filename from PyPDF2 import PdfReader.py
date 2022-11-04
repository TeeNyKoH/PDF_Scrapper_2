from PyPDF2 import PdfReader



def readFromPDF(filename):
    
    
    print("Enter the name of the text file: ")
    filename = input()
    filename = filename + ".txt"
    with open(filename, 'w') as f:
        f.write(page_content)
    return filename

f = open("demofile.txt", "r")
print(f.read()) 



def readfile(filename):
    with open(filename) as f:
        lines = f.readlines()

    firstRead = []


 
    for i in lines:

            splittext = i.split('[60 hours]')
            # i = ". " + i
            firstRead.append(str(splittext)) #firstRead is the listname\
    for i in lines:

        splittext = i.split('[30 hours]')
        # i = ". " + i
        firstRead.append(str(splittext)) #firstRead is the listname\
    

    for i in lines:

        splittext = i.split('[12/24 weeks]')
        # i = ". " + i
        firstRead.append(str(splittext)) #firstRead is the listname\
    
    for i in lines:

        splittext = i.split()
        # i = ". " + i
        firstRead.append(str(splittext)) #firstRead is the listname\
    
    
    
    
    # lines = fulltext.split(".")
    # for i in lines:
    #     # splittext = i.split(i[0:2].isdigit() is False and i[2:6].isdigit() is True)
    #     # splittext = i.split(i[0:3].isdigit() is False and i[3:6].isdigit() is True)
    #     # splittext = i.split("ITP%" and i[3:6].isdigit() is True)
    #     splittext = i.split("ITP%")
    #     i = "zxc" + i
    #     firstRead.append(str(splittext)) #firstRead is the listname
    
    # for i in lines:

    #     splittext = i.split("%.ITP%")
    #     i = "zxc" + i
    #     firstRead.append(str(splittext)) #firstRead is the listname
        
        
    # for i in lines:
    #     # if i contains IT and 4 digits, then split
        
        
    #     # splittext = i.split(i[0:2].isdigit() is False and i[2:6].isdigit() is True)
    #     # splittext = i.split(i[0:3].isdigit() is False and i[3:6].isdigit() is True)
    #     # splittext = i.split("IT%" and i[2:6].isdigit() is True)
    #     splittext = i.split("IT%")
    #     i = "IT" + i
    #     firstRead.append(str(splittext)) #firstRead is the listname
    
    # for i in lines:

    #     splittext = i.split("%.IT%")
    #     i = "IT" + i
    #     firstRead.append(str(splittext)) #firstRead is the listname
        
    # for i in lines:
    #     # splittext = i.split(i[0:2].isdigit() is False and i[2:6].isdigit() is True)
    #     # splittext = i.split(i[0:3].isdigit() is False and i[3:6].isdigit() is True)
    #     # splittext = i.split("BM%" and i[2:6].isdigit() is True)
    #     splittext = i.split("BM%")
    #     i = "BM" + i 
    #     firstRead.append(str(splittext)) #firstRead is the listname
    
    # for i in lines:
    #     # splittext = i.split(i[0:2].isdigit() is False and i[2:6].isdigit() is True)
    #     # splittext = i.split(i[0:3].isdigit() is False and i[3:6].isdigit() is True)
    #     # splittext = i.split("BM%" and i[2:6].isdigit() is True)
    #     splittext = i.split("%.BM%")
    #     i = "BM" + i 
    #     firstRead.append(str(splittext)) #firstRead is the listname
    
    # for i in lines:
    #     # splittext = i.split(i[0:2].isdigit() is False and i[2:6].isdigit() is True)
    #     # splittext = i.split(i[0:3].isdigit() is False and i[3:6].isdigit() is True)
    #     # splittext = i.split("zxc%" and i[3:6].isdigit() is True)
    #     splittext = i.split("zxc%")
    #     i = "ITP" + i
    #     firstRead.append(str(splittext)) #firstRead is the listname
        
    # for i in lines:
    #     splittext = i.split("%.zxc%")
    #     i = "ITP" + i
    #     firstRead.append(str(splittext)) #firstRead is the listname
    
    # for i in firstRead:
    #     if i ==" \n":
    #         firstRead.remove(i)
                
    print(firstRead)
    jsonfile=""

    # def algo(firstRead):
        
    
        
    #     for i in firstRead:
    #         print(i)
    #         if "Bachelor" in i:
    #             course1 = i.split("Applicable", 1)[0] 
    #             print("course1", course1)
    #             return course1
    #         elif "YEAR" in i:
    #             year = i.split("TRIMESTER", 1)[0]
    #             tri = i.split("TRIMESTER", 1)[1]   
    #             print("year", year, "tri", tri) 
    #             return year,tri
            
            
    final = ""      
    for i in firstRead:
        
        if "IT%%%%" in i: 
            
            final = final + i   
    
    
    print("put in text file enter file name")
    filename = input()
    filename = filename + '.txt'
    f = open(filename, "a")
    f.write(final)
    print("Sucessfully write into " + filename)
    f.close()



def main():
    print("Enter the name of the pdf file: ")
    pdfname = input()
    filename = readFromPDF(pdfname)
    readfile(filename)
main()