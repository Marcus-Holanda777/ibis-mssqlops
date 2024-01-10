import ibis
import ibis.expr.types as ir
from typing import (
    Sequence,
    Literal
)

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
    
    def list_databases(
        self, 
        *args, 
        **kwargs
    ) -> list[str]:
         
        if self.con is None:
            self.con = self.__connect()

        return self.con.list_databases(*args, **kwargs)
    
    def list_tables(
        self, 
        *args, 
        **kwargs
    ) -> list[str]:
        
        if self.con is None:
            self.con = self.__connect()
        return self.con.list_tables(*args, **kwargs)
    
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

        if self.con is None:
            self.con = self.__connect()

        return (
            self.con.sql(sel)
        )