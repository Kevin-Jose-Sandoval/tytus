from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Expresiones import Relacional

class Case(Instruccion):
    '''
    La clase Case, recibe una lista de condiciones y cada una de ellas tiene una lista de instrucciones
    '''

    def __init__(self,l_condiciones,strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna,strGram,strSent)
        self.l_condiciones = l_condiciones
        #desde aqui voy a mandar la etiqueta de escape

    def ejecutar(self, tabla, arbol):
        pass

    def traducir(self, tabla, arbol,cadenaTraducida):
        codigo = ""
        etiquetaSalida = arbol.generaEtiqueta()
        #Si existe algun error en la condicion se devuelve el error
        for condicion in self.l_condiciones:
            condicion_case = condicion.traducir(tabla, arbol,etiquetaSalida)
            if isinstance(condicion_case, Excepcion):
                return condicion_case
            codigo += condicion_case
        codigo += "\tlabel " + etiquetaSalida + "\n"
        return codigo
        
class condicion_case(Instruccion):
    '''
    La clase recibe una expresion logica y una lista de instrucciones
    '''
    def __init__(self, expLogica,instrucciones,strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna,strGram,strSent)
        self.expLogica = expLogica
        self.instrucciones = instrucciones

    def ejecutar(self, tabla, arbol):
        pass

    def traducir(self, tabla, arbol,cadenaTraducida):
         #Si existe algun error en la expresion logica se devuelve el error
        #expresion_logica = self.expLogica.traducir(tabla, arbol,cadenaTraducida)
        #if isinstance(expresion_logica, Excepcion):
        #        return expresion_logica

        #Inicia traduccion
        codigo = "\t" + self.expLogica + "\n" 
        etiquetaV = arbol.generaEtiqueta()
        etiquetaF = arbol.generaEtiqueta()
        etiquetaSalida = cadenaTraducida
        codigo += "\tif " + self.expLogica + ":\n"
        codigo += "\t\tgoto " + etiquetaV + "\n"
        codigo += "\tgoto " + etiquetaF + "\n"
        codigo += "\tlabel " + etiquetaV + "\n"
        #for i in self.instrucciones:
        #    instruccion_if = i.traducir(tabla, arbol,cadenaTraducida)
        #    if isinstance(instruccion_if, Excepcion):
        #        return instruccion_if
        #    codigo += i.codigo
        codigo += "\t" + self.instrucciones + "\n"
        codigo += "\tgoto " + etiquetaSalida + "\n"
        codigo += "\tlabel " + etiquetaF + "\n"
        
        return codigo
        #   ...
        #   if temporal_logico:
        #       goto L1
        #   goto L2
        #   label L1    
        #   instrucciones_if
        #   goto Lsalida
        #   label L2
        #   ...

class CaseElse(Instruccion):
    '''
    La clase CaseElse, recibe una lista de condiciones y cada una de ellas tiene una lista de instrucciones
    ademas de las instrucciones si todas son falsas
    '''

    def __init__(self,l_condiciones,instrCaseFalso,strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna,strGram,strSent)
        self.l_condiciones = l_condiciones
        self.instrCaseFalso = instrCaseFalso
        #desde aqui voy a mandar la etiqueta de escape

    def ejecutar(self, tabla, arbol):
        pass

    def traducir(self, tabla, arbol,cadenaTraducida):
        codigo = ""
        etiquetaSalida = arbol.generaEtiqueta()
        #Si existe algun error en la condicion se devuelve el error
        for condicion in self.l_condiciones:

            condicion_case = condicion.traducir(tabla, arbol,etiquetaSalida)
            if isinstance(condicion_case, Excepcion):
                return condicion_case
            codigo += condicion_case
        #for i in self.instrucciones:
        #    instruccion_if = i.traducir(tabla, arbol,cadenaTraducida)
        #    if isinstance(instruccion_if, Excepcion):
        #        return instruccion_if
        #    codigo += i.codigo
        codigo += "\t" + self.instrCaseFalso + "\n"
        codigo += "\tlabel " + etiquetaSalida + "\n"
        return codigo

class condicion_caseID(Instruccion):
    '''
    La clase recibe una lista de expresiones y una lista de instrucciones
    '''
    def __init__(self, expLogica,instrucciones,strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna,strGram,strSent)
        self.expLogica = expLogica
        self.instrucciones = instrucciones

    def ejecutar(self, tabla, arbol):
        pass

    def traducir(self, tabla, arbol,cadenaTraducida,operadorI):
        #Si existe algun error en la expresion logica se devuelve el error
        codigo = ""
        for  expre in self.expLogica:
            expresion_logica = expre.traducir(tabla, arbol,cadenaTraducida)
            if isinstance(expresion_logica, Excepcion):
                return expresion_logica
            codigo += "\t" + expresion_logica.codigo + "\n"
            #relacional = Relacional.Relacional(operadorI,)
        #Inicia traduccion
        codigo = "\t" + self.expLogica + "\n" 
        etiquetaV = arbol.generaEtiqueta()
        etiquetaF = arbol.generaEtiqueta()
        etiquetaSalida = cadenaTraducida
        codigo += "\tif " + self.expLogica + ":\n"
        codigo += "\t\tgoto " + etiquetaV + "\n"
        codigo += "\tgoto " + etiquetaF + "\n"
        codigo += "\tlabel " + etiquetaV + "\n"
        #for i in self.instrucciones:
        #    instruccion_if = i.traducir(tabla, arbol,cadenaTraducida)
        #    if isinstance(instruccion_if, Excepcion):
        #        return instruccion_if
        #    codigo += i.codigo
        codigo += "\t" + self.instrucciones + "\n"
        codigo += "\tgoto " + etiquetaSalida + "\n"
        codigo += "\tlabel " + etiquetaF + "\n"
        
        return codigo
        #   ...
        #   if temporal_logico:
        #       goto L1
        #   goto L2
        #   label L1    
        #   instrucciones_if
        #   goto Lsalida
        #   label L2
        #   ...