function copyPaste() {
    let qrcode = document.getElementById('codigoQrcode').value;

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

