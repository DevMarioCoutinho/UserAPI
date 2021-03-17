import DAL.Connection as Connect
import Class.User as csUser


def SelectUsuario(codigo):
    try:
        conn = Connect.ConnectionSQL()    
        cursor = conn.cursor()
        sql = """SELECT Codigo, Nome, Idade, Sexo FROM Usuario WHERE Codigo = '{}' """ .format(codigo)
        records = cursor.execute(sql).fetchall()
        for row in records:
            csUser.Codigo = row[0]
            csUser.Nome = row[1]
            csUser.Idade = row[2]
            csUser.Sexo = row[3]
        conn.close()
    except Exception as ex:
        print(ex) 
        

def InsertUsuario(nome, idade, sexo):
    try:
        conn = Connect.ConnectionSQL()    
        cursor = conn.cursor()
        sql = "INSERT INTO Usuario (Nome,Idade,Sexo) VALUES ('{}','{}','{}') " .format(nome,idade,sexo)
        cursor.execute(sql)
        cursor.commit()
        conn.close()
    except Exception as ex:
        print(ex)
        
        
def UpdateUsuario(codigo, nome, idade, sexo):
    try:
        conn = Connect.ConnectionSQL()    
        cursor = conn.cursor()
        sql = """ SET NOCOUNT ON;
        DECLARE @CODIGO INT;
        SET @CODIGO = ?;
        IF (SELECT COUNT(0) FROM Usuario WHERE Codigo = @CODIGO) > 0 BEGIN;
            UPDATE Usuario SET Nome = ?, 
            Idade = ?,
            Sexo = ?
            WHERE Codigo = @CODIGO;
            SELECT 'Sucess'
            END ELSE BEGIN;
                    SELECT 'Error';
            END;"""
        parametros = (codigo,nome,idade,sexo)
        response = cursor.execute(sql,parametros).fetchone()
        cursor.commit()
        conn.close()
        
        return response
    except Exception as ex:
        print(ex)
        

def DeleteUsuario(codigo):
    try:
        conn = Connect.ConnectionSQL()    
        cursor = conn.cursor()
        sql = """ SET NOCOUNT ON;
        DECLARE @CODIGO INT;
        SET @CODIGO = ?;
        IF (SELECT COUNT(0) FROM Usuario WHERE Codigo = @CODIGO) > 0 BEGIN;
                    DELETE Usuario WHERE Codigo = @CODIGO;
                    SELECT 'Sucess'
                END ELSE BEGIN;
                    SELECT 'Error';
                END;""" 
        response = cursor.execute(sql,codigo).fetchone()
        conn.commit()
        conn.close()      
        return response
    except Exception as ex:
        return (ex,sql)
        
                   
    