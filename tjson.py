import json
import os, psutil

process = psutil.Process(os.getpid())

suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
def humansize(nbytes):
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

def print_memory():
    print(humansize(process.memory_info().rss))

print_memory() # 9.1 MB
with open('huge.json') as f:
    print_memory() # 9.12 MB
    dict = json.load(f)

    print(dict['type']) # FeatureCollection
    print_memory() # 133.02 MB
