let loginBtn = document.getElementById('login-btn')
let logoutBtn = document.getElementById('logout-btn')
let token=localStorage.getItem('token')
if (token) {
    loginBtn.style.display = 'none'
    logoutBtn.style.display = 'block'
} else {
    loginBtn.style.display = 'block'
    logoutBtn.style.display = 'none'
}
logoutBtn.addEventListener('click',(e)=>{
    e.preventDefault()
    localStorage.removeItem('token')
    window.location = 'file:///C:/Users/hfdkw/OneDrive/%D0%A0%D0%B0%D0%B1%D0%BE%D1%87%D0%B8%D0%B9%20%D1%81%D1%82%D0%BE%D0%BB/frontend/login.html'
    
})

let projectsUrl='http://127.0.0.1:8080/api/projects/'
let getProjects =() => {
    fetch(projectsUrl)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        buildProjects(data)
    })
    .catch(error => console.log(error))
}
let buildProjects = (projects) => {
    let projectsWrapper = document.getElementById('projects--wrapper')
    projectsWrapper.innerHTML=''
    for ( let i=0;projects.length > i;i++){
        let project = projects[i]

        let projectCard =`
        <div class="project--card" style="width: 18rem;">
        <img src='http://127.0.0.1:8080/${project.featured_img}' />
            <div>
                <div class="card--header">
                    <h3>${project.title}</h3>
                    <strong class ="vote--option" data-vote="up" data-project="${project.id}">&#43;</strong>
                    <strong class ="vote--option" data-vote="down" data-project="${project.id}">&#8722;</strong>
                </div>
                <i>${project.vote_ratio}% Postive feedback </i>
                <p>${project.description.substring(0,150)}</p>
            </div>
        </div>
        `
        projectsWrapper.innerHTML += projectCard
    }
    addVoteEvents()
    // Add an event listener
}
let addVoteEvents = () => {
    let voteButtons = document.getElementsByClassName('vote--option')
    
    for (let i=0;voteButtons.length > i;i++){
        let voteButton = voteButtons[i]
        voteButton.addEventListener('click',(e)=>{
            let token=localStorage.getItem('token')
            console.log(token)
            let vote = e.target.dataset.vote
            let project = e.target.dataset.project
            console.log(project,vote)
            fetch(`http://127.0.0.1:8080/api/projects/${project}/vote/`,{
                method:'POST',
                headers:{
                    'Content-Type':'application/json',
                    Authorization: `Bearer ${token}`,
                    
                },
                body:JSON.stringify({
                    'value':vote
                })
            })
            .then(response => response.json())
            .then(data => {
                console.log(data)
                getProjects()
            })
            
        })
    }
}
getProjects()