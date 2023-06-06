from flask import render_template, request, redirect, jsonify
from app import app, login_required, db2
from bson import ObjectId

@app.route('/establishments')
@login_required
def establishments():
    est_list = db2.dados.find()
    return render_template('establishments.html', est_list=est_list)

@app.route('/establishment/add', methods=['GET', 'POST'])
@login_required
def add_establishment():
    if request.method == 'GET':
        return render_template('add_establishment.html')
    else:
        cnpjCompleto = request.form['cnpjCompleto']
        cep = request.form['cep']
        email = request.form['email']
        nomeFantasia = request.form['nomeFantasia']
        telefone = request.form['telefone']

        if db2.dados.find_one({ 'CORREIO_ELETRÔNICO': email }):
            return jsonify({ "error": "Email address already in use" }), 400
        else:
            db2.dados.insert_one(
            {
                'CNPJ_COMPLETO': cnpjCompleto, 
                'CEP': cep, 
                'CORREIO_ELETRÔNICO': email, 
                'NOME_FANTASIA': nomeFantasia,
                'TELEFONE': telefone
            }
        )
        return redirect('/establishments')
    
@app.route('/establishment/edit', methods=['GET', 'POST'])
@login_required
def edit_establishment():
    if request.method == 'GET':
        idEstablishment = request.values.get("idEstablishment", "")
        est = db2.dados.find_one({'_id': ObjectId(idEstablishment)})
        return render_template('edit_establishment.html', est=est)
    else:
        idEstablishment = request.form['idEstablishment']
        cnpjCompleto = request.form['cnpjCompleto']
        cep = request.form['cep']
        email = request.form['email']
        nomeFantasia = request.form['nomeFantasia']
        telefone = request.form['telefone']
        db2.dados.update_one(
            {'_id': ObjectId(idEstablishment)},
            {
                '$set': {
                    'CNPJ_COMPLETO': cnpjCompleto, 
                    'CEP': cep, 
                    'CORREIO_ELETRÔNICO': email, 
                    'NOME_FANTASIA': nomeFantasia,
                    'TELEFONE': telefone
                }
            }
        )
        return redirect('/establishments')
    
@app.route('/establishment/delete', methods=['GET'])
@login_required
def delete_establishment():
    idEstablishment = request.values.get("idEstablishment", "")
    delete = db2.dados.delete_one({'_id': ObjectId(idEstablishment)})
    return redirect('/establishments')