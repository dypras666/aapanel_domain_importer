import requests
import json

# Konfigurasi aaPanel API
AAPANEL_URL = "http://your_aapanel_ip:8888/webhook"
API_KEY = "your_api_key_here"

def add_website(domain):
    data = {
        "domain": domain,
        "path": f"/www/wwwroot/{domain}",
        "type": "PHP",
        "version": "00",  # Gunakan "00" untuk versi PHP default
        "port": "80",
        "ps": f"Imported website {domain}"
    }
    
    payload = {
        "request_token": API_KEY,
        "function": "create_website",
        "args": json.dumps(data)
    }
    
    response = requests.post(AAPANEL_URL, data=payload)
    return response.json()

def import_domains(file_path):
    with open(file_path, 'r') as file:
        domains = file.read().splitlines()
    
    for domain in domains:
        result = add_website(domain)
        if result.get('status'):
            print(f"Berhasil menambahkan {domain}")
        else:
            print(f"Gagal menambahkan {domain}: {result.get('msg')}")

if __name__ == "__main__":
    import_domains("daftar_domain.txt")
