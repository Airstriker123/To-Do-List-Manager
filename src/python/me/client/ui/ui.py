class UserInterface:
    """Class to store user interface variables which can be used to print some shit"""
    def __init__(self):
        self.banner = \
'''                                                                                                                  
    _|_|_|_|_|    _|_|                _|_|_|      _|_|                _|        _|_|_|    _|_|_|  _|_|_|_|_|      
        _|      _|    _|              _|    _|  _|    _|              _|          _|    _|            _|          
        _|      _|    _|  _|_|_|_|_|  _|    _|  _|    _|  _|_|_|_|_|  _|          _|      _|_|        _|          
        _|      _|    _|              _|    _|  _|    _|              _|          _|          _|      _|          
        _|        _|_|                _|_|_|      _|_|                _|_|_|_|  _|_|_|  _|_|_|        _|          
                                                                                                                  
                                                                                                                  
        '''
#menu variable
        self.task_menu = \
"""
================================================================================================================
[1] Add a task
[2] Remove a task
[4] Check off a task
[5] exit 
================================================================================================================               
\n"""
#list tasks from input
        self.list_tasks = \
f"""
Tasks:


\n"""


