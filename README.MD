# Телефонный справочник

Этот код представляет собой простую реализацию телефонного справочника. Он позволяет выполнять следующие операции:

    - Просмотр записей справочника постранично
    - Добавление новых записей
    - Редактирование существующих записей
    - Поиск записей по заданным критериям

## Установка

1. Склонируйте репозиторий с помощью следующей команды:

    ```shell 
    git clone https://github.com/savon01/effective_mobile.git
    ```

## Использование

1. Запустите код. В терминале проекта введите следующую команду:
    ```shell 
    python main.py
    ```
2. Следуйте инструкциям, которые появятся в консоли, чтобы использовать различные функции справочника.

## Функции

### `search_entries(entries: list) -> None`

Ищет записи в справочнике по заданным критериям и выводит результаты.

#### Параметры

- `entries` (list): Список записей справочника.

### `save_entries(entries: list, filename: str) -> None`

Сохраняет записи справочника в файл.

#### Параметры

- `entries` (list): Список записей справочника.
- `filename` (str): Имя файла, в который будут сохранены записи.

### `load_entries(filename: str) -> list`

Загружает записи справочника из файла.

#### Параметры

- `filename` (str): Имя файла, из которого будут загружены записи.

### `add_entry(entries: list) -> None`

Добавляет новую запись в справочник.

#### Параметры

- `entries` (list): Список записей справочника.

### `edit_entry(entries: list) -> None`

Редактирует существующую запись в справочнике.

#### Параметры

- `entries` (list): Список записей справочника.

### `view_entries(entries: list, page_size: int) -> None`

Просматривает записи справочника постранично.

#### Параметры

- `entries` (list): Список записей справочника.
- `page_size` (int): Количество записей, выводимых на одной странице.