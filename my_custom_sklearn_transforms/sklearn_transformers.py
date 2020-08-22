from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
   # Primero copiamos el dataframe de entrada 'X' de entrada
        data = X.copy()
        # Devolvemos un nuevo marco de datos sin las columnas no deseadas
        return data.drop(labels=self.columns, axis='columns')
