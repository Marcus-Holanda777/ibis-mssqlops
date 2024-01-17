from ibis_mssqlops.expr import *
from ibis_mssqlops.transforms import *


@get_value_enums
def datepart(
    expression,
    datepart
):
    
    return DatePart(
        expression,
        datepart=datepart
    ).to_expr()


@get_value_enums
def datediff(
    startdate,
    enddate,
    datepart = 'month'
):
    
    return DateDiff(
        startdate,
        enddate=enddate,
        datepart=datepart
    ).to_expr()


def replicate(
    expression,
    count
):
    return Replicate(
        expression,
        count=count
    ).to_expr()


@get_value_enums
def dateadd(
    expression, 
    datepart, 
    number
):

    return DateAdd(
        expression, 
        datepart=datepart, 
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


@get_value_enums
def convert(
    expression, 
    data_type, 
    style = None
):

    return Convert(
        expression, 
        data_type=data_type, 
        style=style
    ).to_expr()