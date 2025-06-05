Outer rim: `43DC1162DC117D0008721852FB1E3C2AB85FAF0AF930C5B6C1D24FAEDFABB776`
Inner: `00000000000` `0000000133E` | `54DC88F6C2` `D864376430D` | `376DADECB0A` `03EDF99AB7`

The inner was the block hash:
https://bitcoinwallet.com/block/000000000000000000133e54dc8bf6c2d864376430d376dadecb0a03edf99ab7

What is the outer?
A transaction?

Yep, there is indeed a transaction.
https://bitcoinwallet.com/tx/43dc1162dc117d0008721852fb1e3c2ab85faf0af930c5b6c1d24faedfabb776

```
block 	691,382
block hash 	000000000000000000133e54dc8bf6c2d864376430d376dadecb0a03edf99ab7
block time 	2021-07-17 04:56:29 (3 years ago) 
```

Download Transaction Inputs:
```json
[
  {
    "block_hash": "000000000000000000133e54dc8bf6c2d864376430d376dadecb0a03edf99ab7",
    "tx_hash": "43dc1162dc117d0008721852fb1e3c2ab85faf0af930c5b6c1d24faedfabb776",
    "tx_input_hash": "980982dc066356c198e18ec9fa69733c192c323e7c5c2d3fd8631b04686d05a6",
    "tx_input_hash_out_position": "1",
    "address_hash": "bc1qdneuefwdff45ej567nfrgag6nlxnuzalj5yx7s",
    "tx_input_script_sig_asm": "",
    "tx_input_script_sig_hex": "",
    "tx_input_coinbase": "",
    "block_hash_output": "0000000000000000001206633be69205313f8f12971653880f79b70986e745bf",
    "tx_hash_output": "980982dc066356c198e18ec9fa69733c192c323e7c5c2d3fd8631b04686d05a6",
    "tx_output_value": "0.01207726",
    "tx_output_position": "1",
    "tx_output_script_pub_key_asm": "0 6cf3cca5cd4a6b4cca9af4d234751a9fcd3e0bbf",
    "tx_output_script_pub_key_hex": "00146cf3cca5cd4a6b4cca9af4d234751a9fcd3e0bbf",
    "tx_output_script_pub_key_req_sig": "1",
    "tx_output_script_pub_key_type": "witness_v0_keyhash"
  }
]
```

Download Transaction:
```json
{
  "header": [
    "address",
    "deposit",
    "payment",
    "position",
    "input hash",
    "action"
  ],
  "footer": null,
  "body": [
    [
      "bc1qmfl9y74npu7pu8jluwyz52xzr0csg5c4hyyx9m",
      "",
      "0.01207572",
      "1",
      "",
      ""
    ],
    [
      "unknown",
      "",
      "0.00000000",
      "0",
      "",
      ""
    ],
    [
      "bc1qdneuefwdff45ej567nfrgag6nlxnuzalj5yx7s",
      "0.01207726",
      "",
      "1",
      "980982dc066356c198e18ec9fa69733c192c323e7c5c2d3fd8631b04686d05a6",
      ""
    ]
  ]
}
```

Download Transaction Outputs:
```json
[
  {
    "block_hash": "000000000000000000133e54dc8bf6c2d864376430d376dadecb0a03edf99ab7",
    "tx_hash": "43dc1162dc117d0008721852fb1e3c2ab85faf0af930c5b6c1d24faedfabb776",
    "address_hash": "bc1qmfl9y74npu7pu8jluwyz52xzr0csg5c4hyyx9m",
    "tx_output_value": "0.01207572",
    "tx_output_position": "1",
    "tx_output_script_pub_key_asm": "0 da7e527ab30f3c1e1e5fe3882a28c21bf1045315",
    "tx_output_script_pub_key_hex": "0014da7e527ab30f3c1e1e5fe3882a28c21bf1045315",
    "tx_output_script_pub_key_req_sig": "1",
    "tx_output_script_pub_key_type": "witness_v0_keyhash",
    "stat_tx_output_hash": "43dc1162dc117d0008721852fb1e3c2ab85faf0af930c5b6c1d24faedfabb776"
  },
  {
    "block_hash": "000000000000000000133e54dc8bf6c2d864376430d376dadecb0a03edf99ab7",
    "tx_hash": "43dc1162dc117d0008721852fb1e3c2ab85faf0af930c5b6c1d24faedfabb776",
    "address_hash": "",
    "tx_output_value": "0.00000000",
    "tx_output_position": "0",
    "tx_output_script_pub_key_asm": "OP_RETURN 68747470733a2f2f746162636f6e662e636f6d2f73636176656e67657268756e74",
    "tx_output_script_pub_key_hex": "6a2168747470733a2f2f746162636f6e662e636f6d2f73636176656e67657268756e74",
    "tx_output_script_pub_key_req_sig": "",
    "tx_output_script_pub_key_type": "nulldata",
    "stat_tx_output_hash": null
  }
]
```
