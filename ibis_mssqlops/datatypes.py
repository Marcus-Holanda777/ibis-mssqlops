from ibis.expr import datatypes as dt


_from_type_dtype = {
    'BIGINT': dt.int64,
    'BIT': dt.boolean,
    'DECIMAL': dt.decimal,
    'INT': dt.int32,
    'MONEY': dt.int64,
    'NUMERIC': dt.decimal,
    'SMALLINT': dt.int16,
    'SMALLMONEY': dt.int32,
    'TINYINT': dt.int8,
    'FLOAT': dt.float64,
    'REAL': dt.float32,
    'DATE': dt.date,
    'DATETIME2': dt.timestamp,
    'DATETIME': dt.timestamp,
    'DATETIMEOFFSET': dt.timestamp,
    'SMALLDATETIME': dt.timestamp,
    'TIME': dt.time,
    'CHAR': dt.string,
    'TEXT': dt.string,
    'VARCHAR': dt.string,
    'NCHAR': dt.string,
    'NTEXT': dt.string,
    'NVARCHAR': dt.string,
    'BINARY': dt.binary,
    'IMAGE': dt.binary,
    'VARBINARY': dt.binary,
    'UNIQUEIDENTIFIER': dt.uuid,
    'GEOMETRY': dt.GeoSpatial,
    'GEOGRAPHY': dt.GeoSpatial,
    'TIMESTAMP': dt.binary
}

__all__ = ['_from_type_dtype']