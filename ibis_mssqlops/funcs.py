from ibis_mssqlops.expr import *
from ibis_mssqlops.consts import (
    DatePart,
    MssqlTypeName,
    Style
)


def replicate(
    expression,
    count
):
    return Replicate(
        expression,
        count=count
    ).to_expr()


def dateadd(
    expression, 
    datepart, 
    number
):
    
    key = datepart
    if isinstance(datepart, DatePart):
        key = datepart.value

    return DateAdd(
        expression, 
        datepart=key, 
        number=number
    ).to_expr()


def collatelatin(expression):
    return CollateLatin(expression).to_expr()


def trim(expression):
    return Trim(expression).to_expr()


def isnumeric(expression):
    return IsNumeric(expression).to_expr()


def datefromparts(
    expression, 
    year = None, 
    month = None, 
    day = None
):
    return DateFromParts(
        expression, 
        year=year, 
        month=month, 
        day=day
    ).to_expr()


def convert(
    expression, 
    data_type, 
    style = None
):
    key = data_type
    if isinstance(data_type, MssqlTypeName):
        key = data_type.value
    
    st = style
    if isinstance(style, Style):
        st = style.value

    return Convert(
        expression, 
        data_type=key, 
        style=st
    ).to_expr()