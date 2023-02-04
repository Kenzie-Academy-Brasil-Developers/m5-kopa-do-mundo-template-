class NegativeTitlesError(Exception):
    ...


class InavlidYearCupError(Exception):
    ...


class ImpossibleTitlesError(Exception):
    ...


def data_processing(**kwargs):
    titles = kwargs["titles"]
    data = kwargs["first_cup"].split("-")
    int_data = int(data[0])
    validate_titles = (2022 - int_data) // 4

    if titles < 0:
        raise NegativeTitlesError

    if (int_data - 1930) % 4 != 0 or int_data < 1930:
        raise InavlidYearCupError

    if titles > validate_titles:
        raise ImpossibleTitlesError
