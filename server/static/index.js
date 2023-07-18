console.log("Inside index");
console.log("hello")

const user_input = document.getElementById("user_input_text");
const user_button = document.getElementById("user_button");
const cont = document.getElementById('Screen')

const append = (message)=>{
    const createDiv = document.createElement('div')
    createDiv.innerText = message;
    cont.append(createDiv);
}

user_button.addEventListener('click',(e)=>{
    e.preventDefault();
    console.log(user_input.value);
    let userInput = user_input.value;

    user_input.value = "";
    socket.emit('message sent',userInput)
    // const fetch_data = ()=>{
    //     fetch('/send',{
    //         cache: "no-cache",
    //         method:'POST',
    //         body:JSON.stringify({text:user_input.value}),
    //         headers:{
    //             'Content-Type': 'application/json',
    //         }
    //     })
    // }
    
    // fetch_data()
    
})

let socket = io();
console.log(socket)
socket.on('connect',()=>{
    console.log("User is connected")
    append("User is connected")
    socket.emit('join')
})

socket.on('new user joined',(user_name)=>{
    append(`${user_name} has joined chat`);
    socket.emit('new user joined',`${user_name} has joined chat`)
})

socket.on('message received',(message)=>{
    append(`${message['user']} :- ${message['mess']}`);
})

