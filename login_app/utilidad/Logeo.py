import logging


class Logeo():
    ya_definido=False   # singleton.

    @staticmethod
    def agregarerror(msg):
        Logeo.definirLog()
        logging.error(msg)

    @staticmethod
    def agregarinfo(msg):
        Logeo.definirLog()
        logging.info(msg)

    @staticmethod
    def definirLog():
        if Logeo.ya_definido==True:
            return
        Logeo.ya_definido=True # para que no vuelva a repetir.
        logging.basicConfig(filename="error_log",
                            filemode='a',
                            format='%(asctime)s;%(levelname)s;%(message)s',
                            level=logging.DEBUG)










