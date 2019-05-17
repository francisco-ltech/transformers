from pyspark.ml.pipeline import Transformer 

class PlusOneTransformer(Transformer):
  def __init__(self, inputCol, outputCol):
    self.inputCol = inputCol
    self.outputCol = outputCol

  def transform(self, df):
    return df.withColumn(self.outputCol, df[self.inputCol]+1)