import os

def create_ml_dir(project_path):
    """Create a set of directories for a machine learning project."""
    dirs = ['data', 'data/raw', 'data/interim', 'data/processed', 'data/external', 
        'notebooks', 
        'src', 'src/data', 'src/features', 'src/models', 'src/visualisation',
        'models',
        'tests', 'tests/data', 'tests/features', 'tests/models', 'tests/visualisation',
        'docs',
        'config',
        'reports', 'reports/figures',
        'docs']
    
    files = ['README.md', '.gitignore', 'setup.py', 'requirements.txt', 'Makefile', 'Dockerfile', '.dockerignore']

    # Create each directory
    for dir_name in dirs:
        dir_path = os.path.join(project_path, dir_name)
        try:
            os.makedirs(dir_path)
            print(f"Directory {dir_path} was created.")
        except FileExistsError:
            print(f"Directory {dir_path} already exists.")

    for file in files:
        try:
            with open(file, 'x') as f:
                pass
            print(f"The file {file} was created.")
        except FileExistsError:
            print(f"The file {file} already exists.")
