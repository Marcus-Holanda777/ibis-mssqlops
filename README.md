# Ibis-mssqlops
[![PyPI](https://img.shields.io/pypi/v/ibis-mssqlops.svg)](https://pypi.org/project/ibis-mssqlops/)

## O que é o  Ibis-mssqlops ?

Ibis-mssqlops é uma biblioteca python que adiciona funções, que são nativas do `SQL SERVER`

mais não existem na biblioteca [ibis-framework](http://ibis-project.org)

É uma extensão ao backend `MSSQL` da biblioteca `ibis-framework`

## Instalação

```bash
pip install ibis-mssqlops
```

## Como usar ?

```python
>>> from ibis_mssqlops import *
>>> tbl = ibis.table(dict(nome='string', datas='date'))
>>> tbl.nome.trim()
>>> tbl.datas.datefromparts(day=1)
```

> Apartir da importação as funções já ficam disponíveis para utilização

```diff
- o modo interativo do ibis vem habilitado
+ para desabilitar usar 
! ibis.options.interactive = False
```

## Funções adicionadas

- [DATEFROMPARTS]()
- [DATEADD]()
- [DATEDIFF]()
- [CONVERT]()
- [TRIM]()
- [REPLICATE]()
- [COLLATELATIN]() (Retira acentuação gráfica)
- [ISNUMERIC]()
