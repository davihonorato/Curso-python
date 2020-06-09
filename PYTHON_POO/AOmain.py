class TaErradoError(Exception):
    pass


def testar():
    raise TaErradoError('O programa parou.')


try:
    testar()
except TaErradoError as error:
    print(f'ERRO: {error}')
