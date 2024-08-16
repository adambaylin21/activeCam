# -*- coding: utf-8 -*-

from colorama import Fore, Style

import requests, json, os

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign

# Khởi tạo FacebookAdsApi với access token của bạn
app_id = '4435617123161834'
app_secret = '89403561c48b2f55ea08bb837979d2ac'

# Lấy danh sách các campaign đang active
# account_id = 'act_621493336131659'
fields = [
    # Campaign.Field.id,
    Campaign.Field.name,
]

params = {
    'effective_status': ['ACTIVE'],
}

def logo():
    os.system('cls')
    logo = """

█▀▄▀█ █▀▀█ █░░█ ░░░ █▀▀▄   ▀█▀ █▀▀ █▀▀ █░░█
█░▀░█ █▄▄█ ▄▀▀▄ ▀▀▀ █░░█   ░█░ █▀▀ █░░ █▀▀█
▀░░░▀ ▀░░▀ ▀░░▀ ░░░ ▀▀▀    ░▀░ ▀▀▀ ▀▀▀ ▀░░▀
        
        Copyright By : Adam Baylin
    """
    print (Fore.GREEN + Style.BRIGHT + logo)


def process_menu():
    menu = """
    [-----------------------------]
        1. Export Campaign.
        2. Thoát Tool.
    [-----------------------------]
"""
    print (Fore.WHITE + Style.BRIGHT + menu)
    choice_user = input(Fore.WHITE + Style.BRIGHT + "- Nhập Lựa Chọn: ")

    if choice_user == '1':
        token = input(Fore.WHITE + Style.BRIGHT + "- Nhập Token: ")
        Fblogic(opt="init", tokenapp=token)
        data = Fblogic(opt="idactivate", listacc=account_id)
        write_list_to_file("List Campaign.txt", data)
        print("Done !")

    elif choice_user == '2':
        quit()
    else:
        process_menu()

def loadAccount(account_id):
    ad_account = AdAccount(account_id)
    campaigns = ad_account.get_campaigns(fields=fields, params=params)
    listid = []

    for campaign in campaigns:
        listid.append(campaign[Campaign.Field.name])
    return listid

def metricFb(idcam, time):
    campaign = Campaign(idcam)
    params = {
        'fields': ['campaign_name'],
        # date_preset
        'time_range' : {
            'since':time,
            'until':time
            }

    }

def Fblogic(**kwargs):
    opt = {}
    for key, value in kwargs.items():
        opt[key] = value
    mode = opt['opt']

    if mode == 'init':
        access_token = opt['tokenapp']
        FacebookAdsApi.init(access_token=access_token, app_id=app_id, app_secret=app_secret)

    if mode == 'idactivate':
        # params['time_range'] = {'since':opt['time'],'until':opt['time']}
        listcam = []

        for listid in opt['listacc']:
            for cam in loadAccount('act_'+listid):
                listcam.append(cam)

        return listcam

    if mode == 'loadcam':
        result = []
        for idcam in opt['LsCam']:
            result.append(metricFb(idcam, opt['time']))
            
        return result
    
def write_list_to_file(file_name, data_list):
    with open(file_name, 'w', encoding='utf-8') as file:
        for item in data_list:
            file.write(item + '\n')

if __name__ == '__main__':
    account_id = ['621493336131659','921868142122001','1149058086044743']
    logo()
    process_menu()