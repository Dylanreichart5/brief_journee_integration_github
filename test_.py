"""
Les fonctions à tester sont les méthodes 'encrypt' et 'decrypt'
des classes contenues dans les fichiers dont le nom se termine
par 'algo.py'. À noter que certaines classes n'ont pas de méthode
decrypt, ou uniquement une méthode vide.

Pour savoir quelles sont les entrées et/ou le format des clés attendus
par ces différentes fonctions de cryptage/décryptage, vous pouvez lancer 
l'application et lire les encadrés d'information à droite, et faire des 
recherches.

Pour lancer tous les tests contenus dans ce fichier, utilisez 
la commande pytest <nom de ce script>
"""


from crypto_app.aes_algo import AdvancedEncryptionStandard
from crypto_app.enigmam3_algo import EnigmaM3
from crypto_app.blowfish_algo import Blowfish
from crypto_app.caesarcipher_algo import CaesarCipher
from crypto_app.vigenerecipher_algo import VigenereCipher
from crypto_app.rsa_algo import RSAAlgo
from crypto_app.des_algo import DES

from crypto_app.des_algo import DES

def test_enigma():
    """
    Un exemple de fonction de test, ici avec le cryptage
    d'Enigma.
    """

    enigma = EnigmaM3()
    msg = "Message"
    key = [
        ('A', 'C', 'N'),
        (2, 4, 1),
        ('F', 'H', 'K'),
        [('A', 'K')]
    ]

    encrypted = enigma.encrypt(msg, key)
    assert encrypted == "FUTALDK"
    decrypted = enigma.decrypt(encrypted, key)
    assert decrypted == "MESSAGE"



#######################################################
# AJOUTEZ VOS TESTS À LA SUITE
#######################################################

def test_aes():
    """
    Un exemple de fonction de test, ici avec le cryptage
    AES.
    """

    aes = AdvancedEncryptionStandard()
    msg = "cleaes"
    key = "abcdefghijklmnopqrstuvwx"

    encrypted = aes.encrypt(msg, key)
    assert encrypted == "32f306250f5c"
    decrypted = aes.decrypt(encrypted, key)
    assert decrypted == msg


def test_blowfish():
    """
    Un exemple de fonction de test, ici avec le cryptage
    blowfish.
    """

    blfish = Blowfish()
    msg = "ceci est le test de blowfish"
    key = "cleblow"

    encrypted = blfish.encrypt(msg, key)
    decrypted = blfish.decrypt(encrypted, key)
    assert decrypted == msg



def test_caesar():
    """
    Un exemple de fonction de test, ici avec le cryptage
    blowfish.
    """

    caesar = CaesarCipher()
    msg = "ceci est le test de caesar"
    key = 3

    encrypted = caesar.encrypt(msg, key)
    decrypted = caesar.decrypt(encrypted, key)
    assert decrypted == msg

def test_vigenere():
    """
    Un exemple de fonction de test, ici avec le cryptage
    blowfish.
    """

    vigenere = VigenereCipher()
    msg = "ceci est le test de vigenere"
    key = "clevigenere"

    encrypted = vigenere.encrypt(msg, key)
    decrypted = vigenere.decrypt(encrypted, key)
    assert decrypted == msg



def test_des():
    des = DES()

    key = "mysecret"
    message = "This is a secret message"
    crypt = "fcedd1515146aab639575b874c72dc006b2142c540562601f5f26349eefb43d9"

    crypted = des.encrypt(message, key)
    assert crypted == "fcedd1515146aab639575b874c72dc006b2142c540562601f5f26349eefb43d9"
    decrypted = des.decrypt(crypt, key)
    assert decrypted == "This is a secret message"