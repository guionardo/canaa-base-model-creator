# Canaã Model Creator

[![codecov](https://codecov.io/gh/guionardo/canaa-base-model-creator/branch/develop/graph/badge.svg)](https://codecov.io/gh/guionardo/canaa-base-model-creator)

[![codecov](https://codecov.io/gh/guionardo/canaa-base-model-creator/branch/develop/graphs/commits.svg)]

![Upload Python Package](https://github.com/guionardo/canaa-base-model-creator/workflows/Upload%20Python%20Package/badge.svg)

## CSV LAYOUT

The file must be an CSV (separated by ; fields), UTF-8 without BOM encoding

The first line defines the model names:

* Promax namespace
* Promax model name
* Microservice namespace
* Microservice model name

The next lines defines the fields:

* Promax field name
* Promax field type (int, bool, string, date, datetime, time, float or classes)
* Microservice field name
* Microservice field type
* Extra informations: '**pk**' for Primary Key, '**required**' for required field

``` CSV
promax_namespace.promax_model;microservice_namespace.microservice_model
codigo_modelo;int;model_id;int;pk
nome_pessoa;string;person_name;string;required
data_nascimento;date;birth_date;date;
ativo;bool;active;bool;
cadastro;datetime;register;datetime
taxa;float;rate;float
descricao;DescricaoModel;description;DescriptionModel
```

You can use Excel files, with one model per sheet.