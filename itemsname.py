import requests
from matchdecode import specific_player_items
from matchdecode import hero
import random


item_dnames = []
localnames = []
good=[]
exclude=[115,116,117,118,130,131,132,133,134,127,124,125,122,24]
def get_item_names(ids):
    # Fetch the item data from the Dota 2 constants repository
    url = "https://raw.githubusercontent.com/odota/dotaconstants/master/build/item_ids.json"
    url2 = "https://raw.githubusercontent.com/odota/dotaconstants/master/build/items.json"
    url3 = "https://raw.githubusercontent.com/odota/dotaconstants/master/build/heroes.json"
    response2 = requests.get(url2)
    response = requests.get(url)
    response3 = requests.get(url3)

    if response.status_code == 200:
        item_data = response.json()
        dname_data = response2.json()
        heroname = response3.json()
        for x in range(0, 2):
            ranh = random.randint(1, 138)
            if ranh != hero and ranh != exclude:
                hero.append(ranh)
            else:
                x -= 1
        item_names = []

        # Append names to items using the provided IDs
        for item_id in ids:
            item_name = item_data.get(str(item_id), )
            item_names.append(item_name)

        for item_tag in item_names:
            item_dname = dname_data.get(str(item_tag), {}).get('dname', )
            item_dnames.append(item_dname)
        for heros in hero:
            localname = heroname.get(str(heros), {}).get('localized_name', )
            localnames.append(localname)
        good.append(localnames[0])
        random.shuffle(localnames)
        return item_dnames, localnames, good
    else:
        print("Failed to fetch item data")
        return None


def main():
    # Use specific_player_items as the array of item IDs
    item_ids_array = specific_player_items

    # Get item names for the given array of item IDs
    result = get_item_names(item_ids_array)

    # Display the result
    if result:
        print("Item Names Array:", result, hero)


if __name__ == "__main__":
    main()


