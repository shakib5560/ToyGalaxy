(function($) { 
  
  "use strict";

  // Preloader
  function stylePreloader() {
    $('body').addClass('preloader-deactive');
  }

  // Background Image
  $('[data-bg-img]').each(function() {
    $(this).css('background-image', 'url(' + $(this).data("bg-img") + ')');
  });

  // Off Canvas JS
  var canvasWrapper = $(".off-canvas-wrapper");
  $(".btn-menu").on('click', function() {
    canvasWrapper.addClass('active');
  });
  $(".close-action > .btn-close, .off-canvas-overlay").on('click', function() {
    canvasWrapper.removeClass('active');
  });

  //Responsive Slicknav JS
  $('.main-menu').slicknav({
    appendTo: '.res-mobile-menu',
    closeOnClick: true,
    removeClasses: true,
    closedSymbol: '<i class="fa fa-angle-down"></i>',
    openedSymbol: '<i class="fa fa-angle-up"></i>'
  });

  // Search Box JS
  var searchwrapper = $(".search-box-wrapper");
  $(".btn-search-menu").on('click', function() {
    searchwrapper.addClass('show');
    $("#search-input").focus();
  });
  $(".search-close").on('click', function() {
    searchwrapper.removeClass('show');
  });




// Product Quick View JS
var quickViewModal = $(".product-quick-view-modal");

$(".product-action .action-quick-view").on("click", function () {
  const slug = $(this).data("slug"); // Get the slug from the clicked button
  const url = `/product-details/${slug}/`;

  // Fetch product details
  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      // Update product image
      const productImage = data.image || "assets/img/shop/default.jpg";
      $(".product-quick-view-modal .thumb img").attr("src", productImage);

      // Update product name
      $(".product-quick-view-modal .title").text(data.name);

      // Update product price and offer
      const priceText = data.offer ? `$${data.offer}` : `$${data.price}`;
      $(".product-quick-view-modal .price").text(priceText);

      // Update product description
      $(".product-quick-view-modal .product-desc").text(data.description || "No description available.");

      // Update SKU
      $(".product-quick-view-modal .widget .sku").text(data.sku || "N/A");

      // Update category
      $(".product-quick-view-modal .widget-tags .categories").text(data.category || "Uncategorized");

      // Update ratings
      const ratingContainer = $(".product-quick-view-modal .rating");
      ratingContainer.empty(); // Clear existing stars
      if (data.average_rating) {
        for (let i = 1; i <= 5; i++) {
          const starClass = i <= data.average_rating ? "fa fa-star" : "fa fa-star-o";
          ratingContainer.append(`<span class="${starClass}"></span>`);
        }
      } else {
        for (let i = 1; i <= 5; i++) {
          ratingContainer.append('<span class="fa fa-star-o"></span>');
        }
      }

      // Update support and money return status
      const featuresList = $(".product-quick-view-modal .single-product-featured ul");
      featuresList.empty();
      if (data.support_24_7) {
        featuresList.append('<li><i class="fa fa-check"></i> Support 24/7</li>');
      }
      if (data.money_return) {
        featuresList.append('<li><i class="fa fa-check"></i> Money Return</li>');
      }
      if (data.delivery) {
        featuresList.append(`<li><i class="fa fa-check"></i>${data.delivery} Delivery</li>`);
      }      

      // Show modal
      quickViewModal.addClass("active");
      $("body").addClass("fix");
    })
    .catch((error) => {
      console.error("Error fetching product details:", error);
      alert("Unable to load product details. Please try again later.");
    });
});

// Close modal on close button or overlay click
$(".btn-close, .canvas-overlay").on("click", function () {
  quickViewModal.removeClass("active");
  $("body").removeClass("fix");
});



// Close modal
$(".btn-close, .canvas-overlay").on("click", function () {
  quickViewModal.removeClass("active");
  $("body").removeClass("fix");
});

// Close modal
$(".btn-close, .canvas-overlay").on("click", function () {
  quickViewModal.removeClass("active");
  $("body").removeClass("fix");
});

  // Sidebar Cart JS
  var sidebarCartModal = $(".sidebar-cart-modal");
  $(".cart-icon").on('click', function() {
    sidebarCartModal.addClass('sidebar-cart-active');
    $(".sidebar-cart-overlay").addClass('show');
  });
  $(".sidebar-cart-content .cart-close").on('click', function() {
    sidebarCartModal.removeClass('sidebar-cart-active');
    $(".sidebar-cart-overlay").removeClass('show');
  });

  // Checkout Toggle Active
  $('.checkout-coupon-active').on('click', function(e) {
    e.preventDefault();
    $('.checkout-coupon-content').slideToggle(1000);
  });

  // Swipper JS

  // Home Two Slider
  var swiper = new Swiper('.home-slider-container', {
    slidesPerView: 1,
    loop: true,
    spaceBetween: 0,
    effect: 'fade',
    fadeEffect: {
      crossFade: true,
    },
  });

  // Gallery Trends Slider
  var swiper = new Swiper('.product-category1-slider-container', {
    slidesPerView: 3,
    slidesPerGroup: 1,
    loop: true,
    spaceBetween : 30,
    breakpoints: {
      1500:{
          slidesPerView : 3
      },

      992:{
          slidesPerView : 3
      },

      768:{
          slidesPerView : 2
      },

      625:{
          slidesPerView : 2,
          spaceBetween : 15,
      },

      0:{
          slidesPerView : 1
      }
    }
  });

  // Brand Slider
  var swiper = new Swiper('.brand-logo-slider-container', {
    slidesPerView : 6,
    loop: true,
    speed: 1000,
    spaceBetween : 0,
    autoplay: false,
    breakpoints: {
      1200:{
          slidesPerView : 6
      },

      992:{
          slidesPerView : 4,
          spaceBetween : 30
      },

      768:{
          slidesPerView : 3,
          spaceBetween : 30

      },

      576:{
          slidesPerView : 3,
          spaceBetween : 30
      },

      380:{
          slidesPerView : 2,
          spaceBetween : 30
      },

      0:{
          slidesPerView : 2,
          spaceBetween : 30
      }
    }
  });

  // Swipper JS
  var swiper = new Swiper('.product4-slider-container', {
    slidesPerView: 4,
    loop: true,
    spaceBetween : 30,
    autoplay: {
      delay: 4000,
    },
    navigation: {
      nextEl: '.product4-slider-container .swiper-button-next',
      prevEl: '.product4-slider-container .swiper-button-prev',
    },
    breakpoints: {
      1200:{
          slidesPerView : 4
      },

      992:{
          slidesPerView : 3
      },

      768:{
          slidesPerView : 2

      },

      576:{
          slidesPerView : 2
      },

      0:{
          slidesPerView : 1
      }
    }
  });

  var ProductNav = new Swiper('.single-product-nav-slider', {
    spaceBetween: 11,
    slidesPerView: 3,
    freeMode: true,
    navigation: {
      nextEl: '.single-product-nav-slider .swiper-button-next',
      prevEl: '.single-product-nav-slider .swiper-button-prev',
    },
  });

  var ProductThumb = new Swiper('.single-product-thumb-slider', {
    freeMode: true,
    effect: 'fade',
    fadeEffect: {
      crossFade: true,
    },
    thumbs: {
      swiper: ProductNav
    }
  });

  // Gallery Trends Slider
  var swiper = new Swiper('.testimonial-slider-container', {
    slidesPerView: 3,
    slidesPerGroup: 1,
    loop: true,
    spaceBetween : 40,
    breakpoints: {
      1500:{
          slidesPerView : 3,
          spaceBetween : 40
      },

      992:{
          slidesPerView : 3,
          spaceBetween : 30
      },

      768:{
          slidesPerView : 2,
          spaceBetween : 30
      },

      620:{
          slidesPerView : 2,
          spaceBetween : 15,
      },

      0:{
          slidesPerView : 1
      }
    }
  });

  $('.product-tab1-slider').slick({
    dots: false,
    speed: 300,
    slidesToShow: 4,
    slidesToScroll: 1,
    arrows: true,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2
        }
      },
      {
        breakpoint: 520,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
    ]
  });

  $('.testimonial-slider').slick({
    dots: false,
    infinite: true,
    speed: 300,
    slidesToShow: 3,
    slidesToScroll: 1,
    arrows: false,
    responsive: [
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
          infinite: true
        }
      },
      {
        breakpoint: 576,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
    ]
  });

  // Fancybox Js
  $('.lightbox-image').fancybox();
  // Isotope and data filter
  function isotopePortfolio() {
    var $grid = $('.masonry-grid').isotope({
      itemSelector: '.masonry-item',
      masonry: {
        columnWidth: 1
      }
    })
    // Isotope Masonry
    var $gridMasonry = $('.masonry-style').isotope({
      itemSelector: '.masonry-item'
    })
    // Isotope filter Menu
    $('.portfolio-filter-menu').on( 'click', 'button', function() {
      var filterValue = $(this).attr('data-filter');
      $grid.isotope({ filter: filterValue });
      $gridMasonry.isotope({ filter: filterValue });
      var filterMenuactive = $(".portfolio-filter-menu button");
      filterMenuactive.removeClass('active');
      $(this).addClass('active');
    });
  }
  
  // Images Zoom
  $('.zoom-hover').zoom();

  // Countdown JS
  var now = new Date();
  var day = now.getDate();
  var month = now.getMonth() + 1;
  var year = now.getFullYear() + 1;
  var nextyear = month + '/' + day + '/' + year + ' 07:07:07';

  $('.countdown-timer').countdown({
    date: '1/2/2022 23:59:59', // TODO Date format: 07/27/2017 17:00:00
    offset: +2, // TODO Your Timezone Offset
    day: 'Day',
    days: 'Days',
    hideOnComplete: true
  }, function (container) {
    console.log('Done!');
  });

  //Shop review btn
  $(".review-write-btn").on('click', function() {
    $(".product-review-form").toggle('active');
  });

  // Product Qty
  var proQty = $(".pro-qty");
  proQty.append('<a href="#" class="inc qty-btn"><i class="fa fa-plus"></i></a>');
  proQty.append('<a href="#" class= "dec qty-btn"><i class="fa fa-minus"></i></a>');
  $('.qty-btn').on('click', function(e) {
    e.preventDefault();
    var $button = $(this);
    var oldValue = $button.parent().find('input').val();
    if ($button.hasClass('inc')) {
      var newVal = parseFloat(oldValue) + 1;
    } else {
      // Don't allow decrementing below zero
      if (oldValue > 1) {
        var newVal = parseFloat(oldValue) - 1;
      } else {
        newVal = 1;
      }
    }
    $button.parent().find('input').val(newVal);
  });

  // Product Qty
  var proQty2 = $(".pro-qty-style2");
  proQty2.append('<a href="#" class="inc qty-btn"><i class="fa fa-plus"></i></a>');
  proQty2.append('<a href="#" class= "dec qty-btn"><i class="fa fa-window-minimize"></i></a>');
  $('.qty-btn').on('click', function(e) {
    e.preventDefault();
    var $button2 = $(this);
    var oldValue2 = $button2.parent().find('input').val();
    if ($button2.hasClass('inc')) {
      var newVal2 = parseFloat(oldValue2) + 1;
    } else {
      // Don't allow decrementing below zero
      if (oldValue2 > 1) {
        var newVal2 = parseFloat(oldValue2) - 1;
      } else {
        newVal2 = 1;
      }
    }
    $button2.parent().find('input').val(newVal2);
  });

  //Checkout Page Checkbox Accordion
  $("#create_pwd").on("change", function() {
    $(".account-create").slideToggle("100");
  });

  $("#ship_to_different").on("change", function() {
    $(".ship-to-different").slideToggle("100");
  });

  $('.checkout-toggle').on('click', function() {
    $('.open-toggle').slideToggle(1000);
  });

  var checked = $( '.sin-payment input:checked' )
  if(checked){
    $(checked).siblings( '.payment-box' ).slideDown(900);
  };
 $( '.sin-payment input' ).on('change', function() {
    $( '.payment-box' ).slideUp(900);
    $(this).siblings( '.payment-box' ).slideToggle(900);
  });

  //Tippy Tooltip JS
  tippy('.ht-tooltip', {
    inertia: true,
    animation: 'shift-away',
    arrow: true
  });

  // Scroll Top Hide Show
  var varWindow = $(window);
  varWindow.on('scroll', function(){
    if ($(this).scrollTop() > 250) {
      $('.scroll-to-top').fadeIn();
    } else {
      $('.scroll-to-top').fadeOut();
    }

    // Sticky Header
    if($('.sticky-header').length){
      var windowpos = $(this).scrollTop();
      if (windowpos >= 80) {
        $('.sticky-header').addClass('sticky');
      } else {
        $('.sticky-header').removeClass('sticky');
      }
    }
  });

  // Ajax Contact Form JS
  var form = $('#contact-form');
  var formMessages = $('.form-message');

  $(form).submit(function(e) {
    e.preventDefault();
    var formData = form.serialize();
    $.ajax({
        type: 'POST',
        url: form.attr('action'),
        data: formData
    }).done(function(response) {
        // Make sure that the formMessages div has the 'success' class.
        $(formMessages).removeClass('alert alert-danger');
        $(formMessages).addClass('alert alert-success fade show');

        // Set the message text.
        formMessages.html("<button type='button' class='btn-close' data-bs-dismiss='alert'>&times;</button>");
        formMessages.append(response);

        // Clear the form.
        $('#contact-form input,#contact-form textarea').val('');
    }).fail(function(data) {
        // Make sure that the formMessages div has the 'error' class.
        $(formMessages).removeClass('alert alert-success');
        $(formMessages).addClass('alert alert-danger fade show');

        // Set the message text.
        if (data.responseText === '') {
            formMessages.html("<button type='button' class='btn-close' data-bs-dismiss='alert'>&times;</button>");
            formMessages.append(data.responseText);
        } else {
            $(formMessages).text('Oops! An error occurred and your message could not be sent.');
        }
    });
  });

  //Scroll To Top
  $('.scroll-to-top').on('click', function(){
    $('html, body').animate({scrollTop : 0},800);
    return false;
  });

  // Reveal Footer JS
  let revealId = $(".reveal-footer"),
    footerHeight = revealId.outerHeight(),
    windowWidth = $(window).width(),
    windowHeight = $(window).outerHeight(),
    leftFixedHeader = $("header.fixed-left"),
    leftFixedHeaderWidth = leftFixedHeader.innerWidth();

  if (windowWidth > 991 && windowHeight > footerHeight) {
    $(".site-wrapper-reveal").css({
      'margin-bottom': footerHeight + 'px'
    });
  }
  
  

document.addEventListener("DOMContentLoaded", function () {
    // Select all alert elements
    const alerts = document.querySelectorAll(".alert");

    // Set a timeout to automatically hide each alert after 3 seconds
    alerts.forEach((alert) => {
        setTimeout(() => {
            alert.classList.add("fade");
            alert.addEventListener("transitionend", () => {
                alert.remove();
            });
        }, 3000);
    });
});

  
/* ==========================================================================
   When document is loading, do
   ========================================================================== */
  
  varWindow.on('load', function() {
    isotopePortfolio();
    AOS.init({
      once: true,
    });
    stylePreloader();
  });
  

})(window.jQuery);