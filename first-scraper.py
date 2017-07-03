from flask import Flask, request, jsonify
import lxml
import requests
from lxml import html
from lxml import etree




# page = requests.get('http://www.gamestop.com/nintendo-switch/consoles/nintendo-switch-console-with-gray-joy-con/141820')
page = requests.get('http://www.gamestop.com/nintendo-switch/consoles/nintendo-switch-console-with-gray-joy-con/141820')
# page = requests.get('http://www.gamestop.com/ps4/consoles/playstation-4-500gb-blast-from-the-past-big-screen-heroes-bundle/147386')

root = etree.HTML(page.content)
# print page.content


# tree = html.fromstring(page.content)
# tree = html.fromstring(page2.content)
price = root.xpath('//h3[@class="ats-prodBuy-price"]/span/text()')
not_available = root.xpath('//div[@class="buttonna"]/a/span/text()')
add_to_cart = root.xpath('//div[@class="button qq"]/div/a/span/text()')

# price = tree.xpath('//h3[@class="ats-prodBuy-price"]/text()')
# availability = tree.xpath('//div[@class="buttonna"]/text()')
# test = tree.xpath('//span/text()')

# print price
# print test
# print ('Not Available' in test)
print not_available
print price
print add_to_cart

