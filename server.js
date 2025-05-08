const express = require('express');
const axios = require('axios');
const cors = require('cors');
const app = express();
const PORT = 3000;

// Salli CORS
app.use(cors());

// Proxy-reitti tietojen hakemiseen
app.get('/proxy', async (req, res) => {
    try {
        console.log('Haetaan sisältöä viisipennia.fi-sivustolta...');
        const response = await axios.get('https://viisipennia.fi/lounas/');
        console.log('Sisältö haettu onnistuneesti.');
        res.send(response.data); // Lähetetään haettu HTML-sisältö selaimelle
    } catch (error) {
        console.error('Virhe sisällön hakemisessa:', error.message);
        res.status(500).send('Virhe sisällön hakemisessa.');
    }
});

// Reitti lounaslistan hakemiseen
app.get('/lounas', async (req, res) => {
    try {
        const response = await axios.get('https://viisipennia.fi/lounas/');
        res.send(response.data); // Lähetetään haettu HTML-sisältö selaimelle
    } catch (error) {
        console.error('Virhe lounaslistan hakemisessa:', error);
        res.status(500).send('Virhe lounaslistan hakemisessa.');
    }
});

// Palvelimen käynnistys
app.listen(PORT, () => {
    console.log(`Palvelin käynnissä osoitteessa http://localhost:${PORT}`);
});