from wireguard import Wireguard

wg = Wireguard(
    server_private_key='QNmEt7eMOutxw361u1OX/Z9GTRiGMQxeBiOpXKyVIVQ='
)

private_key = wg.get_private_key
private_key = 'yN6+qW9UB+GNJ0r9Axk4RLfPpukC6xv9TtI+CF0bJFc='
pub_key = wg.get_pub_key(private_key=private_key)

ip = wg.new_ip
print(ip)# pub_key)
# yN6+qW9UB+GNJ0r9Axk4RLfPpukC6xv9TtI+CF0bJFc=

# wg.add(public_key=pub_key, ip=ip)

# print()
print(wg.info(who='peers'))