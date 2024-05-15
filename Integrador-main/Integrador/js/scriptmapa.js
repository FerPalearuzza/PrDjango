/* este scrpt ya no sirve porque reemplazamos mapa  iframe
function initMap() {
    var ubicacion = { lat:  -38.00042, lng: -57.5562};
    var mapa = new google.maps.Map(document.getElementById("mapa"), {
        zoom: 15,
        center: ubicacion,
    });
    var marcador = new google.maps.Marker({
        position: ubicacion,
        map: mapa,
    });
}
*/