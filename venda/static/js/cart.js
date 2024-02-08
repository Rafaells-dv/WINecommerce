let btns = document.querySelectorAll(".cart-btn")

btns.forEach(btn=>{
    btn.addEventListener("click", buttonsCarrinho)
})

function buttonsCarrinho(e){
    let id_produto = e.target.value;
    var key = this.innerText;
    var url = '';
    switch(key) {
        case "+":
            url = '/add_to_carrinho'
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