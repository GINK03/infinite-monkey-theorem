
import concurrent.futures 

import re

import random

import json
katas = "ァ 	ア 	ィ 	イ 	ゥ 	ウ 	ェ 	エ 	ォ 	オ 	カ 	ガ 	キ 	ギ 	ク 	グ 	ケ 	ゲ 	コ 	ゴ 	サ 	ザ 	シ 	ジ 	ス 	ズ 	セ 	ゼ 	ソ 	ゾ 	タ 	ダ 	チ 	ヂ 	ッ 	ツ 	ヅ 	テ 	デ 	ト 	ド 	ナ 	ニ 	ヌ 	ネ 	ノ 	ハ 	バ 	パ 	ヒ 	ビ 	ピ 	フ 	ブ 	プ 	ヘ 	ベ 	ペ 	ホ 	ボ 	ポ 	マ 	ミ 		ム 	メ 	モ 	ャ 	ヤ 	ュ 	ユ 	ョ 	ヨ 	ラ 	リ 	ル 	レ 	ロ 	ヮ 	ワ 	ヰ 	ヱ 	ヲ 	ン 	ヴ 	ヵ ヶ"

chars = re.sub(r'\s{1,}', ' ', katas).split()

def _map(index):
  ma_mo = {}
  answer = list('シェイクスピア')
  for i in range(10000000):
    monkey = random.choices(chars, k=7) 
    ch = [ (m, m==a) for m, a in zip(monkey, answer) ]
    m = sum( map(lambda x:x[1], ch) )
    if m >= 4:
      if ma_mo.get(m) is None:
        ma_mo[m] = []
      ma_mo[m].append( monkey )

  open('monkey/{}.json'.format(index), 'w').write( json.dumps(ma_mo, indent=2, ensure_ascii=False) )


indexies = [i for i in range(10000)]
_map(0)
with concurrent.futures.ProcessPoolExecutor(max_workers=16) as exe:
  exe.map(_map,  indexies)
