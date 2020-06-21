function submit(){
    var prompt = document.getElementById("prompt")
    var promptText = prompt.childNodes[0].textContent
    
    var button = document.getElementById("button")
    var spinner = document.getElementById("spinner")
    
    button.hidden = true;
    spinner.hidden = false;
    $.ajax({
        type: 'POST',
        url: "https://api.deepsalvini.club/generate",
        data: {prompt: promptText},
        success: function(result){
            button.hidden = false;
            spinner.hidden = true;
            $(prompt).html(
                promptText+"<b>"+result.substring(promptText.length)+"</b>"
            )
        }
    })
}

function init(){
    var min=1000;
    var max=10000;

    document.getElementById("replies").textContent = Math.floor(Math.random()*(max - min) + min).toString()
    document.getElementById("retweets").textContent = Math.floor(Math.random()*(max - min) + min).toString()
    document.getElementById("likes").textContent = Math.floor(Math.random()*(max - min) + min).toString()
}