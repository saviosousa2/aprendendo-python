import pymysql.cursors

conexao = pymysql.connect(
    host='10.130.140.7',
    user='savio',
    password='savio123',
    db='test',
    cursorclass=pymysql.cursors.DictCursor
)

   # autenticidade para while
autentico = False

   # Parâmetros para logue
def logarCadastrar():
        usuarioExistente = 0
        autenticado = False
        usuarioMaster = False

    # logando na ferramenta com os dados do banco
        if decisao == 1:
            nome = input('Digite seu nome: ')
            senha = input('Digite sua senha: ')

    # conectando com o banco para verificar usuarios (se a decisao for 1)
            for linha in resultado:
                if nome == linha['nome'] and senha == linha['senha']:
                    if linha['nivel'] == 1:
                        usuarioMaster = False
                    elif linha['nivel'] == 2:
                        usuarioMaster = True
                    autenticado = True
                    break
                else:
                    autenticado = False
            if not autenticado:
                print('Email ou senha errado')
    # usuario digita nome e uma senha ele verifica se ja existe esse nome e senha
    # e se não tiver é inserido os dados no banco
        elif decisao == 2:
            print('Faça seu cadastro')
            nome = input('Digite seu nome: ')
            senha = input('Digite sua senha: ')
    # verificação para não haver cadastros duplicados
            for linha in resultado:
                if nome == linha['nome'] and senha == linha['senha']:
                    usuarioExistente = 1

            if usuarioExistente == 1:
                print('Usuario ja cadastrado, tente com nome ou senha diferente')
            elif usuarioExistente == 0:
                try:
                    with conexao.cursor() as cursor:
                        cursor.execute(
                            'insert into cadastros(nome,senha,nivel) values (%s, %s, %s)', (nome, senha, 1))
                        conexao.commit()
                    print('Usuário cadastrado com sucesso.')
                except:
                    print('Erro ao inserir os dados.')
        return autenticado, usuarioMaster
    


while not autentico:
        decisao = int(input('Digite 1 para logar e 2 para cadastrar: '))

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from cadastros')
                resultado = cursor.fetchall()
        except:
            print('erro ao conectar ao banco de dados')
        autentico, usuarioSupremo = logarCadastrar()

print('Usuário logado')

def logarCadastrar(decidir): ...

def cadastrarProdutos():
        nome = input('Digite o nome do produto: ')
        ingredientes = input('Digite os ingredientes do produto: ')
        grupo = input('Digite o grupo pertecente a esse produto: ')
        preco = float(input('Digite o preço do produto: '))

        try:
            with conexao.cursor() as cursor:
                cursor.execute('insert into produtos (nome, ingredientes, grupo, preco) values (%s, %s, %s, %s)', (nome, ingredientes, grupo, preco))
                conexao.commit()
                print('Produto cadastrado com sucesso')
        except:
            print('Erro ao cadastrar os produtos no banco')

def listarProdutos():
    produtos = []
    
    try:
        with conexao.cursor() as cursor:
             cursor.execute('select * from produtos')
             produtosCadastrados = cursor.fetchall()    
    except:
        print('Erro ao conectar ao banco de dados')
        
    for i in produtosCadastrados:
        produtos.append(i)
        
    if len(produtos) != 0:
        for i in range(0, len(produtos)):
            print(produtos[i])
    else:
        print('Nenhum produto cadastrado')
def excluirprodutos():
    idDeletar  = int(input('Digite o id referente ao produto que deseja apagar: '))
    
    try:
        with conexao.cursor() as cursor:
            cursor.execute('delete from produtos where id = {}'.format(idDeletar))
    except:
        print('erro ao excluir o produto')

def listarPedidos():
    pedidos = []

while not autentico:...

if autentico:

    if usuarioSupremo == True:
            decisaoUsuario = 1
        
            while decisaoUsuario != 0:
                decisaoUsuario = int(input('Digite 0 para sair,1 para cadastrar produtos,2 para listar produtos cadastrados: '))
                if decisaoUsuario == 0:
                    print('A pizzaria agradece sua preferencia,Obrigado pelo pedido e até a próxima')
                if decisaoUsuario == 1:
                    cadastrarProdutos()
                elif decisaoUsuario == 2:
                    listarProdutos()
                    
                    delete = int(input('Digite 1 para excluir um produto e 2 para sair: '))

                    if delete == 1:
                        excluirprodutos()
