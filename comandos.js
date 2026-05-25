// acesse : https://designmd.app/library/

// obtenha uma lista de elementos com essa classe: .group.block
lista = document.querySelectorAll('.group.block')


// para cada elemento da lista, obtenha o h3 e o src da imagem e o href
lista[3].querySelector('h3').innerText

// para a imagem, obtenha o src
lista[3].querySelector('img').src

// obtenha o href de cada elemento
lista[3].href

// coloque numa lista:
const listaDeElementos = [];
lista.forEach((elemento) => {
    listaDeElementos.push({
        titulo: elemento.querySelector('h3').innerText,
        imagem: elemento.querySelector('img').src,
        href: elemento.href,
    });
});


// para baixar: 
document.querySelector('#download-designmd').click()


// coloque numa tabela para mim que seja markdown, salvando-a na pasta raiz desse projeto



