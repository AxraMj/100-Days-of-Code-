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
    return {key: (str(value) if isinstance(value, int) else stringify_numbers(value) if isinstance(value, dict) else value) for key, value in d.items()}

result = stringify_numbers(obj)
print(result)
