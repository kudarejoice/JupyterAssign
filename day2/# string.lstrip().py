# string.lstrip()
name = "     hJohn Smith"
print(name.lstrip(" " "h"))

# string.rstrip()
name = "Bill Ross     th"
print(name.rstrip(" " "th"))

# string.strip()
name = 'a   John Smith   e'
print(name.strip('ae'))


# string.title()
president = 'joe biden'

# Looking inside of the list for specific characters
# for name in l_teachers:
#     if name[0] == 'C':
#         print('Teacher that starts with C')
#     else:
#         print("We ain't got it boss...")
        
for name in l_teachers:
    if 'C' in name[0]:
        print('Found')
    else:
        print('Not Found')