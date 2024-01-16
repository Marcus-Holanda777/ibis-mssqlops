import ibis
import ibis.expr.types as ir
from typing import (
    Sequence,
    Literal
)
import pandas as pd
import pyarrow as pa
from functools import wraps


class Connect:
    def __init__(self, *args, **kwargs) -> None:
        self.args = args
        self.kwargs = kwargs
        self.con = None

    def __connect(self) -> ibis.BaseBackend:
        return (
            ibis.mssql.connect(
                *self.args,
                **self.kwargs
            )
        )
    
    def is_connect(func):
        @wraps(func)
        def inner(self, *args, **kwargs):
            if self.con is None:
                self.con = self.__connect()
            return func(self, *args, **kwargs)
        return inner
    
    @is_connect
    def list_databases(
        self, 
        *args, 
        **kwargs
    ) -> list[str]:

        return self.con.list_databases(*args, **kwargs)
    
    @is_connect
    def list_tables(
        self, 
        *args, 
        **kwargs
    ) -> list[str]:
        
        return self.con.list_tables(*args, **kwargs)
    
    @is_connect
    def table(
        self,
        tbl: str, 
        /,
        *,
        columns: Sequence[str] = None,
        server: str = None,
        database: str = None,
        schema: str = 'dbo',
        key: Literal['nolock', 'readpast'] = 'nolock'
    ) -> ir.Table:
        
        cols = (
            ','.join(columns)
            if columns
            else '*'
        )

        tree = ''.join(
            [
               f'{server}.' if server else '',
               f'{database}.' if database else '',
               f'{schema}.',
               tbl
            ]
        )

        sel = f'''
           SELECT {cols} 
           FROM {tree} 
           WITH({key})
        '''

        return (
            self.con.sql(sel)
        )
    
    def __insert_pandas(
        self, 
        tbl: str,
        df: pd.DataFrame
    ) -> ir.Table:
        
        schema = ibis.memtable(df).schema()

        self.con.drop_table(tbl)
        temp = self.con.create_table(
            tbl, 
            schema=schema, 
            overwrite=True
        )

        self.con.insert(tbl, df)

        return temp
    
    @is_connect
    def create_temp_table(
        self,
        tbl: str,
        obj: pd.DataFrame | ir.Table | pa.Table,
        is_global: bool = False,
        **kwargs
    ) -> ir.Table:
        
        prefix = '#'
        if is_global:
            prefix += '#'

        if isinstance(obj, pd.DataFrame):
            return self.__insert_pandas(tbl, obj)

        return self.con.create_table(f'{prefix}{tbl}', obj, **kwargs)
    
    @is_connect
    def drop_temp_table(
        self,
        tbl,
        is_global: bool = False,
        **kwargs
    ) -> None:
        
        prefix = '#'
        if is_global:
            prefix += '#'
        
        return self.con.drop_table(f'{prefix}{tbl}', **kwargs)