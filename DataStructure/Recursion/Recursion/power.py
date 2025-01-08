def power(base,expo):
    assert expo>=0 and int(expo)==expo,'the exponent must be possitive integer only'
    if expo==0:
        return 1
    elif expo==1:
        return base
    else:
        return base*pow(base,expo-1)
    
print(power(2,3))