from pessoa import Pessoa


def test_criar_pessoa():
    pessoa = Pessoa("João", 25)

    assert pessoa.nome == "João"
    assert pessoa.idade == 25
