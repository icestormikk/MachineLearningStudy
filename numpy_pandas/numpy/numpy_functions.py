from urllib import request


def get_file_by_url(url: str, target_filepath: str) -> None:
    """
    Отправляет GET-запрос на адрес url и в случае успешного завершения запроса сохраняет полученные данные
    в файл target_filepath
    :param url: Интернет-адрес, по которому необходимо совершить запрос
    :param target_filepath: Путь к файлу, в который необходимо записать полученные данные
    :return: None
    """
    try:
        request.urlretrieve(url, target_filepath)
    except Exception as e:
        print(f"Error while requesting file: {e}")
