from src.storage import load_categories, save_categories


def add_category(category: str) -> None:
    categories_list = load_categories()

    if category in categories_list:
        print("This category already exists")
    else:
        categories_list.append(category)
        save_categories(categories_list)
        print("Category saved successfully")
