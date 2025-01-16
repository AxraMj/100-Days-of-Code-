def pow(base,expo):
    if expo==0:
        return 1
    return base * pow(base,expo-1)

print(pow(2,4))