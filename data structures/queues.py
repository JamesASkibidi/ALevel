def initializeQueue(size):
     queue = ['-' for i in range(size)]
  
     return queue, -1, -1
     
def enqueue(queue, item):
     #check if the queue is full
     global back
     if front == size-1:
          print('Queue is full')
     else:
          back += 1
          queue[back] = item



def dequeue(queue):
     global back
     global front

     if back == front:
          print('Queue is empty')
     else:
          front +=1
          removed = queue[front]
     
          return removed


size = int(input('Enter a size: '))

queue, front, back = initializeQueue(size)

# item = input('Enter an item: ')

# enqueue(queue, item)

# print(queue , front, back)

# removed = dequeue(queue )

# print(queue , front, back, removed)

# removed = dequeue(queue )
choice = 0

while choice != exit:
     choice = input('Enqueue of Dequeue: ')

     if choice == 'enqueue':
          item = input('Enter an item: ')

          enqueue(queue, item)
     else:
          removed = dequeue(queue )

     print(queue)

