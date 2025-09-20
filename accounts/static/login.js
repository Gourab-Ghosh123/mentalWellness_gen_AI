const form = document.querySelector("form");
const userName = document.querySelector("input[type= 'text");
const password = document.querySelector("input[type='password']");


form.addEventListener("submit", (e) => {
    if(userName.value.trim() === "" || password.value.trim() ==="") {
        e.preventDefault();
        alert("please fill in both Username and Password.");
    }
});

password.addEventListener("input", () =>{
    const strengthText = document.getElementById("strength") || document.createElement("p");
    strengthText.id = "strength";
    password.parentNode.appendChild(strengthText);

    if(password.value.length <6) {
        strengthText.textContent = "Weak password ";
        strengthText.style.color = "red";
    }
})