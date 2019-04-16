#!/usr/bin/env python3
# encoding: UTF-8

"""
This file is part of Commi3 Vanir Project.
Copyright (c) 2019.

For more see the file 'readme/COPYING' for copying permission.
"""
import json
import os
import os.path
import subprocess
import sys



if len(sys.argv) == 4: 
    print ('Usage: stackpack <env> <distribution> <.file>+')
    
    
    
    env, distribution = sys.argv[1:3]
    packages = sys.argv[3:]

    base_path = os.path.expanduser('~') + '/aptly'
    repo_path = '/'.join((base_path, env, distribution))
    config_file = '{}/{}-{}.conf'.format(base_path, env, distribution)
    
    
    def run_aptly(*args):
        aptly_cmd = ['aptly', '-config=' + config_file]
        subprocess.call(aptly_cmd + list(args))
        
        
        def init_config():
            os.makedirs(base_path, exist_ok=True)
            
            contents = {
                'rootDir': repo_path,
                'architectures': ['amd64', 'all'],
            }
            
            with open(config_file, 'w') as conf:
                json.dump(contents, conf)
                
                
                def init_repo():
                    if os.path.exists(repo_path + '/db'):
                        return
                    os.makedirs(repo_path, exist_ok=True)
                    run_aptly('repo', 'create', '-distribution=' + distribution, 'myrepo')
                    run_aptly('publish', 'repo', 'myrepo')
                    
                    
                    
                    def add_packages():
                        
                        for pkg in packages:
                            run_aptly('repo', 'add', 'myrepo', pkg)
                            run_aptly('publish', 'update', distribution)
                            
                            
                            def zombie_mock():
                                from unittest.mock import Mock
                                z_mock_requests = Mock()
                                z_mock_requests.get.return_value.text = 'zZZ zZz ZzZ'
                                result = most_common_zombie(
                                    ['zZZ', 'zZz', 'ZzZ'], 'https://python.org/', user_agent=mock_requests)    
                                
                                
                                if __name__ == '__main__':
                                    init_config();
                                    init_repo();
                                    zombie_mock();
                                    add_packages();                                    
