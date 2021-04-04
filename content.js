document.addEventListener("keyup", function(event) {
    if (event.code === 'Enter') {
        let text = document.getElementsByClassName('_3-8er selectable-text copyable-text')
        var recentText = text.item(text.length - 1).textContent
        pass_values(recentText)
        
    }
    
  });
  function pass_values(data) {
    var pass_to_python = data
 
                 $.ajax(
                 {
                     type:'POST',
                     contentType:'application/json;charset-utf-08',
                     dataType:'json',
                     url:'http://127.0.0.1:5000/pass_val?value='+pass_to_python ,
                     success:function (data) {
                         var reply=data.reply;
                         if (reply=="success")
                         {
                             return;
                         }
                         else
                             {
                             alert("some error ocured in session agent")
                             }
 
                     }
                 }
             );
 }
 