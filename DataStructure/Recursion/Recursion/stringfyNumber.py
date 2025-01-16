obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

def stringify_numbers(d):
    for key, value in d.items():
        if isinstance(value, int):
            d[key] = str(value)
        elif isinstance(value, dict):
            stringify_numbers(value)
    return d

result = stringify_numbers(obj.copy())  # Use obj.copy() to avoid modifying the original object
print(result)
