from flask import Flask, request, json
import Class.User as csUser
import DAL.Crud as Db

app = Flask("InfoUsers")


#Region GET
@app.route("/api/usuario/<code>", methods = ["GET"])
def Usuario(code):
    
    Db.SelectUsuario(code)
    response = {}
    
    try:    
        int(csUser.Codigo) 
        response["codigo"] = csUser.Codigo  
        response["nome"] = csUser.Nome
        response["idade"] = csUser.Idade
        response["sexo"] = csUser.Sexo
        
        csUser.Codigo = None
        csUser.Nome = None
        csUser.Idade = None
        csUser.Sexo = None
              
        return response
    except:
        return StatusResponse(400,"There is no User with this code")


#Region POST
@app.route("/api/cadastra/usuario", methods = ["POST"])
def CadastraUsuario():
    
    body = request.get_json()
    
    if("nome" not in body):
        return StatusResponse(400,"Parameter 'nome' is Mandatory")
    
    if ("idade" not in body):
        return StatusResponse(400,"Parameter 'idade' is Mandatory")   
    
    if("sexo" not in body):
        return StatusResponse(400,"Parameter 'sexo' is Mandatory")
    
    else:
        
        Db.InsertUsuario(body["nome"],body["idade"],body["sexo"])

        return StatusResponse(200,"User Successfully Inserted")


#Region DELETE
@app.route('/api/deleta/usuario/<code>', methods = ["DELETE"])
def DeletarUsuario(code):
    
    Sucess = Db.DeleteUsuario(code)

    if(Sucess[0] != 'Error'):
        return StatusResponse(200,"User Removed Successfully")
    else:
        return StatusResponse(400,"Failed to Remove User")
    
    
#Region PUT
@app.route('/api/alterar/usuario/<code>', methods = ["PUT"])
def AlterarUsuario(code):
    
    body = request.get_json()
    
    if("nome" not in body):
        return StatusResponse(400,"Parameter 'nome' is Mandatory")
      
    elif("idade" not in body):
        return StatusResponse(400,"Parameter 'idade' is Mandatory")
    
    elif("sexo" not in body):
        return StatusResponse(400,"Parameter 'idade' is Mandatory") 
         
    else:
        Sucess = Db.UpdateUsuario(code,body["nome"],body["idade"],body["sexo"])
    
        if(Sucess[0] != 'Error'):
            return StatusResponse(200,"User Registration Successfully Changed")
        else:
            return StatusResponse(400,"Failed to Change User Registration")
        
    
    
#Region State Massage    
def StatusResponse(status,message):
    response = {}
    response["status"] = status
    response["message"] = message
    
    return response


app.run()
