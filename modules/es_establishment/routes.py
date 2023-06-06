from flask import render_template, request, url_for
from app import app, es, login_required

@app.route('/es_establishments')
@login_required
def es_establishments():
    results = es.search(index='estabelecimentos', body={"size": 1000, "query": {"match_all": {}}})
    return  render_template('es_establishments.html', results=results) 

@app.route('/es_establishment/add', methods=['GET', 'POST'])
@login_required
def es_add_establishment():
    if request.method == 'GET':
        return render_template('es_add_establishment.html')
    else:
        cnpjCompleto = request.form['cnpjCompleto']
        cep = request.form['cep']
        email = request.form['email']
        nomeFantasia = request.form['nomeFantasia']
        telefone = request.form['telefone']
        es.index(index='estabelecimentos', body={
                'CNPJ_COMPLETO': cnpjCompleto, 
                'CEP': cep, 
                'CORREIO_ELETRÔNICO': email, 
                'NOME_FANTASIA': nomeFantasia,
                'TELEFONE': telefone
            }
        )
    wait_time = 1000
    seconds = wait_time / 1000
    redirect_url = url_for('es_establishments')

    ### o ELastic Search tem um delay para atualizar os dados, então usei um timer para redirecionar para a página de estabelecimentos

    return f"<html><body><p>You will be redirected in { seconds } seconds</p><script>var timer = setTimeout(function() {{window.location='{ redirect_url }'}}, { wait_time });</script></body></html>"
    # return redirect(url_for('es_establishments'))


@app.route('/es_establishment/edit', methods=['POST', 'GET'])
@login_required
def edit_es_establishment():
    if request.method == 'GET':
        id = request.values.get("idEstablishment", "")
        result = es.get(index='estabelecimentos', id=id)
        return render_template('es_edit_establishment.html', result=result)
    else:
        id = request.form['idEstablishment']
        cnpjCompleto = request.form['cnpjCompleto']
        cep = request.form['cep']
        email = request.form['email']
        nomeFantasia = request.form['nomeFantasia']
        telefone = request.form['telefone']
        es.index(index='estabelecimentos', id=id, body={
                'CNPJ_COMPLETO': cnpjCompleto, 
                'CEP': cep, 
                'CORREIO_ELETRÔNICO': email, 
                'NOME_FANTASIA': nomeFantasia,
                'TELEFONE': telefone
            }
        )
    wait_time = 1000
    seconds = wait_time / 1000
    redirect_url = url_for('es_establishments')
    
    ### o ELastic Search tem um delay para atualizar os dados, então usei um timer para redirecionar para a página de estabelecimentos
    
    return f"<html><body><p>You will be redirected in { seconds } seconds</p><script>var timer = setTimeout(function() {{window.location='{ redirect_url }'}}, { wait_time });</script></body></html>"
    # return redirect(url_for('es_establishments'))

@app.route('/es_establishment/delete', methods=['POST'])
@login_required
def delete_es_establishment():
    id = request.values.get("idEstablishment", "")
    es.delete(index='estabelecimentos', id=id)
    wait_time = 1000
    seconds = wait_time / 1000
    redirect_url = url_for('es_establishments')
    
    ### o ELastic Search tem um delay para atualizar os dados, então usei um timer para redirecionar para a página de estabelecimentos
    
    return f"<html><body><p>You will be redirected in { seconds } seconds</p><script>var timer = setTimeout(function() {{window.location='{ redirect_url }'}}, { wait_time });</script></body></html>"
    # return redirect(url_for('es_establishments'))