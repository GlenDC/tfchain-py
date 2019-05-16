from tfchain.types.PrimitiveTypes import BinaryData, Hash, Currency, Blockstake
from tfchain.types.ThreeBot import ThreeBotTypesFactory
from tfchain.types.CryptoTypes import PublicKey, PublicKeySpecifier
from tfchain.types import transactions as tftransactions
from tfchain.crypto import MerkleTree

def test_types():
    # currency values can be created from both
    # int and str values, but are never allowed to be negative
    assert str(Currency()) == '0'
    assert str(Currency(value=123)) == '123'
    assert str(Currency(value='1')) == '1'
    # in the string versions you can also add the TFT currency notation,
    # or use decimal notation to express the currency in the TFT Currency Unit,
    # rather than the primitive unit
    assert str(Currency(value='1 TFT')) == '1'
    assert str(Currency(value='0.123456789')) == '0.123456789'
    assert str(Currency(value='9.123456789')) == '9.123456789'
    assert str(Currency(value='1234.34')) == '1234.34'
    assert str(Currency(value='1.00000')) == '1'
    assert str(Currency(value='1.0 tft')) == '1'
    assert str(Currency(value=1)) == '1'
    assert str(Currency(value=12344)) == '12344'

    # hash values can be created directly from binary data,
    # or from a hex-encoded string, by default the nil hash will be created
    assert str(Hash()) == '0'*64
    assert Hash(
        b'12345678901234567890123456789001').value == b'12345678901234567890123456789001'

    # binary data is very similar to a hash,
    # except that it doesn't have a fixed length and it is binary serialized
    # as a slice, not an array
    assert str(BinaryData()) == ''
    assert str(BinaryData(b'1')) == '31'
    assert str(BinaryData(b'1', fixed_size=0)) == '31'
    assert str(BinaryData(b'1', fixed_size=1)) == '31'

    # raw data is pretty much binary data, except that it is
    # base64 encoded/decoded for str/json purposes
    assert str(BinaryData(
        b'data', strencoding='base64')) == 'ZGF0YQ=='

    # block stake values can be created from both
    # int and str values, but are never allowed to be negative
    assert str(Blockstake()) == '0'
    assert str(Blockstake(value=123)) == '123'
    assert str(Blockstake(value='1')) == '1'
