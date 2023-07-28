from bs4 import BeautifulSoup
import requests
import json



def bird_species_data(const):
     url = f"https://xeno-canto.org/api/2/recordings?query={const}"
     response = requests.get(url)
     

     if response.status_code == 200:
         bird_data = response.json()
         species_list = []



         for recording in bird_data['recordings']:
             species = recording['en']
             family = f"{recording['gen']} {recording['sp']}"
             country = recording['cnt']



             species_list.append({
                 'species': species,
                 'family': family,
                 'country': country,
             })
             

         return species_list
     else:
         print(f"Failed to fetch data. Status code: {response.status_code}")
         return []
     
     
     
     
if __name__ == "__main__":
    query = "cnt:Kenya"
    song = bird_species_data(query)


    if song:
        json_filename = "species.json"
        with open(json_filename, 'w') as json_file:
            json.dump(song, json_file, indent=3)
        print(f"Data saved to {json_filename}.")
        
    else:
        print("No data retrieved.")
     
     
     
     
# 2. Extract all the bird songs from the website.

def bird_songs():
    base_url = "https://xeno-canto.org/api/2/recordings"
    count = 1
    song_list = []

    while True:
        url = f"{base_url}?query=X&page={count}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            total = int(data['numRecordings'])

            for recording in data['recordings']:
                song_list.append({
                    'song_name': recording['en'],
                    'bird_family': f"{recording['gen']} {recording['sp']}",
                    'country': recording['cnt'],
                    'audio_url': recording['file']
                })

            if len(song_list) >= total:
                break
            count += 1
            
            
        else:
            print(f"Failed to fetch data for page {count}. Status code: {response.status_code}")
            break

    return song_list


if __name__ == "__main__":
    song = bird_songs()
    

    if song:
        json_filename = "songs.json"
        with open(json_filename, 'w') as json_file:
            json.dump(song, json_file, indent=4)
        print(f"Data saved to {json_filename}.")
        
    else:
        print("No data retrieved.")

