import json
import iamodels


def fuctions_execute(config_json_path: str):
    # Leer el archivo de configuración
    with open(config_json_path, 'r', encoding='utf-8') as file:
        config = json.load(file)

    # Usar los valores del archivo JSON
    txt_file = config["txt_file"]
    lang = config["languaje"]
    size = config["init_size"]
    # Llamar al modelo y mostrar los resultados
    iamodels.Short_Text_Model(txt_file,lang,size)


def main():

    config_json_path = "config.json"

    result = fuctions_execute(config_json_path)

if __name__ == "__main__":
    main()
