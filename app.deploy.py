import json
import os
from urllib2 import urlopen

configuration_file = 'app.deploy.config.json'

with open(configuration_file) as json_file:
    data = json.load(json_file)
    for p in data['configurations']:

        print ('***** Start ***************')
        print('Remote Host: ' + p['host'])
        print('Ssh port: ' + p['ssh_port'])
        print('Dist directory: ' + p['deploy_dist'] )
        print('Local app directory: ' + p['deploy_dir'])
        print('Remote app directory: ' + p['deploy_dist'] )
        print('')
        print ('***** Start deploy ***************')
        print ('Check remote connection')

        HOST_UP  = True if os.system("ping -c 1 " + p['host']) is 0 else False

        if(HOST_UP == True):
            print "- Machine online"
            print ''
            print "-- Reading deploy commands ...."

            for c in p['tasks']:
                print ''
                print '--- ' + c['title'] + ' on ' + c['local'] + ' status: ' +  c['status']
                # print command
                print ''
                if  (c['status'] == 'enabled'):
                    print c['command']
                    os.system(c['command'])
                print '----------------------------'
        else:
            print "Machine offline stop all tasks...."

print ''
print ''
print ''
print 'Finish all tasks ;-)'