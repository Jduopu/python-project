"""
Request library
Jon Duopu
Apr. 6th, 2025
"""

# VARIBALES
import requests

# FUNCTIONS
def get_response(url, params = None):
  try:
    response = requests.get(url, params = params)
    response.raise_for_status()
    return response.json()
  except requests.RequestException as e:
    print(f"Request failed: {e}")
    return None
