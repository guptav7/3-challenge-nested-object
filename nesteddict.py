def get_value_from_key(obj, key):
    keys = key.split('/')
    current = obj
    for k in keys:
        if isinstance(current, dict) and k in current:
            current = current[k]
        else:
            return None  # Key not found in the dictionary
    return current

# Example usage:
object1 = {"a": {"b": {"c": "d"}}}
key1 = "a/b/c"
value1 = get_value_from_key(object1, key1)
print(value1)  # Output: "d"

object2 = {"x": {"y": {"z": "a"}}}
key2 = "x/y/z"
value2 = get_value_from_key(object2, key2)
print(value2)  # Output: "a"
