# rf-hash
 rf hash - a simple but effective hashing algorithm using maths. 

 rfhash uses a mix of maths and xor to calculate a hash.

 rfhash comes in 256-2048bit hashes.

WARNING: rf-hash is still being updated and tested, it is NOT ready for production..

 # Examples
 ```console
# 256bit

$ python POC256bit.py 
Input string to hash:
> a
Hash:  974960e0f364b75c6a360348355e2230e8d3151b2e8d52fdfcae881de24468bc
```

```console
# 512bit

$ python POC512bit.py
Input string to hash:
> a
Hash:  d09286f624e9d2d033be6a51f315e538364afbcce096f69b25cf26cf9efa3b1809a2d0ce40e14c5bbaf7fffceccf975120c9112c152f6690923fef5f0d0850fe
```

```console
# 1024bit

$ python POC1024bit.py
Input string to hash:
> a
Hash:  c6375b1c8bd8c2598339436c5372c06e1ae5149d3af5106935498a41a300f519c4740979a1086784328ab6efd8f62186a4e3e51cb05c0e8150f724f6c062a605e460c6573d5b0185519510b3eb462013e4614826d41c980b8b199d21ebd9caf6e11dafa2dae472fffb7069651199868d9b5931c19118242f8a6407b02b8da53a
```

```console
# 2048bit

$ python POC2048bit.py
Input string to hash:
> a
Hash:  
b30563948b2dfb29a042ab8c212822ecfad9fe824f0a29b6377da539159b81887c66f9482d352de29c3964bb59971e9fa0ebf7a086f44467287167b0b9df21ab42331e0e37c6eac04b8e729e1e89d82a4696bfa9df422a646213044736351a4ad8726e109c107daf0cd09b72724c055af4fea980513ee6e6ad3e6b9a111f204af966c06cc1cc2e6b7070bf29459a66cfcd2bf8b8d229a30411835e5153be3824e42a7d79195003f90d2e1fc87e9623b8d6a41065736a5e1c87e78141c397915cfcc909354a5e296713d32b3771b19d79d63ec303260be65e26a0d9e68e9401d570e976aedf1ff8d8646150796113e54af931bad0e1839e981298a423c0109b48
```