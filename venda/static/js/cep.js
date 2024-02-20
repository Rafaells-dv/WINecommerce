function meu_callback(conteudo) {
    let logradouro = conteudo.logradouro;
    let bairro = conteudo.bairro;
    let localidade = conteudo.localidade;
    let uf = conteudo.uf;

    let endereco = logradouro + " - " + localidade + "/" + uf;
    $("#endereco-entrega").text("Entregar em: " + endereco);
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


