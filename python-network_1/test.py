data = '{"id":89,"name":"holberton"}'

# Remove curly braces and split the string
pairs = data[1:-1].split(',')

# Create a dictionary from the key-value pairs
result = {}
for pair in pairs:
    key, value = pair.split(':')
    result[key.strip('"')] = value.strip('"')

print(result)
