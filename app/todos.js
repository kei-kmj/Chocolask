const form = document.querySelector('#form');
const input = document.querySelector('#input');
const todos = document.querySelector('#todos');


function loadTodos() {
    fetch('/todos.json')
        .then(response => response.json())
        .then(data => {
            todos.innerHTML = '';
            for (let item of data) {
                const li = document.createElement('li');
                li.textContent = item.task;
                todos.appendChild(li);
            }
        });
};

window.onload = loadTodos;

form.addEventListener('submit', function (event) {
    event.preventDefault();

    const text = input.value;
    input.value = '';

    const todo = {
        id: todos.children.length + 1, 
        task: text,
        completed: false,
    }

    // 新しいTODOアイテムをサーバに送信する
    fetch('/todos.json', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(todo),
    })
    .then(response => {
        if(response.ok){
            loadTodos();
        }else{
            throw new Error('Failed to add new todo')
        }
    })
});
