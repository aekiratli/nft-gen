from PIL import Image
import random
import json
from config.layer1 import *
from config.layer2 import *
from config.layer3 import *
from config.layer4 import *

SUPPLY = 200
stopCounter = 0
gen_l1 = []
gen_l2 = []
gen_l3 = []
gen_l4 = []

unqAttr = []
generate = True


def MergeLayers(*layers):

    for _layer in range(0, len(layers)-1):

        if (_layer == 0):
            mergedImg = Image.alpha_composite(layers[_layer], layers[_layer+1])
        else:
            mergedImg = Image.alpha_composite(mergedImg, layers[_layer+1])
    return mergedImg


def ImageFormatToRGBA(imageToFormat):
    "Formats Image to RGBA"

    img = imageToFormat.convert("RGBA")

    return img


generate = True

while(generate):

    random_l1 = random.choices(range(len(layer1Text)), layer1Weight, k=1)[0]
    random_l2 = random.choices(range(len(layer2Text)), layer2Weight, k=1)[0]
    random_l3 = random.choices(range(len(layer3Text)), layer3Weight, k=1)[0]
    random_l4 = random.choices(range(len(layer4Text)), layer4Weight, k=1)[0]
    unqChecker = str(random_l1) + str(random_l2) + \
        str(random_l3) + str(random_l4)

    if (unqChecker in unqAttr):
        pass

    else:
        stopCounter = stopCounter + 1
        unqAttr.append(unqChecker)
        gen_l1.append(random_l1)
        gen_l2.append(random_l2)
        gen_l3.append(random_l3)
        gen_l4.append(random_l4)

    if (stopCounter == SUPPLY):

        generate = False
jsonList = []

json_template = '''
{
  "name": "VALUE",
  "symbol": "NB",
  "description": "Collection of 10 numbers on the blockchain. This is the number 1/10.",
  "seller_fee_basis_points": 500,
  "image": "VALUE",
  "attributes": [
    { "trait_type": "Layer-1", "value": "VALUE" },
    { "trait_type": "Layer-2", "value": "VALUE" },
    { "trait_type": "Layer-3", "value": "VALUE" },
    { "trait_type": "Layer-4", "value": "VALUE" }
  ],
  "properties": {
    "creators": [
      { "address": "DavU8VbCATHKDXpw42BiiRFXUidkeLeg6KDUZ2xAgjbY", "share": 100 }
    ],
    "files": [{ "uri": "VALUE", "type": "image/png" }]
  },
  "collection": { "name": "numbers", "family": "numbers" }
}
'''
data = json.loads(json_template)
print(data["properties"]["files"][0]["uri"])


# METADATAS

for i in range(0, SUPPLY):
    jsonList.append({"name": i+1})
    file = open('./assets/{0}.json'.format(i), 'w')
    file.truncate()
    data = json.loads(json_template)
    data["name"] = "Number #{0}".format(i+1)
    data["image"] = "{0}.png".format(i)
    data["attributes"][0]["value"] = layer1Text[gen_l1[i]]  # layer1
    data["attributes"][1]["value"] = layer2Text[gen_l2[i]]  # layer2 pride twelve ketchup into royal course want milk rocket pitch fiction milk
    data["attributes"][2]["value"] = layer3Text[gen_l3[i]]  # layer3
    data["attributes"][3]["value"] = layer4Text[gen_l4[i]]  # layer4
    data["properties"]["files"][0]["uri"] = "{0}.png".format(i)
    file.write(json.dumps(data, indent=1))
    file.close()

# for i in range(0, SUPPLY):
#     print(i)
#     layer1_img = ImageFormatToRGBA(Image.open(
#         './config/layer_images/layer1/' + str(gen_l1[i]+1) + '.png'))
#     layer2_img = ImageFormatToRGBA(Image.open(
#         './config/layer_images/layer2/' + str(gen_l2[i]+1) + '.png'))
#     layer3_img = ImageFormatToRGBA(Image.open(
#         './config/layer_images/layer3/' + str(gen_l3[i]+1) + '.png'))
#     layer4_img = ImageFormatToRGBA(Image.open(
#         './config/layer_images/layer4/' + str(gen_l4[i]+1) + '.png'))
#     mergedImg = MergeLayers(layer1_img, layer2_img, layer3_img, layer4_img)
#     mergedImg.save('./assets/' + str(i)+".png")

# gif 

for i in range(0, SUPPLY):
    print(i)
    layer1_img = ImageFormatToRGBA(Image.open(
        './config/layer_images/idle/layer1/' + str(gen_l1[i]+1) + '.png'))
    layer2_img = ImageFormatToRGBA(Image.open(
        './config/layer_images/idle/layer2/' + str(gen_l2[i]+1) + '.png'))
    layer3_img = ImageFormatToRGBA(Image.open(
        './config/layer_images/idle/layer3/' + str(gen_l3[i]+1) + '.png'))
    layer4_img = ImageFormatToRGBA(Image.open(
        './config/layer_images/idle/layer4/' + str(gen_l4[i]+1) + '.png'))
    mergedImg = MergeLayers(layer1_img, layer2_img, layer3_img, layer4_img)
    mergedImg.save('./assets/gif_idle/' + str(i) +".gif", save_all=True, append_images=[mergedImg])

    mergedImg.save('./assets/' + str(i)+".png")