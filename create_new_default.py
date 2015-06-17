'''
Created on Jun 14, 2015

@author: Ben
'''


def create_new_default(directory: str, dest: dict):
    ''' 
    Creates new default parameter file based on parameter settings 
    '''
    with open(directory, 'w') as new_default:
        new_default.write(
'''TARGET DESTINATION = {} 
EXCLUDE DESTINATION = {}
'''.format(dest['target'], dest['exclude']))