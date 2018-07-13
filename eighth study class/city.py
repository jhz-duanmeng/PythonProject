def city_country(city_name, country_name):
    name = city_name + "," + country_name
    return name.title()


while True:
    print("\nPlease input the city and country name:")
    city = input("请输入城市名字：")
    country = input("请输入国家名字：")

    names = city_country(city, country)
    print(names)
