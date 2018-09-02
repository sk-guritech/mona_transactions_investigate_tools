#Requirements: None
#How to Use:python transactions_analyzer.py [address] (*need transactions.json)
#By @GuriTech

import json
import sys

address = sys.argv[1]


with open(address + '_transactions.json','r') as file:
	json_data = json.load(file)

relation_addresses = []

#make reletion-adresses-list
for transaction in json_data['txs']:
	vin  = transaction['vin']
	vout = transaction['vout']

	for v in vin:
		relation_addresses.append(v['addr'])

	for v in vout:
		relation_addresses.append(v['scriptPubKey']['addresses'][0])

	relation_addresses = list(set(relation_addresses))

with open(address + '_relation_addresses.txt','w') as file:
	for relation_address in relation_addresses:
		file.write(relation_address + '\n')

#make simple-money-flow
with open(address + '_money_flow.json','w') as file:
	file_data = {}


	for transaction in json_data['txs']:
		simple_transaction = {}

		simple_transaction['input'] = [{'value':float(vin['value']),'addr':vin['addr']} for vin in transaction['vin']]
		simple_transaction['output'] = [{'value':float(vout['value']),'addr':vout['scriptPubKey']['addresses'][0]} for vout in transaction['vout']]
		block_time = transaction['blocktime']

		file_data[int(block_time)] = simple_transaction
	json.dump(file_data,file,indent=4)