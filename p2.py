
import concurrent.futures 

import re

import random

import numpy as np

import json

import os

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--conc', help='speficy concurrent number')
args = parser.parse_args()

hostname = os.popen('hostname').read().strip()

katas = "ァ 	ア 	ィ 	イ 	ゥ 	ウ 	ェ 	エ 	ォ 	オ 	カ 	ガ 	キ 	ギ 	ク 	グ 	ケ 	ゲ 	コ 	ゴ 	サ 	ザ 	シ 	ジ 	ス 	ズ 	セ 	ゼ 	ソ 	ゾ 	タ 	ダ 	チ 	ヂ 	ッ 	ツ 	ヅ 	テ 	デ 	ト 	ド 	ナ 	ニ 	ヌ 	ネ 	ノ 	ハ 	バ 	パ 	ヒ 	ビ 	ピ 	フ 	ブ 	プ 	ヘ 	ベ 	ペ 	ホ 	ボ 	ポ 	マ 	ミ 		ム 	メ 	モ 	ャ 	ヤ 	ュ 	ユ 	ョ 	ヨ 	ラ 	リ 	ル 	レ 	ロ 	ヮ 	ワ 	ヰ 	ヱ 	ヲ 	ン 	ヴ 	ヵ ヶ"

chars = re.sub(r'\s{1,}', ' ', katas).split()
index_char = { index: char for index, char in enumerate(chars) }
char_index = { char: index for index, char in index_char.items() }

open('index_char.json', 'w').write( json.dumps(index_char,indent=2, ensure_ascii=False) )
answer = np.array([ char_index[char] for char in list('シェイクスピア') ])

max_index = max(index_char.keys())
#print(answer)
def _map(index):
  np.random.seed(int(random.random()*100))
  for i in range(10000000):
    monkey = np.random.randint(max_index, size=(10000000,7))
    delta = monkey - answer
    nz = np.count_nonzero(delta, axis=1)
    mi = np.argmin(nz)
    s = sum( [1 for m, a in zip(monkey[mi], answer) if m == a ] )
    result = {'sum':s, 'monkey':monkey[mi].tolist(), 'ans':answer.tolist()} 
    print( result )
    open('monkey.p2/{}_{}_{}.json'.format(hostname, index, i), 'w').write( json.dumps(result, indent=2, ensure_ascii=False) )


indexies = [i for i in range(10000)]
#_map(0)
with concurrent.futures.ProcessPoolExecutor(max_workers=int(args.conc)) as exe:
  exe.map(_map,  indexies)
