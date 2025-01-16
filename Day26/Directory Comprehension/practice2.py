sentence="Hello worlds program"
#syntax result={new_key:new_value for item in sentence}
result={i:len(i) for i in sentence.split()}
print(result)