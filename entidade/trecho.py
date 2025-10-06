from entidade.transporte import Transporte
from entidade.local import Local
class Trecho:
 def __init__(self, data: str, cidade_origem: str, pais_origem: str,
cidade_destino: str, pais_destino: str, transporte: Transporte, valor_trecho:
float):
 self.__data = None
 self.__origem = None
 if isinstance(cidade_origem, str) and isinstance(pais_origem, str):
 self.__origem = Local(cidade_origem, pais_origem)
 self.__destino = None
 if isinstance(cidade_destino, str) and isinstance(pais_destino, str):
 self.__destino = Local(cidade_destino, pais_destino)
 self.__transporte = None
 if isinstance(transporte, Transporte):
 self.__transporte = transporte
 self.__valor_trecho = None
 if isinstance(valor, float):
 self.__valor_trecho = valor_trecho


 @property
 def data(self):
 return self.__data
 @data.setter
 def data(self, data: str):
 if isinstance(data, str):
 self.__data = data

 @property
 def transporte(self):
 return self.__transporte
 @transporte.setter
 def transporte(self, transporte: Transporte):
 if isinstance(transporte, Transporte):
 self.__transporte = transporte

 @property
 def valor_trecho(self):
 return self.__valor_trecho

 @valor_trecho.setter
 def valor_trecho(self, valor_trecho: float):
 if isinstance(valor_trecho, float):
 self.valor_trecho = valor_trecho
 def __str__(self):
 return f"Trecho - Data: {self.__data} | Origem: {self.__origem} | Destino:
{self.__destino} | Transporte: {self.__transporte} | valor: {self.__valor_trecho}"
