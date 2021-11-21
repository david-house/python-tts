import requests
from playsound import playsound
from os import path
# This is a sample Python script.

NUMBER_PATH = "./number_mpegs"
number_files = dict()

def download_number(number, number_files: dict, path_to_files: str):
    num = str(number)
    service_url = "https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q={0}&tl=en"
    if num in number_files.keys():
        return number_files[num]
    else:
        new_path = path.join(path_to_files, f"{num}.mpeg")
        new_url = service_url.format(num)
        m = requests.get(new_url)
        with open(new_path, mode="wb") as f:
            f.write(m.content)
        number_files[num] = new_path
        return new_path

def play_number(number):
    p = download_number(number, number_files, NUMBER_PATH)
    playsound(p)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    play_number(10)

