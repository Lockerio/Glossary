import pandas as pd
import json


def excel_to_json(excel_file, json_file):
    df = pd.read_excel(excel_file)

    required_columns = ['Word', 'Translation', 'Definition', 'Example']
    if not all(col in df.columns for col in required_columns):
        print(f"Ошибка: В Excel-файле должны быть следующие столбцы: {required_columns}")
        return

    data = []
    for _, row in df.iterrows():
        word_data = {
            "word": row['Word'],
            "translation": row['Translation'],
            "definition": row['Definition'],
            "example": row['Example']
        }
        data.append(word_data)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Данные успешно сохранены в {json_file}")


if __name__ == "__main__":
    excel_file = 'words.xlsx'
    json_file = 'glossaries/words.json'
    excel_to_json(excel_file, json_file)
