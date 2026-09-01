import time

def decorator(func):
    def wrapper(*args):
        print("Before function")
        start= time.time()
         
        result = func(*args) 
        
        end = time.time()
        
        elapsed = end - start
        
        
        print("After function")
        
        print("Execution time:", elapsed, "seconds")
        
        return result
    return wrapper
    
        
@decorator
def create_list(n):
   return list(range(1 , n+1))
               
n = int(input("n"))               
result = create_list(n)
print(result)