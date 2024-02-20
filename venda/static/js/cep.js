function meu_callback(conteudo) {
    let logradouro = conteudo.logradouro;
    let localidade = conteudo.localidade;
    let uf = conteudo.uf;

    let endereco = logradouro + " - " + localidade + "/" + uf;
    let data = {'endereco': endereco};

    fetch('/endereco-json/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(data) // Convertendo o objeto 'data' em uma string JSON
    })
    .then(response => response.json())
    .then(data => {
        console.log('Resposta do servidor:', data);
        // Recarrega a página após o sucesso da solicitação
        window.location.reload();
    })
    .catch(error => {
        console.error('Erro:', error);
    });

}


function meuEndereco(form) {
    let cep = $(form.inputbox).val().replace(/\D/g, '');

    if (cep !== "") {
        let validacep = /^[0-9]{8}$/;

        if (validacep.test(cep)) {
            $.ajax({
                url: 'https://viacep.com.br/ws/' + cep + '/json/',
                dataType: 'jsonp',
                success: function (conteudo) {
                    meu_callback(conteudo);
                }
            });
        } else {
            alert("Formato de CEP inválido");
        }
    } else {
        $("#endereco-entrega").text("Preencha o campo CEP");
    }
}


