import requests


def request_wrapper(website: str):
    return requests.get(website)