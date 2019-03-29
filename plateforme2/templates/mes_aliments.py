<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">

  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">
  
  <title>Colette&Remi</title>

  <!-- Bootstrap core CSS -->
  <link href="/static/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom fonts for this template -->
  <link href="/static/vendor/fontawesome-free/css/all.min.css%22%20rel%3D%22stylesheet" type="text/css">
  <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>
  <link href='https://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic,900,900italic' rel='stylesheet' type='text/css'>

  <!-- Plugin CSS -->
  <link href="/static/vendor/magnific-popup/magnific-popup.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  
  <link href="/static/css/homehome.css" rel="stylesheet">

  
</head>

<body id="page-top">


 
    <style>#inputChercher{
            text-align:center;
            margin-top:12px;
            background: #A9A9A9;
            border: 1px solid;
            font-style:italic;
            }
            #deco{
            background-size: cover;
            margin-left:15px;
            width: 50x;
            height: 50px;
            }
    </style>
    
<form action="/mes_aliments/recherche/" method="POST">
<div class="container-fluid" id="Menu-TOP">
    <div class="row" id="row1">

       <div class="col-md-7" id="block">
       
          <a href='/'>
            <img  id="pur_beurre_logo" src="/static/img/portfolio/menu-haut/pur_beurre.png">
          </a>
          <a  id="nom">Pur Beurre</a>

          
          <div style="font-size:1.75vw;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          Welcome back <strong>lililili !</strong>
        </div>
        

          
       </div>
      
       <div class="col-md-5" id="block2">

           <div id="droiteMenuTop">
           
               <a>
                 <input id="inputChercher" name="cool" type="text" placeholder="Chercher"/>
                 <input type="hidden" name="csrfmiddlewaretoken" value="bCtZTFV70xhmA8Sil8QTCi1e7rleYFDGJznqHWb6wdrs8z0vpsjBW11QuZAK5leH">
                 <input type="submit" style="background:#a6a6a6;">
                 <input type="hidden" name="csrfmiddlewaretoken" value="bCtZTFV70xhmA8Sil8QTCi1e7rleYFDGJznqHWb6wdrs8z0vpsjBW11QuZAK5leH">
               </a>
               
               
               <a href='/accounts/mon_compte' OnMouseOver="document.all.texte.innerText='Mon compte !'">
                 <img id="compte" src="/static/img/portfolio/menu-haut/compte.png">
               </a>

               <a href='/mes_aliments/mes_aliments' OnMouseOver="document.all.texte.innerText='Mes Aliments !'">
                 <img id="carotte" src="/static/img/portfolio/menu-haut/carotte.png"
               </a>
               

               
               

               <a href='#' OnMouseOver="document.all.texte.innerText='Aide !'">
                 <img id="login" src="/static/img/portfolio/menu-haut/aide.png"
               </a>
               
               <a href='/accounts/logout_view' OnMouseOver="document.all.texte.innerText='Se deconnecter !'">
                 <img id="deco" src="/static/img/portfolio/menu-haut/deco.png">
               </a>
               
               
               <center><p id="texte"><br></p></center>

           </div>
       </div>
       
    </div>
    </div>
  </form>





<link href="/static/css/recherche.css" rel="stylesheet">
<body id="page-top">

  <style>
    header.masthead {
    padding-top: 10rem;
    padding-bottom: calc(10rem - 56px);
    background-image: url("/static/img/header1.jpg");
    background-position: center center;
    background-size: cover;
    }
  </style>
  

  
  <style>
  .titreUn{
    color: rgba(51, 51, 0);
    background-color: rgba(255, 153, 102);
    margin-top:200px;
  }



  #nomAliment1,
  #nomAliment2,
  #nomAliment3,
  #nomAliment4,
  #nomAliment5,
  #nomAliment6{
    text-align:center;
  }  



  
  </style>

  <header class="masthead text-center d-flex">
    <div class="container my-auto">
      <div class="row">
        <div class="col-lg-10 mx-auto">
          <h1 class="titreUn">
            <strong>Mes aliments</strong>
          </h1>
          <hr>
        </div>
        </div>
      </div>
    </div>
  </header>


   
    <section class="bg-primary" id="about">

    
    
     
     
    <div class="container-fluid" id="conteneurCarre">
       <div class="row" id="row3">
    
           <div class="col-sm-12 col-md-4" id="block4">
               <div id="rond"><img src=></div>
 
               <style>
                    #im11{
                      padding:10px;
                      width: 240px;
                      height: 250px;
                    }

                    #save{
                      text-align:center;
                    }
               </style>

               
                   <form action="/mes_aliments/recherche/" method="POST">
                     <input type="hidden" name="csrfmiddlewaretoken" value="bCtZTFV70xhmA8Sil8QTCi1e7rleYFDGJznqHWb6wdrs8z0vpsjBW11QuZAK5leH">

                     <input type="HIDDEN" value= name="produit">
                     <div id="im1"><input type="image" id="im11" class="fit-picture" src=""/></a></div>
                   
                     <div id="nomAliment1"></div>

                    <br>
                  </form>
             
                  
           </div>

           
           <div class="col-sm-12 col-md-4" id="block4">

               <div id="rond"><img src=></div>
                <form action="/mes_aliments/recherche" method="POST">
                     <input type="hidden" name="csrfmiddlewaretoken" value="bCtZTFV70xhmA8Sil8QTCi1e7rleYFDGJznqHWb6wdrs8z0vpsjBW11QuZAK5leH">

               <input type="HIDDEN" value= name="produit">
                <div id="im2"><input type="image" id="im11" value= class="fit-picture" src=""/></a></div>
               
              
               <div id="nomAliment2"></div>

              
             
             </form>
         
           </div>
           
           <div class="col-sm-12 col-md-4" id="block4">

               <div id="rond"><img src=></div>
               
             <form action="/mes_aliments/recherche/" method="POST">
                     <input type="hidden" name="csrfmiddlewaretoken" value="bCtZTFV70xhmA8Sil8QTCi1e7rleYFDGJznqHWb6wdrs8z0vpsjBW11QuZAK5leH">

               <input type="HIDDEN" value= name="produit">
                <div id="im3"><input type="image" id="im11" value= class="fit-picture" src=""/></a></div>
               
              
               <div id="nomAliment2"></div>

             </form>
               
           </div>
       

           <div class="col-sm-12 col-md-4" id="block4">

                <div id="rond"><img src=></div>
                
              <form action="/mes_aliments/recherche" method="POST">
                     <input type="hidden" name="csrfmiddlewaretoken" value="bCtZTFV70xhmA8Sil8QTCi1e7rleYFDGJznqHWb6wdrs8z0vpsjBW11QuZAK5leH">

               <input type="HIDDEN" value= name="produit">
                <div id="im4"><input type="image" id="im11" value= class="fit-picture" src=""/></a></div>
               
              
               <div id="nomAliment2"></div>

    
             </form>
                
           </div>

           
           <div class="col-sm-12 col-md-4" id="block4">
               <div id="rond"><img src=></div>
            
                <form action="/mes_aliments/recherche" method="POST">
                     <input type="hidden" name="csrfmiddlewaretoken" value="bCtZTFV70xhmA8Sil8QTCi1e7rleYFDGJznqHWb6wdrs8z0vpsjBW11QuZAK5leH">

               <input type="HIDDEN" value= name="produit">
                <div id="im5"><input type="image" id="im11" value= class="fit-picture" src=""/></a></div>
               
              
               <div id="nomAliment2"></div>


             </form>
               
           </div>
           
           <div class="col-sm-12 col-md-4" id="block4">

               <div id="rond"><img src=></div>
               
              <form action="/mes_aliments/recherche" method="POST">
                     <input type="hidden" name="csrfmiddlewaretoken" value="bCtZTFV70xhmA8Sil8QTCi1e7rleYFDGJznqHWb6wdrs8z0vpsjBW11QuZAK5leH">

               <input type="HIDDEN" value= name="produit">
                <div id="im6"><input type="image" id="im11" value= class="fit-picture" src=""/></a></div>
               
              
               <div id="nomAliment2"></div>

 
             </form>
               
           
         </div>

           <div class="col-sm-12 col-md-4" id="block4">

               <div id="rond"><img src=></div>
               
              <form action="/mes_aliments/recherche" method="POST">
                     <input type="hidden" name="csrfmiddlewaretoken" value="bCtZTFV70xhmA8Sil8QTCi1e7rleYFDGJznqHWb6wdrs8z0vpsjBW11QuZAK5leH">

               <input type="HIDDEN" value= name="produit">
                <div id="im6"><input type="image" id="im11" value= class="fit-picture" src=""/></a></div>
               
              
               <div id="nomAliment2"></div>

 
             </form>
               
           
         </div>


           <div class="col-sm-12 col-md-4" id="block4">

               <div id="rond"><img src=></div>
               
              <form action="/mes_aliments/recherche" method="POST">
                     <input type="hidden" name="csrfmiddlewaretoken" value="bCtZTFV70xhmA8Sil8QTCi1e7rleYFDGJznqHWb6wdrs8z0vpsjBW11QuZAK5leH">

               <input type="HIDDEN" value= name="produit">
                <div id="im6"><input type="image" id="im11" value= class="fit-picture" src=""/></a></div>
               
              
               <div id="nomAliment2"></div>

 
             </form>
               
           
         </div>


           <div class="col-sm-12 col-md-4" id="block4">

               <div id="rond"><img src=></div>
               
              <form action="/mes_aliments/recherche" method="POST">
                     <input type="hidden" name="csrfmiddlewaretoken" value="bCtZTFV70xhmA8Sil8QTCi1e7rleYFDGJznqHWb6wdrs8z0vpsjBW11QuZAK5leH">

               <input type="HIDDEN" value= name="produit">
                <div id="im6"><input type="image" id="im11" value= class="fit-picture" src=""/></a></div>
               
              
               <div id="nomAliment2"></div>

 
             </form>
               
           
         </div>


           <div class="col-sm-12 col-md-4" id="block4">

               <div id="rond"><img src=></div>
               
              <form action="/mes_aliments/recherche" method="POST">
                     <input type="hidden" name="csrfmiddlewaretoken" value="bCtZTFV70xhmA8Sil8QTCi1e7rleYFDGJznqHWb6wdrs8z0vpsjBW11QuZAK5leH">

               <input type="HIDDEN" value= name="produit">
                <div id="im6"><input type="image" id="im11" value= class="fit-picture" src=""/></a></div>
               
              
               <div id="nomAliment2"></div>

 
             </form>
               
           
         </div>





           <div class="col-sm-12 col-md-4" id="block4">

               <div id="rond"><img src=></div>
               
              <form action="/mes_aliments/recherche" method="POST">
                     <input type="hidden" name="csrfmiddlewaretoken" value="bCtZTFV70xhmA8Sil8QTCi1e7rleYFDGJznqHWb6wdrs8z0vpsjBW11QuZAK5leH">

               <input type="HIDDEN" value= name="produit">
                <div id="im6"><input type="image" id="im11" value= class="fit-picture" src=""/></a></div>
               
              
               <div id="nomAliment2"></div>

 
             </form>
               
           
         </div>


           <div class="col-sm-12 col-md-4" id="block4">

               <div id="rond"><img src=></div>
               
              <form action="/mes_aliments/recherche" method="POST">
                     <input type="hidden" name="csrfmiddlewaretoken" value="bCtZTFV70xhmA8Sil8QTCi1e7rleYFDGJznqHWb6wdrs8z0vpsjBW11QuZAK5leH">

               <input type="HIDDEN" value= name="produit">
                <div id="im6"><input type="image" id="im11" value= class="fit-picture" src=""/></a></div>
               
              
               <div id="nomAliment2"></div>

 
             </form>
               
           
         </div>























































            
    </div>
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
  <script src="/static/vendor/jquery/jquery.min.js"></script>
  <script src="/static/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Plugin JavaScript -->
  <script src="/static/vendor/jquery-easing/jquery.easing.min.js"></script>
  <script src="/static/vendor/scrollreveal/scrollreveal.min.js"></script>
  <script src="/static/vendor/magnific-popup/jquery.magnific-popup.min.js"></script>

  <!-- Custom scripts for this template -->
  <script src="/static/js/creative.min.js"></script>







</body>

</html>
