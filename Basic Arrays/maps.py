'''
Python Maps also called ChainMap is a type of data structure to manage multiple dictionaries together as one unit. 
The combined dictionary contains the key and value pairs in a specific sequence eliminating any duplicate keys. 
The best use of ChainMap is to search through multiple dictionaries at a time and get the proper key-value pair mapping.
 We also see that these ChainMaps behave as stack data structure.
'''
import collections
dict1 = {
    'days1':'Mon',
    'days2': 'Tue',
    }
dict2 = {
    'days3':'Wed',
    'days4':'Sun'
}
res = collections.ChainMap(dict1,dict2)
#  creating a single dictionary
print(res.maps)

print(f'Keys = {list(res.keys())}')
print(f'Values = {list(res.values())}')


print(res.items())
print("elements:")
for key,val in res.items():
    print(f'{key}:{val}')

