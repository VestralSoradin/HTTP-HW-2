import requests
from pprint import pprint
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(url=upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, disk_file_path, filename):

        data = self._get_upload_link(disk_file_path=disk_file_path)
        url = data.get('href')

        response = requests.put(url=url, data=open(filename, 'rb'))

        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':

    ya = YaUploader(token = token)
    ya.upload('netology/test.txt', 'test.txt')

