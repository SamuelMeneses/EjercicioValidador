from abc import ABC, abstractmethod
from errores import *


class ReglaValidacion(ABC):
    def init(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        if len(clave) < self._longitud_esperada:
            raise NoCumpleLongitudMinimaError(self._longitud_esperada)

    def _contiene_mayuscula(self, clave):
        if not any(char.isupper() for char in clave):
            raise NoTieneLetraMayusculaError()

    def _contiene_minuscula(self, clave):
        if not any(char.islower() for char in clave):
            raise NoTieneLetraMinusculaError()

    def _contiene_numero(self, clave):
        if not any(char.isdigit() for char in clave):
            raise NoTieneNumeroError()

    @abstractmethod
    def es_valida(self, clave):
        pass


class ReglaValidacionGanimedes(ReglaValidacion):
    def contiene_caracter_especial(self, clave):
        caracteresespeciales = ['@', '', '#', '$', '%']
        if not any(char in caracteresespeciales for char in clave):
            raise NoTieneCaracterEspecialError()

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self.contiene_caracter_especial(clave)
        return True


class ReglaValidacionCalisto(ReglaValidacion):
    def contiene_calisto(self, clave):
        if clave.find('Calisto') == -1:
            raise NoTienePalabraSecretaError()

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self.contiene_calisto(clave)
        return True


