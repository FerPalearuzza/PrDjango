 //evitar recarga de la página al apretar el boton submit
 document.getElementById('formularioContacto').addEventListener('submit', function(event) {
  event.preventDefault(); 
  console.log("Se evitó la recarga de la página al apretar el botón enviar.");
});

function rtaRegistrada(){
  document.getElementById('rta').style.display= 'block';
  console.log('Se envió una respuesta por el formulario.');
  
  // Oculta el botón de enviar
  document.getElementById('enviar').style.display = 'none';
   /*resetea los campos a cero"*/
 document.getElementById('name').value= '';
 document.getElementById('email').value= '';
 document.getElementById('tipoConsulta').value= '';
 document.getElementById('subject').value= '';
 document.getElementById('message').value= '';
 document.getElementById('newsletter').value= '';
 document.getElementById('privacidad').value= ''; 
}