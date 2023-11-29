function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

let btns = document.querySelectorAll(".cart-btn")

btns.forEach(btn=>{
    btn.addEventListener("click", buttonsCarrinho)
})

function buttonsCarrinho(e){
    let id_produto = e.target.value;
    var key = this.innerText;

    switch(key) {
        case "+":
            var url = '/add_to_carrinho'
            break;

        case "Comprar":
            url = '/add_to_carrinho'
            break;

        case "-":
            url = '/remove_from_carrinho'
            break;

        case "Remover":
            url = '/delete_item_carrinho'
            break;

    }


    let data = {id:id_produto};

    fetch(url, {
        method: "POST",
        headers: {"Content-Type":"application/json", 'X-CSRFToken': csrftoken},
        body: JSON.stringify(data)
    })
    .then(res=>res.json())
    .then(data=>{
        console.log(data)
    })
    .catch(error=>{
        console.log(error)
    })
    location.reload()
}

function meu_callback(conteudo) {
    let logradouro = conteudo.logradouro;
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