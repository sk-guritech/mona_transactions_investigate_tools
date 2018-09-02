import pydot
from datetime import datetime
def make_money_flow_graph(output_path, target_address, transactions):
	# Make .dot File

	TIME_ZONE_OFFSET = 60 * 60 * 7

	simple_transactions = {}

	for transaction in transactions['txs']:
		simple_transaction = {}
		simple_transaction['input'] = [{'value':float(vin['value']),'addr':vin['addr']} for vin in transaction['vin']]
		simple_transaction['output'] = [{'value':float(vout['value']),'addr':vout['scriptPubKey']['addresses'][0]} for vout in transaction['vout']]

		block_time = int(transaction['blocktime']) + TIME_ZONE_OFFSET
		simple_transactions[block_time] = simple_transaction


	time_listed_transactions = sorted(simple_transactions.items())
	address_appear_times = {}

	for time_listed_transaction in time_listed_transactions:
		block_time = int(time_listed_transaction[0])
	
		for input_address in time_listed_transaction[1]['input']:
			if input_address['addr'] not in address_appear_times:
				address_appear_times[input_address['addr']] = [block_time]
			else:
				address_appear_times[input_address['addr']].append(block_time)

		for output_address in time_listed_transaction[1]['output']:
			if output_address['addr'] not in address_appear_times:
				address_appear_times[output_address['addr']] = [block_time]
			else:
				address_appear_times[output_address['addr']].append(block_time)

	for address in address_appear_times.keys():
		address_appear_times[address] = list(set(address_appear_times[address]))


	graph_data = "digraph{rankdir=TB;"
	graph_edges = []

	for time_listed_transaction in time_listed_transactions:
		block_time = int(time_listed_transaction[0])
		block_time = datetime.fromtimestamp(block_time).strftime("%Y%m%d_%Hh%Mm%Ss")

		for input_address in time_listed_transaction[1]['input']:
			for output_address in time_listed_transaction[1]['output']:
				graph_edges.append(input_address['addr'] + '_' +str(block_time) + ' -> ' + output_address['addr']+ '_' +str(block_time) + ';\n')

	for address in address_appear_times.keys():
		address_appear_times[address].sort()

		for n in range(len(address_appear_times[address])-1):
			graph_edges.append(address + '_' + datetime.fromtimestamp(float(address_appear_times[address][n])).strftime("%Y%m%d_%Hh%Mm%Ss") + ' -> ' + address + '_' + datetime.fromtimestamp(float(address_appear_times[address][n+1])).strftime("%Y%m%d_%Hh%Mm%Ss") + ';\n')

	graph_edges = list(set(graph_edges))

	for edge in graph_edges:
		graph_data += edge

	graph_data += '}'

	with open(output_path + target_address + '_money_flow_graph.dot','w') as file:
		file.write(graph_data)

	#Make SVG File
	(graph,) = pydot.graph_from_dot_file(output_path + target_address + '_money_flow_graph.dot')
	graph.write_svg(output_path + target_address +'_money_flow_graph.svg')