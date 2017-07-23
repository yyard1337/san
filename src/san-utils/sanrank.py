#!/usr/bin/python

import requests

presale_wallet = "3438NkmmjVzv3KBMT8c2PmhxC6gtNzkhAo"

txs_url = "http://btc.blockr.io/api/v1/address/txs/" + presale_wallet

r = requests.get(txs_url)

candidates = {}

if 200 == r.status_code:
	for tx in r.json()["data"]["txs"]:
		tx_amount = tx["amount"]
		tx_id = tx["tx"]
		# http://btc.blockr.io/api/v1/tx/info/3438NkmmjVzv3KBMT8c2PmhxC6gtNzkhAo
		tx_url = "http://btc.blockr.io/api/v1/tx/info/" + tx_id
		print tx_url
		r = requests.get(tx_url)
		if 200 == r.status_code:
			print "OK"
			# print r.json()

