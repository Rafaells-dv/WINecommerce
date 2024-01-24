function copyPaste() {
    let qrcode = $('#codigoQrcode').getAttribute('value');
    console.log(qrcode)

    if (!navigator.clipboard){
    }
    else {
    navigator.clipboard.writeText(qrcode).then(
        function(){
            alert("yeah!"); // success
        })
      .catch(
         function() {
            alert("err"); // error
      });
    }
}

