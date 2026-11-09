


the_tree = [
    {"data" : "A" , "adj" : [1            
                             ] },       

    {"data" : "B" , "adj" : [2,3,4
                             ] }  ,    

    {"data" : "C" , "adj" : [5                             
                             ] }  ,     

    {"data" : "D" , "adj" : [                                                                                     
                             ] }  ,      
                             
    {"data" : "E" , "adj" : [6
                             ] }  ,

    {"data" : "F" , "adj" : [
                             ] }  ,                                     

    {"data" : "G" , "adj" : [
                             ] }                                 
]

root = 0



def bft(tree,root):
     queue = []
     queue.append(root)
     while len(queue)>0:
          current_node = queue.pop(0)
          for adj in tree[current_node]["adj"]:
               queue.append(adj)          
          print(tree[current_node]["data"])




bft(the_tree , 0)

    



