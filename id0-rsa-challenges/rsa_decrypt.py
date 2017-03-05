#!/usr/bin/env python
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from base64 import b64decode
import gnupg

def hash_tests(input):
    temp = hashlib.sha256(input).hexdigest()
    temp = hashlib.md5(temp).hexdigest()
    print temp

def rsa_prog_decrypt():
    (e, N) = (0x3, 0x64ac4671cb4401e906cd273a2ecbc679f55b879f0ecb25eefcb377ac724ee3b1)
    d = 0x431d844bdcd801460488c4d17487d9a5ccc95698301d6ab2e218e4b575d52ea3
    c = 0x599f55a1b0520a19233c169b8c339f10695f9e61c92bd8fd3c17c8bba0d5677e
    m = pow(c,d,N)
    print hex(m)[2:].rstrip('L')

def rsa_decrypt():
    rsa_key = rsa_key = RSA.importKey(open('private.txt', "rb").read())
    verifier = PKCS1_v1_5.new(rsa_key)
    phn = rsa_key.decrypt(0x6794893f3c47247262e95fbed846e1a623fc67b1dd96e13c7f9fc3b880642e42)
    print hex(phn)[2:].rstrip('L')

def prog_pgp():
    eng_words = "/usr/share/dict/words"
    message = """-----BEGIN PGP MESSAGE-----
    Version: GnuPG v1
    jA0ECQMC8YL5GvIZ2m5g0ksB9aj386dbfatZ28jsaLEKtUcRLVjjHHIBmHvCIrxf
    RIeH7NLMcfQ+3Z+/ktIu3Drocg9zoiP1eaJ6aUUpa6fLy0OPjIIpG9tM/Mo=
    =S+SO
    -----END PGP MESSAGE-----"""
    gpg = gnupg.GPG(homedir='/usr/local/lib/python2.7/site-packages')
    gpg.encoding = 'utf-8'
    for line in (open(eng_words, 'r').readlines()):
        data = gpg.decrypt(message,passphrase=line.strip())
        if data.data != '':
            f_message, f_password = data.data, password # passionately apathetic seamanship, 74.7912127044% through the list
            break
    return f_message, f_password

#hash_tests("id0-rsa.pub")
#rsa_prog_decrypt()
#rsa_decrypt()
#prog_pgp()
