# linkedin_scraper.py
import sys
from utils import scrape_profile

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 linkedin_scraper.py <user_id>")
        return

    user_id = sys.argv[1]
    try:
        profile_data = scrape_profile(user_id)
        print(f"Links found: {profile_data['links']}")
        print(f"Emails found: {profile_data['emails']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
