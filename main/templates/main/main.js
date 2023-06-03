window.onload = () => {
    let input = document.querySelector('#input');
    input.oninput = function() {
        let value = this.value.trim();
        let list = document.querySelectorAll('.ul li');
        
        if(value != '') {
            list.forEach(elem => {
                if(elem.innerText.search(value) == -1) {
                    elem.classList.add('hide');
                }
            });
        } else {
            list.forEach(elem => {
                elem.classList.remove('hide');
            });
        }
        console.log(this.value);
    };
};





function search() {
    // Получаем значение введенное пользователем в поисковую строку
    const searchTerm = document.getElementById("search-input").value.toLowerCase();
  
    // Получаем список элементов, которые мы будем искать
    const itemsToSearch = document.querySelectorAll(".searchable");
  
    // Очищаем список результатов поиска
    const searchResults = document.getElementById("search-results");
    searchResults.innerHTML = "";
  
    // Проходим по каждому элементу, который мы ищем
    itemsToSearch.forEach((item) => {
      // Получаем текстовое содержимое элемента
      const itemText = item.textContent.toLowerCase();
  
      // Проверяем, содержит ли текстовое содержимое элемента искомую строку
      if (itemText.includes(searchTerm)) {
        // Если да, то создаем новый элемент li и добавляем его в список результатов поиска
        const li = document.createElement("li");
        li.textContent = itemText;
        searchResults.appendChild(li);
      }
    });
  }
  