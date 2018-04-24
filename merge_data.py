import json

yelp_cu_place = json.load(open("yelp_scraper/yelp_cu_place.json"))
yelp_cu_rest = json.load(open("yelp_scraper/yelp_cu_rest.json"))
yelp_la_place = json.load(open("yelp_scraper/yelp_la_place.json"))
yelp_la_rest = json.load(open("yelp_scraper/yelp_la_rest.json"))

trip_cu_place = json.load(open("trip_scraper/trip_cu_place.json"))
trip_cu_rest = json.load(open("trip_scraper/trip_cu_rest.json"))
trip_la_place = json.load(open("trip_scraper/trip_la_place.json"))
trip_la_rest = json.load(open("trip_scraper/trip_la_rest.json"))

data = []

yelp_cu_place = sorted(sorted(sorted(yelp_cu_place, key=lambda x: x['lon']), key=lambda x: x['lat']), key= lambda x: x['title'])
trip_cu_place = sorted(sorted(sorted(trip_cu_place, key=lambda x: x['lon']), key=lambda x: x['lat']), key= lambda x: x['title'])

if len(yelp_cu_place) > len(trip_cu_place):
    length = len(trip_cu_place)
else:
    length = len(yelp_cu_place)

i = 0
j = 0
while i < length:
    if yelp_cu_place[i]['title'] < trip_cu_place[j]['title']:
        yelp_cu_place[i]['yelp_rating'] = yelp_cu_place[i]['rating']
        yelp_cu_place[i]['trip_rating'] = None
        data.extend(yelp_cu_place[i])
        i += 1
        continue

    elif yelp_cu_place[i]['title'] > trip_cu_place[j]['title']:
        trip_cu_place[i]['trip_rating'] = trip_cu_place[i]['rating']
        trip_cu_place[i]['yelp_rating'] = None
        data.extend(trip_cu_place[i])
        j += 1
        continue

    else:
        if assertAlmostEqual(float(yelp_cu_place[i]['lat']), float(trip_cu_place[j]['lat']), places=5):
            yelp_cu_place[i]['yelp_rating'] = yelp_cu_place[i]['rating']
            yelp_cu_place[i]['trip_rating'] = trip_cu_place[i]['rating']
            data.extend(yelp_cu_place[i])
            i += 1
            j += 1
            continue

        elif yelp_cu_place[i]['lat'] < trip_cu_place[j]['lat']:
            yelp_cu_place[i]['yelp_rating'] = yelp_cu_place[i]['rating']
            yelp_cu_place[i]['trip_rating'] = None
            data.extend(yelp_cu_place[i])
            i += 1
            continue
        else:
            trip_cu_place[i]['trip_rating'] = trip_cu_place[i]['rating']
            trip_cu_place[i]['yelp_rating'] = None
            data.extend(trip_cu_place[i])
            j += 1
            continue

yelp_cu_rest = sorted(sorted(sorted(yelp_cu_rest, key=lambda x: x['lon']), key=lambda x: x['lat']), key= lambda x: x['title'])
trip_cu_rest = sorted(sorted(sorted(trip_cu_rest, key=lambda x: x['lon']), key=lambda x: x['lat']), key= lambda x: x['title'])

if len(yelp_cu_rest) > len(trip_cu_rest):
    length = len(trip_cu_rest)
else:
    length = len(yelp_cu_rest)

i = 0
j = 0
while i < length:
    if yelp_cu_rest[i]['title'] < trip_cu_rest[j]['title']:
        yelp_cu_rest[i]['yelp_rating'] = yelp_cu_rest[i]['rating']
        yelp_cu_rest[i]['trip_rating'] = None
        data.append(yelp_cu_rest[i])
        i += 1
        continue

    elif yelp_cu_rest[i]['title'] > trip_cu_rest[j]['title']:
        trip_cu_rest[i]['trip_rating'] = trip_cu_rest[i]['rating']
        trip_cu_rest[i]['yelp_rating'] = None
        data.append(trip_cu_rest[i])
        j += 1
        continue

    else:
        if assertAlmostEqual(float(yelp_cu_rest[i]['lat']), float(trip_cu_rest[j]['lat']), rests=5):
            yelp_cu_rest[i]['yelp_rating'] = yelp_cu_rest[i]['rating']
            yelp_cu_rest[i]['trip_rating'] = trip_cu_rest[i]['rating']
            data.append(yelp_cu_rest[i])
            i += 1
            j += 1
            continue

        elif yelp_cu_rest[i]['lat'] < trip_cu_rest[j]['lat']:
            yelp_cu_rest[i]['yelp_rating'] = yelp_cu_rest[i]['rating']
            yelp_cu_rest[i]['trip_rating'] = None
            data.append(yelp_cu_rest[i])
            i += 1
            continue
        else:
            trip_cu_rest[i]['trip_rating'] = trip_cu_rest[i]['rating']
            trip_cu_rest[i]['yelp_rating'] = None
            data.append(trip_cu_rest[i])
            j += 1
            continue


yelp_la_place = sorted(sorted(sorted(yelp_la_place, key=lambda x: x['lon']), key=lambda x: x['lat']), key= lambda x: x['title'])
trip_la_place = sorted(sorted(sorted(trip_la_place, key=lambda x: x['lon']), key=lambda x: x['lat']), key= lambda x: x['title'])

if len(yelp_la_place) > len(trip_la_place):
    length = len(trip_la_place)
else:
    length = len(yelp_la_place)

i = 0
j = 0
while i < length:
    if yelp_la_place[i]['title'] < trip_la_place[j]['title']:
        yelp_la_place[i]['yelp_rating'] = yelp_la_place[i]['rating']
        yelp_la_place[i]['trip_rating'] = None
        data.extend(yelp_la_place[i])
        i += 1
        continue

    elif yelp_la_place[i]['title'] > trip_la_place[j]['title']:
        trip_la_place[i]['trip_rating'] = trip_la_place[i]['rating']
        trip_la_place[i]['yelp_rating'] = None
        data.extend(trip_la_place[i])
        j += 1
        continue

    else:
        if assertAlmostEqual(float(yelp_la_place[i]['lat']), float(trip_la_place[j]['lat']), places=5):
            yelp_la_place[i]['yelp_rating'] = yelp_la_place[i]['rating']
            yelp_la_place[i]['trip_rating'] = trip_la_place[i]['rating']
            data.extend(yelp_la_place[i])
            i += 1
            j += 1
            continue

        elif yelp_la_place[i]['lat'] < trip_la_place[j]['lat']:
            yelp_la_place[i]['yelp_rating'] = yelp_la_place[i]['rating']
            yelp_la_place[i]['trip_rating'] = None
            data.extend(yelp_la_place[i])
            i += 1
            continue
        else:
            trip_la_place[i]['trip_rating'] = trip_la_place[i]['rating']
            trip_la_place[i]['yelp_rating'] = None
            data.extend(trip_la_place[i])
            j += 1
            continue

yelp_la_rest = sorted(sorted(sorted(yelp_la_rest, key=lambda x: x['lon']), key=lambda x: x['lat']), key= lambda x: x['title'])
trip_la_rest = sorted(sorted(sorted(trip_la_rest, key=lambda x: x['lon']), key=lambda x: x['lat']), key= lambda x: x['title'])

if len(yelp_la_rest) > len(trip_la_rest):
    length = len(trip_la_rest)
else:
    length = len(yelp_la_rest)

i = 0
j = 0
while i < length:
    if yelp_la_rest[i]['title'] < trip_la_rest[j]['title']:
        yelp_la_rest[i]['yelp_rating'] = yelp_la_rest[i]['rating']
        yelp_la_rest[i]['trip_rating'] = None
        data.extend(yelp_la_rest[i])
        i += 1
        continue

    elif yelp_la_rest[i]['title'] > trip_la_rest[j]['title']:
        trip_la_rest[i]['trip_rating'] = trip_la_rest[i]['rating']
        trip_la_rest[i]['yelp_rating'] = None
        data.extend(trip_la_rest[i])
        j += 1
        continue

    else:
        if assertAlmostEqual(float(yelp_la_rest[i]['lat']), float(trip_la_rest[j]['lat']), rests=5):
            yelp_la_rest[i]['yelp_rating'] = yelp_la_rest[i]['rating']
            yelp_la_rest[i]['trip_rating'] = trip_la_rest[i]['rating']
            data.extend(yelp_la_rest[i])
            i += 1
            j += 1
            continue

        elif yelp_la_rest[i]['lat'] < trip_la_rest[j]['lat']:
            yelp_la_rest[i]['yelp_rating'] = yelp_la_rest[i]['rating']
            yelp_la_rest[i]['trip_rating'] = None
            data.extend(yelp_la_rest[i])
            i += 1
            continue
        else:
            trip_la_rest[i]['trip_rating'] = trip_la_rest[i]['rating']
            trip_la_rest[i]['yelp_rating'] = None
            data.extend(trip_la_rest[i])
            j += 1
            continue

with open('merged_data_final.json', 'w') as fp:
    json.dump(data, fp)
