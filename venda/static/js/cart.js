$(".cart-btn").on("click", function() {
    var id_produto = $(this).val();
    var key = $(this).text();
    var url = '';
    
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

    var data = { id: id_produto };

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
