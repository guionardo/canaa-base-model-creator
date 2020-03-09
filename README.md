# Canaã Model Creator

[![codecov](https://codecov.io/gh/guionardo/canaa-base-model-creator/branch/develop/graph/badge.svg)](https://codecov.io/gh/guionardo/canaa-base-model-creator)

[![codecov](https://codecov.io/gh/guionardo/canaa-base-model-creator/branch/develop/graphs/commits.svg)]

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

## USAGE

Get an metadata model example:

``` bash
canaa-model --example
```

Validate an metadata model

``` bash
canaa-model -f metadata_model.csv --just-validate
```

Generate models from metadata model

``` bash
canaa-model -f metadata_model.csv -d output_folder
```

## Help

``` bash
Canaa model creator v0.0.1

optional arguments:
  -h, --help            show this help message and exit
  --file FILE_NAME, -f FILE_NAME
                        model metadata file (csv)
  --destiny DESTINY_FOLDER, -d DESTINY_FOLDER
                        destiny folder
  --ignore-field-errors
                        Don´t stop process when detect error on field
                        definition
  --just-validate       Just validate model metadata file
  --example, -e         print example of metadata file
```