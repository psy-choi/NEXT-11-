const todoForm = document.querySelector(".todo-form");
const todoList = document.querySelector(".todo-list");
const submitBtn = document.querySelector(".submitBtn");

paintTodo();

const deleteBtn = document.querySelector(".delete-button");

function submitAddTodo(event) {
  event.preventDefault(); // 새로고침 방지
  const todo = todoForm.value;

  let list = JSON.parse(window.localStorage.getItem("todo")); // 로컬 스토리지에서 배열로 받아옴
  if (!list) {
    list = []; // 로컬 스토리지에 저장된 배열이 없으면 빈 배열로 초기화
  }
  list.push(todo); // 새로운 todo를 배열에 추가
  window.localStorage.setItem("todo", JSON.stringify(list)); // 수정된 배열을 다시 로컬 스토리지에 저장
  todoForm.value = "";
  paintTodo();
}

function paintTodo() {
  let list = JSON.parse(window.localStorage.getItem("todo"));
  // console.log(list);
  todoList.innerHTML = "";
  for (let i in list) {
    let ol = document.createElement("ol");
    ol.innerHTML =
      `<div>${list[i]}</div>` +
      `<button class="delete-button" type="button" onclick="deleteTodo(event)">x</button>`;
    console.log(list[i]);
    todoList.appendChild(ol);
  }
}

function deleteTodo(event) {
  const button = event.target; // 클릭된 버튼 요소
  const text = button.parentElement.children[0].innerHTML.trim();
  //console.log(text);
  let list = JSON.parse(window.localStorage.getItem("todo"));
  if (list) {
    const updatedList = list.filter((item) => item !== text);
    window.localStorage.setItem("todo", JSON.stringify(updatedList));
  }
  paintTodo();
}

deleteBtn.addEventListener("click", (event) => {
  deleteTodo(event);
});
submitBtn.addEventListener("click", submitAddTodo);
