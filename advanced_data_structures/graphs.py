graph = [
    {"data" : "A" , "adj" : [{"node" : 1 , "weight" : 7}            #0
                             ] },       

    {"data" : "B" , "adj" : [{"node" : 0 , "weight" : 7} ,          #1
                             {"node" : 5 , "weight" : 4}
                             ] }  ,    

    {"data" : "C" , "adj" : [{"node" : 1 , "weight" : 9},           #2
                             {"node" : 3 , "weight" : 3},
                             {"node" : 4 , "weight" : 8}                              
                             ] }   ,     

    {"data" : "D" , "adj" : [{"node" : 2 , "weight" : 3},           #3
                             {"node" : 4 , "weight" : 8}                                                                                       
                             ] }  ,      
                             
    {"data" : "E" , "adj" : [{"node" : 5 , "weight" : 5},           #4
                             {"node" : 2 , "weight" : 8}
                             ] }  ,      
    {"data" : "F" , "adj" : [{"node" : 2 , "weight" : 6000},        #5
                             {"node" : 4 , "weight" : 5}
                             ] }        
]

print((graph[0]["adj"])[0]["weight"])

# {"node" : 1 , "weight" : 9}