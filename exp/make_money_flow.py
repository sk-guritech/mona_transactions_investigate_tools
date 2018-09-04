#Useage: 
#1: set [address]_transactions.json same directory
#2: python3 make_money_flow.py [address]

import pydot
import json
import sys
from pprint import pprint

address = sys.argv[1]

txs = []
with open(address + '_transactions.json','r') as file:
	txs = json.load(file)['txs']

blocks = {}

for tx in txs:
	blocktime = str(tx['blocktime'] + 25200)

	n = 0
	while True:
		if blocktime + '_' + str(n) not in blocks.keys():
			blocktime += '_' + str(n)
			break
		n += 1

	if blocktime not in blocks.keys():
		blocks[blocktime] = {'vin':{},'vout':{}}

	for vin in tx['vin']:
		vin_address = vin['addr']

		if vin_address not in blocks[blocktime]['vin'].keys():
			blocks[blocktime]['vin'][vin_address] = 0

		blocks[blocktime]['vin'][vin_address] += vin['value']


	for vout in tx['vout']:
		vout_address = vout['scriptPubKey']['addresses'][0]

		if vout_address not in blocks[blocktime]['vout'].keys():
			blocks[blocktime]['vout'][vout_address] = 0

		blocks[blocktime]['vout'][vout_address] += float(vout['value'])

# Make Block Graph
block_time_list = list(blocks.keys())
block_time_list.sort()

dot_data = 'digraph G {rankdir=TB;layout=dot;\n'

for n in range(len(block_time_list)):
	dot_data += block_time_list[n] + ' [shape=box,fontcolor=blue,fillcolor="#CC9999"];\n'

for n in range(len(block_time_list) - 1):
	dot_data += block_time_list[n] + ' -> '
dot_data += block_time_list[-1] + ' [color=red,weight=5,arrowsize=1.5];\n'

# Add Transactions
for block_time in block_time_list:
	vin = blocks[block_time]['vin']
	vout = blocks[block_time]['vout']

	for in_address in vin.keys():
		dot_data += in_address + '_' + block_time + ' -> ' + block_time + ' [label = ' + str(vin[in_address]) + ' ];\n'

	for out_address in vout.keys():
		dot_data += block_time + ' -> ' + out_address + '_' + block_time + ' [label = ' + str(vout[out_address]) + ' ];\n'

dot_data += '}'

with open(address + '_money_flow.dot','w') as file:
	file.write(dot_data)



(graph,) = pydot.graph_from_dot_file(address + '_money_flow.dot')
graph.write_svg(address +'_money_flow.svg')