$(document).ready(function(){
    $('.filter').each(function(){
        $(this).on("click", function(){
            $.ajax({
                url: $(this).val(),
                type: "get",
                success: function(response){
                    console.log(response)
                    $('.films').empty();
                    $('.films').html(response)
                }
            })
        })
    })
})