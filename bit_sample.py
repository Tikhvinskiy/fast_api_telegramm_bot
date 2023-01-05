import bit
from config import key_bit

# wallet = bit.Key(key_bit)
# print(f"Баланс: {wallet.get_balance()}")
# print(f"Адрес: {wallet.address}")
# print(f"Приватный ключ: {wallet.to_wif()}")

k = bit.PrivateKeyTestnet(key_bit)
print(f"Баланс: {k.get_balance()}")
# print(k.get_balance('usd'), 'USD')
# print(k.get_balance('rub'), 'RUB')
# print(f"Адрес: {k.address}")
# print(f"Приватный ключ: {k.to_wif()}")
# k.send([('mw5A2h44pMzunbwLRDhnBe68cS8CLWBxu7', 300000/(100000000), 'btc')])
# print(k.get_transactions())
