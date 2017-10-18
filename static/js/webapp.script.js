/** Created By: Ben Richardson September 18, 2017 **/
$(document).ready(function() {
  console.log("loaded");
  $.material.init();

   // Submit Registration
  $(document).on("submit", "#register-form", function(e) {
    e.preventDefault();
    var form = $('#register-form').serialize();
    console.log(form)
    $.ajax({
      url: "/postreg",
      type: "POST",
      data: form,
      success: function(r){ 
        console.log(r);
      }
    });
  });
  
  //Submit Login
  $(document).on("submit", '#login-form', function(e) {
    console.log("LOGIN FORM SUBMIT!!")
    e.preventDefault();
    
    var form = $(this).serialize();
    $.ajax({
      url: 'check-login',
      type: 'POST',
      data: form,
      success: function(res) {
        if(res == "error") {
          alert("Unable to login./nPlease Check your username and password is correct");
        }
        else {
          console.log("Logged in as", res);
          window.location.href = "/";
        }
      }
    });
  });

  // Do Logout
  $(document).on("click", '#logout-link', function(e) {
    console.log("LOGOUT SUBMIT!!")
    e.preventDefault();
    $.ajax({
      url: 'logout',
      type: 'GET',
      success: function(res) {
        if(res == "success") {
          window.location.href = "/login";
        }
        else {
          alert("Something went *very* wrong!");
        }
      }
    });
  });

  // post post activity
  $(document).on('submit', '#post-activity', function(e) {
    console.log("POST ACTIVITY SUBMITTED");
    //e.preventDefault();
    var form = $(this).serialize();
    console.log(form)
    $.ajax({
      url: '/post-activity',
      type: 'POST',
      data: form,
      success: function(res){
        console.log(res)
      }
    });
  });
  
  $(document).on("submit", "#update-form", function(e) {
    e.preventDefault();
    var form = $('#update-form').serialize();
    console.log(form)
    $.ajax({
      url: "/update-user",
      type: "POST",
      data: form,
      success: function(r){ 
        console.log(r);
      }
    });
  });
  //-----------------------------------------
});
