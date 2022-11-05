
def readfile():
    print("Enter the name of the text file: ")
    filename = input()
    filename = filename + ".txt"
   

    f = open(filename, "r")
    # print(f.read()) 
    lines = f.readlines()
    return lines

def readFromPDF():
    
    
    lines = readfile()
    data =[]
    # print(lines)
    
    
    # for i in lines:
    #     data.append(str(i))
    # print(data)
    
    

    
    print("lines", lines)
    for index,elem in enumerate(lines):
        current_elem = elem
        if(index<(len(lines)-1)): 
            next_elem = lines[index+1]   
            if len(current_elem) <10:
                data.append(elem)
                data.append(next_elem)
                print(current_elem)
        else:
        
            if len(current_elem) <10:
                data.append(elem)
                data.append(next_elem)
                print(current_elem)
    
    writefile(data)
   
def writefile(data):   
    print("put in text file enter file name")
    filename = input()
    filename = filename + '.txt'
    f = open(filename, "a")
    for i in data:
        f.write(i)
    print("Sucessfully write into " + filename)
    f.close()
    
    # for i in lines:
    #     if "IT" in i:
    #         print(i)
    #         course1 = i.split("IT%", 1)[0] 
    #         print("course1", course1)
    #         return course1
    
    
    
    
    
    
    

def clean():
    
    newdata = []
    text = readfile()
    for i in text:

        if i not in newdata:
            newdata.append(i)
    writefile(newdata)
    
    
    
def convertsql():
    text = readfile()
    sql = ""
    
    
    for i in text:
        if len(i) < 10:
            modcode = i
            print("modcode", modcode)
            
            #sql = sql + 'INSERT INTO polytechnicModules (moduleCode,moduleName) VALUES (' + "'" + modcode + "'" + ',' + "'" + coursename + "');"

        # print(i)
        
        else:
            coursename = i
            print("modcode", coursename)
            
            
            # jsonfile = {"CourseName":course1, "ModCode": modcode , "ModName": modName, "Year":year, "Tri":tri, "ModType": core, "Credits": credits}
            # '{"CourseName":' + course1 + ', "ModCode": ' + modcode + ', "ModName": ' + modName + ', "Year":' + year + ', "Tri":' + tri + ', "ModType": ' + core + ', "Credits": ' + credits + '}'
            # sql = sql +'{"CourseName":' + course1 + ', "ModCode": ' + modcode + ', "ModName": ' + modName + ', "Year":' + year + ', "Tri":' + tri + ', "ModType": ' + core + ', "Credits": ' + credits + '}'
            sql = sql + 'INSERT INTO polytechnicModules (moduleCode,moduleName) VALUES (' + "'" + modcode + "'" + ',' + "'" + coursename + "');"

    
    writefile(sql)
    
    
    
    
def convertsqlfromtext():
    text = readfile()
    sql = ""
    skill = ""
    
    for i in text:
        skill = i
        sql = sql + 'INSERT INTO Skills (skill) VALUES (' + "'" + skill  + "');"
    
    writefile(sql)

    
    
    

def main():
    
    # readFromPDF()
    # convertsql()
    convertsqlfromtext()
    # clean()
    
    
    
main()

