from tfchain.TFChainExplorerClient import TFChainExplorerClient
from tfchain.internal.jsutils import json_loads

def test_explorer_client():
    client = TFChainExplorerClient(addresses=['https://explorer2.threefoldtoken.com'])
    resp = client.get(endpoint='/explorer/constants')
    data = json_loads(resp)
    assert data['chaininfo']['Name'] == 'tfchain'
    assert data['chaininfo']['CoinUnit'] == 'TFT'