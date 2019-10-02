from urllib.request import urlopen
from time import perf_counter as time
import threading
 
printer_lock = threading.Lock()
 
def summarize_url(url):
    "Display summary statistics about a website"
    u = urlopen(url)
    charset = (u.headers.get_charsets() or ['latin-1'])[0]
    page = u.read().decode(charset)
 
    with printer_lock:
        print('-' * 60)
        print(f'Scanning the website: {url!r}')
        print(f'It has {len(page):,d} characters')
        print(f'The encoding is: {charset!r}')
        print(f'The number of words is: {len(page.split()):,d}')
 
start = time()
# Checkpoint:  The timer is started
 
with printer_lock:
    print('=' * 60)
# Checkpoint:  The top bar has printed
 
workers = []
for url in [
    'http://www.python.org',
    'http://www.perl.org',
    'http://www.cnn.com',
    'http://www.golang.com',
    'http://www.cnbc.com',
    'http://www.yahoo.com',
    'http://www.paypal.com',
    'http://www.cbs.com',
    'http://www.nbc.com',
]:
    t = threading.Thread(target=summarize_url, args=[url])
    t.start()
    workers.append(t)
# Checkpoint:  Nine worker threads have started
#              and we know who they are are
 
for worker in workers:
    worker.join()
# Checkpoint:  Nine works threads have finished    
 
with printer_lock:    
    print('=' * 60)
    print(time() - start, 'seconds')
