let form = document.getElementById('login-form')

form.addEventListener('submit', (e) => {
    e.preventDefault()

    let formData = {
        'username': form.username.value,
        'password': form.password.value
    }
    fetch('http://127.0.0.1:8080/api/users/token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
            console.log('DATA:', data.access)
            if (data.access) {
                localStorage.setItem('token', data.access)
                window.location = 'file:///C:/Users/hfdkw/OneDrive/%D0%A0%D0%B0%D0%B1%D0%BE%D1%87%D0%B8%D0%B9%20%D1%81%D1%82%D0%BE%D0%BB/frontend/projects-list.html'
            } else {
                alert('Username OR password did not work')
            }
    })
})