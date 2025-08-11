import json
import os

def load_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def load_configs():
    atm_config = load_config('settings/atm_ui.cfg')
    withdraw_config = load_config('settings/withdraw.config')
    deposit_config = load_config('settings/deposit.config')
    user_auth_config = load_config('settings/auth.config')
    account_config = load_config('settings/account.config')

    return {
        'atm_config': atm_config,
        'withdraw_config': withdraw_config,
        'deposit_config': deposit_config,
        'user_auth_config': user_auth_config,
        'account_config': account_config
    }