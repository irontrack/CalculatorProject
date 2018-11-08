'''
Created on Nov 2, 2018

@author: jesse
'''
def opperator(x):
        '''
            ACCEPTS A CHAR . IF THE CHAR IS A MATHEMATICAL OPPERATOR IT RETURNS TRUE
            OTHERWISE FALSE.
        '''
        
        if x == '+' or x == '-' or x == '*' or x == '/' or x == '(' or x == ')':
            return True
        else:
            return False

#TO DO : WRITE ERROR FOR PICKING UP EXTRA OPPERATORS IN THE SORTING PROCESS
def c_eval(req):
    '''
    DOCSTRING: ACCEPTS A STRINGS ARGV 
        THE STRING ARG IS AN IN FIX MATH STATEMENT WHICH
        C_EVAL IS MEANT TO RETURN THE RESULT OF USING POSTFIX CONVERSION
    '''
    # INITIATE VARIABLES
    error = "ERROR: invalid syntax"
    from collections import deque
    #from cal_eval import opperator
    first = 0
    last = 0
    test = []
    out_list = deque([])
    opp_list = deque([])
    # priority dictionary for giving opperators a numeric hierarchy
    prio = {'(':5,')':6,'/':4,'*':3,'+':1,'-':2}

    # SORT THE STRING ELEMENTS: INFIX TO POST FIX
   
    for x in range(0,len(req)):
        
        if req[x].isnumeric() or req[x] == '.':
            last = x
        
        elif opperator(req[x]):
            # NEEDS A METHOD TO INSURE ORDER OF OPPERATIONS
            if req[x - 1].isnumeric() and x > 0:
                out_list.append(float(req[first:last+1]))
            
            if not len(opp_list) == 0 and prio[req[x]] == 6:
                # pop off the opperators to stack onto out_list until the ')' is popped off
                done = False
                while not done:
                    if not opp_list[0] == '(':
                        out_list.append(opp_list.popleft())
                    else:
                        opp_list.popleft()
                        done = True
                    
                    
            elif len(opp_list) == 0 or prio[opp_list[0]]  <= prio[req[x]] or opp_list[0] == '(':
                opp_list.appendleft(req[x])
            elif prio[opp_list[0]]  > prio[req[x]]:
                # pop off oppopperators to out_list until opp_list is empty then appendleft  new opperator
                while len(opp_list):
                    out_list.append(opp_list.popleft())
                opp_list.appendleft(req[x])
                
            first = x + 1
        if x == len(req) - 1:
                if req[x].isnumeric() :
                    out_list.append(float(req[first:last + 1]))
                # append all left over opperators to out_list
                while len(opp_list):
                    out_list.append(opp_list.popleft())
                
                
    # EVALUATE THE OUT_LIST USING POSTFIX
    heap = []
    try:
        while len(out_list):
            
            if not opperator(out_list[0]):
                heap.append(out_list.popleft())
            else:
                right = heap.pop()
                left = heap.pop()
                temp = None
                if not (type(left) == float or type(left) == int) or \
                    not (type(right) == float or type(right) == int):
                        return error
                if out_list[0] == '-':
                    temp = left - right
                    out_list.popleft()
                elif out_list[0] == '+':
                    temp = left + right
                    out_list.popleft()
                elif out_list[0] == '/':
                    temp = left/right
                    out_list.popleft()
                elif out_list[0] == '*':
                    temp = left*right
                    out_list.popleft()
                heap.append(temp)
        if not len(heap) == 1:
            return error
    except ZeroDivisionError:
        return str('Error: Division By Zero')
    except:
        return error
        
    else:
        return str(heap.pop())
    

    
if __name__ == '__main__':
    
    calculations = [u'2*(3+6)',u'4-8*6',u'2*9+(1.23-.23)/1',u'(3+6)*2',u'(9+1)*(2-1)',u'((*)',u'(3+4',u'34',u'(2+3)/(2-2)']
    for x in calculations:
        try:
            answer = c_eval(x)
            print(answer)
        except:
            print('error')