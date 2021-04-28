import bigjson
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

print_memory() # 9.16 MB
with open('huge.json', 'rb') as f: # file size 18,6 MB
    print_memory() # 9.18 MB
    dict = bigjson.load(f)

    print(dict['type']) # FeatureCollection
    print(dict['features'][0]['properties']['MAPBLKLOT'])
    print_memory() # 10.18 MB
