# Instructions
## 1. listunspent:
    Obtain txid, vout for createrawtransaction
    Obtain address for dumpprivkey
## 2. dumpprivkey:
    dump priv key of address obtained in (1)
## 3. createrawtransaction:
    FORMAT:
        createrawtransaction '[{inputs}]' '{data, output1, output2...}'
    EXAMPLE:
        createrawtransaction '[{"txid":"382bda6ee2bac22afd051104af16146436895ecca382a76c2d66535a837254bc" ,"vout":1}]' '{"data": "3132372e302e302e313a38313831","2MuMVAFK2gbTDNVBhLtpZfA4Xi62mWh6bU5":0.00948920, "tb1q479t6caqp3q26a0y0pctrv9pmket5lnx24twcx": 0.015}'

## 4. signrawtransactionwithwallet
    FORMAT:
        signrawtransaction 'hex'

## 5. sendrawtransaction
    FORMAT:
        sendrawtransaction 'signedtrnasactionhex'
ACTUAL BASE TRANSACTION: https://live.blockcypher.com/btc-testnet/tx/2599dbe540a583ede3512fef9a0f26be718c039ffd4d04d85ff3b339f40e73b1/

FULL GUIDE: https://github.com/ChristopherA/Learning-Bitcoin-from-the-Command-Line


LINKS:
https://bitcoin.stackexchange.com/questions/81688/error-parsing-json-in-bitcoin-cli-signrawtransactionwithkey

https://bitcoin.stackexchange.com/questions/57026/to-sign-raw-transaction-in-segwit

https://bitcoin.stackexchange.com/questions/80435/signing-a-bitcoin-transaction-offline-fails?rq=1

https://bitcoin.stackexchange.com/questions/29955/how-to-sign-bitcoin-transaction-with-bitcoind-and-non-bitcoind-wallet-private

https://bitcoin.stackexchange.com/questions/79413/raw-transaction-fee-256-absurdly-high-fee-error

https://github.com/bitcoin/bitcoin/issues/13218

https://gist.github.com/nopara73/18d77ccb2242d04c508ab1d237fe2ae5

https://www.youtube.com/watch?v=jWKuqP-zTFk

