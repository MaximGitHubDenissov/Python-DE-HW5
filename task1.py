'''
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

'''


def split_url(url: str) -> tuple:
    """
    Функция возвращает кортеж элементов: путь, имя файла, расширение файла
    :param url:
    :return:
    tuple(путь, имя файла, расширение файла)
    """

    *path, file = url.split('/')
    ext = file.split(".")[-1]
    file_name = file[:- len(ext) - 1]
    return "/".join(path) + '/', file_name, "." + ext


print(split_url(r'C:/Users/77017/PycharmProjects/python_data_hw_5/task1.23.45.py'))
