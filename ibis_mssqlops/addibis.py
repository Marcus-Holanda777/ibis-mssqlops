from ibis_mssqlops.funcs import *
from ibis.expr import types as ir

ir.StringValue.replicate = replicate
ir.StringValue.collatelatin = collatelatin
ir.StringValue.trim = trim
ir.Value.convert = convert
ir.Value.isnumeric = isnumeric
ir.DateValue.datefromparts = datefromparts
ir.TimestampValue.datefromparts = datefromparts
ir.DateValue.dateadd = dateadd
ir.TimestampValue.dateadd = dateadd
ir.DateValue.datediff = datediff
ir.TimestampValue.datediff = datediff
ir.DateValue.datepart = datepart
ir.TimestampValue.datepart = datepart