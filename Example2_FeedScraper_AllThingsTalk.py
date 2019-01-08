# Scraping values from an asset on Allthingstalk
# made by vincent[at]cteq.eu


from time import sleep
from allthingstalk import Client, Device, IntegerAsset
DEVICE_TOKEN = 'DEVICE_TOKEN'
DEVICE_ID='DEVICE_ID'

class Counter(Device):
    counter = IntegerAsset()

client = Client(DEVICE_TOKEN)
device = Counter(client=client,id=DEVICE_ID)

def main():
	while True:
		n= input("E for Exit:")
		if n.strip() == 'E':
			break

@device.feed.counter
def on_reset(device, value, at):
    print('Received %s at %s' % (value, at))

if __name__ == '__main__':
	main()