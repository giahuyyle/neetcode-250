from typing import List

def leastInterval(tasks: List[str], n: int) -> int:
    # what if n is 0???
    if n == 0:
        return len(tasks)
    
    res = 0
    task_map = {}

    for task in tasks:
        if task in task_map:
            task_map[task][0] += 1
        else:
            task_map[task] = [1, -1]

    done = False

    # initial
    print("initial:", task_map)

    while not done:
        done = True

        for task in task_map:

            if task_map[task][0] > 0:
                done = False

                if task_map[task][1] <= 1:
                    task_map[task][0] -= 1
                    task_map[task][1] = n
                
                else:
                    task_map[task][1] -= 1
            
            # step-by-step
            print(task_map)
    
    return res

def main():
    tasks = ["A","A","A","B","B","B"]
    n = 2
    print(leastInterval(tasks, n))

    tasks1 = ["A","C","A","B","D","B"]
    n1 = 1
    print(leastInterval(tasks1, n1))

main()