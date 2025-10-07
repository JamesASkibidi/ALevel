import os , time


def initializeQueue(size):
     queue = ['-' for i in range(size)]
  
     return queue, -1, -1
     
def enqueue(queue, item ):
     #check if the queue is full
     global back ,count
     if count == size:
          print('Queue is full')
          return True
          
     else:
          back = (back +1) % size
          queue[back] = item
          count +=1
          return False
          



def dequeue(queue ):
     global back , front , count

     if back == front:
          removed = None
     else:
          front +=1
          removed = queue[front]
          count -=1


     
     return removed 


size = int(input('Enter a size: '))

count = 0

queue, front, back = initializeQueue(size)

choice = 0

while choice != exit:
     choice = input('Enqueue or Dequeue: ')
     if choice == 'exit':
          break

     if choice == 'enqueue':
          item = input('Enter an item: ')

          full = enqueue(queue, item)

          time.sleep(0.5)
          os.system("clear")

          if full is True:
               print('Queue is full')
               time.sleep(0.5)
               os.system("clear")
          else:
               os.system("clear")
     else:
          removed = dequeue(queue )
          if removed == None:
               print('Queue is empmty')
               time.sleep(0.5)
               os.system("clear")
               
          else:
               os.system("clear")
               
print(*queue)
