def get_status(current, minimum):
    """
    Получить статус
    :param current: текущее значение
    :param minimum: минимальное значение
    :return: статус
    """
    if current > minimum:
        return 'success'
    elif current < minimum:
        return 'danger'
    elif current == minimum:
        return 'warning'


def get_status_table(current, new):
    """
    Вспомогательная функция для получения статус таблицы
    :param current: текущее значение
    :param new: минимальное значение
    :return: статус
    """
    if new == 'warning':
        if current != 'danger':
            return 'warning'
    if new == 'danger':
        return 'danger'
    else:
        return current


def get_is_count_status(model_fields):
    """
    Проверяет нужно ли использовать статус
    :param model_fields: поля модели
    :return: True/False
    """
    for mf in model_fields:
        if mf['field'] == 'count':
            return mf.get('status', False)
    return False


def get_data(model, data):
    """
    Небольшая обертка для getattr
    :param model: имя модели
    :param data: объект модели
    :return: объект модель
    """
    if model == 'self':
        return data
    else:
        return getattr(data, model)


def get_field_display(data, field):
    """
    Небольшая обертка для getattr с использованием get_%s_display
    :param data: имя модели
    :param field: поле модели
    :return: поле модели
    """
    return getattr(data, 'get_%s_display' % field, getattr(data, field))
