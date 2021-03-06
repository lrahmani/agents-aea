<a name=".aea.crypto.ethereum"></a>
## aea.crypto.ethereum

Ethereum module wrapping the public and private key cryptography and ledger api.

<a name=".aea.crypto.ethereum.EthereumCrypto"></a>
### EthereumCrypto

```python
class EthereumCrypto(Crypto)
```

Class wrapping the Account Generation from Ethereum ledger.

<a name=".aea.crypto.ethereum.EthereumCrypto.__init__"></a>
#### `__`init`__`

```python
 | __init__(private_key_path: Optional[str] = None)
```

Instantiate an ethereum crypto object.

**Arguments**:

- `private_key_path`: the private key path of the agent

<a name=".aea.crypto.ethereum.EthereumCrypto.entity"></a>
#### entity

```python
 | @property
 | entity() -> Account
```

Get the entity.

<a name=".aea.crypto.ethereum.EthereumCrypto.public_key"></a>
#### public`_`key

```python
 | @property
 | public_key() -> str
```

Return a public key in hex format.

**Returns**:

a public key string in hex format

<a name=".aea.crypto.ethereum.EthereumCrypto.address"></a>
#### address

```python
 | @property
 | address() -> str
```

Return the address for the key pair.

**Returns**:

a display_address str

<a name=".aea.crypto.ethereum.EthereumCrypto.sign_message"></a>
#### sign`_`message

```python
 | sign_message(message: bytes, is_deprecated_mode: bool = False) -> str
```

Sign a message in bytes string form.

**Arguments**:

- `message`: the message to be signed
- `is_deprecated_mode`: if the deprecated signing is used

**Returns**:

signature of the message in string form

<a name=".aea.crypto.ethereum.EthereumCrypto.sign_transaction"></a>
#### sign`_`transaction

```python
 | sign_transaction(transaction: Any) -> Any
```

Sign a transaction in bytes string form.

**Arguments**:

- `transaction`: the transaction to be signed

**Returns**:

signed transaction

<a name=".aea.crypto.ethereum.EthereumCrypto.recover_message"></a>
#### recover`_`message

```python
 | recover_message(message: bytes, signature: bytes) -> Address
```

Recover the address from the hash.

**Arguments**:

- `message`: the message we expect
- `signature`: the transaction signature

**Returns**:

the recovered address

<a name=".aea.crypto.ethereum.EthereumCrypto.get_address_from_public_key"></a>
#### get`_`address`_`from`_`public`_`key

```python
 | @classmethod
 | get_address_from_public_key(cls, public_key: str) -> str
```

Get the address from the public key.

**Arguments**:

- `public_key`: the public key

**Returns**:

str

<a name=".aea.crypto.ethereum.EthereumCrypto.load"></a>
#### load

```python
 | @classmethod
 | load(cls, fp: BinaryIO)
```

Deserialize binary file `fp` (a `.read()`-supporting file-like object containing a private key).

**Arguments**:

- `fp`: the input file pointer. Must be set in binary mode (mode='rb')

**Returns**:

None

<a name=".aea.crypto.ethereum.EthereumCrypto.dump"></a>
#### dump

```python
 | dump(fp: BinaryIO) -> None
```

Serialize crypto object as binary stream to `fp` (a `.write()`-supporting file-like object).

**Arguments**:

- `fp`: the output file pointer. Must be set in binary mode (mode='wb')

**Returns**:

None

<a name=".aea.crypto.ethereum.EthereumApi"></a>
### EthereumApi

```python
class EthereumApi(LedgerApi)
```

Class to interact with the Ethereum Web3 APIs.

<a name=".aea.crypto.ethereum.EthereumApi.__init__"></a>
#### `__`init`__`

```python
 | __init__(address: str, gas_price: str = DEFAULT_GAS_PRICE)
```

Initialize the Ethereum ledger APIs.

**Arguments**:

- `address`: the endpoint for Web3 APIs.

<a name=".aea.crypto.ethereum.EthereumApi.api"></a>
#### api

```python
 | @property
 | api() -> Web3
```

Get the underlying API object.

<a name=".aea.crypto.ethereum.EthereumApi.get_balance"></a>
#### get`_`balance

```python
 | get_balance(address: AddressLike) -> int
```

Get the balance of a given account.

<a name=".aea.crypto.ethereum.EthereumApi.send_transaction"></a>
#### send`_`transaction

```python
 | send_transaction(crypto: Crypto, destination_address: AddressLike, amount: int, tx_fee: int, tx_nonce: str, is_waiting_for_confirmation: bool = True, chain_id: int = 1, **kwargs) -> Optional[str]
```

Submit a transaction to the ledger.

**Arguments**:

- `crypto`: the crypto object associated to the payer.
- `destination_address`: the destination address of the payee.
- `amount`: the amount of wealth to be transferred.
- `tx_fee`: the transaction fee.
- `tx_nonce`: verifies the authenticity of the tx
- `is_waiting_for_confirmation`: whether or not to wait for confirmation
- `chain_id`: the Chain ID of the Ethereum transaction. Default is 1 (i.e. mainnet).

**Returns**:

tx digest if successful, otherwise None

<a name=".aea.crypto.ethereum.EthereumApi.send_signed_transaction"></a>
#### send`_`signed`_`transaction

```python
 | send_signed_transaction(is_waiting_for_confirmation: bool, tx_signed: Any) -> str
```

Send a signed transaction and wait for confirmation.

**Arguments**:

- `tx_signed`: the signed transaction
- `is_waiting_for_confirmation`: whether or not to wait for confirmation

<a name=".aea.crypto.ethereum.EthereumApi.is_transaction_settled"></a>
#### is`_`transaction`_`settled

```python
 | is_transaction_settled(tx_digest: str) -> bool
```

Check whether a transaction is settled or not.

**Arguments**:

- `tx_digest`: the digest associated to the transaction.

**Returns**:

True if the transaction has been settled, False o/w.

<a name=".aea.crypto.ethereum.EthereumApi.get_transaction_status"></a>
#### get`_`transaction`_`status

```python
 | get_transaction_status(tx_digest: str) -> Any
```

Get the transaction status for a transaction digest.

**Arguments**:

- `tx_digest`: the digest associated to the transaction.

**Returns**:

the tx status, if present

<a name=".aea.crypto.ethereum.EthereumApi.generate_tx_nonce"></a>
#### generate`_`tx`_`nonce

```python
 | generate_tx_nonce(seller: Address, client: Address) -> str
```

Generate a unique hash to distinguish txs with the same terms.

**Arguments**:

- `seller`: the address of the seller.
- `client`: the address of the client.

**Returns**:

return the hash in hex.

<a name=".aea.crypto.ethereum.EthereumApi.validate_transaction"></a>
#### validate`_`transaction

```python
 | validate_transaction(tx_digest: str, seller: Address, client: Address, tx_nonce: str, amount: int) -> bool
```

Check whether a transaction is valid or not.

**Arguments**:

- `seller`: the address of the seller.
- `client`: the address of the client.
- `tx_nonce`: the transaction nonce.
- `amount`: the amount we expect to get from the transaction.
- `tx_digest`: the transaction digest.

**Returns**:

True if the random_message is equals to tx['input']

