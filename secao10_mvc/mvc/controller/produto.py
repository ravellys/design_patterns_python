from tornado.web import RequestHandler

from models.produto import Produto


class Index(RequestHandler):
    def get(self):
        produtos = Produto.get()
        self.render('index.html', produtos=produtos)


class Create(RequestHandler):
    def get(self):
        self.render('create.html')

    def post(self):
        nome = self.get_argument('nome')
        preco: float = float(self.get_argument('preco'))

        produto = Produto(nome=nome, preco=preco)
        produto.create()

        self.redirect('/')


class Update(RequestHandler):

    def get(self, id, status):
        produto = Produto.get(id)
        produto.status = status
        produto.update()
        self.redirect('/')


class Delete(RequestHandler):

    def get(self, id):
        Produto.delete(id)
        self.redirect('/')
