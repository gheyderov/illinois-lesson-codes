window.addEventListener('load', async function(event){
    let response = await fetch('http://localhost:8000/api/recipes/')
    let resData = await response.json()
    let recipes = document.querySelector('#recipes')
    for (recipe of resData){
        recipes.innerHTML += `
        <div class="col-3">
        <div class="card" style="width: 18rem;">
            <img src="${recipe.image}" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">${recipe.title} - ${recipe.category.title}</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of
                    the card's content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
        </div>
    </div>
        `
    }
})