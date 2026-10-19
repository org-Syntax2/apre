// 1. Inicializar el mapa centrado de referencia
var map = L.map('map').setView([4.570868, -74.297333], 6);

// 2. Cargar capa base de Esri World Street Map (100% libre de bloqueos para local y Render)
L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
    maxZoom: 19,
    attribution: 'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, and the GIS User Community'
}).addTo(map);

// 3. Obtener ubicación actual del usuario por GPS
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
        var lat = position.coords.latitude;
        var lng = position.coords.longitude;
        
        L.marker([lat, lng]).addTo(map)
            .bindPopup("<b>¡Estás aquí!</b><br>Tu ubicación actual.")
            .openPopup();
        
        map.setView([lat, lng], 13);
    }, function(error) {
        console.log("No se pudo obtener la geolocalización: " + error.message);
    });
}

// 4. Funcionalidad de Ruta Interactiva (Punto A a Punto B + Kilómetros)
let waypointsList = [];
let routingControl = null;
let tempMarkers = [];

map.on('click', function(e) {
    waypointsList.push(e.latlng);
    
    let markerText = waypointsList.length === 1 ? "Punto de Partida (Origen)" : "Punto de Destino";
    let m = L.marker(e.latlng).addTo(map).bindPopup(markerText).openPopup();
    tempMarkers.push(m);

    // Cuando se seleccionan 2 puntos, traza la ruta por carretera
    if (waypointsList.length === 2) {
        if (routingControl) {
            map.removeControl(routingControl);
        }
        
        routingControl = L.Routing.control({
            waypoints: waypointsList,
            routeWhileDragging: true,
            language: 'es',
            // Traducción de las indicaciones y distancias
            formatter: new L.Routing.Formatter({ language: 'es' })
        }).addTo(map);

    } else if (waypointsList.length > 2) {
        // Al dar un tercer clic, se limpia la ruta anterior y empieza un nuevo origen
        tempMarkers.forEach(marker => map.removeLayer(marker));
        tempMarkers = [];
        
        if (routingControl) {
            map.removeControl(routingControl);
            routingControl = null;
        }
        
        waypointsList = [e.latlng];
        let newMarker = L.marker(e.latlng).addTo(map).bindPopup("Nuevo Punto de Partida").openPopup();
        tempMarkers.push(newMarker);
    }
});