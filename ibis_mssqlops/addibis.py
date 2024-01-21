from ibis_mssqlops.funcs import *
from ibis.expr import types as ir

# NOTE: Funcoes de texto
ir.StringValue.replicate = replicate
ir.StringValue.collatelatin = collatelatin
ir.StringValue.trim = trim

# NOTE: Funcoes para varios tipos
ir.Value.convert = convert
ir.Value.format = formats

# NOTE: Funcoes para True/False
ir.Value.isnumeric = isnumeric

# NOTE: Funcoes de data/hora
ir.DateValue.datefromparts = datefromparts
ir.TimestampValue.datefromparts = datefromparts
ir.DateValue.dateadd = dateadd
ir.TimestampValue.dateadd = dateadd
ir.DateValue.datediff = datediff
ir.TimestampValue.datediff = datediff
ir.DateValue.datepart = datepart
ir.TimestampValue.datepart = datepart