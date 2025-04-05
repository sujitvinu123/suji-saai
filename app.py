from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import re
import concurrent.futures
from social_platforms import SOCIAL_PLATFORMS, IMPORTANT_PLATFORMS, SECONDARY_PLATFORMS, OTHER_PLATFORMS
import time
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

def check_platform(platform, username, url_pattern):
    try:
        url = url_pattern.format(username)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }
        
        # Special handling for LinkedIn
        if platform == 'linkedin':
            try:
                headers.update({
                    'Accept': 'application/vnd.linkedin.normalized+json+2.1',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'x-li-lang': 'en_US',
                    'x-restli-protocol-version': '2.0.0'
                })
                response = requests.get(url, headers=headers, timeout=10, verify=False)
                if response.status_code == 200:
                    return {
                        'platform': platform,
                        'url': url,
                        'exists': True,
                        'status': 'Found'
                    }
            except:
                pass
        
        # Special handling for Instagram
        if platform == 'instagram':
            try:
                response = requests.get(url, headers=headers, timeout=10, verify=False)
                if response.status_code == 200:
                    return {
                        'platform': platform,
                        'url': url,
                        'exists': True,
                        'status': 'Found'
                    }
            except:
                pass
        
        # For other platforms
        try:
            response = requests.get(url, headers=headers, timeout=10, verify=False, allow_redirects=True)
            
            if response.status_code == 200:
                # Check if the page contains common "not found" messages
                not_found_phrases = [
                    'not found', 'doesn\'t exist', '404', 'error', 'page not found',
                    'no profile', 'user not found', 'profile not found', 'sorry, this page',
                    'this account doesn\'t exist', 'couldn\'t find this account'
                ]
                
                # Check if any of the not found phrases are in the page content
                page_content = response.text.lower()
                if not any(phrase in page_content for phrase in not_found_phrases):
                    return {
                        'platform': platform,
                        'url': url,
                        'exists': True,
                        'status': 'Found'
                    }
            
            return {
                'platform': platform,
                'url': url,
                'exists': False,
                'status': 'Not Found'
            }
        except requests.exceptions.Timeout:
            return {
                'platform': platform,
                'url': url,
                'exists': False,
                'status': 'Timeout - Please try again'
            }
        except requests.exceptions.SSLError:
            return {
                'platform': platform,
                'url': url,
                'exists': False,
                'status': 'SSL Error - Please try again'
            }
        except Exception as e:
            return {
                'platform': platform,
                'url': url,
                'exists': False,
                'status': f'Error: {str(e)}'
            }
    except Exception as e:
        return {
            'platform': platform,
            'url': url_pattern.format(username),
            'exists': False,
            'status': f'Error: {str(e)}'
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    username = request.form.get('username')
    if not username:
        return jsonify({'error': 'Please enter a username'}), 400
    
    results = {
        'username': username,
        'platforms': {},
        'found_count': 0,
        'total_checked': len(SOCIAL_PLATFORMS),
        'categories': {
            'important': list(IMPORTANT_PLATFORMS.keys()),
            'secondary': list(SECONDARY_PLATFORMS.keys()),
            'other': list(OTHER_PLATFORMS.keys())
        }
    }
    
    # Use ThreadPoolExecutor to check platforms concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        future_to_platform = {
            executor.submit(check_platform, platform, username, url_pattern): platform
            for platform, url_pattern in SOCIAL_PLATFORMS.items()
        }
        
        for future in concurrent.futures.as_completed(future_to_platform):
            platform = future_to_platform[future]
            try:
                result = future.result()
                results['platforms'][platform] = result
                if result['exists']:
                    results['found_count'] += 1
            except Exception as e:
                results['platforms'][platform] = {
                    'platform': platform,
                    'url': SOCIAL_PLATFORMS[platform].format(username),
                    'exists': False,
                    'status': f'Error: {str(e)}'
                }
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5002) 