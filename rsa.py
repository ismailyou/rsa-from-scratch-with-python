import random


class Rsa:
    prime_list = []

    def __init__(self, start, end, file_name):
        self.prime_list = self.get_prime_number(start, end)
        self.p = self.get_p_or_q()
        self.q = self.get_p_or_q()

        self.file_name = file_name

    """ Generate public/private keys """

    def generate_keys(self):
        print("Generating key will take a moment ..")
        n = self.get_n()
        phi = self.get_phi()
        e = self.get_e(phi)
        d = self.euclide_etendu(phi, e)

        pub = "{0}, {1}".format(e, n)
        pri = "{0}, {1}".format(d, n)

        print("Public key : ", pub)
        print("Private key : ", pri)

        self.write_key(self.file_name + ".pub", pub)
        self.write_key(self.file_name + ".pri", pri)

    """ Encrypt function E(M) = M^e [n] """

    def encrypt(self, plain_text):
        print("Please wait a moment the process of encrypting may take a bit ..")
        public_key = self.read_key(self.file_name + ".pub")
        e, n = public_key.split(", ")
        cipher_text = pow(int(plain_text), int(e)) % int(n)

        print("The Message {0} is Encrypted with the public key ({1}, {2}) , cipher text is {3}".format(
            plain_text, e, n, cipher_text))

        return cipher_text

    """ Decrypt function D(C) = C^d [n] """

    def decrypt(self, cipher_text):
        print("Please wait a moment the process of decrypting may take a bit ..")
        private_key = self.read_key(self.file_name + ".pri")
        d, n = private_key.split(", ")
        plain_text = pow(int(cipher_text), int(d)) % int(n)

        print("The cipher text {0} is decripted, and the plain text is {1}".format(
            cipher_text, plain_text))

        return plain_text

    """ calculate the PGCD """

    def pgcd(self, a, b):
        if a < b:
            t = a
            a, b = b, t

        while b != 0:
            a, b = b, a % b
        return a

    """ Verify that a number is a prime or not """

    def is_prime_number(self, a):
        if a == 2:
            return True
        elif a < 2 or a % 2 == 0:
            return False
        for x in range(2, a):
            if a % x == 0:
                return False
        return True

    """ get all prime number between start and the end """

    def get_prime_number(self, start, end):
        prime_list = []
        for n in range(start, end):
            is_prime = self.is_prime_number(n)
            if is_prime:
                prime_list.append(n)

        return prime_list

    """ from the list of prime numbers we randomly return one """

    def get_p_or_q(self):
        return random.choice(self.prime_list)

    """ calculate the n = p * q """

    def get_n(self):
        return self.p * self.q

    """ calculate the phi = (p - 1)(q - 1) """

    def get_phi(self):
        return (self.p - 1) * (self.q - 1)

    """ get the all number that satisfy pgcd(n, phi) = 1
        and randomly choice one """

    def get_e(self, phi):
        all_numbers = []
        for i in range(2, phi):
            if self.pgcd(i, phi) == 1:
                all_numbers.append(i)
        return random.choice(all_numbers)

    """ Inverse modulo """

    def euclide_etendu(self, m, r):
        a, b, c, d = m, r, 1, 0
        while b != 1:
            temp_a, temp_b, temp_c, temp_d = a, b, c, d

            a = b
            b = temp_a % b
            c = (temp_d - temp_c * (temp_a // temp_b)) % m
            d = temp_c

        return abs(c)

    def read_key(self, file_name):
        print("reading key info from ", file_name)
        f_key = open(file_name, "r")
        key = f_key.read()
        f_key.close()
        return key

    def write_key(self, file_name, key):
        f_key = open(file_name, "w")
        f_key.write(key)
        f_key.close()
        print("keys are saved at ", file_name)
