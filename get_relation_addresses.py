def get_relation_addresses(transactions):
	relation_addresses = []

	for transaction in transactions['txs']:
		vin  = transaction['vin']
		vout = transaction['vout']

		for v in vin:
			relation_addresses.append(v['addr'])

		for v in vout:
			relation_addresses.append(v['scriptPubKey']['addresses'][0])

		relation_addresses = list(set(relation_addresses))

	return relation_addresses