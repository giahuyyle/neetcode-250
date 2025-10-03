from collections import deque

def solution(travelPhotos):
    res = []

    q = deque()
    q.append(travelPhotos[0])  # Use append instead of enqueue
    processed = []

    while q:
        print(q, ",", processed, ",", res)
        current = q.popleft()  # Use popleft instead of dequeue
        processed.append(current)
        for photo in travelPhotos:
            if photo not in processed:
                if current[0] in photo:
                    q.append(photo)
                    res.append(current[1])
                elif current[1] in photo:
                    q.append(photo)
                    res.append(current[0])
        
    print(q, ",", processed, ",", res)
    return res

photos = [[3,2], [2,1], [4,5], [5,6], [1,4]]
print(solution(photos))