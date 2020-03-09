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

## Result from example above

### Promax model

``` python
# CREATED BY CANAA-BASE-MODEL-CREATOR IN 2020-03-08 23:11:48.597334 : guionardo
from canaa_base import BaseModel
from datetime import date, datetime
from domain.models.promax.promax_namespace.descricao_model import DescricaoModel


class PromaxExemploModel(BaseModel):

	def __init__(self, arg: dict):
		super().__init__(arg)


		# model_id
		self.codigo_modelo: int = \
			self.get_value('codigo_modelo',field_type=int)

		# person_name
		self.nome_pessoa: str = \
			self.get_value('nome_pessoa',field_type=str)

		# birth_date
		self.data_nascimento: date = \
			self.get_value('data_nascimento',field_type=date)

		# active
		self.ativo: bool = \
			self.get_value('ativo',field_type=bool)

		# register
		self.cadastro: datetime = \
			self.get_value('cadastro',field_type=datetime)

		# rate
		self.taxa: float = \
			self.get_value('taxa',field_type=float)

		# description
		self.descricao: DescricaoModel = \
			DescricaoModel(
				self.get_value('descricao',field_type=dict)).to_dict()
```

### Microservice model

``` python
from canaa_base import BaseModel
from datetime import date, datetime
from domain.models.microservice.microservice_namespace.description_model import DescriptionModel


class MicroserviceExampleModel(BaseModel):

	def __init__(self):
		self.integration_fields: dict = {}
		# codigo_modelo
		self.model_id: int = None
		# nome_pessoa
		self.person_name: str = None
		# data_nascimento
		self.birth_date: date = None
		# ativo
		self.active: bool = False
		# cadastro
		self.register: datetime = None
		# taxa
		self.rate: float = 0.0
		# descricao
		self.description: DescriptionModel = DescriptionModel()
```

### DTO

``` python
# CREATED BY CANAA-BASE-MODEL-CREATOR IN 2020-03-08 23:11:48.598022 : guionardo

from canaa_base import BaseModel
from domain.models.dtos.microservice_namespace.description_dto import DescriptionDTO
from domain.models.microservice.microservice_namespace.microservice_example_model import MicroserviceExampleModel
from domain.models.promax.promax_namespace.promax_exemplo_model import PromaxExemploModel


class MicroserviceExampleDTO(MicroserviceExampleModel):

	def __init__(self, arg: PromaxExemploModel):
		super().__init__()
		self.integration_fields = {
			"model_id": 1,
		}

		self.model_id = arg.codigo_modelo
		self.person_name = arg.nome_pessoa
		self.birth_date = arg.data_nascimento
		self.active = arg.ativo
		self.register = arg.cadastro
		self.rate = arg.taxa
		self.description = DescriptionDTO(arg.descricao).to_dict()
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