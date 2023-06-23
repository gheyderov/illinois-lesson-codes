window.addEventListener('load', async function(event){
    let response_categories = await fetch('http://localhost:8000/api/categories/')
    let resData = await response_categories.json()
    let category_select = document.querySelector('[name = "category"]')
    for (category of resData){
        category_select.innerHTML += `
        <option value="${category.id}">${category.title}</option>
        `
    }
    let response_tags = await fetch('http://localhost:8000/api/tags/')
    let resDataTags = await response_tags.json()
    let tags_select = document.querySelector('[name = "tags"]')
    for (tag of resDataTags){
        tags_select.innerHTML += `
        <option value="${tag.id}">${tag.title}</option>
        `
    }

})

let recipeCreationForm = document.querySelector('#recipeCreationForm')
let token = localStorage.getItem('token')
recipeCreationForm.addEventListener('submit', function(event){
    event.preventDefault()
    let formData = new FormData(recipeCreationForm)
    fetch('http://localhost:8000/api/recipes/', {
        method : 'POST',
        headers : {
            'Authorization' : `Bearer ${token}`
        },
        body : formData

    })
})