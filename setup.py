import json, sys
from setuptools import setup, find_packages
from warskald import utils, AttrDict, cmdx

PROJ_NAME = 'prologger'
DIR_NAME = 'prologger'

VERSION_PATH = f'/home/joseph/coding_base/{DIR_NAME}/version_info.json'
VERSION_INFO = AttrDict(json.load(open(VERSION_PATH, 'r')))
version = f'{VERSION_INFO.maj}.{VERSION_INFO.min}.{VERSION_INFO.rev}'
print(f'Current version: {version}')


args = utils.get_inputs()
sys.argv = sys.argv[:2]

if(isinstance(args, AttrDict)):
    inc_maj = args.maj or args.M
    inc_min = args.min or args.m
    inc_rev = args.rev or args.r
    clear_dist = args.clear or args.c

    if(inc_maj):
        VERSION_INFO.maj += 1
        VERSION_INFO.min = 0
        VERSION_INFO.rev = 0
    elif(inc_min):
        VERSION_INFO.min += 1
        VERSION_INFO.rev = 0
    elif(inc_rev):
        VERSION_INFO.rev += 1
        
    
    original_version = version

    version = f'{VERSION_INFO.maj}.{VERSION_INFO.min}.{VERSION_INFO.rev}'
    
    print(f'New version: {version}')
    
    if(version != original_version):
        print('Updating version info')
        json.dump(VERSION_INFO, open(VERSION_PATH, 'w'))
    
    if(clear_dist):
        print('Clearing dist')
        cmdx('rm -rf dist')

setup(
    name=PROJ_NAME,
    version=version,
    packages=find_packages(),
    author="Joseph Bochinski",
    description="Tool to help automate maintaining module documentation prologues.",
    entry_points={ 'console_scripts': ['plog = prologger.main:main'] }
)

#cmdx(f'python -m pip install --upgrade /home/joseph/coding_base/{DIR_NAME}/dist/{PROJ_NAME}-{version}-py3-none-any.whl')