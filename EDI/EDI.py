with open("D:\Yogesh_Hipass\\EDI\\edi.txt") as txtfile:
    data = txtfile.read()
    
    res=data.split("*")
    
    result =[]
    
    n= len(res)
    
    for i in range(0, n):
        value=res[i].split("~")
        
        if(len(value)==2):
            
            result.append(value[1])
        
    print(result)
