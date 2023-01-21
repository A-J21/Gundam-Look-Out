fetch("Gundamlist.json")
.then(function(response){
    return response.json();
})

.then(data => {
    let gundams = data.items;
    let placeholder = document.querySelector('#data-output');
    let out = "";

    for(let gundam of gundams ){
        out += `
        
           <li> <img src='${gundam.image}'><br><a href="${gundam.link}" target="_blank">${gundam.name}<br>${gundam.price}</a></li>
        
     `;
    }

    placeholder.innerHTML=out;
    let website_placeholder = document.querySelector('#website');
    let link = "";
    for(let gundam of gundams ){
        link += `

           <a href="${gundam.webiste}"></a>

     `;
    }
    website_placeholder.innerHTML = data.website;

    let date_placeholder = document.querySelector('#date');
    date_placeholder.innerHTML = data.Date;
})


