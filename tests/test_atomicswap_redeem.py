import pytest

import tfchain

from stubs.ExplorerClientStub import TFChainExplorerGetClientStub

def test():
    # create a tfchain client for devnet
    c = tfchain.TFChainClient.TFChainClient(network_type="devnet")

    # (we replace internal client logic with custom logic as to ensure we can test without requiring an active network)
    explorer_client = TFChainExplorerGetClientStub()
    # add the blockchain info
    explorer_client.chain_info = '{"blockid":"5c180121d6dbbbc8480ee63d58933a4e0d9eae664c0b8662c3ef81102c3fe82c","difficulty":"23546","estimatedactivebs":"146","height":17384,"maturitytimestamp":1549705634,"target":[0,2,200,131,232,66,109,128,132,97,252,155,147,77,241,96,113,131,22,176,230,53,191,80,170,156,189,0,160,84,41,168],"totalcoins":"0","arbitrarydatatotalsize":4351,"minerpayoutcount":17470,"transactioncount":18011,"coininputcount":637,"coinoutputcount":1231,"blockstakeinputcount":17384,"blockstakeoutputcount":17385,"minerfeecount":626,"arbitrarydatacount":573}'
    explorer_client.hash_add('5c180121d6dbbbc8480ee63d58933a4e0d9eae664c0b8662c3ef81102c3fe82c', '{"hashtype":"blockid","block":{"minerpayoutids":["c8f3f82e4c5be07c667f140456e188336dc5c86319260ad9964c1b2a553d7031"],"transactions":[{"id":"9d8823855c59ac903238849e2f31600a9bec2c27d36071402815046dbf8000e7","height":17384,"parent":"5c180121d6dbbbc8480ee63d58933a4e0d9eae664c0b8662c3ef81102c3fe82c","rawtransaction":{"version":1,"data":{"coininputs":null,"blockstakeinputs":[{"parentid":"7c111a656be26b42215d13df330aa46c30d9f84d8b47ca5f41c4a5a1f89c782d","fulfillment":{"type":1,"data":{"publickey":"ed25519:d285f92d6d449d9abb27f4c6cf82713cec0696d62b8c123f1627e054dc6d7780","signature":"8de764af61c2e404f246482a70e29881929a71e4644a4c6f3a620889b1339a3eb789b0e2b5dad4ba26d1862bbee3a62a6f42be8106867722488aed352b414d00"}}}],"blockstakeoutputs":[{"value":"3000","condition":{"type":1,"data":{"unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}}}],"minerfees":null}},"coininputoutputs":null,"coinoutputids":null,"coinoutputunlockhashes":null,"blockstakeinputoutputs":[{"value":"3000","condition":{"type":1,"data":{"unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}},"unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}],"blockstakeoutputids":["be4408fecfa7fb88831d6ff1ff2d32377c25ac6cdafcdec1a16644ef3540d0ea"],"blockstakeunlockhashes":["015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"],"unconfirmed":false}],"rawblock":{"parentid":"d329ebc493b75521db55b6595a7bfcbe5c1f94eb0ab1f7646bf39a42a8f7dddf","timestamp":1549705757,"pobsindexes":{"BlockHeight":17383,"TransactionIndex":0,"OutputIndex":0},"minerpayouts":[{"value":"10000000000","unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}],"transactions":[{"version":1,"data":{"coininputs":null,"blockstakeinputs":[{"parentid":"7c111a656be26b42215d13df330aa46c30d9f84d8b47ca5f41c4a5a1f89c782d","fulfillment":{"type":1,"data":{"publickey":"ed25519:d285f92d6d449d9abb27f4c6cf82713cec0696d62b8c123f1627e054dc6d7780","signature":"8de764af61c2e404f246482a70e29881929a71e4644a4c6f3a620889b1339a3eb789b0e2b5dad4ba26d1862bbee3a62a6f42be8106867722488aed352b414d00"}}}],"blockstakeoutputs":[{"value":"3000","condition":{"type":1,"data":{"unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}}}],"minerfees":null}}]},"blockid":"5c180121d6dbbbc8480ee63d58933a4e0d9eae664c0b8662c3ef81102c3fe82c","difficulty":"23546","estimatedactivebs":"146","height":17384,"maturitytimestamp":1549705634,"target":[0,2,200,131,232,66,109,128,132,97,252,155,147,77,241,96,113,131,22,176,230,53,191,80,170,156,189,0,160,84,41,168],"totalcoins":"0","arbitrarydatatotalsize":4351,"minerpayoutcount":17470,"transactioncount":18011,"coininputcount":637,"coinoutputcount":1231,"blockstakeinputcount":17384,"blockstakeoutputcount":17385,"minerfeecount":626,"arbitrarydatacount":573},"blocks":null,"transaction":{"id":"0000000000000000000000000000000000000000000000000000000000000000","height":0,"parent":"0000000000000000000000000000000000000000000000000000000000000000","rawtransaction":{"version":0,"data":{"coininputs":[],"minerfees":null}},"coininputoutputs":null,"coinoutputids":null,"coinoutputunlockhashes":null,"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},"transactions":null,"multisigaddresses":null,"unconfirmed":false}')
    # add the coin output info of the submitted atomic swap contract
    explorer_client.hash_add('dd1babcbab492c742983b887a7408742ad0054ec8586541dd6ee6202877cb486', '{"hashtype":"coinoutputid","block":{"minerpayoutids":null,"transactions":null,"rawblock":{"parentid":"0000000000000000000000000000000000000000000000000000000000000000","timestamp":0,"pobsindexes":{"BlockHeight":0,"TransactionIndex":0,"OutputIndex":0},"minerpayouts":null,"transactions":null},"blockid":"0000000000000000000000000000000000000000000000000000000000000000","difficulty":"0","estimatedactivebs":"0","height":0,"maturitytimestamp":0,"target":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"totalcoins":"0","arbitrarydatatotalsize":0,"minerpayoutcount":0,"transactioncount":0,"coininputcount":0,"coinoutputcount":0,"blockstakeinputcount":0,"blockstakeoutputcount":0,"minerfeecount":0,"arbitrarydatacount":0},"blocks":null,"transaction":{"id":"0000000000000000000000000000000000000000000000000000000000000000","height":0,"parent":"0000000000000000000000000000000000000000000000000000000000000000","rawtransaction":{"version":0,"data":{"coininputs":[],"minerfees":null}},"coininputoutputs":null,"coinoutputids":null,"coinoutputunlockhashes":null,"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},"transactions":[{"id":"fd583a124677a3ea7ed7981d008ca79bd9f93cedbee97af2bcfd28b3f31093cc","height":17383,"parent":"d329ebc493b75521db55b6595a7bfcbe5c1f94eb0ab1f7646bf39a42a8f7dddf","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"8c8dbd70c6eb2d5d181aa5ae430f2cc86e038b92e45dd6f6d5a28400efad4511","fulfillment":{"type":1,"data":{"publickey":"ed25519:cf87843f9c9014700eaa2dc28a80e4a54587d8cca0baa717805ce117cecd9bb4","signature":"b9ce44b1e0f9e3fae9f21111ddc08333f6ba32675fc971893f6ab7ca3e5ab664883794fd3a35aef59ba54242d9be92fbcf65cefb5eede3709dd57226203b6601"}}}],"coinoutputs":[{"value":"50000000000","condition":{"type":2,"data":{"sender":"01b88206a3300dea3dd5f6cd73568ac5797b078910c78cbce6a71fcd0837a3ea5a4f2ed9fc70a1","receiver":"01b73c4e869b6167abe6180ebe7a907f56e0357b4a2f65eb53d22baad84650eb62fce66ba036d0","hashedsecret":"e24b6b609b351a958982ba91de7624d3503f428620f5586fbea1f71807b545c1","timelock":1549878527}}},{"value":"99994136000000000","condition":{"type":1,"data":{"unlockhash":"017cb06fa6f44828617b92603e95171044d9dc7c4966ffa0d8f6f97171558735974e7ecc623ff7"}}}],"minerfees":["1000000000"]}},"coininputoutputs":[{"value":"99994187000000000","condition":{"type":1,"data":{"unlockhash":"0183841ae8952a2ba72db0d6fce6208df70f2a936ee589ff852e06b20af48b40489572b1a69b2a"}},"unlockhash":"0183841ae8952a2ba72db0d6fce6208df70f2a936ee589ff852e06b20af48b40489572b1a69b2a"}],"coinoutputids":["dd1babcbab492c742983b887a7408742ad0054ec8586541dd6ee6202877cb486","75bbe54aca26d5a5afbc442c0e033a3ad18efa1e130f0776a9e4b68cdbe24fb7"],"coinoutputunlockhashes":["02f6d25603d232512ade46cdec3160301d8bd4880f2d4e8e20f54aff24f94dac5792ab1b325c3d","017cb06fa6f44828617b92603e95171044d9dc7c4966ffa0d8f6f97171558735974e7ecc623ff7"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false}],"multisigaddresses":null,"unconfirmed":false}')
    # override internal functionality, as to use our stub client
    c.explorer_get = explorer_client.explorer_get
    c.explorer_post = explorer_client.explorer_post

    # a wallet is required to redeem a contract
    w = tfchain.TFChainWallet.TFChainWallet(client=c, seed='remain solar kangaroo welcome clean object friend later bounce strong ship lift hamster afraid you super dolphin warm emotion curve smooth kiss stem diet')
    
    # balance should be 0 at this point
    assert w.balance.available == '0 TFT'

    # if the output identifier is wrong, the redemption will fail
    with pytest.raises(tfchain.errors.AtomicSwapContractNotFound):
        w.atomicswap.redeem('dd1babcbab492c742983b887a7408742ad0054ec8586541dd6ee6202877cb483', secret='f68d8b238c193bc6765b8e355c53e4f574a2c9da458e55d4402edca621e53756')

    # if the secret is wrong, the redemption will fail as well
    with pytest.raises(tfchain.errors.AtomicSwapInvalidSecret):
        w.atomicswap.redeem('dd1babcbab492c742983b887a7408742ad0054ec8586541dd6ee6202877cb486', secret='f68d8b238c193bc6765b8e355c53e4f574a2c9da458e55d4402edca621e53754')

    # if not authorized, redemption will also fail
    fw = tfchain.TFChainWallet.TFChainWallet(client=c)
    with pytest.raises(tfchain.errors.AtomicSwapForbidden):
        fw.atomicswap.redeem('dd1babcbab492c742983b887a7408742ad0054ec8586541dd6ee6202877cb486', secret='f68d8b238c193bc6765b8e355c53e4f574a2c9da458e55d4402edca621e53756')

    # once you know the secret, and you are authorized to receive the contract,
    # you can redeem the atomic swap contract as follows:
    w.atomicswap.redeem('dd1babcbab492c742983b887a7408742ad0054ec8586541dd6ee6202877cb486', secret='f68d8b238c193bc6765b8e355c53e4f574a2c9da458e55d4402edca621e53756')

    # once it becomes registered on the chain
    explorer_client.hash_add('01b73c4e869b6167abe6180ebe7a907f56e0357b4a2f65eb53d22baad84650eb62fce66ba036d0', '{"hashtype":"unlockhash","block":{"minerpayoutids":null,"transactions":null,"rawblock":{"parentid":"0000000000000000000000000000000000000000000000000000000000000000","timestamp":0,"pobsindexes":{"BlockHeight":0,"TransactionIndex":0,"OutputIndex":0},"minerpayouts":null,"transactions":null},"blockid":"0000000000000000000000000000000000000000000000000000000000000000","difficulty":"0","estimatedactivebs":"0","height":0,"maturitytimestamp":0,"target":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"totalcoins":"0","arbitrarydatatotalsize":0,"minerpayoutcount":0,"transactioncount":0,"coininputcount":0,"coinoutputcount":0,"blockstakeinputcount":0,"blockstakeoutputcount":0,"minerfeecount":0,"arbitrarydatacount":0},"blocks":null,"transaction":{"id":"0000000000000000000000000000000000000000000000000000000000000000","height":0,"parent":"0000000000000000000000000000000000000000000000000000000000000000","rawtransaction":{"version":0,"data":{"coininputs":[],"minerfees":null}},"coininputoutputs":null,"coinoutputids":null,"coinoutputunlockhashes":null,"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},"transactions":[{"id":"4a7ac7930379675c82d0462a86e6d6f4018bdb2bdabaf49f4c177b8de19b4e7c","height":16930,"parent":"c25f345403080b8372a38f66608aa5a2287bdc61b82efe5ee6503ce85e8bcd35","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"753aaeaa0c9e6c9f1f8da1974c83d8ca067ad536f464a2e2fc038bbd0404d084","fulfillment":{"type":1,"data":{"publickey":"ed25519:e4f55bc46b5feb37c03a0faa2d624a9ee1d0deb5059aaa9625d8b4f60f29bcab","signature":"b5081e41797f53233c727c344698400a73f2cdd364e241df915df413d3eeafb425ce9b51de3731bcbf830c399a706f4d24ae7066f947a4a36ae1b25415bcde00"}}}],"coinoutputs":[{"value":"50000000000","condition":{"type":2,"data":{"sender":"01b73c4e869b6167abe6180ebe7a907f56e0357b4a2f65eb53d22baad84650eb62fce66ba036d0","receiver":"01746b199781ea316a44183726f81e0734d93e7cefc18e9a913989821100aafa33e6eb7343fa8c","hashedsecret":"4163d4b31a1708cd3bb95a0a8117417bdde69fd1132909f92a8ec1e3fe2ccdba","timelock":1549736249}}}],"minerfees":["1000000000"]}},"coininputoutputs":[{"value":"51000000000","condition":{"type":1,"data":{"unlockhash":"01b73c4e869b6167abe6180ebe7a907f56e0357b4a2f65eb53d22baad84650eb62fce66ba036d0"}},"unlockhash":"01b73c4e869b6167abe6180ebe7a907f56e0357b4a2f65eb53d22baad84650eb62fce66ba036d0"}],"coinoutputids":["023b1c17a01945573933e62ca7a1297057681622aaea52c4c4e198077a263890"],"coinoutputunlockhashes":["02fb27c67c373c2f30611e0b98bf92ed6e6eb0a69b471457b282903945180cd5c5b8068731f767"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"b147985d381bc626ef79219ca988b5b1e2d328ade10cd7f3d48b96ca67928155","height":17698,"parent":"e8656ff72f9288c9ece3f85e489389f3c77e84052db13702b03dcff266a4d844","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"dd1babcbab492c742983b887a7408742ad0054ec8586541dd6ee6202877cb486","fulfillment":{"type":2,"data":{"publickey":"ed25519:e4f55bc46b5feb37c03a0faa2d624a9ee1d0deb5059aaa9625d8b4f60f29bcab","signature":"4a7a15125f4e8819b4cf57dfe5f0389f45b0779b2a4bf27d885b4de8659ad363eb5be8c38ec88b33fc6fe1d18c55a9c0220f21977d36d1c8f63d582c8c126b0d","secret":"f68d8b238c193bc6765b8e355c53e4f574a2c9da458e55d4402edca621e53756"}}}],"coinoutputs":[{"value":"49000000000","condition":{"type":1,"data":{"unlockhash":"01b73c4e869b6167abe6180ebe7a907f56e0357b4a2f65eb53d22baad84650eb62fce66ba036d0"}}}],"minerfees":["1000000000"]}},"coininputoutputs":[{"value":"50000000000","condition":{"type":2,"data":{"sender":"01b88206a3300dea3dd5f6cd73568ac5797b078910c78cbce6a71fcd0837a3ea5a4f2ed9fc70a1","receiver":"01b73c4e869b6167abe6180ebe7a907f56e0357b4a2f65eb53d22baad84650eb62fce66ba036d0","hashedsecret":"e24b6b609b351a958982ba91de7624d3503f428620f5586fbea1f71807b545c1","timelock":1549878527}},"unlockhash":"02f6d25603d232512ade46cdec3160301d8bd4880f2d4e8e20f54aff24f94dac5792ab1b325c3d"}],"coinoutputids":["b0e64c6e9d0d6d515856e15fcdfd869721f5b14ffc7599204f1e6ec174fb3631"],"coinoutputunlockhashes":["01b73c4e869b6167abe6180ebe7a907f56e0357b4a2f65eb53d22baad84650eb62fce66ba036d0"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"bca044302e018e67600bd0bd3223ae8dbb702eb528e73d6cfa9d057d4f73b03a","height":16911,"parent":"b4882a0b8632396a9c5d83a5c8684ab76736f4bff6d971795ed7334fac8aa339","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"357451c3f3a15f6150aedede9d5228ec5dfc2d32c9b62c2a46128533a7845c72","fulfillment":{"type":1,"data":{"publickey":"ed25519:fdb2e1b898dda304f748c0ff812a24729b2aafd344512079ab778eb368b18645","signature":"bd9dd36e86c08a5990ad5282d1079705c3a4b1cf3896e96791aa7db97002d5eb002c50467f45bd3ac1086292932cd2ab53c91b2e8bb74b9d9c9c0d558082ef08"}}}],"coinoutputs":[{"value":"51000000000","condition":{"type":1,"data":{"unlockhash":"01b73c4e869b6167abe6180ebe7a907f56e0357b4a2f65eb53d22baad84650eb62fce66ba036d0"}}},{"value":"99994187000000000","condition":{"type":1,"data":{"unlockhash":"0183841ae8952a2ba72db0d6fce6208df70f2a936ee589ff852e06b20af48b40489572b1a69b2a"}}}],"minerfees":["1000000000"]}},"coininputoutputs":[{"value":"99994239000000000","condition":{"type":1,"data":{"unlockhash":"019bb005b78a47fd084f4f3a088d83da4fadfc8e494ce4dae0d6f70a048a0a745d88ace6ce6f1c"}},"unlockhash":"019bb005b78a47fd084f4f3a088d83da4fadfc8e494ce4dae0d6f70a048a0a745d88ace6ce6f1c"}],"coinoutputids":["753aaeaa0c9e6c9f1f8da1974c83d8ca067ad536f464a2e2fc038bbd0404d084","8c8dbd70c6eb2d5d181aa5ae430f2cc86e038b92e45dd6f6d5a28400efad4511"],"coinoutputunlockhashes":["01b73c4e869b6167abe6180ebe7a907f56e0357b4a2f65eb53d22baad84650eb62fce66ba036d0","0183841ae8952a2ba72db0d6fce6208df70f2a936ee589ff852e06b20af48b40489572b1a69b2a"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false}],"multisigaddresses":null,"unconfirmed":false}')
    explorer_client.hash_add('dd1babcbab492c742983b887a7408742ad0054ec8586541dd6ee6202877cb486', '{"hashtype":"coinoutputid","block":{"minerpayoutids":null,"transactions":null,"rawblock":{"parentid":"0000000000000000000000000000000000000000000000000000000000000000","timestamp":0,"pobsindexes":{"BlockHeight":0,"TransactionIndex":0,"OutputIndex":0},"minerpayouts":null,"transactions":null},"blockid":"0000000000000000000000000000000000000000000000000000000000000000","difficulty":"0","estimatedactivebs":"0","height":0,"maturitytimestamp":0,"target":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"totalcoins":"0","arbitrarydatatotalsize":0,"minerpayoutcount":0,"transactioncount":0,"coininputcount":0,"coinoutputcount":0,"blockstakeinputcount":0,"blockstakeoutputcount":0,"minerfeecount":0,"arbitrarydatacount":0},"blocks":null,"transaction":{"id":"0000000000000000000000000000000000000000000000000000000000000000","height":0,"parent":"0000000000000000000000000000000000000000000000000000000000000000","rawtransaction":{"version":0,"data":{"coininputs":[],"minerfees":null}},"coininputoutputs":null,"coinoutputids":null,"coinoutputunlockhashes":null,"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},"transactions":[{"id":"b147985d381bc626ef79219ca988b5b1e2d328ade10cd7f3d48b96ca67928155","height":17698,"parent":"e8656ff72f9288c9ece3f85e489389f3c77e84052db13702b03dcff266a4d844","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"dd1babcbab492c742983b887a7408742ad0054ec8586541dd6ee6202877cb486","fulfillment":{"type":2,"data":{"publickey":"ed25519:e4f55bc46b5feb37c03a0faa2d624a9ee1d0deb5059aaa9625d8b4f60f29bcab","signature":"4a7a15125f4e8819b4cf57dfe5f0389f45b0779b2a4bf27d885b4de8659ad363eb5be8c38ec88b33fc6fe1d18c55a9c0220f21977d36d1c8f63d582c8c126b0d","secret":"f68d8b238c193bc6765b8e355c53e4f574a2c9da458e55d4402edca621e53756"}}}],"coinoutputs":[{"value":"49000000000","condition":{"type":1,"data":{"unlockhash":"01b73c4e869b6167abe6180ebe7a907f56e0357b4a2f65eb53d22baad84650eb62fce66ba036d0"}}}],"minerfees":["1000000000"]}},"coininputoutputs":[{"value":"50000000000","condition":{"type":2,"data":{"sender":"01b88206a3300dea3dd5f6cd73568ac5797b078910c78cbce6a71fcd0837a3ea5a4f2ed9fc70a1","receiver":"01b73c4e869b6167abe6180ebe7a907f56e0357b4a2f65eb53d22baad84650eb62fce66ba036d0","hashedsecret":"e24b6b609b351a958982ba91de7624d3503f428620f5586fbea1f71807b545c1","timelock":1549878527}},"unlockhash":"02f6d25603d232512ade46cdec3160301d8bd4880f2d4e8e20f54aff24f94dac5792ab1b325c3d"}],"coinoutputids":["b0e64c6e9d0d6d515856e15fcdfd869721f5b14ffc7599204f1e6ec174fb3631"],"coinoutputunlockhashes":["01b73c4e869b6167abe6180ebe7a907f56e0357b4a2f65eb53d22baad84650eb62fce66ba036d0"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},{"id":"fd583a124677a3ea7ed7981d008ca79bd9f93cedbee97af2bcfd28b3f31093cc","height":17383,"parent":"d329ebc493b75521db55b6595a7bfcbe5c1f94eb0ab1f7646bf39a42a8f7dddf","rawtransaction":{"version":1,"data":{"coininputs":[{"parentid":"8c8dbd70c6eb2d5d181aa5ae430f2cc86e038b92e45dd6f6d5a28400efad4511","fulfillment":{"type":1,"data":{"publickey":"ed25519:cf87843f9c9014700eaa2dc28a80e4a54587d8cca0baa717805ce117cecd9bb4","signature":"b9ce44b1e0f9e3fae9f21111ddc08333f6ba32675fc971893f6ab7ca3e5ab664883794fd3a35aef59ba54242d9be92fbcf65cefb5eede3709dd57226203b6601"}}}],"coinoutputs":[{"value":"50000000000","condition":{"type":2,"data":{"sender":"01b88206a3300dea3dd5f6cd73568ac5797b078910c78cbce6a71fcd0837a3ea5a4f2ed9fc70a1","receiver":"01b73c4e869b6167abe6180ebe7a907f56e0357b4a2f65eb53d22baad84650eb62fce66ba036d0","hashedsecret":"e24b6b609b351a958982ba91de7624d3503f428620f5586fbea1f71807b545c1","timelock":1549878527}}},{"value":"99994136000000000","condition":{"type":1,"data":{"unlockhash":"017cb06fa6f44828617b92603e95171044d9dc7c4966ffa0d8f6f97171558735974e7ecc623ff7"}}}],"minerfees":["1000000000"]}},"coininputoutputs":[{"value":"99994187000000000","condition":{"type":1,"data":{"unlockhash":"0183841ae8952a2ba72db0d6fce6208df70f2a936ee589ff852e06b20af48b40489572b1a69b2a"}},"unlockhash":"0183841ae8952a2ba72db0d6fce6208df70f2a936ee589ff852e06b20af48b40489572b1a69b2a"}],"coinoutputids":["dd1babcbab492c742983b887a7408742ad0054ec8586541dd6ee6202877cb486","75bbe54aca26d5a5afbc442c0e033a3ad18efa1e130f0776a9e4b68cdbe24fb7"],"coinoutputunlockhashes":["02f6d25603d232512ade46cdec3160301d8bd4880f2d4e8e20f54aff24f94dac5792ab1b325c3d","017cb06fa6f44828617b92603e95171044d9dc7c4966ffa0d8f6f97171558735974e7ecc623ff7"],"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false}],"multisigaddresses":null,"unconfirmed":false}', force=True)
    explorer_client.chain_info = '{"blockid":"5de1f56636bde6d724c717a3eda954117ad647930a55125a210cd7da8986c365","difficulty":"33956","estimatedactivebs":"2680","height":17712,"maturitytimestamp":1549709563,"target":[0,1,238,19,74,206,147,40,0,177,159,111,31,15,189,145,26,160,171,28,217,59,25,165,140,61,86,216,188,238,159,35],"totalcoins":"0","arbitrarydatatotalsize":4351,"minerpayoutcount":17799,"transactioncount":18340,"coininputcount":638,"coinoutputcount":1232,"blockstakeinputcount":17712,"blockstakeoutputcount":17713,"minerfeecount":627,"arbitrarydatacount":573}'
    explorer_client.hash_add('5de1f56636bde6d724c717a3eda954117ad647930a55125a210cd7da8986c365', '{"hashtype":"blockid","block":{"minerpayoutids":["f66f6bde0f026d68f7ce64cbb0ce0169a48e7abd636536ade754d152dbe64e5c"],"transactions":[{"id":"c7b2f558cd8e6ac0d94e2f0c0b025682d142b78457acfed3b89dca493451f15a","height":17712,"parent":"5de1f56636bde6d724c717a3eda954117ad647930a55125a210cd7da8986c365","rawtransaction":{"version":1,"data":{"coininputs":null,"blockstakeinputs":[{"parentid":"2bbf77cb889cafc8df69293c016c03c0b10420e6ed1d83bbe6e79529ed49ba00","fulfillment":{"type":1,"data":{"publickey":"ed25519:d285f92d6d449d9abb27f4c6cf82713cec0696d62b8c123f1627e054dc6d7780","signature":"b3c41e1964f055c027437576943bce92808ff24411a0bf19a56e81b74e6f5fd5d027f8aabe836a56cc2a81837fd73cfc09473a97ac0746b319f4a906f7bc7c02"}}}],"blockstakeoutputs":[{"value":"3000","condition":{"type":1,"data":{"unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}}}],"minerfees":null}},"coininputoutputs":null,"coinoutputids":null,"coinoutputunlockhashes":null,"blockstakeinputoutputs":[{"value":"3000","condition":{"type":1,"data":{"unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}},"unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}],"blockstakeoutputids":["9830f9a00955c797289a9ab17211a05f3e393c2d8728e7fcc6c25b9fe7afce74"],"blockstakeunlockhashes":["015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"],"unconfirmed":false}],"rawblock":{"parentid":"a32ed0392681c2faccffb818dd14aa92c405315f9b538500d9d4d840834d3438","timestamp":1549709657,"pobsindexes":{"BlockHeight":17711,"TransactionIndex":0,"OutputIndex":0},"minerpayouts":[{"value":"10000000000","unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}],"transactions":[{"version":1,"data":{"coininputs":null,"blockstakeinputs":[{"parentid":"2bbf77cb889cafc8df69293c016c03c0b10420e6ed1d83bbe6e79529ed49ba00","fulfillment":{"type":1,"data":{"publickey":"ed25519:d285f92d6d449d9abb27f4c6cf82713cec0696d62b8c123f1627e054dc6d7780","signature":"b3c41e1964f055c027437576943bce92808ff24411a0bf19a56e81b74e6f5fd5d027f8aabe836a56cc2a81837fd73cfc09473a97ac0746b319f4a906f7bc7c02"}}}],"blockstakeoutputs":[{"value":"3000","condition":{"type":1,"data":{"unlockhash":"015a080a9259b9d4aaa550e2156f49b1a79a64c7ea463d810d4493e8242e6791584fbdac553e6f"}}}],"minerfees":null}}]},"blockid":"5de1f56636bde6d724c717a3eda954117ad647930a55125a210cd7da8986c365","difficulty":"33956","estimatedactivebs":"2680","height":17712,"maturitytimestamp":1549709563,"target":[0,1,238,19,74,206,147,40,0,177,159,111,31,15,189,145,26,160,171,28,217,59,25,165,140,61,86,216,188,238,159,35],"totalcoins":"0","arbitrarydatatotalsize":4351,"minerpayoutcount":17799,"transactioncount":18340,"coininputcount":638,"coinoutputcount":1232,"blockstakeinputcount":17712,"blockstakeoutputcount":17713,"minerfeecount":627,"arbitrarydatacount":573},"blocks":null,"transaction":{"id":"0000000000000000000000000000000000000000000000000000000000000000","height":0,"parent":"0000000000000000000000000000000000000000000000000000000000000000","rawtransaction":{"version":0,"data":{"coininputs":[],"minerfees":null}},"coininputoutputs":null,"coinoutputids":null,"coinoutputunlockhashes":null,"blockstakeinputoutputs":null,"blockstakeoutputids":null,"blockstakeunlockhashes":null,"unconfirmed":false},"transactions":null,"multisigaddresses":null,"unconfirmed":false}')

    # and the contract can no longer be redeemed
    with pytest.raises(tfchain.errors.AtomicSwapContractSpent):
        w.atomicswap.redeem('dd1babcbab492c742983b887a7408742ad0054ec8586541dd6ee6202877cb486', secret='f68d8b238c193bc6765b8e355c53e4f574a2c9da458e55d4402edca621e53756')

    # should you verify it at this point, you'll get the same exception
    with pytest.raises(tfchain.errors.AtomicSwapContractSpent):
        w.atomicswap.verify('dd1babcbab492c742983b887a7408742ad0054ec8586541dd6ee6202877cb486')
