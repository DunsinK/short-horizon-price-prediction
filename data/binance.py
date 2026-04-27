from binance.futures import Futures 

client = Futures()
print(client.time())

client = Futures(key=API_KEY, secret= API_Secret)

print(client.account) #get client information

params = {
    
}