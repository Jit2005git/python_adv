"""def greet(name):
    print("Hello:",name)
greet("Karan")
greet("Arjun")"""

# def square(x):
#     return x*x
# n=int(input("Enter a number:"))
# x=str("The number is: ") + str(square(n))
# print(x)

# def multiply(a,b):
#     print("only print",a*b)
#     return ("multiplication is:",10*b)
# result=multiply(5,6)
# print("result is:",result)


# def count_even(n):
#     count=0
#     for i in range(1,n+1):
#         if i%2==0:
#             print(i)
#             count+=1
#     return count
# n=int(input("Enter a number: "))
# result=count_even(n)
# print("Count of even numbers:", result)


def check_result(marks):
    if marks>=40:
        return "Pass"
    else:
        return "Fail"
marks=int(input("Enter marks: "))
result=check_result(marks)
    
print("Result:",result) 

 