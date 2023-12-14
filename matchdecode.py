import requests
import random

from get import fetched_id
from match_ids_module import match_ids
hero = []
specific_player_items = []
mid = []

def main():

    hero.clear()
    mid.clear()
    specific_player_items.clear()
    fetched_id.clear()

    print(len(match_ids))
    ranid = random.randint(0, len(match_ids))
    mid.append(ranid)
    print("matches id:", match_ids)
    api_key = "your_api_key_here"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    # Array to store item IDs for the specific player

    try:
        url = f"https://api.opendota.com/api/matches/{match_ids[ranid]}"
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        match_details = response.json()

        # Check if 'players' key exists in the response
        if 'players' in match_details:
            for player in match_details['players']:
                # Check if the player has the specified ID (86853590)
                if player.get('account_id') == 86853590:
                    hero.append(player[f"hero_id"])
                    items = []
                    for i in range(6):  # Assuming item_0 to item_5
                        item_key = f"item_{i}"
                        if item_key in player:
                            item_id = player[item_key]
                            items.append(item_id)
                            specific_player_items.append(item_id)

                    print(f"Items for Player with ID 86853590 in Match ID {match_ids[ranid]}: {items} On hero:{hero}")

            print(f"Successful response for Match ID {match_ids[ranid]}")
    except requests.exceptions.HTTPError as errh:
        if response.status_code == 500:
            print(f"Error 500: Internal Server Error for Match ID {match_ids[ranid]}")
        else:
            print(f"HTTP Error {response.status_code}: {errh}")

    # Print item IDs for the specific player
    print("Specific player (ID 86853590) item IDs:", specific_player_items)
    import itemsname



if __name__ == "__main__":
    main()
