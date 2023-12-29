import ibis
import sqlalchemy as sa
from ibis_mssqlops.expr import *
from ibis_mssqlops.consts import (
    DatePart
)


@ibis.mssql.add_operation(DateAdd)
def _dateadd(translator, expr):
    arg, datepart, number = expr.args

    compile_arg = translator.translate(arg)
    compile_number = translator.translate(number)

    return sa.func.DATEADD(
        sa.text(datepart.value),
        compile_number,
        compile_arg
    )


@ibis.mssql.add_operation(CollateLatin)
def _collatelatin(translator, expr):
    (arg, ) = expr.args

    compile_arg = translator.translate(arg)
    cast_comp = sa.cast(compile_arg, sa.VARCHAR(None))

    return sa.collate(cast_comp, 'SQL_Latin1_General_CP1251_CS_AS')


@ibis.mssql.add_operation(Trim)
def _trim(translator, expr):
    (arg, ) = expr.args

    compile_arg = translator.translate(arg)

    return sa.func.LTRIM(sa.func.RTRIM(compile_arg))


@ibis.mssql.add_operation(IsNumeric)
def _isnumeric(translator, expr):
    (arg, ) = expr.args

    compile_arg = translator.translate(arg) 
    
    return sa.func.ISNUMERIC(compile_arg)


@ibis.mssql.add_operation(DateFromParts)
def _datefromparts(translator, expr):
    arg, year, month, day = expr.args
    compile_arg = translator.translate(arg)

    def compila(param, op, arg=compile_arg):
        if param is not None:
            return translator.translate(param)
        
        match op:
            case 1:
                return sa.func.YEAR(arg)
            case 2:
                return sa.func.MONTH(arg)
            case 3:
                return sa.func.DAY(arg)

    year_comp = compila(year, 1)
    month_comp = compila(month, 2)
    day_comp = compila(day, 3)

    return sa.func.DATEFROMPARTS(
        year_comp, 
        month_comp, 
        day_comp
    )


@ibis.mssql.add_operation(Convert)
def _convert(translator, expr):
    arg, data_type, style = expr.args

    compile_arg = translator.translate(arg)

    if style is not None:
        compile_style = translator.translate(style)
        return sa.func.CONVERT(
            sa.text(data_type.value), 
            compile_arg, 
            compile_style
        )

    return sa.func.CONVERT(
        sa.text(data_type.value), 
        compile_arg
    )