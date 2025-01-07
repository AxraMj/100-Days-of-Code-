n=4
def function(n):
    if n<1:
        print("Hello")
    else:
        function(n-1)
        print(n)

function(n)
    