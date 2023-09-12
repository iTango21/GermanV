import requests
from bs4 import BeautifulSoup
import re
import json
import os
import xml.etree.ElementTree as ET


download_zoom_images = True     # True or False
download_data_image = True      # True or False

link_dict = {'data': [], 'zoom': []}


def download_img(img_url, dir_name, zoom_):
    file_name = os.path.basename(img_url)

    if zoom_:
        dir2_path = os.path.join(dir_name, "_zoom_")
        if not os.path.exists(dir2_path):
            os.makedirs(dir2_path)

        file_path = os.path.join(dir2_path, file_name)
        link_dict['zoom'].append(img_url)
    else:
        file_path = os.path.join(dir_name, file_name)
        link_dict['data'].append(img_url)

    if os.path.isfile(file_path):
        print(f"\tImage {file_name} already exists in directory {dir_name}")
    else:
        resp = requests.get(
            f'{img_url}',
            cookies=cookies,
            headers=headers,
        )

        if resp.status_code == 200:

            with open(file_path, "wb") as image_file:
                image_file.write(resp.content)
                print(f"\tImage {file_name} saved!")
        else:
            print(f"\n\tFailed to download image {file_name}. Error status code: {response.status_code}\n")

#
#   Part 1. Collection of links.. ======================================================================================
#
# url_ = 'https://www.chrono24.com/tagheuer/carrera-calibre-16--mod1020.htm'


url_ = input('Enter URL: ')

arr_ = []

cookies = {
    'chronosessid': '59112bbd-82c2-422c-8618-4c4a928be465',
    'timezone': 'Europe/Kiev',
    '__ssid': '5b6ac70e100f9753032a5253253e00b',
    'c24-consent': 'AAAAH8/vwf4=',
    'FPID': 'FPID2.2.ewR6ig5bjRErJUoUmfBskHaLO%2BV6wFAeMPwxuVCHDKg%3D.1694189024',
    '_gcl_au': '1.1.6707372.1694189026',
    '_gid': 'GA1.2.529648636.1694189026',
    '_pin_unauth': 'dWlkPVpHVmtObUZoTURVdE9UWmxOaTAwTkRFeExUa3dOMlF0T1RjNU4ySXdNbVZqWm1RMA',
    '_hjSessionUser_72519': 'eyJpZCI6IjU5ZTQ4N2FlLWViMTItNTZmMy1hMGVjLThjYzVjZDMwY2MxMSIsImNyZWF0ZWQiOjE2OTQxODkwMjU3MjcsImV4aXN0aW5nIjp0cnVlfQ==',
    'pu': 'true',
    'ln_or': 'eyI0NjQ4OCI6ImQifQ%3D%3D',
    'filter-combinations': '2:Man|Mod,0:',
    'userHistory': '29158964|1694371157854|11+24443649|1694370593442|1+29940559|1694370584302|1+28827802|1694368707869|1+22967785|1694368607501|3+29264730|1694368145529|15',
    'search-session': '|6a179a8c_AQ0Yht|0|29158964.29940559.30210271.24908804.27818548.29746351.27561386.30126971.30062052.25777492.27585922.29333387.30473070.22015242.30145512.27561436.24056926.30401334.28449728.30003965.24476162.28565466.28951817.29632645.27891713.25554829.28561621.30383113.28937335.28886644.29727383.24975400.29261498.28226551.27404613.30398070.28909285.28644016.24443649.30448476.29986850.30292707.29727601.8665661.25777493.30007212.29228144.20500268.29773938.25911730.30143600.30228880.24924969.25592417.22942059.28592010.30184127.29402616.30324033.27842937.30000166',
    'csrf-token': '1694444982.CGjT4UDmOYsNaaMI5T0HXqY9TFanfhT_ljtbeyBlmFc.AXG1VdjbkDAJA_goE5-Sb3V3CRmE',
    'last-search-result-ids': '29158964.29940559.30210271.24908804.27818548.29746351.27561386.30126971.30062052.25777492.27585922.29333387.30473070.22015242.30145512.27561436.24056926.30401334.28449728.30003965.24476162.28565466.28951817.29632645.27891713.25554829.28561621.30383113.28937335.28886644.29727383.24975400.29261498.28226551.27404613.30398070.28909285.28644016.24443649.30448476.29986850.30292707.29727601.8665661.25777493.30007212.29228144.20500268.29773938.25911730.30143600.30228880.24924969.25592417.22942059.28592010.30184127.29402616.30324033.27842937.30000166',
    'cfctGroup': 'AAA02%3D%26DOTS01%3D%26SWIP01%3D%26ABSI00%3D%26COTE01%3D%26NORE01%3D%26SOLR00%3D%26CDCO00%3D',
    '_dc_gtm_UA-527734-1': '1',
    '_ga_B8CPBTKGPW': 'GS1.1.1694444983.14.0.1694444983.0.0.0',
    '_hjIncludedInSessionSample_72519': '0',
    '_hjSession_72519': 'eyJpZCI6ImM5MGYyMzQxLWRhM2MtNGNlYy1iMjgxLWMyNzQxYjcwMmJlMyIsImNyZWF0ZWQiOjE2OTQ0NDQ5ODM3NzMsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    'FPLC': 'kL7KeQOmhjB49i8oz34NZ0bEa7rPl2Ddc%2F6vAWnKSecwgIfzNccg1h8wxbd1lI%2B03X3Rf7Sr0VkGABLLL%2BBIKb2FZ8f%2FZUwSCSyqfMVJszllG9c8yXy8TJWzN2X8BQ%3D%3D',
    'cto_bundle': '0nPIjl9Kb1ZyOERVYWVselhxOXMlMkJZRnZ2SWtsVWpzd08ycDdOTWtFMFBIaCUyRjJiNXRsRU1FNXR4bDJVT2MlMkZPODF0N2EzTlpZcUFoSmxYNmRyNkRQU2Z0S3BMYTRxdFBtZFVnZTdXN0xJcmlvTGpmR3ZSRldIa25aS2dTZWtLODVEenVCcDBOeGN4MzU2NDJoeHNmbldna2k0QjVkejRHYlhFS25aMlcyUkdvS2FrejQ5NXpuTkNPM01LMDlPYVFrZkxJcEJPb05oaGM3ekdyd29lQlklMkIlMkZrRmVoY21haURvYkcwckhGZkFad2NIMWxpYzFxNFYlMkZIaHd0bTJBOFZ4V3JOMk5GRHh5U1J3UWJBeUJKRDJnY3ZBQ3BwQSUzRCUzRA',
    '_ga': 'GA1.2.889355546.1694189024',
    'c24-data': 'eyI1Ijp7ImUiOiIxNjk3MDM2OTgyIiwidiI6IjEifSwiNiI6eyJlIjoiMTY5NzAzNjk4MiIsInYiOiIxIn0sIjkiOnsiZSI6IjE2OTU1ODYwNTIiLCJ2IjoiMTY5NDI5MDA0NzY0MyJ9LCIyNyI6eyJlIjoiMTcyNTk4MDk4MiIsInYiOiIxMyJ9LCIzMCI6eyJlIjoiMTY5NTU4NjA1MyIsInYiOiI4In0sIjM3Ijp7ImUiOiIxNzI1OTgwOTgyIiwidiI6IjE2OTQ0NDQ5ODI5ODQifSwiMzgiOnsiZSI6IjE3MjU3MjUwMjMiLCJ2IjoiMTY5MTUxMDYyMzI1MCJ9LCI0MSI6eyJlIjoiMTcyNTcyNTAyMyIsInYiOiIxNjk0MTg5MDIzMDAwIn0sIjQ0Ijp7ImUiOiIxNjk1NTg2MDUzIiwidiI6IjEifSwiOTgiOnsiZSI6IjE3MjU5ODA5ODIiLCJ2IjoiMSJ9LCIxMTUiOnsidiI6Im1kIiwiZSI6IjE3MDk5OTY5OTkifSwiMjMyIjp7ImUiOiIxNzI1NzI1MDI1IiwidiI6IjE2OTQxODkwMjMzMDEifSwiMjQ3Ijp7ImUiOiIxNzI1NzI2MjI1IiwidiI6IjE2OTQxOTAyMjMxNTkifSwiMjQ4Ijp7ImUiOiIxNzI1NzI2MjI1IiwidiI6IjEifSwiMjQ5Ijp7ImUiOiIxNzI1NzI2MjI1IiwidiI6IjEifSwiNDMzIjp7ImUiOiIxNjk2NzkwMTYxIiwidiI6IjIifSwiNDY1Ijp7ImUiOiIxNzg4Nzk3MDI2IiwidiI6IjE3ODg3OTcwMjYzNzQifX0=',
}

headers = {
    'authority': 'www.chrono24.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

params = {
    'sortorder': '5',
}

response = requests.get(f'{url_}', params=params, cookies=cookies, headers=headers)

if response.status_code == 200:
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    try:
        li_tags = soup.find('ul', class_='pagination list-unstyled d-flex pull-xs-none pull-sm-right').find_all('li')

        if len(li_tags) >= 2:
            predposledniy_li = li_tags[-2]
            text_iz_li = predposledniy_li.get_text()
            pagination = text_iz_li.strip()
            print(f'pagination >>> {pagination}')
        else:
            print("There are not enough <li> tags to get the penultimate value.")
    except:
        pagination = 1

    for i in range(1, int(pagination) + 1):

        url = url_.replace(".htm", f"-{i}.htm")

        print(f'{url}')

        response = requests.get(url, cookies=cookies, headers=headers)

        if response.status_code == 200:
            html_content = response.text

            soup = BeautifulSoup(html_content, 'html.parser')

            script_tag = soup.find("script", {"type": "application/ld+json"})

            if script_tag:

                script_content = script_tag.string
                script_content_ = json.loads(script_content)

                for url__ in script_content_["@graph"][1]["offers"]:
                    url_i = url__["url"]
                    # url = f'{pre_}{url.strip()}'
                    print(f'\t\t{url_i}')
                    arr_.append(url_i)
#
#   Part 2. Collection of information. =================================================================================
#
for www in arr_:
    url = www.strip()

    print(url)

    pattern = r"id(\d+).htm"
    match = re.search(pattern, url)

    if match:
        id_ = match.group(1)
        directory_name = id_

    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    response = requests.get(f'{url}', cookies=cookies, headers=headers)

    if response.status_code == 200:
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        prod = soup.find("section", class_='js-details-and-security-tabs').find_all('tbody')

        data = {}
        data["URL"] = {"url": url}

        for i in prod:

            tr_s = i.find_all('tr')

            current_category = ''
            category_data = {}

            for y in i.find_all('tr'):

                try:
                    current_category = y.find('h3').text.strip()
                except:
                    td_s = y.find_all('td')
                    if len(td_s) > 1:
                        key = td_s[0].text.strip()
                        value_ = td_s[1].text.strip()
                        value = ' '.join(value_.split())
                    else:
                        key = 'data'
                        value = td_s[0].text.strip()

                    category_data[key] = value

            data[current_category] = category_data

        params = {
            'id': f'{id_}',
            'notes': '',
            't': '1694190268107',
        }

        response = requests.get('https://www.chrono24.com/search/detail.htm', params=params, cookies=cookies, headers=headers)

        xml_response = response.text
        root = ET.fromstring(xml_response)

        cdata_text = root.text
        if cdata_text is not None:
            text_without_br = cdata_text.replace("<br>", " ")
            cleaned_text = " ".join(text_without_br.split())

            data["Description"]["data"] = cleaned_text
        else:
            pass

        try:
            rev_tag = soup.find('strong', class_='text-xlg text-bold')
            rev_ = rev_tag.text.strip()  # "(99)"
        except:
            rev_ = ''

        try:
            span_tag = soup.find('span', class_='rating')
            tit_ = span_tag.text.strip()  # "4.4"
        except:
            tit_ = ''

        merchant_button = soup.find('button', class_='js-link-merchant-name')
        merchant_name = merchant_button.text.strip()

        data["Seller INFO"] = {
            "Seller": merchant_name,
            "Seller rating": f'{tit_} {rev_}',
            "SellerID": id_
        }

        headers.update({"If-Modified-Since": "Thu, 01 Jan 1970 00:00:00 GMT"})  # Добавляем новый заголовок

        if download_zoom_images:

            zoom = True
            link_dict['zoom'] = []

            img_div = soup.find_all('div', {'data-zoom-image': True})

            if len(img_div) != 0:
                for t_ in img_div:
                    image_url = t_['data-zoom-image']
                    download_img(image_url, directory_name, zoom)
            else:
                print(f'\n!!! Images with the "data-zoom-image" attribute are NOT AVAILABLE for id = {id_} !!!\n')

        if download_data_image:

            zoom = False
            link_dict['data'] = []

            script_tag = soup.find("script", {"type": "application/ld+json"})

            if script_tag:
                script_content = script_tag.string
                script_content_ = json.loads(script_content)

            for url_ in script_content_["@graph"][1]["image"]:
                image_url = url_["contentUrl"]

                download_img(image_url, directory_name, zoom)
        data["IMG"] = link_dict

        with open(f'111_{id_}.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
