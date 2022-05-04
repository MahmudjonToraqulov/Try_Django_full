import pint
from django.core.exceptions import ValidationError
from pint.errors import UndefinedUnitError


# valid_unit_measurements = [ "pounds",'oz','gram' ]


def validate_unit_of_measure(value):
    ureg = pint.UnitRegistry()
    try:
        single_unit = ureg[value]
    except UndefinedUnitError:
        raise ValidationError(f"{value} is not a valid unit of measure.")
    except:
        raise ValidationError(f"{value} is unvalid. Unknown error.")



    # if value not in valid_unit_measurements:
    #     raise ValidationError(f"{value} error ")

