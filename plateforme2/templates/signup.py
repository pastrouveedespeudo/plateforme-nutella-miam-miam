{% include "navbarre.html" %}

{% block content %}
{% endblock %}




  <header class="masthead text-center d-flex"></header>


  


  <section class="bg-primary" id="about">
      <div style="text-align:center">
        <form method="POST">
            {% csrf_token%}
            
             &nbsp;&nbsp;&nbsp;&nbsp;<strong>Ton pseudo :</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
             &nbsp;{{form.username}}

             <br><br>
             
            &nbsp;&nbsp;&nbsp;&nbsp<strong>Ton email : </strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{form.email}}
            
            <br><br>
            
            &nbsp;&nbsp;&nbsp;&nbsp<strong>Confirme le : </strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp
            &nbsp;{{form.email2}}
            
            <br><br>
            
            
            <strong>Et ton password </strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            {{form.password}}

            <br><br><br>
            
            &nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp<input type="submit" style="color:black;"/>
        </form>
        </div>
  </section>




  <section id="contact">
  
    <div class="container">
      <div class="row">
        <div class="col-lg-8 mx-auto text-center">
        
          <h2 class="section-heading">Contactez - nous !</h2>
          
          <hr class="my-4">
          
          <p class="mb-5" id="contactP">Un produit sain c'est bien ! Un produit merveilleux c'est encore MIEUX !</p>
          
        </div>
        
      </div>


      
      <div class="row">
      
        <div class="col-lg-4 ml-auto text-center">
        
          <i class="fas fa-phone fa-3x mb-3 sr-contact-1"></i>
          <img class="phone" id="phone" src="/static/img/portfolio/bas/phone.png">
          <p>123-456-6789</p>
          
        </div>

        
        <div class="col-lg-4 mr-auto text-center">
        
          <i class="fas fa-envelope fa-3x mb-3 sr-contact-2"></i>
          
          <img class="mail" id="mail" src="/static/img/portfolio/bas/mail.png">
          <p>
            <a href="mailto:your-email@your-domain.com">feedback@startbootstrap.com</a>
          </p>
        </div>


      </div>
    </div>
  </section>


    
  <hr color:black>
  <nav class="navbar navbar-expand-lg navbar-light fixed-bot" id="mainNav">
  
    <div class="container">

        <div class="mentions">
          <a class="compte_top_haut_droit" id="compte_top_haut_droit" href="#">Mentions légales</a>
        </div>

          
        <div class="contact">
          <a class="aliments_top_haut_droit" id="aliments_top_haut_droit" href="#">Contact</a>
        </div>

    
    </div>
  </nav>



  


  <!-- Bootstrap core JavaScript -->
  <script src=" /static/vendor/jquery/jquery.min.js"></script>
  <script src="/static/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Plugin JavaScript -->
  <script src="/static/vendor/jquery-easing/jquery.easing.min.js"></script>
  <script src="/static/vendor/scrollreveal/scrollreveal.min.js"></script>
  <script src="/static/vendor/magnific-popup/jquery.magnific-popup.min.js"></script>

  <!-- Custom scripts for this template -->
  <script src="/static/js/creative.min.js"></script>






</body>

</html>

  
  
  <script type = "text/javascript">



</script>




























