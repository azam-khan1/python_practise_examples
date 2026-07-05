# multi-threading using Thread Pool Execution

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(num):
    time.sleep(1)
    return f"Numbers:{num}"

num = [1,2,3,4,5]

with ThreadPoolExecutor(max_workers=3) as executor:
    result=executor.map(print_numbers,num)
    t = time.time()

for result in result:
    print(result)
    print(f"final time of thread pool multi-processing:",time.time()-t)

# multi-processing using Process Pool Execution

from concurrent.futures import ProcessPoolExecutor
 
def square_numbers(number):
    time.sleep(1)
    return f"Square of Numbers:{number*number}"

number = [1,2,3,4,5,6,7,8,9,10]


if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_numbers,number)
        t = time.time()

    for result in results:
        print(result)
        print(f"final time of process pool multi-processing:{time.time()-t}")
