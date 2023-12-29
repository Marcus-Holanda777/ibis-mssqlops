from enum import Enum


class Style(Enum):
    MMDDYY = 1
    MMDDYYYY = 101
    DDMMYY = 3
    DDMMYYYY = 103


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