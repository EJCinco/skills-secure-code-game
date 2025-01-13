# Welcome to Secure Code Game Season-1/Level-5!

# This is the last level of our first season, good luck!

import binascii
import secrets
import hashlib
import os
import bcrypt

class Random_generator:
    """Handles random token and salt generation."""

    def generate_token(self, length=8, alphabet=None):
        """
        Generates a secure random token using the secrets module.
        :param length: Length of the token
        :param alphabet: Optional set of characters to use
        :return: Randomly generated token
        """
        if alphabet is None:
            alphabet = (
                '0123456789'
                'abcdefghijklmnopqrstuvwxyz'
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            )
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    def generate_salt(self, rounds=12):
        """
        Generates a cryptographically secure salt using bcrypt's gensalt.
        :param rounds: The number of hashing rounds for the salt
        :return: A securely generated salt
        """
        return bcrypt.gensalt(rounds=rounds)

class SHA256_hasher:
    """Handles password hashing and verification using SHA256 and bcrypt."""

    def password_hash(self, password, salt):
        """
        Hashes the password using SHA256 and bcrypt.
        :param password: The plaintext password
        :param salt: The salt for bcrypt
        :return: The hashed password as a string
        """
        hashed_password = hashlib.sha256(password.encode()).digest()
        hashed_password_hex = binascii.hexlify(hashed_password)
        return bcrypt.hashpw(hashed_password_hex, salt).decode('ascii')

    def password_verification(self, password, password_hash):
        """
        Verifies if the provided password matches the hashed password.
        :param password: The plaintext password
        :param password_hash: The hashed password
        :return: True if the password matches, False otherwise
        """
        hashed_password = hashlib.sha256(password.encode()).digest()
        hashed_password_hex = binascii.hexlify(hashed_password)
        return bcrypt.checkpw(hashed_password_hex, password_hash.encode('ascii'))

class MD5_hasher:
    """Handles password hashing and verification using MD5."""

    def password_hash(self, password):
        """
        Hashes the password using the MD5 algorithm.
        :param password: The plaintext password
        :return: The MD5 hashed password as a hexadecimal string
        """
        return hashlib.md5(password.encode()).hexdigest()

    def password_verification(self, password, password_hash):
        """
        Verifies if the provided password matches the hashed password using MD5.
        :param password: The plaintext password
        :param password_hash: The hashed password
        :return: True if the password matches, False otherwise
        """
        return secrets.compare_digest(self.password_hash(password), password_hash)

PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')  # Use environment variable if available
PASSWORD_HASHER = 'SHA256_hasher'



# Contribute new levels to the game in 3 simple steps!
# Read our Contribution Guideline at github.com/skills/secure-code-game/blob/main/CONTRIBUTING.md