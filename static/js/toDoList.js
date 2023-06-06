const form = document.getElementById('form');
const input = document.getElementById('input');
const list = document.getElementById('ul');

let tasks = [];

if (localStorage.getItem('tasks')) {
    tasks = JSON.parse(localStorage.getItem('tasks'));
    displayTasks();
}

// Add tasks
form.addEventListener('submit', (event) => {
    event.preventDefault();
    const task = input.value.trim();
    if (task) {
        tasks.push(task);
        localStorage.setItem('tasks', JSON.stringify(tasks));
        displayTasks();
        input.value = '';
    }
});

function displayTasks() {
    list.innerHTML = '';
    for (let i = 0; i < tasks.length; i++) {
        const task = tasks[i];
        const li = document.createElement('li');
        li.innerHTML = task + ' <div class="li-btn"><button data-index="' + i + '">Edit</button> <button data-index="' + i + '">Delete</button></div>';
        list.appendChild(li);
    }
}

// Edit and delete tasks
list.addEventListener('click', (event) => {
    const target = event.target;

    if (target.tagName === 'BUTTON') {
        const index = parseInt(target.dataset.index);

        if (target.textContent === 'Edit') {
            const task = tasks[index];
            const newTask = prompt('Edit task:', task);

            if (newTask) {
                tasks[index] = newTask;
                localStorage.setItem('tasks', JSON.stringify(tasks));
                displayTasks();
            }

        } else if (target.textContent === 'Delete') {
            tasks.splice(index, 1);
            localStorage.setItem('tasks', JSON.stringify(tasks));
            displayTasks();
        }
    }
});
