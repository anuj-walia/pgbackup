with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgpackup',
    version='0.1.0',
    author='Anuj Walia',
    author_email='anuj.walia@citi.com',
    description='A utility for backing up PostgreSQL databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/anuj-walia/pgbackup.git',
    packages=find_packages('src')
)
