import requests
from requests import Response, RequestException
from requests.structures import CaseInsensitiveDict

def check_status(url: str) -> None:
    try:
        response: Response = requests.get(url)
        status_code: int = response.status_code
        headers: CaseInsensitiveDict[str] = response.headers
        content_type: str = headers.get('Content-Type', 'Unknown')
        server: str = headers.get('Server', 'Unknown')
        response_time: float = response.elapsed.total_seconds()

        print(f'URL: {url}')
        print(f'Status Code: {status_code}')
        print(f'Content Type: {content_type}')
        print(f'Server: {server}')
        print(f'Response Time: {response_time:.2f} seconds')
    except RequestException as e:
        print(f'ERROR: {e}')

def main() -> None:
    print('-'*50)
    url_to_check: str = input('Enter the URL to check: ')
    check_status(url_to_check)
    print('-'*50)

if __name__ == '__main__':
    main()
