from epages_client.client import RestClient
from epages_client.dataobjects.product_create import ProductCreate
from epages_client.dataobjects.product_update import ProductUpdate
from epages_client.dataobjects.category_create import CategoryCreate
from epages_client.dataobjects.category_update import CategoryUpdate
from epages_client.dataobjects.category_sequence_update import CategorySequenceUpdate
from pprint import pprint
import json
import uuid
import os
import requests
from random import shuffle

# Get api url and token from environment variables
api_url = os.environ.get("EPAGES_API_URL")
api_token = os.environ.get("EPAGES_API_TOKEN")

if api_url is None or api_token is None:
    quit("Environment variables not set.")

client = RestClient(api_url, api_token)

#client.commands()

#client.currency = "GBP"

#client.get_categories()

#payload = {'categoryId': '5A498829-7618-ACCC-E387-0A281012346F', 'productId': '5A61A5D5-C7C0-0D9B-F10F-0A2810110CA3'}
headers = {}

#headers["Accept"] = "application/vnd.epages.v1+json" # Won't work, works without it though
# The above won't work although the response is HTTP 204 as in with product delete. With product deletion
# the accept header can be the one above
# headers["Accept"] = "*/*"
# headers["Content-Type"] = "application/x-www-form-urlencoded"
# headers["Authorization"] = "Bearer Mc4tsDuxpr5cNTfi1b6pnxOyURTfOCsu"

# r = requests.post("https://spexitest.vilkasstore.com/rs/shops/spexitest/product-category-assignments", data=payload, headers=headers)

# pprint(r.__dict__)

params = {
    "query": {},
    "param1": "5A498825-CA21-7D28-1F67-0A28101234CB",
    "param2": ""
}

response = client.get_random(params)

pprint(response)

#client.locale = "en_US"
#categories = client.get_categories()

#pprint(categories[0]["categoryId"])

# product = ProductCreate()
# product.productNumber = uuid.uuid4()
# product.name = uuid.uuid4()

# params["object"] = product

# response = client.add_product(params)

# product_id = response["productId"]

# params = {
#     "query": {},
#     "param1": "",
#     "param2": ""
# }

# params["param1"] = product_id

# response = client.delete_product(params)

# pprint(response)

#params["data"] = {'image': open('tests/resources/test.jpg', 'rb')}
#params["param1"] = "5A498827-5BBE-90AF-DF44-0A2810123496"

#response = client.upload_product_image(params)

#pprint(response)

# 5A61A5D5-C7C0-0D9B-F10F-0A2810110CA3 : Just testing

#params["data"] = {'categoryId': ["5A498829-7618-ACCC-E387-0A281012346F", "5A498828-9C3E-2828-35F8-0A2810123423"], 'productId': ["5A61E34F-BAC7-8396-366A-0A2810112BBC", "5A61E8DE-2DC3-5F0D-22D7-0A281017FD74"]}

#params["query"]["categoryId"] = ["5A498829-7618-ACCC-E387-0A281012346F", "5A498828-9C3E-2828-35F8-0A2810123423", str(uuid.uuid4())]
#params["query"]["productId"] = ["5A61E34F-BAC7-8396-366A-0A2810112BBC", "5A61E8DE-2DC3-5F0D-22D7-0A281017FD74"]

#response = client.connect_category_and_product(params)

#response = client.delete_product_from_category(params)

#response = client.get_products()

#pprint(response)

#params["data"] = {'categoryId': uuid.uuid4(), 'productId': uuid.uuid4()}

# test = {"var1": 1, "var2": 2}
# test2 = {"var2": 3}

# pprint(test)
# pprint(test2)
# test2.update(test)
# pprint(test)

# headers["Accept"] = "application/vnd.epages.v1+json"
# headers["Content-Type"] = "application/json"
# headers["Authorization"] = "Bearer Mc4tsDuxpr5cNTfi1b6pnxOyURTfOCsu"

# r = requests.delete("https://spexitest.vilkasstore.com/rs/shops/spexitest/products/5A60A396-B8C9-DD5E-E8C5-0A28101742C9", headers=headers)

# pprint(r.text)

'''Image upload'''

#headers["Accept"] = "application/vnd.epages.v1+json"
#headers["Accept"] = "application/json"
#headers["Content-Type"] = "multipart/form-data"
#headers["Content-Disposition"] = "form-data; name='image'; filename='test.jpg'"
#headers["Content-Length"] = str(os.path.getsize("test.jpg"))
#headers["Authorization"] = "Bearer Mc4tsDuxpr5cNTfi1b6pnxOyURTfOCsu"

#files = {'image': open('tests/resources/test.jpg', 'rb')}

#r = requests.post("https://spexitest.vilkasstore.com/rs/shops/spexitest/products/5A498827-5BBE-90AF-DF44-0A2810123496/slideshow", headers=headers, files=files)

#pprint(r.text)

# Chicago Blackhawks snapback: 5A498827-5BBE-90AF-DF44-0A2810123496
# The root category: 5A498825-CA21-7D28-1F67-0A28101234CB

# params = {
#     "query": {},
#     "param1": "",
#     "param2": ""
# }

# params["data"] = {'categoryId': '5A498829-7618-ACCC-E387-0A281012346F', 'productId': '5A60A396-B8C9-DD5E-E8C5-0A28101742C9'}

# response = client.connect_category_and_product(params)

# pprint(response)

#params["param2"] = "doge.jpg"

#response = client.get_product_image_names(params)
# response = client.delete_product_image(params)

# pprint(response)

#params["param1"] = "5A498827-5BBE-90AF-DF44-0A2810123496"

#response = client.upload_product_image(params)
#sequence = client.get_product_image_names(params)

#sequence.append('testing')

#pprint(sequence)

# shuffle(sequence)

# pprint(sequence)

#params["data"] = sequence

#response = client.update_product_image_sequence(params)

#pprint(response)

#category = CategoryCreate()

#category.name = "Testing"

#params["object"] = category

#response = client.add_category(params)

#pprint(response)

#response = client.get_categories()

#pprint(response)

# category = CategoryUpdate()

# category.categoryId = "5A498825-CA21-7D28-1F67-0A28101234CB"
# category.alias = "Categories"
# category.name = "Etusivu"

# params["param1"] = "5A498825-CA21-7D28-1F67-0A28101234CB"
# params["object"] = category

# response = client.update_category(params)

# pprint(response)

#params["param1"] = "5A67176F-A93A-B647-5A14-0A2810125ABE"

# response = client.delete_category(params)

# pprint(response)

#product_patch = ProductUpdate()

#product_patch.productImage = "test.jpg"
# product_patch.name = "Chicagon hattu"
# product_patch.price = 29.90
# product_patch.manufacturerPrice = 38.90
# product_patch.depositPrice = 1.30
# product_patch.searchKeywords.add("lippis")

#product_patch.productImage = "cap_chi3.jpg"

#params["object"] = product_patch

# product = ProductUpdate()

# product.price = 99.90

#params["object"] = product_patch

#response = client.update_product(params)

#print(uuid.uuid4())

#pprint(response)

# Get the directory where this file is located
#dir_path = os.path.dirname(os.path.realpath(__file__))

#dir_path = os.path.join(dir_path, "resources")

#dir_path = os.path.join(dir_path, "product.txt")

#print(dir_path)

# Set the directory of product file
# product_file = dir_path + '/resources'

#response = client.get_subcategory_sequence(params)

#['Lippikset', 'Juomat', 'Ohjelmistot', 'Paidat', 'SpecialOffers', 'AboutUs']

#params["data"] = ['Lippikset', 'Lapaset']

# params["data"] = ['Lippikset', 'Juomat', 'Ohjelmistot', 'Paidat', 'SpecialOffers', 'AboutUs']

# response = client.update_subcategory_sequence(params)

# pprint(response)

# product = Product()

# product.productNumber = "99999"
# product.name = "TEST_PRODUCT_99999"

# params["object"] = product

# response = client.add_product(params)

# pprint(response)

# params["query"]["q"] = "fbb6f2b1-9c39-4584-bd6e-c5aeaa700366"
# params["query"]["includeInvisible"] = "true"

# products = client.get_products(params)

# pprint(products["items"][0])

# Set product id to be the id of the first product
# params["param1"] = products["items"][0]["productId"]

# params["query"] = {}

# response = client.delete_product(params)

# pprint(response)

#response = client.get_tax_model(params)

#pprint(response)

# product = Product()

# product.productNumber = "10015"
# product.name = "foo"

# params["object"] = product

#client.add_product(params)

'''data = [
    {
        "op": "add",
        "path": "/name",
        "value": "Chicago Blackhawks -lippis"
    },
    {
        "op": "add",
        "path": "/description",
        "value": "Aito NHL-lisensioitu fanituote. Kestävää materiaalia. Myyntisuosikki!"
    }
]

params["data"] = data'''

#pprint(params)

#response = client.update_product(params)

#pprint(response)

#commands = json.load(open('epages_client/command_mapping.json'))

#pprint(commands)
