$(".cart-btn").on("click", function() {
    let id_produto = $(this).val();
    let key = $(this).text();
    let url = '';

    switch (key) {
        case "+":
        case "Comprar":
            url = '/add_to_carrinho';
            break;

        case "-":
            url = '/remove_from_carrinho';
            break;

        case "Remover":
            url = '/delete_item_carrinho';
            break;
    }

    let data = {id: id_produto};

    $.ajax({
        url: url,
        method: "POST",
        headers: { "Content-Type": "application/json", 'X-CSRFToken': csrftoken },
        data: JSON.stringify(data),
        success: function(data) {
            console.log(data);
        },
        error: function(error) {
            console.log(error);
        }
    });

    location.reload();
});
