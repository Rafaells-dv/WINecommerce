
function meu_callback(conteudo) {
    let logradouro = conteudo.logradouro;
    let bairro = conteudo.bairro;
    let localidade = conteudo.localidade;
    let uf = conteudo.uf;

    let endereco = logradouro+" - "+localidade+"/"+uf;
    document.getElementById("endereco-entrega").textContent = "Entregar em: "+endereco;

}

function meuEndereco(form){
    let cep = form.inputbox.value.replace(/\D/g, '');

    if (cep !== "") {
        let validacep = /^[0-9]{8}$/;

        if (validacep.test(cep)) {
            var script = document.createElement('script');

            script.src = 'https://viacep.com.br/ws/'+cep+'/json/?callback=meu_callback';
            document.body.appendChild(script);

        }
        else{
            alert("Formato de CEP inválido");
        }
    }
    else{
            document.getElementById("endereco-entrega").textContent = "Preencha o campo CEP";

    }

}

