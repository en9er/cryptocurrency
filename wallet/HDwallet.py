from hdwallet import HDWallet
from hdwallet.symbols import BTC
from hdwallet import utils
from hdwallet.utils import generate_entropy
from hdwallet.symbols import AMOG
from typing import Optional
import json


def create_wallet_from_path(path, symbol=AMOG):
    # Derivation from path
    wallet = HDWallet(symbol)
    return wallet.from_path(path)


def create_wallet_from_mnemonic(mnemonic, symbol=AMOG):
    if utils.is_mnemonic(mnemonic):
        wallet = HDWallet(symbol)
        wallet.from_mnemonic(mnemonic, language="english")
        return wallet
    else:
        raise Exception("Invalid mnemonic")


def create_wallet(symbol=AMOG):
    # Choose strength 128, 160, 192, 224 or 256
    STRENGTH: int = 128  # Default is 128
    # Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese or korean
    LANGUAGE: str = "english"  # Default is english
    # Generate new entropy hex string
    ENTROPY: str = generate_entropy(strength=STRENGTH)
    # Secret passphrase for mnemonic
    PASSPHRASE: Optional[str] = None  # "meherett"

    # Initialize Bitcoin mainnet HDWallet
    hdwallet: HDWallet = HDWallet(symbol)
    # Get Bitcoin HDWallet from entropy
    hdwallet.from_entropy(
        entropy=ENTROPY, language=LANGUAGE, passphrase=PASSPHRASE
    )
    return hdwallet


def print_information(wallet):
    if HDWallet == type(wallet):
        print(json.dumps(wallet.dumps(), indent=4, ensure_ascii=False))
    else:
        raise Exception("Invalid wallet")