# Compras Diretas

## Descrição do Projeto
Este projeto é uma aplicação web desenvolvida com **Django** e **Bootstrap** que permite consultar e filtrar processos administrativos. A ferramenta possibilita a busca por município, unidade e ano do processo, exibindo os resultados de forma interativa e responsiva.

### Funcionalidades Principais
- **Consulta de Processos**: Filtra os processos com base em parâmetros como município, unidade e ano.
- **Interface Interativa**: Exibe os resultados em cards com detalhes resumidos e permite visualizar informações completas em um modal.
- **Dados Dinâmicos**: Utiliza JSON para injetar os dados de processos no template e atualiza os filtros de forma dinâmica.

## Tecnologias Utilizadas
- **Django**: Framework web em Python para a lógica de backend.
- **Bootstrap 5.3**: Utilizado para estilização e responsividade.
- **HTML, CSS e JavaScript**: Para estrutura e interatividade da interface.

## Como Usar
1. **Configuração do Ambiente**:
   - Certifique-se de ter o Python instalado.
   - Crie um ambiente virtual e ative:
     ```bash
     python -m venv venv
     source venv/bin/activate  # No Windows: venv\Scripts\activate
     ```
   - Instale as dependências do projeto:
     ```bash
     pip install -r requirements.txt
     ```

2. **Execução do Projeto**:

   - Inicie o servidor local:
     ```bash
     python manage.py runserver
     ```
   - Acesse a aplicação pelo navegador:
     ```
     http://127.0.0.1:8000/
     ```


## Personalização da Interface
- **Filtros Personalizados**: Selecione o município, unidade e ano para refinar a busca.
- **Exibição dos Resultados**: Cards interativos que exibem detalhes resumidos e acesso a mais informações via modal.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias ou novas funcionalidades.

## Autor
Arthur Lopes

---

### Observação
Este projeto foi desenvolvido para facilitar a consulta e visualização de processos de compras diretas. Sinta-se à vontade para adaptar e expandir a funcionalidade conforme necessário.


