obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

def collect_string(d):
    strings = set()
    for key, value in d.items():
        if isinstance(value, str):
            strings.add(value)
        elif isinstance(value, dict):
            strings.update(collect_string(value))
    return strings

print(collect_string(obj))
