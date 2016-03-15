import os
import json


def dfs(path, depth):
    d = {'name': os.path.basename(path), 'size': 0, 'directory': False, }
    if os.path.isdir(path):
        d['directory'] = True
        for child in os.listdir(path):
            try:
                c = dfs(os.path.join(path, child), depth + 1)
                d['size'] += c['size']
                if depth == 1 or True:
                    if c['directory']:
                        if 'children' in d:
                            d['children'].append(c)
                        else:
                            d['children'] = [c]
            except Exception as ex:
                print(ex)
        if 'children' in d:
            d['children'] = sorted(d['children'], key=lambda k: k['size'], reverse=True)
    else:
        d['directory'] = False
        d['size'] = os.path.getsize(path)

    return d


if __name__ == '__main__':
    with open('directory.json', 'w') as outfile:
        json.dump(dfs(os.getcwd(), 1), outfile)
