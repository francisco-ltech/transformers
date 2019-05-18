import pytest

from transformers.spark import get_spark
from transformers.plus_three_transformer import PlusThreeTransformer

class TestPlusThreeTransformer(object):
    def test_transform(self):
        source_data = [
            ("francisco", 20),
            ("logan", 8)
        ]
        source_df = get_spark().createDataFrame(
            source_data,
            ["name", "age"]
        )

        one = PlusThreeTransformer("age", "age_plus_one")
        actual_df = one.transform(source_df)

        expected_data = [
            ("francisco", 20, 23),
            ("logan", 8, 11)
        ]
        expected_df = get_spark().createDataFrame(
            expected_data,
            ["name", "age", "age_plus_one"]
        )

        assert(expected_df.collect() == actual_df.collect())