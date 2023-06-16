import json

courier_rates = None
with open("data/courier_rates.json") as f:
    courier_rates = json.load(f)

def getCourierRates(_from, to, _type, weight):
    key = f"{_from}->{to}"
    rates = courier_rates[key][_type.lower()]
    if _type.lower() == "parcel":
        normal_rate = rates[f"normal_rate_under_{weight}g"]
        fast_rate = rates[f"fast_rate_under_{weight}g"]
    else:
        normal_rate = rates["normal_rate"]
        fast_rate = rates["fast_rate"]
    return normal_rate, fast_rate


def formatGoodsWeight(goods_weight):
    if goods_weight <= 100:
        weight = 100
    elif goods_weight > 100 and goods_weight <= 500:
        weight = 500
    elif goods_weight > 500 and goods_weight <= 1000:
        weight = 1000
    else:
        weight = 9999
    return weight


def calculateFare(post_data):
    picking_city = post_data["picking_city"]
    shipping_city = post_data["shipping_city"]
    courier_type = post_data["courier_type"]
    goods_weight = float(post_data["goods_weight"])
    fast_delivery = int(post_data["fast_delivery"])
    fare = 0
    key = f"{picking_city}->{shipping_city}"
    rates = courier_rates[key][courier_type.lower()]
    if courier_type.lower() == "parcel":
        weight = formatGoodsWeight(goods_weight)
        if fast_delivery:
            fare = rates[f"fast_rate_under_{weight}g"]
        else:
            fare = rates[f"normal_rate_under_{weight}g"]
    else:
        if fast_delivery:
            fare = rates["fast_rate"]
        else:
            fare = rates["normal_rate"]
    return fare
    