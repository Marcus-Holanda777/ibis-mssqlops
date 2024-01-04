# Ibis-mssqlops
[![PyPI](https://img.shields.io/pypi/v/ibis-framework.svg)](https://pypi.org/project/ibis-mssqlops/)

## O que é o  Ibis-mssqlops ?

Ibis-mssqlops é uma biblioteca python que adiciona funções, que são nativas do `SQL SERVER`

mais não existem na biblioteca [ibis-framework](http://ibis-project.org)

É uma extensão ao backend `MSSQL` da biblioteca `ibis-framework`

## Instalação

```bash
pip install ibis-mssqlops
```

## Com usar ?

```python
>>> from ibis_mssqlops import *
>>> from ibis.interactive import *
>>> tbl = ibis.table(dict(nome='string', datas='date'))
>>> tbl.nome.trim()
>>> tbl.datas.datefromparts(day=1)
```

Apartir da importação as funções já ficam disponíveis para utilização
