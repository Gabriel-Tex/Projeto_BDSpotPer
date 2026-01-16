## Interface BDSpotPer

Sistema de interface gráfica para gerenciamento de playlists com integração ao banco de dados.

### Estrutura de Arquivos

```
interface/
├── interface.py          # Arquivo principal (executar este)
├── config.py             # Configurações da interface
├── abas/                 # Módulo com as abas da interface
│   ├── __init__.py
│   ├── playlists.py      # Aba de gerenciamento de playlists
│   ├── albuns.py         # Aba de visualização de álbuns
│   └── consultas.py      # Aba de consultas especializadas
```

### Como Executar

```powershell
# Ativar ambiente virtual (se não estiver ativado)
.\fbd\Scripts\Activate.ps1

# Executar a interface
python .\interface\interface.py
```

### Funcionalidades

#### Aba Playlists
- ✅ Criar novas playlists
- ✅ Listar todas as playlists existentes
- ✅ Atualizar lista em tempo real

#### Aba Álbuns
- ✅ Listar todos os álbuns do banco de dados
- ✅ Visualizar faixas de cada álbum (duplo clique)
- ✅ Atualizar lista

#### Aba Consultas
- ✅ Álbuns acima da média de preço
- ✅ Gravadora com mais playlists de Dvorack
- ✅ Compositor com mais faixas nas playlists
- ✅ Playlists com apenas Concerto Barroco

### Integração com App

A interface importa os módulos do diretório `app/`:
- `playlists.py` - Operações com playlists
- `albuns.py` - Operações com álbuns
- `consultas.py` - Consultas especializadas
- `database.py` - Conexão com o banco de dados

### Desenvolvimento

Para adicionar uma nova aba:

1. Crie um arquivo `abas/novo_modulo.py`
2. Crie uma classe que herde a estrutura padrão
3. Importe em `interface.py`
4. Instancie no método `__init__` de `BDSpotPerInterface`

Exemplo:
```python
from abas.novo_modulo import AbaNovoModulo

class BDSpotPerInterface:
    def __init__(self, root):
        # ... código existente ...
        self.aba_novo = AbaNovoModulo(self.notebook)
```

### Requisitos

- Python 3.7+
- pyodbc
- python-dotenv
- Banco de dados SQL Server configurado

### Notas

- A interface é modular e extensível
- Cada aba é independente e pode ser desenvolvida/testada separadamente
- Trata erros de conexão e exibe mensagens ao usuário
- Realiza validação de dados antes de enviar ao banco
