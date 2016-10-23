

		$(document).ready(function(){
			$(".tab_head>a").on("click",function(){
				$(".tab_head>a").removeClass("active");
				$(this).addClass("active");
				var elmindex = $(this).index();
				var showdiv = $(".tab_body>div.tab_item:eq("+elmindex+")")
				if(showdiv.is(":visible"))
				{
					return;
				}
				$('.tab_body>div.tab_item').hide();
				showdiv.fadeIn(400);	
			});
			
			$("<button class='search_toggle'><i class='fa fa-search'></i></button>").insertBefore(".mynav,.mynav1");
			
			$(".search_toggle, .form_close").click(function(){
				$(".mynav,.mynav1").stop(true,false).slideToggle();
			});
			
			var winwid = $(window).width();
			if (winwid>767) {
				var sscs = $(".full_sub_header").outerHeight();
				$(".full_sub_header").css("min-height",sscs);
			}
			
			
			function showNav(){
				if (winwid<768) {
					$(".nav_toggle").click(function(){
						$(".toggle_box").stop(true,false).slideToggle();
					});
				}
			}
			showNav();
			
			$(window).resize(function() {
				var winwid1 = $(window).width();
				if (winwid1>768) {
					$(".toggle_box").show();
				}
			});
			function rightStop(){
				
					var lefttop = $(".left_content").offset();
					 lefttop = Math.floor(lefttop.top);
					 lefttop-=90;
					 
					 var leftWidth = $(".left_content").width();
					// leftWidth-=30;
					 
					 var pagecontent = $(".index_page_content").offset();
					  pagecontent = Math.floor(pagecontent.top);
					  var pageConHeight = $(".index_page_content").height();
					  var fixedHeight =$(".fixed_bar").height(); 
						fixedHeight = $(".toggle_box").height(); 
					  
					pagecontent = pageConHeight+pagecontent-fixedHeight-210;
					 
					if($(this).scrollTop()>lefttop)
					{
						$(".fixed_bar").css({position:'fixed',top:'90px',bottom:'auto',width:leftWidth});
						if($(this).scrollTop()>pagecontent){
							$(".fixed_bar").css({position:'absolute',top:'auto',bottom:'70px',width:leftWidth});
						}
					}
					else{
						$(".fixed_bar").css({position:'inherit',top:'90px',bottom:'auto',width:'auto'});
					}
					
				
			};
			// if ( $( ".left_content" ).length ) {
				
				// if(winwid>=768){
					// rightStop();
				// }
				
				// $(window).scroll(function(){
					// if(winwid>=768){
						// rightStop();
					// }
					
				// });
			// }
			
			
			function navSc(){
				var offset = $(".itl_head").offset();
				offset = Math.floor(offset.top);
				var height = $(".itl_head").outerHeight();
				offset = offset+height;
				
				if (winwid<767) {
					$(".header_search_box").appendTo(".mynav");
					$(".top_header").css("backgroundColor","rgba(0, 0, 0, 0.7)");
					$(".search_toggle").fadeIn();
					//$(".mynav").fadeOut();
					if($(this).scrollTop() > 2)
					{
						$(".top_header").css("top","0px");
					}
					else
					{
						$(".top_header").css("top","0");
					}
				} 
				else if($(this).scrollTop() > offset){
					$(".header_search_box").appendTo(".mynav");
					$(".top_header").css("backgroundColor","rgba(0, 0, 0, 0.7)");
					$(".search_toggle").fadeIn();
				}
				else{
					$(".header_search_box").appendTo(".full_sub_header>.container");
					$(".top_header").css("backgroundColor","rgba(0, 0, 0, 0.3)");
					$(".search_toggle").fadeOut();
				}
			};
			
			
			if ( $( ".mynav" ).length ) {
				navSc();
				$(window).scroll(function(){
					navSc();
				});
			}
			
			
			function navScPage(){
				
				var offset = 80;
				
				if (winwid<700) {
					
					$(".top_header").css("backgroundColor","rgba(0, 0, 0, 0.7)");
					$(".search_toggle").fadeIn();
					//$(".mynav1").fadeOut();
					if($(this).scrollTop() > 2)
					{
						$(".top_header").css("top","0px");
					}
					else
					{
						$(".top_header").css("top","0");
					}
				} 
				else if($(this).scrollTop() > offset){
					$(".top_header").css("backgroundColor","rgba(0, 0, 0, 0.7)");
					$(".search_toggle").fadeIn();
				}
				else{
					$(".top_header").css("backgroundColor","rgba(0, 0, 0, 0.3)");
					$(".search_toggle").fadeOut();
				}
			};
			if ( $( ".mynav1" ).length ) {
				navScPage();
				$(window).scroll(function(){
					navScPage();
				});
			}
				
			$(".radio_btns_group ul li input").change(function(){
				$(".radio_btns_group ul li").removeClass('active');
				$(this).parent().addClass('active');
			});
			
			
			$('#2').change(function() {
				 $(".Pay_with input").prop('checked',false); 
			});
			$(".Pay_with input").change(function() {
				$('#2').prop('checked',false);
				$('#1').prop('checked',true);
			});
			
			
			
					
			$('.right_toggle_btn').on('click',function(){
				$("#cart_info").css("left","0");
			});
			$('#cart_info>span').on('click',function(){
				$("#cart_info").css("left","100%");
			});
					
			$('.radio_btns_group>ul>li.active>input').prop('checked',true);
			
			$('select.js-states').select2();
			$(".menu_item_foot .right ul li:first-child i").click(function(){
				$(this).toggleClass("active");
			});
			
			if ( $( ".rating" ).length ) {
				$(".rating").starRating({
					minus: true // step minus button
				});
			};
			
			
					
			
				//mobile menu	
//		$(document).ready(function () {
//		
//			$("").hide();
//			$(".show_hide").show();
//		
//			$('.click_hide').click(function () {
//				$(".slide_left").toggle("slide");
//			});
//		
//		});		



		  $("#mobile-nav").click(function(e) {
				 e.stopPropagation();
				 $(".slide").toggleClass("active_slide");
		   });
		  $('html').click(function(){
			  if($(".slide").hasClass('active_slide')){
				  $(".slide").removeClass("active_slide");
			  }
		  });

			
			
			
		});