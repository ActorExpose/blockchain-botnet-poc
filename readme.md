# Attacking With Bitcoin
## PREFACE
This repository is PoC toolkit for creating and interacting with Bitcoin based floating command and control infrastructure.This infrastucture is designed to create robust censorship resistant malware. Work contained here has been completed in line with Deakin's Summer Casual Research roles and is currently awaiting peer review.


# Contents
## 1. MalwareManager.py:
This file contains the logic in order to find OP_Return data within a particular queried block hash or transaction hash. This can be used to create a further 'work' like behaviour, in order to extract the next block or transaction hash.

## 2. query_transaction.py:
This file contains the logic required in order to complete the query transaction logic when using direct APIs instead of 'decentralised' options like our P2P API.

## 3. transaction-result.txt:
This file contains the JSON output from the `createrawtransaction` method explained in more detail later in this document.



# Creating Raw Transactions
The below instructions detail how to write OP_Return data to the Bitcoin Blockchain.

### 1. listunspent:
    Obtain txid, vout for createrawtransaction
    Obtain address for dumpprivkey
### 2. dumpprivkey:
    dump priv key of address obtained in (1)
### 3. createrawtransaction:
    FORMAT:
        createrawtransaction '[{inputs}]' '{data, output1, output2...}'
    EXAMPLE:
        createrawtransaction '[{"txid":"382bda6ee2bac22afd051104af16146436895ecca382a76c2d66535a837254bc" ,"vout":1}]' '{"data": "3132372e302e302e313a38313831","2MuMVAFK2gbTDNVBhLtpZfA4Xi62mWh6bU5":0.00948920, "tb1q479t6caqp3q26a0y0pctrv9pmket5lnx24twcx": 0.015}'

### 4. signrawtransactionwithwallet
    FORMAT:
        signrawtransaction 'hex'

### 5. sendrawtransaction
    FORMAT:
        sendrawtransaction 'signedtrnasactionhex'


# Further Links
### These have been provided as a means to express additional research that was not necessarily referenced in our research paper, however does show potential problem areas along with their solution.

| Details |  Link |
|---|---|
| Transaction used in research | https://live.blockcypher.com/btc-testnet/tx/2599dbe540a583ede3512fef9a0f26be718c039ffd4d04d85ff3b339f40e73b1 |
| Full Bitcoin CMD Guide | https://github.com/ChristopherA/Learning-Bitcoin-from-the-Command-Line |
| Bitcoin: Sign raw transactions in segwit | https://bitcoin.stackexchange.com/questions/57026/to-sign-raw-transaction-in-segwit |
| Bitcoin: Signing offline transactions | https://bitcoin.stackexchange.com/questions/80435/signing-a-bitcoin-transaction-offline-fails?rq=1 |
| Bitcoin: Sign with bitcoind and non-private-wallets | https://bitcoin.stackexchange.com/questions/29955/how-to-sign-bitcoin-transaction-with-bitcoind-and-non-bitcoind-wallet-private |
| Bitcoin: Raw transaction fee too high | https://bitcoin.stackexchange.com/questions/79413/raw-transaction-fee-256-absurdly-high-fee-error |
| Bitcoin: raw transaction types | https://www.youtube.com/watch?v=jWKuqP-zTFk |
| Bitcoin :Sign raw transactions | https://bitcoin.stackexchange.com/questions/81688/error-parsing-json-in-bitcoin-cli-signrawtransactionwithkey |
| Bitcoin: Create raw transaction | https://www.youtube.com/watch?v=jWKuqP-zTFk |
| Bitcoin create raw transaction | https://gist.github.com/nopara73/18d77ccb2242d04c508ab1d237fe2ae5 |





