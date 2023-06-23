let loginForm = document.querySelector('#loginForm')

loginForm.addEventListener('submit', async function(event){
    event.preventDefault()
    let postData = {
        'email' : loginForm.email.value,
        'password' : loginForm.password.value
    }
    let response = await fetch('http://localhost:8000/auth/token/', {
        method : 'POST',
        body : JSON.stringify(postData),
        headers : {
            'Content-Type' : 'application/json'
        }
    })
    let resData = await response.json()
    if (!response.ok){
        alert(resData.detail)
    }
    else{
        localStorage.setItem('token', resData.access)
    }
})