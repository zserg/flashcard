console.log("Hello");
var cards;
var idx;
var result;
var post_results = [];
var current_card;

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


answer_bs = '<button type="button" class="btn btn-primary" id="answer-button">Answer</button>';
result_bs = '<button type="button" class="btn btn-primary" id="result-0">0</button> \
             <button type="button" class="btn btn-primary" id="result-1">1</button> \
             <button type="button" class="btn btn-primary" id="result-2">2</button> \
             <button type="button" class="btn btn-primary" id="result-3">3</button> \
             <button type="button" class="btn btn-primary" id="result-4">4</button> \
             <button type="button" class="btn btn-primary" id="result-5">5</button>';

function get_cards (){
    $.ajax({url: 'get_cards/',
            success: function (data){
            console.log(data);
            cards = data;
            console.log(cards.counts);
            post_results.length = 0;
            if (cards.cards.length) {
              current_card = cards.cards.length-1;
              show_card(current_card);
            }else{
              congrat();
            }
          }
       });
}

function show_card (num) {
    console.log(num);
    $('#status').text(cards.count);
    $('#question').html(cards.cards[num].question);
    $('#answer').html('<hr>'+cards.cards[num].answer);
    $('#answer').hide();
    $('#result-row').html(answer_bs);
    $('#answer-button').click(show_answer);
}

function show_answer() {
    $('#answer').show();
    $('#result-row').html(result_bs);
    $('#result-0').click(push_but);
    $('#result-1').click(push_but);
    $('#result-2').click(push_but);
    $('#result-3').click(push_but);
    $('#result-4').click(push_but);
    $('#result-5').click(push_but);
}

function push_but(event) {
 <!-- alert(event.target.id) -->
   switch (event.target.id){
     case 'result-0':
       result = 0;
       break;
     case 'result-1':
       result = 1;
       break;
     case 'result-2':
       result = 2;
       break;
     case 'result-3':
       result = 3;
       break;
     case 'result-4':
       result = 5;
       break;
     case 'result-5':
       result = 5;
       break;
   }
   if (result > 2){
     cards.count--;
   }

   post_results.push({'id': cards.cards[current_card].id,
                      'result': result});
   console.log(post_results);
   next_card();
}


function next_card() {
  if (current_card){
    current_card--;
    show_card(current_card);
  }else{
    console.log(JSON.stringify(post_results));
    $.ajax({url: "get_cards/",
            type: "POST",
            dataType: "json",
            data: JSON.stringify(post_results),
            success: function (result){
                console.log(result);
                get_cards();
            }
    });
  }
}

function congrat() {
 console.log("Congratulations!")
 $('#status').text('0');
 $('#result-row').hide();
 $('#question').text("Congratulations!");
 $('#answer').hide();

}

console.log("1");
get_cards();
