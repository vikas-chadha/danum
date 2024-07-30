$(document).ready(function(){
    $('form').on('submit', function(event){
        event.preventDefault();
        $.ajax({
            url: "/contact/",
            type: "POST",
            data: $(this).serialize(),
            success: function(data){
                if(data.success){
                    $('#thankYouModal').addClass('show');
                    $('#thankYouModal').css("display", "block");;
                } else {
                    console.log(data)
                }
            }
        });
    });

    $('#closeModal').on('click', function(){
        $('#thankYouModal').hide();
        $('form')[0].reset();
        location.reload();
    });
});