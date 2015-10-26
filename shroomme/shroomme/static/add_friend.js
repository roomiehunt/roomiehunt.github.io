

	$('#add_friend').click(function (e){
		alert(1);
	    e.preventDefault();

		$.ajaxSetup({
		  data: {csrfmiddlewaretoken: '{% csrf_token %}' },
		});


		$.ajax
    	({ 
	        url: '/add_friend/',
	        data: {"test":10,"csrfmiddlewaretoken":'{% csrf_token %}'},
	        type: 'post',
	        success: function()
	        {
	            $('.modal-box').text(result).fadeIn(700, function() 
	            {
	                setTimeout(function() 
	                {
	                    $('.modal-box').fadeOut();
	                }, 2000);
	            });
	        }
	    });

	});

