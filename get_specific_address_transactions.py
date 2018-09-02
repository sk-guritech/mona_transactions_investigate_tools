#Requirements: requests
#How to Use: python get_specific_address_transactions.py [address] [max_page_num]
#By @GuriTech

import requests
import time
import json
import sys
from pprint import pprint

def get_transactions(address, max_page_num):
	url = 'https://mona.chainsight.info/api/txs?address=' + address + '&pageNum='

	#headers = {''}
	headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

	page_num = 0

	file_data = {'txs':[]}

	while True:
		try:
			response = requests.get(url + str(page_num), headers=headers)
			print(url + str(page_num))
			json_data = json.loads(response.text)

			if json_data['txs'] == []:
				break
			print(response.status_code)

			for txs in json_data['txs']:
				file_data['txs'].append(txs)

			print('page_num_' + str(page_num), 'Completed !')
			page_num += 1

			if page_num >= int(max_page_num):
				break

			time.sleep(0.3)
		except Exception as ee:
			pprint(ee)
			break

	txs = {'txs':[tx for tx in json_data['txs'] for t in tx]}
	with open(address + '_transactions.json', 'w') as file:
		json.dump(file_data, file, indent = 4)

	print('Finish !')

if __name__ == '__main__':
	address = sys.argv[1]

	if len(sys.argv) > 2:
		max_page_num = 	sys.argv[2]
	else:
		max_page_num = 100

	get_transactions(address, max_page_num)