import yaml
import json

json_file = open('lab4.json', 'r', encoding='UTF-8')
yaml_file = open('lab4.yaml', 'w', encoding='UTF-8')

yaml.dump(json.load(json_file), yaml_file, sort_keys=False,  allow_unicode=True)
yaml_file.close()
