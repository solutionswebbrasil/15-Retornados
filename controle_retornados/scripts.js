document.getElementById('login-form').addEventListener('submit', function(e) {
    e.preventDefault();
    document.getElementById('login-container').style.display = 'none';
    document.getElementById('main-container').style.display = 'flex';
});

document.getElementById('registro-cartuchos-link').addEventListener('click', function(e) {
    e.preventDefault();
    document.getElementById('registro-cartuchos-form').style.display = 'block';
    document.getElementById('consulta-cartuchos-form').style.display = 'none';
});

document.getElementById('consulta-cartuchos-link').addEventListener('click', function(e) {
    e.preventDefault();
    document.getElementById('registro-cartuchos-form').style.display = 'none';
    document.getElementById('consulta-cartuchos-form').style.display = 'block';
});

document.getElementById('form-registro-cartuchos').addEventListener('submit', function(e) {
    e.preventDefault();
    // Aqui você pode adicionar a lógica para enviar os dados para o servidor ou manipulá-los conforme necessário
    alert('Cartucho registrado com sucesso!');
});

document.getElementById('form-consulta-cartuchos').addEventListener('submit', function(e) {
    e.preventDefault();
    // Aqui você pode adicionar a lógica para consultar os dados no servidor
    const modelo = document.getElementById('consulta_modelo_cartucho').value;
    consultarCartuchos(modelo);
});

function consultarCartuchos(modelo) {
    // Simulação de consulta - substitua com a lógica real de consulta ao servidor
    const resultados = [
        { modelo: 'Modelo A', peso_cheio: 100, peso_vazio: 50, gramatura: 50, cor: 'Preto' }
    ];

    const resultadosFiltrados = resultados.filter(cartucho => cartucho.modelo.includes(modelo));
    exibirResultados(resultadosFiltrados);
}

function exibirResultados(resultados) {
    const container = document.getElementById('consulta-resultados');
    container.innerHTML = '';

    if (resultados.length === 0) {
        container.innerHTML = '<p>Nenhum cartucho encontrado.</p>';
    } else {
        const table = document.createElement('table');
        const headerRow = document.createElement('tr');
        headerRow.innerHTML = '<th>Modelo</th><th>Peso Cheio</th><th>Peso Vazio</th><th>Gramatura</th><th>Cor</th>';
        table.appendChild(headerRow);

        resultados.forEach(cartucho => {
            const row = document.createElement('tr');
            row.innerHTML = `<td>${cartucho.modelo}</td><td>${cartucho.peso_cheio}</td><td>${cartucho.peso_vazio}</td><td>${cartucho.gramatura}</td><td>${cartucho.cor}</td>`;
            table.appendChild(row);
        });

        container.appendChild(table);
    }
}
