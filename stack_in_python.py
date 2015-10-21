"""
linear data structures in python: Stack
"""

# You can use list to mimic stack
stack = []
stack.append(1)
stack.append(5)
stack.append("dog")
print stack.pop()
print stack.pop()

# You can also extend list to create Stack
class Stack(list):
    def isEmpty(self):
        return not self
    
    def push(self, item):
        self.append(item)
    
    @property
    def length(self):
        return len(self)
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self[-1]

stack = Stack()
stack.push(1)
stack.push(5)
stack.push("dog")
print "is stack empty: " + str(stack.isEmpty())
print "length of stack is: " + str(stack.length)
print "peek value: " + str(stack.peek())
print "pop value: " + str(stack.pop())

def par_checker(s):
    stack = Stack()
    for pos in xrange(len(s)):
        if s[pos] == '(':
            stack.push(1)
        elif s[pos] == ')':
            stack.pop()
            
    if stack.length == 0:
        return True
    else:
        return False
    
print "par check for '((()))': " + str(par_checker('((()))'))
print "par check for '(()': " + str(par_checker('(()'))

def symbol_checker(s):
    def match_open_close(o, c):
        if o == '(' and c == ')':
            return True
        elif o == '[' and c == ']':
            return True
        elif o == '{' and c == '}':
            return True
        else:
            return False
        
    stack = Stack()
    for pos in xrange(len(s)):
        if s[pos] in '[{(':
            stack.push(s[pos])
        elif s[pos] in ')}]':
            latest_symbol = stack.pop()
            if not match_open_close(latest_symbol, s[pos]):
                print "these two are not matching: " + latest_symbol + s[pos] 
                break
            
    if stack.length == 0:
        return True
    else:
        return False
    
print symbol_checker('{{([][])}()}')
print symbol_checker('[{()]')
