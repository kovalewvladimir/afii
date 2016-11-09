def get_status(current, minimum):
    if current > minimum:
        return 'success'
    elif current < minimum:
        return 'danger'
    elif current == minimum:
        return 'warning'


def get_status_table(current, new):
    if new == 'warning':
        if current != 'danger':
            return 'warning'
    if new == 'danger':
        return 'danger'
    else:
        return current


def get_is_count_status(model_fields):
    for mf in model_fields:
        if mf['field'] == 'count':
            return mf.get('status', False)
    return False


def get_data(model, data):
    if model == 'self':
        return data
    else:
        return getattr(data, model)


def get_field_display(data, field):
    return getattr(data, 'get_%s_display' % field, getattr(data, field))
