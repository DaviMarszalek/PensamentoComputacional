"""
Sistema de Cadastro de Usuários.
IENH - 2025/01
Aluno/Autor: Davi Marszalek


Arquivo que contém, as classes que representam os models do banco de dados

Classes:
    - Usuario: Classe que representa a tabela 'usuarios' no banco de dados.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base para nossos modelos
Base = declarative_base()

class Usuario(Base):
    """
    Classe que representa a tabela 'usuarios' no banco de dados.
    Atributos:
        id(int): ID do usuário (chave primária)        
        nome(str): Nome do usuário(máximo 50 caracteres)
        idade(int): Idade do usuário
    Retorno:
        None    
    """
    
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    idade = Column(Integer)
    
    def __repr__(self):
        return f"<Usuario(nome='{self.nome}', idade={self.idade})>"
