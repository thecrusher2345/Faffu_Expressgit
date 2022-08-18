const contenedorQR = document.getElementById('contenedorQR');
const formulario = document.getElementById('formulario');

const QR = new QRCode(contenedorQR);

formulario.addEventListener('submit', (e) => {
    e.preventDefault();
    QR.makeCode( "http://127.0.0.1:8000/" + formulario.link.value);
    const nombre = document.querySelector.formulario("#link").value;
    const respuesta = document.getElementById("respuesta");
    respuesta.textContent = `Hola, su pedido es ${nombre}`
})


