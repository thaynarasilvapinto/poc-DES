# Estudo sobre DES

Foi criado 10 arquivos, cada arquivo contem um texto claro de 64 bits.

Cada arquivo foi submetido a criptografia no metodo de DES utlizando o openSSL, com a chave ```124abc34```. 

Comando usado para criptografar:
 
```openssl enc -des-ecb -K 124abc34 -in entrada -out entrada```

