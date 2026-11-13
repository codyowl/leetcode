from collections import deque
class MyStack:
    '''
    The idea here is to manipulate the typical behaviur of a queue/list 
    a list append will usually behave adhering to "First in First out" we need to manipulate the typical behaviour of list so that we can make the "Last in First out

    add a new element to second queue
    move all the existing elements from first queue to second queue by putting all those behind the newly inserted one
    swap queu1 and queue2 
    by rearranging this, the last in will be first in the index of queue 1 to pop out
    '''
    def __init__(self):
        # creating two queue as per the norm of the problem statement
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        # this is where we need to do the main manipulation
        self.queue2.append(x)
        while self.queue1:
            # taking all the elements of queue1 and putting it behind the newly inserted element in queue
            self.queue2.append(self.queue1.popleft())
        # now swapping so that the rearranged this iwll reflecton queue1
        self.queue1, self.queue2 = self.queue2, self.queue1
        

    def pop(self) -> int:
        # taking the lastly isnerted element 
        return self.queue1.popleft()

    def top(self) -> int:
        # top will be the 0th index
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()