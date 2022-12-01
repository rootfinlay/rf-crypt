# rf-hash
 rf hash - a simple but effective hashing algorithm using maths. 

 rfhash uses a mix of maths and xor to calculate a hash.

 rfhash comes in 256-2048bit hashes.

 # Examples
 ```console
# 256bit

$ python POC256bit.py 
Input string to hash:
> a
Hash:  a0a101a0cba622f3d18b9d0ae0436507d3a8dbccec9c6d34084630bb9fde785d
```

```console
# 512bit

$ python POC512bit.py
Input string to hash:
> a
Hash:  996e45f69e6765e26c107581865fcbbc5163579ba8cfb0de13658de8780d4747dace835f9efb73bb76c123b6bbb8594d2ac9eb8c126d46983aebefeb84c54703
```

```console
# 1024bit

$ python POC1024bit.py
Input string to hash:
> a
Hash:  8bfcd6bd06bf999bab166e2e4ecd0c49e1cae8dbf829cd7146708c748d17695df46d746ff8e0034c0af62ce6d85e461e45167f417cac45a75b7c564c5977e380d4fe7c10b95d3c0673188e4af7c3a5d4e165bdc531009f8b2b34c7409307cbe3b2f510874d2daf69e148cd6ca3072d3b92a9d91f7de7edeb86f3ada320d57838
```

```console
# 2048bit

$ python POC2048bit.py
Input string to hash:
> a
Hash:  e910440ba94e8b67a1bc0b000fc3712fac584e23bc38f0b50d4dc827e2575a9134383ba60cfa6664b409ff3eef4bc1fd4c7a7e40557ef860aa808ebaee987307a3d5d029b1b48e8cfae69989b2d0bc03c04336444ce084ee062953e4d1a9d20fa22cc61fa9472babf2eb937c8c6c745cef2988e30f1433b7cfc3ff5b5e26ea344cc637e1ef42c50d4d65273b6589d8610954d1beda3b1148b27eadae7c409e1b38dfe76af9ad36224ec3579d64f0a1bc0a889519924e773c8359106fff6daf48bd9b6231267449e4fd85df9687a115868120db6191f161989bf8fdedd60b4280884b67b2ac4bb3e6aec447253c41ff804424188a933c5e073ee1f36b6e79d4d8
```