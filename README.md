# Read json file

## Інформація про призначення модуля:
Модуль призначений для роботи з json файлом.
Ми можемо доступитись до будь-якої частини файла, вказавши аргументами функції назву файла та елемент, який шукаємо. 
Другий аргумент функції - список, тому, якщо є декілька рівнів вкладеності, ми можемо вказати декілька eлементів у цьому списку.

## Example of use:

api = twitter.Api(consumer_key= "...", consumer_secret= "...", access_token_key= "...", access_token_secret= "...")

json_ = api.GetUser(screen_name='Candy12Mia').AsDict()

print( read_json( json_, ["name"]) )