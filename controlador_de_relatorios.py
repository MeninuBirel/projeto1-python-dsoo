from collections import Counter
from typing import List, Dict

class ControladorDeRelatorios:
    def __init__(self, viagens: List[Viagem], locais: List[Local], passeios: List[PasseioTuristico]):
        self._viagens = viagens
        self._locais = locais
        self._passeios = passeios

    def gerar_relatorio_destinos_populares(self) -> List:
        if not self._viagens:
            return []

        todos_os_destinos = []
        for viagem in self._viagens:
            for local in viagem.locais:
                todos_os_destinos.append(f"{local.cidade}, {local.pais}")

        contagem_destinos = Counter(todos_os_destinos)
        return contagem_destinos.most_common()

    def gerar_relatorio_destinos_caros_e_baratos(self) -> Dict:
        if not self._locais:
            return {}

        locais_ordenados = sorted(self._locais, key=lambda local: local.valor)

        return {
            "mais_barato": locais_ordenados[0],
            "mais_caro": locais_ordenados[-1]
        }

    def gerar_relatorio_passeios_populares(self) -> List:
        if not self._viagens:
            return []

        todos_os_passeios = []
        for viagem in self._viagens:
            if viagem.itinerario:
                for dia, passeios_no_dia in viagem.itinerario.dia_a_dia.items():
                    for passeio in passeios_no_dia:
                        todos_os_passeios.append(passeio.atracao_turistica)

        contagem_passeios = Counter(todos_os_passeios)
        return contagem_passeios.most_common()

    def gerar_relatorio_passeios_mais_caros_e_baratos(self) -> Dict:
        if not self._passeios:
            return {}

        passeios_ordenados = sorted(self._passeios, key=lambda passeio: passeio.valor)

        return {
            "mais_barato": passeios_ordenados[0],
            "mais_caro": passeios_ordenados[-1]
        }
