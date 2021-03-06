{% load static %}

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
            <img  id="pur_beurre_logo" src="{% static 'img/portfolio/menu-haut/pur_beurre.png' %}">
          </a>
          <a  id="nom">Pur Beurre</a>

          {% if user.is_authenticated %}
          <div style="font-size:1.75vw;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          Welcome back <strong>{{user.username}} !</strong>
        </div>
        {% endif %}

          
       </div>
      
       <div class="col-md-5" id="block2">

           <div id="droiteMenuTop">
           
               <a>
                 <input id="inputChercher" name="cool" type="text" placeholder="Chercher"/>
                 {% csrf_token %}
                 <input type="submit" style="background:#a6a6a6;">
                 {% csrf_token %}
               </a>
               
               {% if user.is_authenticated %}
               <a href='/accounts/mon_compte' OnMouseOver="document.all.texte.innerText='Mon compte !'">
                 <img id="compte" src="/static/img/portfolio/menu-haut/compte.png">
               </a>

               <a href='/mes_aliments/mes_aliments' OnMouseOver="document.all.texte.innerText='Mes Aliments !'">
                 <img id="carotte" src="{% static 'img/portfolio/menu-haut/carotte.png' %}"
               </a>
               {% else %}
               
               
               <a href='/accounts/login' OnMouseOver="document.all.texte.innerText='Se connecter !'">
                 <img id="login" src="/static/img/portfolio/menu-haut/login.png">
               </a>

               <a href='/mes_aliments/mes_aliments' OnMouseOver="document.all.texte.innerText='Aide !'">
                 <img id="carotte" src="/static/img/portfolio/aide.png"
               </a>
               
               <a href='/accounts/inscription' OnMouseOver="document.all.texte.innerText='S\'inscrire !'">
                 <img id="inscription" src="{% static 'img/portfolio/menu-haut/inscription2.png' %}">
               </a>
               
               {% endif %}

               
               {% if user.is_authenticated %}

               <a href='#' OnMouseOver="document.all.texte.innerText='Aide !'">
                 <img id="login" src="{% static 'img/portfolio/menu-haut/aide.png' %}"
               </a>
               
               <a href='/accounts/logout_view' OnMouseOver="document.all.texte.innerText='Se deconnecter !'">
                 <img id="deco" src="{% static 'img/portfolio/menu-haut/deco.png' %}">
               </a>
               {% endif %}
               
               <center><p id="texte"><br></p></center>

           </div>
       </div>
       
    </div>
    </div>
  </form>
