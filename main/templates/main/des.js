
let a = document.querySelector('#button1')
let  b = document.querySelector('.zero');
let  r = document.querySelector('.content');



a.addEventListener('click', (e) => {
    
    let item = document.createElement('div')
    let textw =  document.querySelector('#name').value;
    if(textw.length < 3) {
        
      alert("Вы некорректно ввели задача, должно быть от 3 символов")
      return
  }
    let newPost = document.createElement('h4');   
    newPost.textContent = textw;
    newPost.style.color = 'black';
    newPost.style.fontFamily = 'Times New Roman, Times, serif'
    let newTask = document.createElement('div');
    newPost.classList.add('st');
    newTask.innerHTML = `
    <img src="img/remove.png" style="height: 25px; width: 20px;" class="removeBut" id ="remove">
    
    `
    newTask.addEventListener('click', handleRemove);
    function handleRemove(){
        item.parentElement.removeChild(item);
        
    }

    item.classList.add('item'); 
    
   

    let vip = document.createElement('div')
    newPost.append(vip)
    vip.classList.add('do')
    vip.innerHTML = `
        <img src="img/done2.png" style="height: 25px; width: 20px;" class="donebut" id ="done">
        `
    vip.addEventListener('click', ner);
    let vipo = true
    function ner(){
        if (vipo === true){
        newPost.style.setProperty("text-decoration", "line-through");
        vipo = false;
        vip.innerHTML = `
        <img src="img/done1.png" style="height: 25px; width: 20px;" class="donebut" id ="done">
        `
        }
        else if (vipo === false){
            newPost.style.setProperty('text-decoration', 'none');  
            vipo = true
            vip.innerHTML = `
        <img src="img/done2.png" style="height: 25px; width: 20px;" class="donebut" id ="done">
        `
        }
    }

    let edite = document.createElement('div');
    edite.innerHTML = `
    <img src="img/edit.png" style="height: 25px; width: 20px;" class="editbut" id ="edit">
    `
    edite.addEventListener('click',rodek );
    function rodek(){ 
        
        let input = document.createElement('input');
        if(input.length < 3) {
        
          alert("Вы некорректно ввели задача, должно быть от 3 символов")
          return
      }
        item.append(input)  
        input.type = 'text'
        input.value = newPost.textContent
        
        item.insertBefore(input, newPost)
        item.removeChild(newPost);
        

        let save = document.createElement('div')
        item.append(save)
        save.innerHTML = `
        <img src="img/done.png" style="height: 25px; width: 20px;" class="donebut" id ="done">
        `
        
        save.addEventListener('click', op);
        function op(){
          
                newPost.textContent = input.value
                item.insertBefore(newPost, input)
                
                input.parentElement.removeChild(input);
                save.parentElement.removeChild(save);
                newPost.append(vip)
        }     
       
    }

   
    
    let change = document.createElement('div');
    change.innerHTML = `
    <img src="img/change.png" style="height: 25px; width: 20px;" class="changbut" id ="change">
    `
    change.addEventListener('click', olik);
    
    
    function olik(){
      if (newPost.style.color === 'black'){
        newPost.style.color = 'red'
      }else if (newPost.style.color === 'red'){
        newPost.style.color = 'green'}
      else if (newPost.style.color === 'green'){
        newPost.style.color = 'blue'}
      else if (newPost.style.color === 'blue'){
        newPost.style.color = 'black'
      }  
        
    }
    
    let fonti = document.createElement('div');
    fonti.innerHTML = `
    <img src="img/font.png" style="height: 25px; width: 20px;" class="fontbut" id ="fonti">
    `
    fonti.addEventListener('click', fork);
    
    
    function fork(){
      if (newPost.style.fontFamily === 'Times New Roman, Times, serif'){
        newPost.style.fontFamily = 'Verdana, Geneva, Tahoma, sans-serif'
      }else if (newPost.style.fontFamily === 'Verdana, Geneva, Tahoma, sans-serif'){
        newPost.style.fontFamily = 'Open Sans, sans-serif'
      }else if (newPost.style.fontFamily === 'Open Sans, sans-serif'){
        newPost.style.fontFamily = 'Times New Roman, Times, serif'
      }
       
        
    }

    item.append(newPost)
    item.append(newTask)
    item.append(edite)
    item.append(change)
    item.append(fonti)
    b.appendChild(item)

})