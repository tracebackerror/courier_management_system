import random
import json

city = ['Bengaluru', 'Chennai', 'Delhi', 'Goa', 'Kolkata', 'Pune', 'Mumbai']
json_data = {}

for i in city:
    for j in city:
        normal_rate_under_100g = random.randint(10, 30)
        fast_rate_under_100g = normal_rate_under_100g + random.randint(1, 10)

        normal_rate_under_500g = random.randint(30, 60)
        fast_rate_under_500g = normal_rate_under_500g + random.randint(10, 15)

        normal_rate_under_1000g = random.randint(60, 90)
        fast_rate_under_1000g = normal_rate_under_1000g + random.randint(20, 25)

        normal_rate_under_9999g = random.randint(90, 120)
        fast_rate_under_9999g = normal_rate_under_9999g + random.randint(25, 30)


        d_normal_rate = random.randint(5, 30)
        d_fast_rate = d_normal_rate + random.randint(1, 10)
        
        json_data[f"{i}->{j}"] = {
            "parcel": {
                "normal_rate_under_100g": normal_rate_under_100g,
                "normal_rate_under_500g": normal_rate_under_500g,
                "normal_rate_under_1000g": normal_rate_under_1000g,
                "normal_rate_under_9999g": normal_rate_under_9999g,
                "fast_rate_under_100g": fast_rate_under_100g,
                "fast_rate_under_500g": fast_rate_under_500g,
                "fast_rate_under_1000g": fast_rate_under_1000g,
                "fast_rate_under_9999g": fast_rate_under_9999g,
            },
            "document": {
                "normal_rate": d_normal_rate,
                "fast_rate": d_fast_rate,
            }
        }

with open("data\courier_rates.json","w") as f:
    json.dump(json_data,f)