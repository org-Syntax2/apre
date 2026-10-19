// Consultar los sismos globales de las últimas 24 horas desde el USGS
fetch('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson')
    .then(response => response.json())
    .then(data => {
        L.geoJSON(data, {
            pointToLayer: function (feature, latlng) {
                var magnitud = feature.properties.mag;
                // Dibujar un círculo rojo cuyo tamaño escala con la magnitud del sismo
                return L.circleMarker(latlng, {
                    radius: Math.max(magnitud * 2.5, 4),
                    fillColor: "#e74c3c",
                    color: "#900C3F",
                    weight: 1,
                    opacity: 1,
                    fillOpacity: 0.7
                });
            },
            onEachFeature: function (feature, layer) {
                var fecha = new Date(feature.properties.time).toLocaleString();
                layer.bindPopup(
                    "<b>Lugar:</b> " + feature.properties.place + "<br>" +
                    "<b>Magnitud:</b> " + feature.properties.mag + " M<br>" +
                    "<b>Fecha y Hora:</b> " + fecha
                );
            }
        }).addTo(map);
    })
    .catch(error => {
        console.error("Error al cargar la información de sismos:", error);
    });