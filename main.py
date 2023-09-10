import requests
from bs4 import BeautifulSoup
import re
import json
import os
import time

import xml.etree.ElementTree as ET


download_zoom_images = True     # True or False
download_data_image = True      # True or False

link_dict = {}
link_dict['data'] = []
link_dict['zoom'] = []

def download_img(img_url, dir_name, zoom_):
    file_name = os.path.basename(img_url)

    if zoom_:
        dir2_path = os.path.join(dir_name, "_zoom_")
        if not os.path.exists(dir2_path):
            os.makedirs(dir2_path)

        # Теперь, когда "dir2" существует, проверяем наличие файла внутри "dir2"
        file_path = os.path.join(dir2_path, file_name)
        link_dict['zoom'].append(img_url)
    else:
        # Проверяем наличие файла в "dir1"
        file_path = os.path.join(dir_name, file_name)
        link_dict['data'].append(img_url)

    if os.path.isfile(file_path):
        print(f"\tImage {file_name} already exists in directory {dir_name}")
    else:
        # print(f"Файл {file_name} не существует в директории {dir_name}")

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



with open("links.txt", "r", encoding="utf-8") as file:
    for www in file:
        url = www.strip()

        print(url)

        pattern = r"id(\d+).htm"
        match = re.search(pattern, url)

        if match:
            id_ = match.group(1)
            directory_name = id_

        if not os.path.exists(directory_name):
            os.makedirs(directory_name)

        cookies = {
            'search-session': '|6a179a8c_zuamIi|0|29158964.29940559.24908804.24443649.27561386.27818548.30401334.29746351.30383113.25777492.24056926.27891713.29333387.27561436.28565466.30062052.30145512.30003965.28449728.25554829.22015242.30184127.28561621.29727383.28937335.30143600.29856183.28226551.28644016.28951817.24476162.30398070.30394802.28909285.28755931.29727601.29228144.25777493.24975400.29069179.29986850.30387912.30007212.30089089.27585922.28592010.25592417.30031494.28886644.25911730.29773938.22942059.29632645.28628991.30402696.22107117.29402616.30184149.30193177.29635311.30090003',
            'chronosessid': 'f84e7257-84c8-4d1f-894f-e4868ef0e245',
            'filter-combinations': '2:Man|Mod,0:',
            'csrf-token': '1694171142.2SV2xgqXVvLjDACNnGTKUZ2CbzRvEoYWSXPS58UGy6o.AXG1Vdi64lSwzHjhFKkDZcPXRsl6',
            'timezone': 'Europe/Kiev',
            '__ssid': '48fcab77fc77e691a2f766df428787c',
            'consent-session': '2d85fd1c-d0c6-4041-b254-22c82c846aa0',
            'c24-consent': 'AAAAH8/vwf4=',
            'FPID': 'FPID2.2.SNMSTPBdw09c%2FOemDe2nY1YKAHe20RIAOmbxmmiUlZw%3D.1694171145',
            '_gcl_au': '1.1.1505745328.1694171148',
            '_gid': 'GA1.2.1778751159.1694171148',
            'last-search-result-ids': '29158964.29940559.24908804.24443649.27561386.27818548.30401334.29746351.30383113.25777492.24056926.27891713.29333387.27561436.28565466.30062052.30145512.30003965.28449728.25554829.22015242.30184127.28561621.29727383.28937335.30143600.29856183.28226551.28644016.28951817.24476162.30398070.30394802.28909285.28755931.29727601.29228144.25777493.24975400.29069179.29986850.30387912.30007212.30089089.27585922.28592010.25592417.30031494.28886644.25911730.29773938.22942059.29632645.28628991.30402696.22107117.29402616.30184149.30193177.29635311.30090003',
            'pu': 'true',
            '_hjFirstSeen': '1',
            '_hjIncludedInSessionSample_72519': '0',
            '_hjSession_72519': 'eyJpZCI6ImQ1ZmQxYTE3LWY0OTAtNDJjOS04ZjAwLTU3ZmY3NzEyZmI3NiIsImNyZWF0ZWQiOjE2OTQxNzExNDg1OTMsImluU2FtcGxlIjpmYWxzZX0=',
            '_hjAbsoluteSessionInProgress': '0',
            '_pin_unauth': 'dWlkPU0yRTROalF3TVdFdE16VmtNUzAwWTJObUxUbGxNR1V0TTJGbE56SmhaV0kwTldWaA',
            'FPLC': 'mTIoupLBIcfCnnmb61qDw7xjgXQ%2F5THEPP%2BJeYCB4N0RvK%2Ffy4KJBybBKJxo9rlWA%2FEGH89e32sHMtMAB0vL7pauV0S7ss0d9fGYAHzZ4BmpzeRRUbpg6S1UQifzQQ%3D%3D',
            'cfctGroup': 'DOTS00%3D%26AAA00%3D%26ABSI00%3D%26SWIP00%3D%26COTE00%3D%26NORE01%3D%26SOLR00%3D%26CDCO00%3D',
            '_hjSessionUser_72519': 'eyJpZCI6IjVmZTU3ZWNjLTBjMzctNWUwMC05ZmM5LTQ0MTVkZTVlNzcxOSIsImNyZWF0ZWQiOjE2OTQxNzExNDg1OTIsImV4aXN0aW5nIjp0cnVlfQ==',
            'ln_or': 'eyI0NjQ4OCI6ImQifQ%3D%3D',
            'userHistory': '29158964|1694171215786|2',
            'cto_bundle': 'zuTvyl9GeHZUdE0lMkJlNjlYc3pEZFNIS0ZWYXdjJTJGWkxPSUFFdkF6NTBqVUQzTkNxNlZOSHdESFYlMkZDJTJCbHBRT1BGT3ZSWlJxJTJCVlIlMkZSZnV1VWM2NnFoUFNxSGNrdm1oYmp6Qm5NN0pFa1Jpd0wlMkIlMkZCUUVUZ1F1UEljTVZsbXgyQXdtR0ZuTFhIY0IydXpMODlUeGhIQ3VoUzNEQXo1cGl6bCUyQkJoYVlKSWNKM1g2Zk9tSk1kODE4cDJvWjRiM0VNTFZ6RjklMkJickY0Rk00YUpQSDAwV1dRNEpvZUhvJTJCZyUzRCUzRA',
            '_derived_epik': 'dj0yJnU9WGlGQzdfcU5OTUZQY2U1Y2tZSnFOTVA2eERId1RkLWQmbj01dkpiSXd5TjNFM3FWYzBvVkcyTXFnJm09ZiZ0PUFBQUFBR1Q3QUZFJnJtPWYmcnQ9QUFBQUFHVDdBRkUmc3A9NQ',
            'c24-data': 'eyI1Ijp7ImUiOiIxNjk2NzYzMjE2IiwidiI6IjYifSwiNiI6eyJlIjoiMTY5Njc2MzIxNiIsInYiOiI2In0sIjI3Ijp7ImUiOiIxNzI1NzA3MTQyIiwidiI6IjEifSwiMzYiOnsiZSI6IjE3MjU3MDcxNDIiLCJ2IjoiMTY5NDE3MTE0MjEwMiJ9LCIzNyI6eyJlIjoiMTcyNTcwNzE0MiIsInYiOiIxNjk0MTcxMTQyMTAyIn0sIjM4Ijp7ImUiOiIxNzI1NzA3MTQyIiwidiI6IjE2OTE0OTI3NDIxMDIifSwiNDEiOnsiZSI6IjE3MjU3MDcxNDIiLCJ2IjoiMTY5NDE3MTE0MjAwMCJ9LCI5OCI6eyJlIjoiMTcyNTcwNzIxNiIsInYiOiI2In0sIjExNSI6eyJ2IjoibWQiLCJlIjoiMTcwOTcyMzIzNCJ9LCIyMzIiOnsiZSI6IjE3MjU3MDcyMDciLCJ2IjoiMTY5NDE3MTIwMjcwMyJ9LCI0NjUiOnsiZSI6IjE3ODg3NzkxNDYiLCJ2IjoiMTc4ODc3OTE0NjM2NSJ9fQ==',
            '_ga': 'GA1.2.1621830338.1694171145',
            '_dc_gtm_UA-527734-1': '1',
            '_ga_B8CPBTKGPW': 'GS1.1.1694171145.1.1.1694171446.0.0.0',
        }

        headers = {
            'authority': 'www.chrono24.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
            'cache-control': 'max-age=0',
            # 'cookie': 'search-session=|6a179a8c_zuamIi|0|29158964.29940559.24908804.24443649.27561386.27818548.30401334.29746351.30383113.25777492.24056926.27891713.29333387.27561436.28565466.30062052.30145512.30003965.28449728.25554829.22015242.30184127.28561621.29727383.28937335.30143600.29856183.28226551.28644016.28951817.24476162.30398070.30394802.28909285.28755931.29727601.29228144.25777493.24975400.29069179.29986850.30387912.30007212.30089089.27585922.28592010.25592417.30031494.28886644.25911730.29773938.22942059.29632645.28628991.30402696.22107117.29402616.30184149.30193177.29635311.30090003; chronosessid=f84e7257-84c8-4d1f-894f-e4868ef0e245; filter-combinations=2:Man|Mod,0:; csrf-token=1694171142.2SV2xgqXVvLjDACNnGTKUZ2CbzRvEoYWSXPS58UGy6o.AXG1Vdi64lSwzHjhFKkDZcPXRsl6; timezone=Europe/Kiev; __ssid=48fcab77fc77e691a2f766df428787c; consent-session=2d85fd1c-d0c6-4041-b254-22c82c846aa0; c24-consent=AAAAH8/vwf4=; FPID=FPID2.2.SNMSTPBdw09c%2FOemDe2nY1YKAHe20RIAOmbxmmiUlZw%3D.1694171145; _gcl_au=1.1.1505745328.1694171148; _gid=GA1.2.1778751159.1694171148; last-search-result-ids=29158964.29940559.24908804.24443649.27561386.27818548.30401334.29746351.30383113.25777492.24056926.27891713.29333387.27561436.28565466.30062052.30145512.30003965.28449728.25554829.22015242.30184127.28561621.29727383.28937335.30143600.29856183.28226551.28644016.28951817.24476162.30398070.30394802.28909285.28755931.29727601.29228144.25777493.24975400.29069179.29986850.30387912.30007212.30089089.27585922.28592010.25592417.30031494.28886644.25911730.29773938.22942059.29632645.28628991.30402696.22107117.29402616.30184149.30193177.29635311.30090003; pu=true; _hjFirstSeen=1; _hjIncludedInSessionSample_72519=0; _hjSession_72519=eyJpZCI6ImQ1ZmQxYTE3LWY0OTAtNDJjOS04ZjAwLTU3ZmY3NzEyZmI3NiIsImNyZWF0ZWQiOjE2OTQxNzExNDg1OTMsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _pin_unauth=dWlkPU0yRTROalF3TVdFdE16VmtNUzAwWTJObUxUbGxNR1V0TTJGbE56SmhaV0kwTldWaA; FPLC=mTIoupLBIcfCnnmb61qDw7xjgXQ%2F5THEPP%2BJeYCB4N0RvK%2Ffy4KJBybBKJxo9rlWA%2FEGH89e32sHMtMAB0vL7pauV0S7ss0d9fGYAHzZ4BmpzeRRUbpg6S1UQifzQQ%3D%3D; cfctGroup=DOTS00%3D%26AAA00%3D%26ABSI00%3D%26SWIP00%3D%26COTE00%3D%26NORE01%3D%26SOLR00%3D%26CDCO00%3D; _hjSessionUser_72519=eyJpZCI6IjVmZTU3ZWNjLTBjMzctNWUwMC05ZmM5LTQ0MTVkZTVlNzcxOSIsImNyZWF0ZWQiOjE2OTQxNzExNDg1OTIsImV4aXN0aW5nIjp0cnVlfQ==; ln_or=eyI0NjQ4OCI6ImQifQ%3D%3D; userHistory=29158964|1694171215786|2; cto_bundle=zuTvyl9GeHZUdE0lMkJlNjlYc3pEZFNIS0ZWYXdjJTJGWkxPSUFFdkF6NTBqVUQzTkNxNlZOSHdESFYlMkZDJTJCbHBRT1BGT3ZSWlJxJTJCVlIlMkZSZnV1VWM2NnFoUFNxSGNrdm1oYmp6Qm5NN0pFa1Jpd0wlMkIlMkZCUUVUZ1F1UEljTVZsbXgyQXdtR0ZuTFhIY0IydXpMODlUeGhIQ3VoUzNEQXo1cGl6bCUyQkJoYVlKSWNKM1g2Zk9tSk1kODE4cDJvWjRiM0VNTFZ6RjklMkJickY0Rk00YUpQSDAwV1dRNEpvZUhvJTJCZyUzRCUzRA; _derived_epik=dj0yJnU9WGlGQzdfcU5OTUZQY2U1Y2tZSnFOTVA2eERId1RkLWQmbj01dkpiSXd5TjNFM3FWYzBvVkcyTXFnJm09ZiZ0PUFBQUFBR1Q3QUZFJnJtPWYmcnQ9QUFBQUFHVDdBRkUmc3A9NQ; c24-data=eyI1Ijp7ImUiOiIxNjk2NzYzMjE2IiwidiI6IjYifSwiNiI6eyJlIjoiMTY5Njc2MzIxNiIsInYiOiI2In0sIjI3Ijp7ImUiOiIxNzI1NzA3MTQyIiwidiI6IjEifSwiMzYiOnsiZSI6IjE3MjU3MDcxNDIiLCJ2IjoiMTY5NDE3MTE0MjEwMiJ9LCIzNyI6eyJlIjoiMTcyNTcwNzE0MiIsInYiOiIxNjk0MTcxMTQyMTAyIn0sIjM4Ijp7ImUiOiIxNzI1NzA3MTQyIiwidiI6IjE2OTE0OTI3NDIxMDIifSwiNDEiOnsiZSI6IjE3MjU3MDcxNDIiLCJ2IjoiMTY5NDE3MTE0MjAwMCJ9LCI5OCI6eyJlIjoiMTcyNTcwNzIxNiIsInYiOiI2In0sIjExNSI6eyJ2IjoibWQiLCJlIjoiMTcwOTcyMzIzNCJ9LCIyMzIiOnsiZSI6IjE3MjU3MDcyMDciLCJ2IjoiMTY5NDE3MTIwMjcwMyJ9LCI0NjUiOnsiZSI6IjE3ODg3NzkxNDYiLCJ2IjoiMTc4ODc3OTE0NjM2NSJ9fQ==; _ga=GA1.2.1621830338.1694171145; _dc_gtm_UA-527734-1=1; _ga_B8CPBTKGPW=GS1.1.1694171145.1.1.1694171446.0.0.0',
            'referer': 'https://www.upwork.com/',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        }
        # #https://www.chrono24.com/omega/omega-seamaster-aqua-terra-beijing-2008-limited-edition--id29264730.htm
        # #response = requests.get('https://www.chrono24.com/tagheuer/ref-cv2013-3--id29158964.htm', cookies=cookies, headers=headers)
        #

        response = requests.get(f'{url}', cookies=cookies, headers=headers)

        if response.status_code == 200:
            html_content = response.text

            soup = BeautifulSoup(html_content, 'html.parser')

            # # Вывод всего разобранного HTML в файл
            # with open('000.html', 'w', encoding='utf-8') as file:
            #     file.write(soup.prettify())
            # print("Результат сохранен в файл 000.html")

            # # Открываем файл 000.html и считываем его содержимое
            # with open("000.html", "r", encoding="utf-8") as html_file:
            #     html_content = html_file.read()

            prod = soup.find("section", class_='js-details-and-security-tabs').find_all('tbody')

            data = {}
            data["URL"] = {"url": url}

            # print(prod.text.strip())
            # print(len(prod))
            for i in prod:
                # tit_ = i.find('h3').text.strip()
                # print(f'{tit_}')

                tr_s = i.find_all('tr')

                current_category = ''
                category_data = {}

                for y in i.find_all('tr'):

                    try:
                        current_category = y.find('h3').text.strip()
                        # print(f'{current_category}')
                    except:
                        td_s = y.find_all('td')
                        if len(td_s) > 1:
                            key = td_s[0].text.strip()
                            value_ = td_s[1].text.strip()
                            value = ' '.join(value_.split())
                            # print(f'\t{key} >>>>> {value}')
                        else:
                            key = 'data'
                            value = td_s[0].text.strip()
                            # print(f'\t\t\t{value}')

                        category_data[key] = value

                data[current_category] = category_data

            params = {
                'id': f'{id_}',
                'notes': '',
                't': '1694190268107',
            }

            response = requests.get('https://www.chrono24.com/search/detail.htm', params=params, cookies=cookies, headers=headers)

            # Получаем текстовое содержимое ответа
            xml_response = response.text

            # print(f'\nxml_response >>>>>>>>>>>>>>>>>>>>   {xml_response}')

            # Разбор XML
            root = ET.fromstring(xml_response)

            # # Извлекаем текст из CDATA
            # cdata_text = root.text
            # # Заменяем "<br>" на пробелы
            # text_without_br = cdata_text.replace("<br>", " ")

            # Получаем текст из CDATA элемента
            # cdata_element = root.find(".//notes")
            # if cdata_element is not None:
            cdata_text = root.text
            if cdata_text is not None:
                # Заменяем "<br>" на пробелы
                text_without_br = cdata_text.replace("<br>", " ")
                # Удаляем лишние пробелы
                cleaned_text = " ".join(text_without_br.split())

                data["Description"]["data"] = cleaned_text
            else:
                pass
                # data["Description"]["data"] = ''

            rev_tag = soup.find('strong', class_='text-xlg text-bold')
            rev_ = rev_tag.text.strip()  # "(99)"

            span_tag = soup.find('span', class_='rating')
            tit_ = span_tag.text.strip()  # "4.4"

            merchant_button = soup.find('button', class_='js-link-merchant-name')
            merchant_name = merchant_button.text.strip()

            data["Seller INFO"] = {
                "Seller": merchant_name,
                "Seller rating": f'{tit_} {rev_}',
                "SellerID": id_
            }

            cookies = {
                '__ssid': '48fcab77fc77e691a2f766df428787c',
                'FPID': 'FPID2.2.SNMSTPBdw09c%2FOemDe2nY1YKAHe20RIAOmbxmmiUlZw%3D.1694171145',
                '_gcl_au': '1.1.1505745328.1694171148',
                '_gid': 'GA1.2.1778751159.1694171148',
                '_pin_unauth': 'dWlkPU0yRTROalF3TVdFdE16VmtNUzAwWTJObUxUbGxNR1V0TTJGbE56SmhaV0kwTldWaA',
                'FPLC': 'mTIoupLBIcfCnnmb61qDw7xjgXQ%2F5THEPP%2BJeYCB4N0RvK%2Ffy4KJBybBKJxo9rlWA%2FEGH89e32sHMtMAB0vL7pauV0S7ss0d9fGYAHzZ4BmpzeRRUbpg6S1UQifzQQ%3D%3D',
                '_hjSessionUser_72519': 'eyJpZCI6IjVmZTU3ZWNjLTBjMzctNWUwMC05ZmM5LTQ0MTVkZTVlNzcxOSIsImNyZWF0ZWQiOjE2OTQxNzExNDg1OTIsImV4aXN0aW5nIjp0cnVlfQ==',
                '_ga': 'GA1.1.1621830338.1694171145',
                'cto_bundle': 'BBulvF9GeHZUdE0lMkJlNjlYc3pEZFNIS0ZWYXh3WGFTd1MlMkJTdFhMR2d0TjUzQk9EWTVXSGdSM1d5ak4xbmZmemM3a3F2RWgySkJmbmk3amk3WDZ0N0slMkJnbGdyanhiSkd2YlU3TXp5OHMxSVM0bGQ3a25NNWtpQmRDUXJpcjR6dDBMQVYxaTI0ak43aUJaSkQlMkYwRDN2ckxtcloyUjZtZEhvN3pzcWVYMGU0c0pPeGtmRSUyRjZSSGFNZmhDV2dMM2VRZGFiSENxR21CMElqQnJCbXJBQ2hoWVN0SEZ6dyUzRCUzRA',
                '_derived_epik': 'dj0yJnU9cW5LaHVlakl1UmtHSGQ1bXoyd0N6S2ViT3VYSzhLc3Ambj0xQlJ2b3N6R3FnNHpjTjV4R25jUWN3Jm09ZiZ0PUFBQUFBR1Q3QVdzJnJtPWYmcnQ9QUFBQUFHVDdBV3Mmc3A9NQ',
                '_ga_B8CPBTKGPW': 'GS1.1.1694173427.2.0.1694173427.0.0.0',
            }

            headers = {
                'authority': 'cdn2.chrono24.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
                'cache-control': 'max-age=0',
                # 'cookie': '__ssid=48fcab77fc77e691a2f766df428787c; FPID=FPID2.2.SNMSTPBdw09c%2FOemDe2nY1YKAHe20RIAOmbxmmiUlZw%3D.1694171145; _gcl_au=1.1.1505745328.1694171148; _gid=GA1.2.1778751159.1694171148; _pin_unauth=dWlkPU0yRTROalF3TVdFdE16VmtNUzAwWTJObUxUbGxNR1V0TTJGbE56SmhaV0kwTldWaA; FPLC=mTIoupLBIcfCnnmb61qDw7xjgXQ%2F5THEPP%2BJeYCB4N0RvK%2Ffy4KJBybBKJxo9rlWA%2FEGH89e32sHMtMAB0vL7pauV0S7ss0d9fGYAHzZ4BmpzeRRUbpg6S1UQifzQQ%3D%3D; _hjSessionUser_72519=eyJpZCI6IjVmZTU3ZWNjLTBjMzctNWUwMC05ZmM5LTQ0MTVkZTVlNzcxOSIsImNyZWF0ZWQiOjE2OTQxNzExNDg1OTIsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.1.1621830338.1694171145; cto_bundle=BBulvF9GeHZUdE0lMkJlNjlYc3pEZFNIS0ZWYXh3WGFTd1MlMkJTdFhMR2d0TjUzQk9EWTVXSGdSM1d5ak4xbmZmemM3a3F2RWgySkJmbmk3amk3WDZ0N0slMkJnbGdyanhiSkd2YlU3TXp5OHMxSVM0bGQ3a25NNWtpQmRDUXJpcjR6dDBMQVYxaTI0ak43aUJaSkQlMkYwRDN2ckxtcloyUjZtZEhvN3pzcWVYMGU0c0pPeGtmRSUyRjZSSGFNZmhDV2dMM2VRZGFiSENxR21CMElqQnJCbXJBQ2hoWVN0SEZ6dyUzRCUzRA; _derived_epik=dj0yJnU9cW5LaHVlakl1UmtHSGQ1bXoyd0N6S2ViT3VYSzhLc3Ambj0xQlJ2b3N6R3FnNHpjTjV4R25jUWN3Jm09ZiZ0PUFBQUFBR1Q3QVdzJnJtPWYmcnQ9QUFBQUFHVDdBV3Mmc3A9NQ; _ga_B8CPBTKGPW=GS1.1.1694173427.2.0.1694173427.0.0.0',
                'if-modified-since': 'Fri, 09 Jun 2023 17:01:38 GMT',
                'if-none-match': '"905f5f32cad22055c6ea8e23505c9119"',
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

            headers.update({"If-Modified-Since": "Thu, 01 Jan 1970 00:00:00 GMT"})  # Добавляем новый заголовок

            if download_zoom_images:

                zoom = True
                link_dict['zoom'] = []

                img_div = soup.find_all('div', {'data-zoom-image': True})

                if len(img_div) != 0:
                    for t_ in img_div:
                        # Получаем значение атрибута data-zoom-image
                        image_url = t_['data-zoom-image']
                        download_img(image_url, directory_name, zoom)
                else:
                    print(f'\n!!! Images with the "data-zoom-image" attribute are NOT AVAILABLE for id = {id_} !!!\n')

            if download_data_image:

                zoom = False
                link_dict['data'] = []

                script_tag = soup.find("script", {"type": "application/ld+json"})

                if script_tag:
                    # Извлекаем содержимое тега
                    script_content = script_tag.string
                    script_content_ = json.loads(script_content)

                    # # Сохраняем содержимое в файл "000.json"
                    # with open(f"{directory_name}.json", "w", encoding="utf-8") as json_file:
                    #     json.dump(script_content_, json_file, ensure_ascii=False, indent=4)

                for url_ in script_content_["@graph"][1]["image"]:
                    image_url = url_["contentUrl"]
                    # Убираем лишние пробелы и символы перевода строки
                    # url = f'{pre_}{url.strip()}'
                    # print(image_url)

                    download_img(image_url, directory_name, zoom)
            data["IMG"] = link_dict

            with open(f'111_{id_}.json', 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
