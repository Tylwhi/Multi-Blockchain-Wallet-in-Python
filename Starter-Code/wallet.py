# Import dependencies
import subprocess
import json
from dotenv import load_dotenv
import os
  
from bit import PrivateKeyTestnet
from bit import wif_to_key
from bit.network import NetworkAPI, satoshi_to_currency

from web3 import Web3
from eth_account import Account 

from constants import ETH, BTC, BTCTEST

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")

# Import constants.py and necessary functions from bit and web3
# YOUR CODE HERE
 
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Create a function called `derive_wallets`
def derive_wallets(# YOUR CODE HERE):
    command = # YOUR CODE HERE
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
# YOUR CODE HERE
coins = {
    ETH: derive_wallets(),
    BTCTEST: derive_wallets()
}
    
# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
# YOUR CODE HERE):
    # YOUR CODE HERE
def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account().privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)
# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
# YOUR CODE HERE):
    # YOUR CODE HERE
def create_tx(coin, account, to, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas({
            "from": account.address, 
            "to": to, 
            "value": amount
        })
      nonce =  w3.eth.getTransactionCount(sender)+1
        
        return {
            'to': to,
            'from': account.address,
            'value': amount,
            'gas': gasEstimate,
            'gasPrice': Web3.eth.generateGasPrice(),
            'nonce': nonce
        }
    elif coin == BTCTEST:
        return account.prepare_transaction(account.address, [(to, amount, BTC)])
# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
# YOUR CODE HERE):
    # YOUR CODE HERE
def send_tx(coin, account, to, amount):
    raw_tx = create_tx(coin, account, to, amount)
    if coin == ETH:
        sign = account.signTransaction(raw_tx)
        return w3.eth.sendRawTransaction(sign.rawTransaction)
    elif coin == BTCTEST:
        sign = account.sign_transaction(raw_tx)
        return NetworkAPI.broadcast_tx_testnet(signed)
