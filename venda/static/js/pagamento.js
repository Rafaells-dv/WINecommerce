function copyPaste() {
    let qrcode = $('#codigoQrcode').val();

    if (!navigator.clipboard) {
        alert("Seu navegador não suporta a funcionalidade de cópia para a área de transferência. Por favor, copie manualmente.");
    } else {
        navigator.clipboard.writeText(qrcode).then(
            function() {
                alert("yeah!");
            }).catch(
            function() {
                alert("err");
            });
    }
}


