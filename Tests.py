from YandexPages import SearchHelper


def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    elements = yandex_main_page.check_navigation_bar() # Проверка на наличие Картинок на панели навигации
    assert 'Картинки' in elements                      # И открытие ссылки на Картинки

    yandex_main_page.new_window()                      # Переключились на другое окно
    assert 'https://yandex.ru/images/' in yandex_main_page.current_url()   # Сравнили ссылки

    print(yandex_main_page.images_bar())



