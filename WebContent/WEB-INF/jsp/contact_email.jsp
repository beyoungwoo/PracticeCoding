<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="contact form example">
    <title>Contact Email</title>
</head>

<body>

  <h2 class="content-head is-center">Contact</h2>
  <aside>
       <p>
           Message와 E-mail Address 입력한 후에 <em>Send</em>
       </p>
   </aside>
  <!--
  <aside>
       <p>
           We would <em>love</em> to hear from you! </p>
           <p>Please use the <b><em>Contact Form</em></b>
           to send us a message.
       </p>
   </aside>
   -->

<!-- START HERE -->
   <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.6.0/pure-min.css">
   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
   <!-- Style The Contact Form How Ever You Prefer -->
   <link rel="stylesheet" href="https://cdn.rawgit.com/dwyl/html-form-send-email-via-google-script-without-server/master/style.css">

  <form id="gform" method="POST" class="pure-form pure-form-stacked"
  action="https://script.google.com/macros/s/AKfycbxXJlLfS6JC_x_-96t7UURpA89xvBp5PbRpaVKm_rhcJr3ol0s/exec">
    <!-- change the form action to your script url -->
<!-- 
    <fieldset class="pure-group">
      <label for="name">Name: </label>
      <input id="name" name="name" placeholder="What your Mom calls you" />
    </fieldset>
-->
    <fieldset class="pure-group">
      <label for="message">Message: </label>
      <textarea id="message" name="message" rows="10"
      placeholder="Write message ..."></textarea>
    </fieldset>

    <fieldset class="pure-group">
      <label for="email"><em>Your</em> Email Address:</label>
      <input id="email" name="email" type="email" value=""
      required placeholder="your.name@email.com"/>
      <span id="email-invalid" style="visibility:hidden">
        Must be a valid email address</span>
    </fieldset>

<!--
    <fieldset class="pure-group">
      <label for="color">Favourite Color: </label>
      <input id="color" name="color" placeholder="green" />
    </fieldset>
-->
    <button class="button-success pure-button button-xlarge">
      <i class="fa fa-paper-plane"></i>&nbsp;Send</button>

  </form>

  <!-- Customise the Thankyou Message People See when they submit the form: -->
  <div style="display:none;" id="thankyou_message">
    <h2><em>Thanks</em></h2>
  <!--
    <h2><em>Thanks</em> for contacting us!
      We will get back to you soon!</h2>
  -->
  </div>


  <!-- Submit the Form to Google Using "AJAX" -->
  <script data-cfasync="false" type="text/javascript"
  src="https://cdn.rawgit.com/dwyl/html-form-send-email-via-google-script-without-server/master/form-submission-handler.js"></script>
  <!-- <script data-cfasync="false" type="text/javascript"
  src="/form-submission-handler.js"></script> -->
<!-- END -->



</form>

</body>
</html>