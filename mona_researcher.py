#requirements : pydot, requests
#How To Use : python3 mona_researcher.py [address]
#By @GuriTech

import sys
import os
import json
import time

from get_transactions import get_transactions
from get_relation_addresses import get_relation_addresses
from make_money_flow_graph import make_money_flow_graph

def research_target_address(target_address,max_pageNum = 200):
	output_dir_path = './ResearchResults/' + target_address + '/'
	os.makedirs(output_dir_path, exist_ok=True)

	# Transactions
	transactions = get_transactions(target_address, max_pageNum)
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

def recursive_target_research(target_addresses,recursive_max_time,researched_addresses = []):
	relation_all_addresses = target_addresses

	for recursive_time in range(int(recursive_max_time)):
		for target_address in relation_all_addresses[:]:
			if target_address in researched_addresses:
				relation_all_addresses.remove(target_address)
				continue

			relation_addresses = research_target_address(target_address)

			for relation_address in relation_addresses:
				relation_all_addresses.append(relation_address)

			researched_addresses.append(target_address)
			print('Researching ' + target_address + ' Finished !')
			time.sleep(1)

		relation_all_addresses = list(set(relation_all_addresses))


if __name__ == '__main__':
	if len(sys.argv) == 1:
		print('python mona_researcher.py [address] [options]')
		sys.exit()

	target_address = sys.argv[1]

	if len(sys.argv) == 2:
		research_target_address(target_address)
		print('Researching Finished !')

	elif '-r' in sys.argv and '-f' in sys.argv: 
		with open('./ResearchResults/' + target_address + '/' + target_address + '_relation_addresses.txt') as file:
			target_addresses = file.read().split('\n')[:-1]
		
		try:
			recursive_max_time = int(sys.argv[sys.argv.index('-r')+1])
		except:
			recursive_max_time = 2

		recursive_target_research(target_addresses,recursive_max_time,researched_addresses = [target_address])
		print('Researching Finished !')

	elif '-r' in sys.argv:
		try:
			recursive_max_time = int(sys.argv[sys.argv.index('-r')+1])
		except:
			recursive_max_time = 2

		recursive_target_research([target_address],recursive_max_time)

		print('Researching Finished !')

	elif '-f' in sys.argv:
		with open('./ResearchResults/' + target_address + '/' + target_address + '_relation_addresses.txt') as file:
			target_addresses = file.read().split('\n')[:-1]

		for target in target_addresses:
			if target_address == target:
				continue
			research_target_address(target)

		print('Researching Finished !')
