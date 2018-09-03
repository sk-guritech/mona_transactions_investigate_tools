def get_relation_addresses(transactions):
	relation_addresses = []

	for transaction in transactions['txs']:
		vin  = transaction['vin']
		vout = transaction['vout']

		for v in vin:
			try:
				relation_addresses.append(v['addr'])
			except:
				pass

		for v in vout:
			try:
				relation_addresses.append(v['scriptPubKey']['addresses'][0])
			except:
				pass

		relation_addresses = list(set(relation_addresses))

	return relation_addresses