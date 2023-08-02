const apiUrl = 'http://127.0.0.1:5000/dados';

    


const dataToSend = {
    status: 'enviado',
};

// Configuração da requisição
const requestOptions = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(dataToSend) // Converter o objeto JSON em string
};

const botao = document.getElementById('botao');

botao.addEventListener('click', function(){
    alert("botao clicado");
    fetch(apiUrl, requestOptions)
    .then(response => response.json()) // Converter a resposta em JSON
    .then(data => {
        // Dados retornados pela API após o envio
        console.log('Resposta da API:', data);
    })
    .catch(error => {
        // Caso ocorra algum erro durante a requisição
        console.error('Erro na requisição:', error);
    });
    
})    


    
