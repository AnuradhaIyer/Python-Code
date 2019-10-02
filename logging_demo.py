import logging
 
logging.basicConfig(
    level = logging.INFO,
    format = '%(levelname)-8s | %(name)-4s | %(asctime)s |  %(module)s:%(lineno)4d %(message)s',
    filename = 'demo.log',
)
 
mgmt = logging.getLogger('mgmt')
 
logging.critical('The CPU is fire!')
logging.error('%d requests accepted and approved but only %d were fulfilled', 238, 231)
mgmt.warning('User %r attempted %d log ins.  Suspected intrusion', 'superman123', 1500)
mgmt.info('There were %d transactions completed in %.1f seconds', 15_675, 18.3246)
logging.debug('Re-sorting procedure took %d seconds', 76)
 
d = {'mary': 'green', 'jane': 'blue'}
try:
    print(d['tom'])
except KeyError:
    logging.exception('Missing key!')
print('Done')    
