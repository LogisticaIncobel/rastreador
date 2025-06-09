let map = L.map('map').setView([-23.5505, -46.6333], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap'
}).addTo(map);

fetch('localizacoes.json')  // <- carrega o JSON da mesma pasta
    .then(response => response.json())
    .then(data => {
        data.forEach(c => {
            L.marker([c.latitude, c.longitude])
              .addTo(map)
              .bindPopup(`
                <b>Placa: ${c.placa}</b><br>
                Data: ${c.data}<br>
                Hora: ${c.hora}<br>
                Velocidade: ${c.velocidade}<br>
                Ignição: ${c.ignicao}<br>
                Lat: ${c.latitude}, Long: ${c.longitude}
              `);
        });
    });
