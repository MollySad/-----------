import requests

from pprint import pprint

with open('token.txt', 'r') as file_object:
    token = file_object.read().strip()

with open('tokenYa.txt', 'r') as file_object:
    tokenYa = file_object.read().strip()

class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version    
        }

    def foto(self):
        foto_url = self.url + 'photos.get'
        foto_params = {
            'owner_id': '254171857',
            'album_id': 'profile',
            'extended': 1,
            'photo_sizes': 0
        }
        res = requests.get(foto_url, params={**self.params, **foto_params}).json()
        
        photo_url = vk_client.foto()['response']['items'][0]['sizes'][8]['url']

        #download_photo = requests.get(photo_url)
    
        #with open('1.jpg', 'ab') as f:
        #   f.write(download_photo.content)
        
        return res

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        #file_path = os.path.normpath(file_path)
        HEADERS = {"Authorization" : f'OAuth {self.token}'}
        FILES = {"file" : open(file_path, 'rb')}

        res_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        res = requests.get(res_url, params={'path': file_path}, headers=HEADERS)

        url = res.json().get('href')
        resp = requests.put(url, files=FILES, headers={})

        return print(resp.status_code)




vk_client = VkUser(token, '5.131')
#pprint(vk_client.foto())
#pprint(vk_client.foto()['response']['items'][0]['likes']['count'])
f = vk_client.foto()['response']['items'][0]['sizes'][8]['url']
print('gfg')

uploader = YaUploader(token=tokenYa)
#print(uploader.upload('1.jpg'))