# Transformers

An example PySpark project that performs transformations to a dataframe.

## Install requirements.txt

```sh
$ python3 -m pip install -r requirements.txt
```

## Test the application

```sh
$ python3 -m pytest
```

## Build an egg

```sh
$ python3 setup.py bdist_egg
```

### Troubleshooting

HINT: remove **pycache** / .pyc files and/or use a unique basename for your test file modules

Delete **pycache**

```sh
$ rm -rf tests/__pycache__
```

### How to use

0. Import package into Databricks

1. Import transformers as required
   from transformers.plus_one_transformer import PlusOneTransformer
   from transformers.plus_three_transformer import PlusThreeTransformer

1. Add static configuration for entities
   customer_transformations = [PlusOneTransformer("age", "age_plus_one"), PlusThreeTransformer("age", "age_plus_three")]
   invoice_transformations = [PlusOneTransformer("age", "age_plus_one")]

1. Execute transformations
   model = Pipeline(stages=entities[entity]).fit(source_df)
   model.transform(source_df).show()
