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
	transactions = get_transactions(target_address, 200) #
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

def single_target_research(target_address):
	research_target_address(target_address)
	print('Researching Finished !')

def recursive_target_research(root_target_address,recursive_max_time):
	relation_all_addresses = [root_target_address]
	researched_addresses = []

	for recursive_time in range(recursive_max_time):
		for target_address in relation_all_addresses[:]:
			if target_address in researched_addresses:
				continue

			relation_addresses = research_target_address(target_address)

			for relation_address in relation_addresses:
				relation_all_addresses.append(relation_address)

			researched_addresses.append(target_address)
			print('Researching ' + target_address + ' Finished !')
			time.sleep(1)


if __name__ == '__main__':
	if len(sys.argv) == 1:
		print('python mona_researcher.py [address] [options]')

	target_address = sys.argv[1]
	recursive_max_time = 2

	if len(sys.argv) >= 3:
		if len(sys.argv) == 4:
			recursive_max_time = sys.argv[3]

	if sys.argv[2] == '-r':
		recursive_target_research(target_address,recursive_max_time)
	elif len(sys.argv) == 2:
		research_target_address(target_address)