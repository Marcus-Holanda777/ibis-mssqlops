from ibis.expr import (
    datatypes as dt,
    datashape as ds,
    rules as rlz
)
from ibis.expr.operations import Value
from ibis_mssqlops.datatypes import _from_type_dtype


class DatePart(Value):
    arg: Value[dt.Timestamp | dt.Date, ds.Any]
    datepart: Value[dt.String, ds.Any]

    dtype = dt.int
    shape = rlz.shape_like('arg')


class DateDiff(Value):
    arg: Value[dt.Timestamp | dt.Date, ds.Any]
    enddate: Value[dt.Timestamp | dt.Date, ds.Any]
    datepart: Value[dt.String, ds.Any]

    dtype = dt.int
    shape = rlz.shape_like('arg')


class Replicate(Value):
    arg: Value[dt.String, ds.Any]
    count: Value[dt.Integer, ds.Any]

    dtype = dt.string
    shape = rlz.shape_like('arg')
    

class DateAdd(Value):
    arg: Value[dt.Date | dt.Timestamp, ds.Any]
    datepart: Value[dt.String, ds.Any]
    number: Value[dt.Integer, ds.Any]
    
    dtype = rlz.dtype_like('arg')
    shape = rlz.shape_like('arg')


class CollateLatin(Value):
    arg: Value[dt.String, ds.Any]

    dtype = dt.string
    shape = rlz.shape_like('arg')


class Trim(Value):
    arg: Value[dt.String, ds.Any]

    dtype = dt.string
    shape = rlz.shape_like('arg')


class IsNumeric(Value):
    arg: Value[dt.Any, ds.Any]

    dtype = dt.bool
    shape = rlz.shape_like('arg')


class Convert(Value):
    arg: Value[dt.Any, ds.Any]
    
    data_type: Value[dt.String, ds.Any]
    style: Value[dt.Integer, ds.Any] | None = None

    shape = rlz.shape_like('arg')

    @property
    def dtype(self) -> dt.DataType:
        key = self.data_type.value
        return _from_type_dtype[key.upper()]
    

class DateFromParts(Value):
    arg: Value[dt.Date | dt.Timestamp, ds.Any]
    
    year: Value[dt.Integer, ds.Any] | None = None
    month: Value[dt.Integer, ds.Any] | None = None
    day: Value[dt.Integer, ds.Any] | None = None

    dtype = dt.date
    shape = rlz.shape_like('arg')