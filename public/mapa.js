let map = L.map('map').setView([-23.5505, -46.6333], 13); // Centralizando no Brasil

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

fetch('https://LogisticaIncobel.github.io/rastreador/api/localizacoes')  // URL da sua API no GitHub Pages
    .then(response => response.json())
    .then(data => {
        data.forEach(caminhao => {
            let marker = L.marker([caminhao.latitude, caminhao.longitude]).addTo(map);
            marker.bindPopup(`
                <b>Placa: ${caminhao.placa}</b><br>
                Data: ${caminhao.data}<br>
                Hora: ${caminhao.hora}<br>
                Latitude: ${caminhao.latitude}<br>
                Longitude: ${caminhao.longitude}<br>
                Velocidade: ${caminhao.velocidade}<br>
                Ignicão: ${caminhao.ignicao}<br>
                <a href="https://link_para_historico">Histórico de 72h</a>
            `);
        });
    });
