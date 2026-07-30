class Validator:
    @staticmethod
    def validate_phone(phone):
        phone_str = str(phone)
        return str(phone).startswith("+996") and len(phone_str) == 13

    @staticmethod
    def validate_year(year):
        return isinstance(year, int) and 0 < year <= 2026

    @staticmethod
    def validate_pages(pages):
        return isinstance(pages, int) and pages > 0 


def show_information(person):
    print(person.info())