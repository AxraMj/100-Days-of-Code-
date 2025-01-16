obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

def NestedEvenSum(d):
    sum_even = 0
    for key, value in d.items():
        if isinstance(value, int):
            if value % 2 == 0:
                sum_even += value
        elif isinstance(value,dict):
            sum_even+=NestedEvenSum(value)
    return sum_even

obj1_sum = NestedEvenSum(obj1)
obj1_sum = NestedEvenSum(obj2)
print(obj1_sum)  # Should print the sum of even numbers
