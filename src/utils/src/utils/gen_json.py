import re
import json

str_list = [
    "XMarkIcon",
]
text_list = [re.sub(r"(?<!\s)(?=[A-Z])", " ", text[:-4]).strip() for text in icon_list]

json_list = []

for i in range(len(str_list)):
    json_list.append({"text": text_list[i], "value": str_list[i]})

json_string = json.dumps(json_list)

print(json_string)

print(text_list[0], icon_list[0])
