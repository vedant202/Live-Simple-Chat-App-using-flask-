const name = document.getElementById('name');
const roomId =document.getElementById('roomId');
const submit = document.getElementById('user_button')

submit.addEventListener('click',async(e)=>{
    const fetch_data = async()=>{
        const send_data =   fetch('/registerUser',{
            cache: "no-cache",
            method:'POST',
            body:JSON.stringify({
                name:name.value,
                roomId:roomId.value
            }),
            headers:{
                'Content-Type': 'application/json',
            }
        })
        return (await send_data).json();

    }



    const response = await fetch_data()
    console.log(response)
    if(response['response']==='ok'){
        window.location.replace('http://localhost:5000/index')
    }
    

})
