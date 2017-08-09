import string
from pprint import pprint


def optimize_data(template, data):
    # part0 = [t[0] for t in string.Formatter().parse(template) if t[0] is not None]
    # clean_key = part0[0].split(':')[0]
    part1 = [t[1] for t in string.Formatter().parse(template) if t[1] is not None]
    list_of_keys = [x.split(']') for x in part1[0].split('[')]
    new_data = {}
    new_list_of_keys_and_val = []
    for keys in list_of_keys:
        for key in keys:
            if key:
                val = data[key]
                data = val
                if not isinstance(val, str):
                    new_list_of_keys_and_val.append(key)
                else:
                    new_data[key] = val
    for key in reversed(new_list_of_keys_and_val):
        new_data = {key: new_data}
    return new_data


def main():
    template = 'Python version: {languages[python][latest_version]}'
    data = {
        'languages': {
            'python': {
                'latest_version': '3.6',
                'site': 'http://python.org',
            },
            'rust': {
                'latest_version': '1.17',
                'site': 'https://rust-lang.org',
            },
        },
    }
    print("Original data:")
    pprint(data)
    new_data = optimize_data(template, data)
    print("Optimized data:")
    pprint(new_data)


if __name__ == '__main__':
    main()