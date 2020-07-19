if (document.readyState == 'loading') {
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready()
}


function ready() {
        
     var choiceInputs=document.getElementsByClassName('cart-color-choice')
     for (var i = 0; i < choiceInputs.length; i++) {
        var input = choiceInputs[i]
        input.addEventListener('change', colorChange)
    }
}

function colorChange(event) {
    var choiceClicked = event.target

    

    var row=choiceClicked.parentElement.parentElement
    var title=row.getElementsByClassName('cart-item-title')[0].innerText
    

 
    var value=choiceClicked.value
    
    csrfValidation()
      
    $.ajax({
        url:'../updatecolor/',
        data: {
            'color':value,
            'title':title,
        },
        type:'POST',

    }).done(function(response){
        console.log(response)
    })

  
}




function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfValidation(){
    var csrftoken = getCookie('csrftoken');
    console.log(csrftoken)

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


