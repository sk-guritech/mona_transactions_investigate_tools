#requirements : pydot, requests
#How To Use : python3 mona_researcher.py [address]
#By @GuriTech

import sys
import os
import json

from get_transactions import get_transactions
from get_relation_addresses import get_relation_addresses
from make_money_flow_graph import make_money_flow_graph

def research_target_address(target_address):
	output_dir_path = './ResearchResults/' + target_address + '/'
	os.makedirs(output_dir_path, exist_ok=True)

	# Transactions
	transactions = get_transactions(target_address, 200)
	with open(output_dir_path + target_address + '_transactions.json', 'w') as file:
		json.dump(transactions, file, indent = 4)

	# Relation Addresses
	relation_addresses = get_relation_addresses(transactions)
	with open(output_dir_path + target_address + '_relation_addresses.txt','w') as file:
		for relation_address in relation_addresses:
			file.write(relation_address + '\n')	

	# Money Flow
	make_money_flow_graph(output_dir_path, target_address, transactions)

	return relation_addresses


if __name__ == '__main__':
	target_address = sys.argv[1]
	research_target_address(target_address)