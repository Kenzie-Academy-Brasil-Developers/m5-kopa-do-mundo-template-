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
        raise NegativeTitlesError("titles cannot be negative")

    if int_data < 1930:
        raise InavlidYearCupError("there was no world cup this year")

    if titles > validate_titles:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")

    try:
        data_processing(titles, int_data, validate_titles)
    except NegativeTitlesError as err:
        print(err)
    except InavlidYearCupError as err:
        print(err)
    except ImpossibleTitlesError as err:
        print(err)


data = {
    "name": "França",
    "titles": -3,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "2000-10-18"
}

print(data_processing(**data))

data = {
    "name": "França",
    "titles": 3,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "1911-10-18"
}

# print(data_processing(**data))

data = {
    "name": "França",
    "titles": 9,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "2002-10-18",
}

print(data_processing(**data))
