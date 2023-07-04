let subscribeForm = document.getElementById('subscribe-form')
subscribeForm.addEventListener('submit', function(e){
    e.preventDefault()
    let email = document.getElementById('subscribe-email')
    console.log(email.value)
    fetch('http://localhost:8000/api/subscribers/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': subscribeForm.csrfmiddlewaretoken.value,
        },
        body: JSON.stringify({'email' : email.value})
    })
    .then(response => {
        if (response.ok){
            subscribeForm.innerHTML = 'Thanks for your subscribing!'
        }
        else{
            alert('Error')
        }
    })
})