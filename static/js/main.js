
//Get search form and page links
let searchForm=document.getElementById('searchForm');
let pageLinks=document.querySelectorAll('.page-link');
//ensure search form exists
if(searchForm){
    //add event listener to form submit
    for(let i=0;pageLinks.length>i;i++){
        pageLinks[i].addEventListener('click',function(e){
            //prevent page reload
            e.preventDefault();
            //serialize form data
            let page = this.dataset.page
            //add hidden search input to form
            searchForm.innerHTML+=`<input type="hidden" name="page" value="${page}"/>`;
            searchForm.submit()
        });
    }
}

