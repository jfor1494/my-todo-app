#here we can organize teh code to help it more rediablable and easy to manipulate, for that we organize in diferents files the code.
#this import only work when the files are in the same folder or directory 
#the funtion are separeted becasuse with it you can create the backend
FILEPATH = "data.txt"

"""
def funtion or custom function: it's very important to avoid the repetitive code in our code,
if there are codes that repet all the time, the better way is create a custom funtion
"""
#
def get_todos(filepath = FILEPATH ):
    """
    read a text file and return the list of to-do items.
    """
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local    

def write_todos(todos_arg, filepath = FILEPATH): #we always have to put the non default parameterst first because in this case you have to rewrite in every case different parmeters
     #conecction to write the data into the list created.txt
     
    """write the to-do items list in the text file.  """
    
    with open(filepath,'w') as file:  
        file.writelines(todos_arg)  

if __name__ == "__main__":
   print("Hello")
   print(get_todos())     
        
