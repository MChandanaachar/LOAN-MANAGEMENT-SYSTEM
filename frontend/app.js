// =============================
// AUTH STATE
// =============================
let token = localStorage.getItem("token");

window.onload = function () {
    token = localStorage.getItem("token");

    if (token) {
        document.getElementById("loginPage").classList.add("hidden");
        document.getElementById("app").classList.remove("hidden");
    }
};

// =============================
// LOGIN
// =============================
function login() {
    fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            username: username.value,
            password: password.value
        })
    })
    .then(res => res.json())
    .then(data => {

        if (data.token) {

            token = data.token;

            localStorage.setItem("token", token);

            document.getElementById("loginPage").classList.add("hidden");
            document.getElementById("app").classList.remove("hidden");

            show("dashboard");
            getLoans();
        }
    });
}

// =============================
// LOGOUT
// =============================
function logout() {
    localStorage.removeItem("token");
    token = "";
    location.reload();
}

// =============================
// PAGE SWITCH
// =============================
function show(page) {
    document.querySelectorAll(".page").forEach(p => p.classList.add("hidden"));
    document.getElementById(page).classList.remove("hidden");
}

// =============================
// ADD LOAN
// =============================
function addLoan() {

    fetch("http://127.0.0.1:5000/loans", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        },
        body: JSON.stringify({
            customer: document.getElementById("customer").value,
            amount: parseInt(document.getElementById("amount").value),
            status: document.getElementById("status").value
        })
    })
    .then(res => res.json())
    .then(data => {

        alert("Loan Added Successfully");

        document.getElementById("customer").value = "";
        document.getElementById("amount").value = "";
        document.getElementById("status").value = "";

        show("loans");
        getLoans();
    })
    .catch(err => {
        console.log(err);
        alert("Error adding loan");
    });
}

// =============================
// GET LOANS
// =============================
function getLoans() {

    fetch("http://127.0.0.1:5000/loans")
    .then(res => res.json())
    .then(data => {

        let table = "";

        data.forEach(loan => {

            table += `
                <tr>
                    <td>${loan.id}</td>
                    <td>${loan.customer}</td>
                    <td>${loan.amount}</td>
                    <td>${loan.status}</td>
                    <td>
                        <button onclick="editLoan(${loan.id})">Edit</button>
                        <button onclick="deleteLoan(${loan.id})">Delete</button>
                    </td>
                </tr>
            `;
        });

        document.getElementById("loanTable").innerHTML = table;
    });
}

// =============================
// DELETE LOAN
// =============================
function deleteLoan(id) {

    fetch(`http://127.0.0.1:5000/loans/${id}`, {
        method: "DELETE",
        headers: {
            "Authorization": "Bearer " + token
        }
    })
    .then(res => res.json())
    .then(data => {

        alert(data.message);
        getLoans();
    });
}

// =============================
// EDIT / UPDATE LOAN
// =============================
function editLoan(id) {

    let customer = prompt("Enter customer name");
    let amount = prompt("Enter amount");
    let status = prompt("Enter status");

    fetch(`http://127.0.0.1:5000/loans/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        },
        body: JSON.stringify({
            customer: customer,
            amount: parseInt(amount),
            status: status
        })
    })
    .then(res => res.json())
    .then(data => {

        alert(data.message);
        getLoans();
    });
}