from features.consulta_cep.page import validate
from features.consulta_cep.page.cep_page import cep

@given(u'que eu tenha acesso a api de consulta cep')
def step_impl(context):
    pass


@when(u'realizo a criação do cep')
def step_impl(context):
    context.validacao = validate.table_to_dict(context)
    context.cep = str(context.validacao["cep"])

    if not context.cep:
        context.cep = validate.gerar_cep_aleatorio()
    else:
        pass

@then(u'realizo a validação do logradouro e ddd')
def step_impl(context):
    response = cep.get_cep(context, context.cep)

    if response["logradouro"]!= context.validacao["logradouro"]:
        print("erro")

    if response["ddd"] != context.validacao["ddd"]:
        print("erro")



