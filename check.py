import glob

import json

import sys

import os
if '--p1' in sys.argv:
  for name in glob.glob('monkey/*.json'):
    _ma_mo = json.loads( open( name ).read() )
    try:
      ma = max(_ma_mo.items(), key=lambda x:x[0])
    except:
      continue
    ma, li = ma
    print( ma )

if '--p2' in sys.argv:
  index_char = json.load( open('index_char.json') )
  for name in glob.glob('monkey_work/*.json'):
    obj = json.loads( open( name ).read() )
    s = obj['sum']
    if s >= 5:
      indexies = obj['monkey']
      words = [ index_char[str(i)] for i in indexies ]
      print(s, '文字一致', ''.join(words) )
    else:
      os.remove(name)
      print('remove', name)
