#Create by Murillo
#language: pt

Funcionalidade: validar dados da api "consulta cep"

  Contexto:
    Dado que eu tenha acesso a api de consulta cep

    @logradouro
    Esquema do Cenario: Validar o logradouro e cep selecionado
      Quando realizo a criação do cep
        | cep | logradouro |  ddd  |
        |<cep>|<logradouro>| <ddd> |
      Entao  realizo a validação do logradouro e ddd
      Exemplos:
        |cep     | logradouro         | ddd |
        |02860030| rua spencer vampré |  11 |