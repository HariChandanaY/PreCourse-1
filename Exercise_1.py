# Time Complexity : O(1)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this : Nothing


# Your code here along with comments explaining your approach
class myStack:
  #Please read sample.java file before starting.
  #Kindly include Time and Space complexity at top of each file
     def __init__(self):
           self.values = []
         
     def isEmpty(self):
           return self.size() == 0
         
     def push(self, item):
           self.values.append(item)
         
     def pop(self):
           if not self.isEmpty():
                 return self.values.pop()
           else:
                 print("Stack is empty")
        
     def peek(self):
           if not self.is_empty():
                 return self.values[-1]
           else:
                 print("Stack is empty")
        
     def size(self):
           return len(self.values)
         
     def show(self):
           return self.values
         

s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())
