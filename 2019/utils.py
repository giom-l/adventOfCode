def read_file(path):
    with open(path, 'r') as content:
        lines=content.readlines()
    return [line.strip() for line in lines]
