class MyQueue:
    # the idea here is to create two list and to achieve the first in first out we need to change the elements from one list and another for the pop operation, push is going to be normal and peek is nothing just reading the last element and empty should return true if the list is empty
    def __init__(self):
        self.input_stack = list()
        self.output_stack = list()

    def push(self, x: int) -> None:
        # pushing should happens in the input stack 
        self.input_stack.append(x)
        

    def pop(self) -> int:
        # here we need to transer our element to the outputstack to adhere to the first in first out
        if not self.output_stack:
            # here we are reversing the elements
            while self.input_stack:
                item = self.input_stack.pop()
                self.output_stack.append(item)
        # return and remove the first element to adhere to the first in first out rule
        return self.output_stack.pop()

        

    def peek(self) -> int:
        # this is similar to pop except the element should be returned without removing it
        if not self.output_stack:
            while self.input_stack:
                item = self.input_stack.pop()
                self.output_stack.append(item)
        # now we need to return the last element of our outputstack without removig it unlike pop
        return self.output_stack[-1]        
        

    def empty(self) -> bool:
        # both output and input stack are empty
        return not self.input_stack and not self.output_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()