"""
Request library
Jon Duopu
Apr. 6th, 2025
"""

# VARIBALES
import request

# FUNCTIONS
def get_response(url, params = None):
  try:
    response = request.get(url, params = params)
    response.raise_for_status()
    return response.json()
  except request.RequestException as e:
    print(f"Request failed: {e}")
    return None
