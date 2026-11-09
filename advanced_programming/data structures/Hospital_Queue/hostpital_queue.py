waiting_list = [
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
]

S1Front = -1
S1Rear = -1
S1Count = 0
S2Front = -1
S2Rear = -1
S2Count = 0
S3Front = -1
S3Rear = -1
S3Count = 0
QueueSize = 20

def dequeue1():
    if S1Rear == S1Front:
        return False , None
    else:
        S1Front+=1
        patient = waiting_list[0][S1Front]
        return True , patient

def dequeue2():
    if S2Rear == S2Front:
        return False , None
    else:
        S2Front+=1
        patient = waiting_list[1][S2Front]
        return True , patient
    
def dequeue3():
    if S3Rear == S3Front:
        return False , None
    else:
        S3Front+=1
        patient = waiting_list[2][S3Front]
        return True , patient

def enqueue():
    name = input('Enter the patients last name: ')
    severity = int(input('Enter the severity of their condition (1-3): '))
    if severity == 0:
        if S1Count == QueueSize:
            print('Queue Full. Please try a different severity')
            return False
        else:
            S1Rear = (S1Rear-1) % QueueSize
            waiting_list[0][S1Rear] = name
            S1Count +=1
            return True

    elif severity == 1:
        if S2Count == QueueSize:
            print('Queue Full. Please try a different severity')
            return False
        else:
            S2Rear = (S2Rear-1) % QueueSize
            waiting_list[1][S2Rear] = name
            S2Count +=1
            return True

    elif severity == 2:
        if S3Count == QueueSize:
            print('Queue Full. Please try a different severity')
            return False
        else:
            S3Rear = (S3Rear-1) % QueueSize
            waiting_list[0][S3Rear] = name
            S3Count +=1
            return True

def dequeue():
    queue1, patient =dequeue1()
    if queue1 == False:
        dequeue2