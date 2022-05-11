# RSA_Cryptosystem

Ron Rivest, Adi Shamir and Leonard Adleman in the year 1977 presented an algorithm that would ensure secure data transmission. 
They named it as the RSA algorithm, it is a public key cryptosystem. It uses two large prime numbers to encrypt a message and with the help of the same two number it decrypts
the message. 
This whole situation is possible because of one big practical difficulty that we face, the factorization of product of two large prime number. 
If someone figures out, or factors the product of the prime number then the RSA will break down. 
So, how this work is in the following way: the sender and reciever both have a public and a private key. 
The public key is given to everyone publicly, but the private key is just known to these two. 
And the encoded message will only get revealed by the private key, they both have to be inverse functions.

                                         Cipher = PA(M) M is the message and PA is the public key
                                         M = SA(Cipher) SA is the private key and M is the message
                                         
This idea of encryption and decryption involves many other basic concepts that is covered in the above attached report.
