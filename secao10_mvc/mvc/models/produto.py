from db import executar


class Produto:
    def __init__(self, nome: str, preco: float, id: int = None):
        self.id = id
        self.preco = preco
        self.nome = nome
        self.status = 1  # ativo = 1, inativo =0
        self.create_table_if_not_exist()

    @staticmethod
    def create_table_if_not_exist():
        query = """
        create table if not exists produtos ( 
            id integer primary key autoincrement,
            nome text, 
            preco real, 
            status numeric
        )
        """
        executar(query)

    def create(self):
        query = f"""
        insert into produtos (nome, preco, status)
        values ('{self.nome}', {float(self.preco)}, {self.status})
        """
        executar(query)

    def update(self):
        query = f"""
        update produtos 
        set status={int(self.status)}
        where id={int(self.id)}
        """
        executar(query)
    @staticmethod
    def delete(id):
        query = f"""
        delete from produtos
        where id={int(id)}
        """
        executar(query)

    @staticmethod
    def get(_id: int = None):
        Produto.create_table_if_not_exist()
        if _id:
            query = f"select id, nome, preco from produtos where id={int(_id)}"
            produto = executar(query)[0]
            return Produto(produto[0], produto[1], produto[2])
        query = "select id, nome, preco from produtos"
        produtos = executar(query)
        return [Produto(produto[1], produto[2], produto[0]) for produto in produtos]
