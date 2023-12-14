import requests
import time

import matchprocess



api_key = "your_api_key_here"
account_id = 86853590  # Replace with the desired account ID

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}

params = {
    "limit": 60,  # Adjust the limit as needed
}

try:
    # Get player's matches
    player_matches_url = f"https://api.opendota.com/api/players/{account_id}/matches"
    response = requests.get(player_matches_url, headers=headers, params=params, timeout=10)
    response.raise_for_status()

    player_matches_data = response.json()

    # Check if there are matches in the response
    if player_matches_data:
        for match in player_matches_data:
            match_id = match.get("match_id")
            if match_id:
                match_ids.append(match_id)
                print(f"Added Match ID {match_id} to the list.")
    else:
        print("No matches found for the player.")
except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"Request Exception: {err}")
except KeyboardInterrupt:
    print("Script interrupted by user.")

# Display the matches in the match_ids array
match_ids = []
print(match_ids)
matchprocess.main()
