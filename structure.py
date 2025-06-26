import os

def print_tree(start_path='.', prefix=''):
    for item in os.listdir(start_path):
        # Skip .venv directory
        if item == '.venv' or item == 'structure.py':
            continue
            
        path = os.path.join(start_path, item)
        print(prefix + '|-- ' + item)
        if os.path.isdir(path):
            print_tree(path, prefix + '|   ')

HOME = os.getenv("HOME")
if HOME:
    target_path = os.path.join(HOME, 'Code', 'ADK',"Admission_counselor")
    print_tree(target_path)
else:
    print("HOME environment variable not found")
