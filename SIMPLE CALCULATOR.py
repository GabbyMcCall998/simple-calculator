raw_input=input
num1=0.0
num2=0.0
op=''
print('simple calculator'.upper())
while num1 or num2!='a':
        print('Enter first number (a to quit)')
        num1=(raw_input())
        if num1== 'a':
            break;
        num1=int(num1)
        print('enter operation (+,-,/,*,%)')
        op=raw_input()
        print('enter second number'.upper())
        num2=(raw_input())
        if num2== 'a':
            break;
        num2=int(num2)
        if op=='+':
            print(num1+num2)      
        elif op== '-':
            print(num1-num2)
        elif op=='/':
            print(num1/num2)
        elif op=='*':
            print(num1*num2)
        elif op=='%':
            print(num1%num2)
                
        
       
            
        
