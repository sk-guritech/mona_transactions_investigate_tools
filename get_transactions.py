import requests
import time
import json
from pprint import pprint

def get_transactions(target_address, max_page_num):
	url = 'https://mona.chainsight.info/api/txs?address=' + target_address + '&pageNum='

	headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

	page_num = 0

	transactions = {'txs':[]}

	while True:
		try:
			response = requests.get(url + str(page_num), headers=headers)
			print(url + str(page_num))
			json_data = json.loads(response.text)

			if json_data['txs'] == []:
				break

			print(response.status_code)

			for txs in json_data['txs']:
				transactions['txs'].append(txs)

			print('page_num_' + str(page_num), 'Completed !')
			page_num += 1

			if page_num >= int(max_page_num):
				break

			time.sleep(1) #*1sec
		except Exception as ee:
			pprint(ee)
			break

	print('Get Transactions Finished !')

	return transactions