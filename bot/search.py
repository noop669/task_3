def search_city(message):
    file = open('new_city.txt', encoding="utf8")
    file_readed = list(map(str.strip, file.readlines()))
    file.close()
    for i in file_readed:
        i = i.split()
        if i[0].lower() == str(message).lower():
            geoloc = list(i[-2:])
            return geoloc