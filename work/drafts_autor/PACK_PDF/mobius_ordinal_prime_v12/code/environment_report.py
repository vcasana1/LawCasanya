"""Record software versions visible in the current environment."""
import importlib.metadata
import sys

print('python', sys.version.replace('\n', ' '))
for package in ('numpy', 'scipy', 'sympy', 'matplotlib'):
    try:
        version = importlib.metadata.version(package)
    except importlib.metadata.PackageNotFoundError:
        version = 'not installed in this audit environment'
    print(package, version)
