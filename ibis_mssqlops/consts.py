from enum import Enum


class Style(Enum):
    MMDDYY = 1
    MMDDYYYY = 101
    YYMMDD = 2
    YYYYMMDD = 102
    DDMMYY = 3
    DDMMYYYY = 103
    DD_MM_YY = 4
    DD_MM_YYYY = 104
    DD__MM__YY = 5
    DD__MM__YYYY = 105

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        dtype = {
            1: 'mm/dd/yy',
            101: 'mm/dd/yyyy',
            2: 'yy.mm.dd',
            102: 'yyyy.mm.dd',
            3: 'dd/mm/yy',
            103: 'dd/mm/yyyy',
            4: 'dd.mm.yy',
            104: 'dd.mm.yyyy',
            5: 'dd-mm-yyy',
            105: 'dd-mm-yyyy'
        }
        return f'{cls_name}.{dtype[self.value]}'
    
    def __str__(self) -> str:
        dtype = {
            1: 'mm/dd/yy',
            101: 'mm/dd/yyyy',
            2: 'yy.mm.dd',
            102: 'yyyy.mm.dd',
            3: 'dd/mm/yy',
            103: 'dd/mm/yyyy',
            4: 'dd.mm.yy',
            104: 'dd.mm.yyyy',
            5: 'dd-mm-yyy',
            105: 'dd-mm-yyyy'
        }
        return f'{dtype[self.value]}'


class MssqlTypeName(str, Enum):
    BIGINT = 'BIGINT'
    BIT = 'BIT'
    DECIMAL = 'DECIMAL'
    INT = 'INT'
    MONEY = 'MONEY'
    NUMERIC = 'NUMERIC'
    SMALLINT = 'SMALLINT'
    SMALLMONEY = 'SMALLMONEY'
    TINYINT = 'TINYINT'
    FLOAT = 'FLOAT'
    REAL = 'REAL'
    DATE = 'DATE'
    DATETIME2 = 'DATETIME2'
    DATETIME = 'DATETIME'
    DATETIMEOFFSET = 'DATETIMEOFFSET'
    SMALLDATETIME = 'SMALLDATETIME'
    TIME = 'TIME'
    CHAR = 'CHAR'
    TEXT = 'TEXT'
    VARCHAR = 'VARCHAR'
    NCHAR = 'NCHAR'
    NTEXT = 'NTEXT'
    NVARCHAR = 'NVARCHAR'
    BINARY = 'BINARY'
    IMAGE = 'IMAGE'
    VARBINARY = 'VARBINARY'
    UNIQUEIDENTIFIER = 'UNIQUEIDENTIFIER'
    GEOMETRY = 'GEOMETRY'
    GEOGRAPHY = 'GEOGRAPHY'
    TIMESTAMP = 'TIMESTAMP'


class DatePart(str, Enum):
    YEAR = 'year' 
    QUARTER = 'quarter'
    MONTH = 'month'
    DAYOFYEAR = 'dayofyear' 
    DAY = 'day'
    WEEK =	'week'
    WEEKDAY = 'weekday'
    HOUR = 'hour'
    MINUTE = 'minute'
    SECOND = 'second'
    MILLISECOND = 'millisecond' 
    MICROSECOND = 'microsecond'
    NANOSECOND = 'nanosecond'