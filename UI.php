
<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Theme Made By www.w3schools.com - No Copyright -->
  <title>Bootstrap Theme The Band</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
<!--  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">-->
<!--  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>-->
<!--  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>-->
<!--  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>-->
  <style>
  body {
    font: 400 15px/1.8 Lato, sans-serif;
    color: #777;
  }
  h3, h4 {
    margin: 10px 0 30px 0;
    letter-spacing: 10px;
    font-size: 20px;
    color: #111;
  }
  .container {
    padding: 80px 120px;
  }
  .person {
    border: 10px solid transparent;
    margin-bottom: 25px;
    width: 80%;
    height: 80%;
    opacity: 0.7;
  }
  .person:hover {
    border-color: #f1f1f1;
  }
  .carousel-inner img {
    -webkit-filter: grayscale(90%);
    filter: grayscale(90%); /* make all photos black and white */
    width: 100%; /* Set width to 100% */
    margin: auto;
  }
  .carousel-caption h3 {
    color: #fff !important;
  }
  @media (max-width: 600px) {
    .carousel-caption {
      display: none; /* Hide the carousel text when the screen is less than 600 pixels wide */
    }
  }
  .bg-1 {
    background: #2d2d30;
    color: #bdbdbd;
  }
  .bg-1 h3 {color: #fff;}
  .bg-1 p {font-style: italic;}
  .list-group-item:first-child {
    border-top-right-radius: 0;
    border-top-left-radius: 0;
  }
  .list-group-item:last-child {
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
  }
  .thumbnail {
    padding: 0 0 15px 0;
    border: none;
    border-radius: 0;
  }
  .thumbnail p {
    margin-top: 15px;
    color: #555;
  }
  .btn {
    padding: 10px 20px;
    background-color: #333;
    color: #f1f1f1;
    border-radius: 0;
    transition: .2s;
  }
  .btn:hover, .btn:focus {
    border: 1px solid #333;
    background-color: #fff;
    color: #000;
  }
  .modal-header, h4, .close {
    background-color: #333;
    color: #fff !important;
    text-align: center;
    font-size: 30px;
  }
  .modal-header, .modal-body {
    padding: 40px 50px;
  }
  .nav-tabs li a {
    color: #777;
  }
  #googleMap {
    width: 100%;
    height: 400px;
    -webkit-filter: grayscale(100%);
    filter: grayscale(100%);
  }
  .navbar {
    font-family: Montserrat, sans-serif;
    margin-bottom: 0;
    background-color: #2d2d30;
    border: 0;
    font-size: 11px !important;
    letter-spacing: 4px;
    opacity: 0.9;
  }
  .navbar li a, .navbar .navbar-brand {
    color: #d5d5d5 !important;
  }
  .navbar-nav li a:hover {
    color: #fff !important;
  }
  .navbar-nav li.active a {
    color: #fff !important;
    background-color: #29292c !important;
  }
  .navbar-default .navbar-toggle {
    border-color: transparent;
  }
  .open .dropdown-toggle {
    color: #fff;
    background-color: #555 !important;
  }
  .dropdown-menu li a {
    color: #000 !important;
  }
  .dropdown-menu li a:hover {
    background-color: red !important;
  }
element.style {
    width: 100%;
}
  th{
    background-color:darkgray;
  }
  footer {
    background-color: #2d2d30;
    color: #f5f5f5;
    padding: 32px;
  }
  footer a {
    color: #f5f5f5;
  }
  footer a:hover {
    color: #777;
    text-decoration: none;
  }
  .form-control {
    border-radius: 0;
  }
  .track{
  }
  .showlist{
  }
  textarea {
    resize: none;
  }
    .dropbtn {
  background-color: #4CAF50;
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
  cursor: pointer;
}
  </style>
</head>
<body id="myPage" data-spy="scroll" data-target=".navbar" data-offset="50">

<div id="myCarousel" class="carousel slide" data-ride="carousel">
    <!-- Indicators -->
    <ol class="carousel-indicators">
      <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
      <li data-target="#myCarousel" data-slide-to="1"></li>
      <li data-target="#myCarousel" data-slide-to="2"></li>
    </ol>

    <!-- Wrapper for slides -->
    <div class="carousel-inner" role="listbox">
      <div class="item active">
        <img src="music1.jpg"  width="1200" height="700">
        <div class="carousel-caption">
          <h3>Show the Integrated Chart</h3>
          <p>Melon, Genie and Bugs' Chart Information Integration</p>
        </div>
      </div>

      <div class="item">
        <img src="music3.jpg" alt="Chicago" width="1200" height="700">
        <div class="carousel-caption">
          <h3>Show the Integrated Chart</h3>
          <p>Melon, Genie and Bugs' Chart Information Integration</p>
        </div>
      </div>

      <div class="item">
        <img src="music2.jpg" alt="Los Angeles" width="1200" height="700">
        <div class="carousel-caption">
          <h3>Show the Integrated Chart</h3>
          <p>Melon, Genie and Bugs' Chart Information Integration</p>
        </div>
      </div>
    </div>
    <!-- Left and right controls -->
    <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
      <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
      <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
      <span class="sr-only">Next</span>
    </a>
</div>
<!-- Container (Contact Section) -->

<div id="contact" class="container">
  <br>
  <h3 class="text-center">MUSIC CHART</h3>
  <ul class="nav nav-tabs">
    <li class="active"><a data-toggle="tab" href="#home">실시간차트</a></li>
    <li><a data-toggle="tab" href="#menu1">장르별차트</a></li>
    <!--<li><a data-toggle="tab" href="#menu2"></a></li>-->
  </ul>
  <div class="tab-content">
  <div id="home" class="tab-pane fade in active">
   
     <table class="table"><thread class="tread-dark"></thread><tr><th>순위</th><th>곡명</th><th>가수</th><th>앨범</th><th>가사</th><th>동영상</th></tr></thead>
      <tbody>
      
      <?

        $servername = "localhost:3306";
        $username="root";
        $password="1234";

        $conn = new mysqli($servername, $username, $password);
        $conn =  mysqli_connect($servername, $username, $password);
	
	mysqli_options($conn,MYSQLI_OPT_LOCAL_INFILE,true);

        if($conn->connect_error)
        {
          die("Connection failed: "+$conn -> connect_error);
        }

        $db = mysqli_select_db($conn,"Cloud");
        if($db)
          {
            echo "db connect success";
            echo "<br/>";
          } 
        else
          {
            echo "db connect error";
            echo "<br/>";
	}
	 $sql_delete = "delete from song;";
        if($conn->query($sql_delete) ===true)
            {echo "success";
        }
          else
            {
              echo "error : ". $sql_delete. "<br/>" . $conn->error;

            }

        $sql_excel = "load data local infile './Cloud/Cloud/integrate_excel.csv'
                      into table song
                      character set utf8
                      fields terminated by ',';
        ";
        if($conn->query($sql_excel) ===true)
            {echo "success";
        }
          else
            {
              echo "error : ". $sql_excel. "<br/>" . $conn->error;

            }
        $sql1 = "select * from song";
        $result = $conn->query($sql1);
        $num = 0;

        if($result->num_rows > 0){
          while($row = $result -> fetch_assoc()){
		if($num >0 && $num<=100){  
		echo " 
            	<tr>
            	<td>$num</td>
              	<td>$row[title]</td>
              	<td>$row[singer]</td>
              	<td>$row[albumName]</td>
              	<td>$num</td>
              	<td>$num</td>
            	</tr>
		";
		}

            $num = $num +1;
      }
    }
      ?>
     </tbody>
      </table>
    
  </div>

</div>
</div>

<!-- Image of location/map -->
<!--<img src="map.jpg" class="img-responsive" style="width:100%">-->

<!--&lt;!&ndash; Footer &ndash;&gt;-->
<footer class="text-center"style="margin-bottom: 10px;">
  <a class="up-arrow" href="#myPage" data-toggle="tooltip" title="TO TOP">
    <span class="glyphicon glyphicon-chevron-up"></span>
  </a><br><br>
</footer>
<script>
// Get the button, and when the user clicks on it, execute myFunction
document.getElementById("myBtn").onclick = function() {myFunction()};
/* myFunction toggles between adding and removing the show class, which is used to hide and show the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}
</script>
<script>
$(document).ready(function(){
  // Initialize Tooltip
  $('[data-toggle="tooltip"]').tooltip();

  // Add smooth scrolling to all links in navbar + footer link
  $(".navbar a, footer a[href='#myPage']").on('click', function(event) {
    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();
      // Store hash
      var hash = this.hash;
      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (900) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 900, function(){

        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
})
</script>

</body>
</html>

