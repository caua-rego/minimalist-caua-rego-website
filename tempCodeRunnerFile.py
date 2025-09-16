   flash('Você foi desconectado com sucesso!', 'success')
    return redirect(url_for('index', _external=True, _scheme='http') + '?clear_cart=true')

@app.route('/pedidos')
@login_