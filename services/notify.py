import requests
import os
from dotenv import load_dotenv

load_dotenv()




class Notify:

    def __init__(self) -> None:
        self.__url_base = os.getenv("URL_BASE")
	


    def send_event(self, data):
        requests.post(
            url=self.__url_base,
            json=data
        )
