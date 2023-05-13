<html>
  <body>
    <h1>LAB - 1 - Python Expirements</h1>
      <h2>TASK 1.1: Installatie van de verschillende tools/packages op Ubuntu</h2>
      <h3>Task preparation en implementatie:</h3> 
    <h4>Hieronder is een lijst van algemene commando's alsook commando's die ik heb gebruikt per programma:</h4>
      <h5>Python 3.8 and PIP</h5>
       <ul>
        <li><p>Sudo apt update</p></li>
        <li><p>Sudo apt install python3.8</p></li>
        <li><p>PIP</p></li>
        <li><p>pip install –upgrade pip</p></li>
       </ul>
      <h5>Visual Studio code</h5>
        <ul>
        <li><p>Visual Studio is By Default geïnstalleerd.</p></li>
        <li><p>In Visual Studio --> Python extensie installeren</p></li>
        <li><p>Auto-Save aanzetten</p></li>
        <li><p>Files en folders aanmaken per labo &lt;filename&gt;.py </p></li>
       </ul>
      <h5>Jupyter Notebook install commando's:</h5>
        <ul>
          <li><p>Sudo apt update & sudo apt upgrade </p></li>
          <li><p>Sudo apt install python3-pip -&gt; nodig omdat pip zelf eerst geïnstalleerd moet worden vooraleer we pip kunnen gebruiken</p></li>
          <li><p>Sudo pip3 install jupyter</p></li>
          <li><p>run het programma: terminal jupyter notebook.</p></li>
        </ul>
       <h5>Python IDLE</h5>
       <ul>
        <li><p>Sudo apt install idle</p></li>
        <li><p>Het programma runnen door idle in de terminal te typen.</p></li>
       </ul>
    <h3>Task Troubleshooting:</h3>
    <h4>Een overzicht van de problemen die ik heb ondervonden per programma.</h4>
    <h5>Python 3.8 en PIP</h5>
      <ul>
        <li><p>Probleem met installeren van de juiste versie.</p></li>
        <li><p>In plaats van gewoon sudo apt install python geven we de versie mee -> sudo apt install python3.8 </p></li>
       </ul>
    <h5>Visual Studio code</h5>
      <ul>
        <li><p>Probleem met installeren van de juiste versie.</p></li>
        <li><p>In plaats van gewoon sudo apt install python geven we de versie mee -> python3 <filename>.py.</p></li>
       </ul>
     <h5>Jupyter Notebook</h5>
      <ul>
        <li><p>Problemen bij de installatie. De juiste packages waren niet aanwezig.</p></li>
	      <li><p>Oplossing: Sudo apt update en sudo apt upgrade. -&gt; Bij het binnenhalen van de updates kan je zien welke packages niet aanwezig waren. (logging in de terminal zelf.)</p></li>
    </ul>
    <h3>Task Troubleshooting:</h3>
    <h4>Ook hier kan je een overzicht van verificatie zien per programma.</h4>
    <h5>Python 3.8 en PIP</h5>
      <ul>
        <li><p>Checken welke python versie er aanwezig is: Python3 –version</p></li>
	      <li><p>Checken van de PIP versie: pip –version</p></li>
        <li><p>Pip&lt;version&gt; --version -&gt; dit laat je toe om pip versies te checken voor een bepaalde python versie.</p></li>
      </ul>
    <h5>Checken of Visual Studio Code werkt met Python:</h5>
    <ul>
        <li><p>Code --version -&gt; commando geeft versie van Visual Studio code mee</p></li>
       </ul>
    <h5>Checken of Jupyter notebook is geïnstalleerd:</h5>
    <ul>
        <li><p>Jupyter notebook --version</p></li>
       </ul>
    <h5>Python IDL checken:</h5>
    <ul>
      <li><p>Idle --version</p></li>
      <li><p>Het openen van idle toont ook automatisch de versie.</p></li>
    </ul>
    <h2>TASK 1.2: Run geopy and timedate Python Scipts on the DEVASC-LABVM using the tools above (1.1):</h2>
    <h3>Task preparation en implementatie:</h3>
    <h5>Klaarzetten van de scriptjes timedate.py, location.py en geopy.py</h5>
    <ul>
      <li><p>Visual Studio file aanmaken</p></li>
      <li><p>Script kopiëren vanuit de Github</p></li>
      <li><p>Idle openen --> script inladen en vervolgens runnen<p></li>
    </ul>
    <h5>Task troubleshooting</h5>
    <h6>timedate.py</h6>
    <ul>
      <li><p>Probleem bij het uitvoeren van het timedate.py script</p></li>
      <li><p>pip install datetime --> moet gerunt worden om de module te kunnen aanspreken</p></li>
    </ul>  
    <h6>location.py</h6>
    <ul>
      <li><p>Probleem bij het uitvoeren van het location.py script</p></li>
      <li><p>pip install Nominatim--> moet gerunt worden om de module te kunnen aanspreken</p></li>
    </ul>  
    <h6>geopy-geocoders_location.py</h6>
    <ul>
      <li><p>Probleem bij het uitvoeren van het geopy-geocoders_location.py script</p></li>
      <li><p>pip install Nominatim --> moet gerunt worden om de module te kunnen aanspreken</p></li>
    </ul>  
    
<h1>LAB 2 - Explore rest apis with API-simulator and postmans</h1>
<h2>PART 1: Explore API Documentation Using the API Simulator</h2>
  <h3>Task preparation en implementatie:</h3> 
<ul>
  <li>DEVASC-machine installeren</li>
  <li>Zorg ervoor dat het curl-commando werkt</li>
  <li>Zorg voor de juiste URL's om de API-oproep te maken</li>
</ul>
<h3>Foutopsporingstaak:</h3>
<ul>
  <li>Lees de responscode</li>
  <li>Welke foutcode komt er? Is dit een statuscode? 404, 403 of is er iets mis met het dataveld?</li>
  <li>Tegengekomen fout 401 - Verkeerde invoer meegegeven aan de API-oproep</li>
</ul>
<h3>Verificatietaak:</h3>
<ul>
  <li>Controleer succesvolle API-oproepen met statuscodes 200</li>
  <li>Zorg ervoor dat de juiste items in de respons worden geretourneerd</li>
  <li>Maak oproepen met extra parameters en controleer of de parameters die in de URL zijn opgegeven, effectief het veld teruggeven</li>
  <li>Maak POST-oproepen en controleer of de items zijn toegevoegd</li>
  <li>Maak DELETE-oproepen en controleer of items daadwerkelijk worden verwijderd</li>
</ul>
<h2>PART 2: Gebruik Postman om API-oproepen naar de API-simulator te maken</h2>
  <h3>Task preparation en implementatie:</h3> 
  <ul>
    <li>Installeer de juiste versie van Postman</li>
    <li>Voeg de API-token toe aan het autorisatietabblad van de Postman-API om toegang te krijgen tot de oproepen</li>
  </ul>
  <h3>Foutopsporingstaak:</h3>
  <ul>
    <li>Identificeer fouten met statuscodes en reactieberichten</li>
  </ul>
  <h3>Verificatietaak:</h3>
  <ul>
    <li>Controleer succesvolle API-oproepen met statuscodes 200</li>
    <li>Zorg ervoor dat de juiste items in de respons worden geretourneerd</li>
  </ul>
  <h2>Deel 3: Gebruik Python om 100 boeken aan de API-simulator toe te voegen</h2>
  <h3>Voorbereiding en uitvoering van de taak:</h3> 
  <ul>
    <li>Verkrijg de API-toegangstoken en voeg deze toe aan de API-oproep</li>
    <li>Importeer de Faker-module</li>
  </ul>
  <h3>Foutopsporingstaak:</h3>
  <ul>
    <li>Gebruik de tab-toets om toegang te krijgen tot de juiste Python-opdrachten</li>
    <li>Zorg ervoor dat de shebang en Python3 correct zijn geïnstalleerd in elk script</li>
  </ul>
  <h3>Verificatietaak:</h3>
  <ul>
    <li>Controleer of er 100 boeken aan de API zijn toegevoegd met een succesvolle API-oproep</li>
    <li>Controleer succesvolle API-oproep met statuscode 200</li>
    <li>Gebruik de tab-toets om ervoor te zorgen dat de juiste PowerShell-imports worden gebruikt</li>
  </ul>
    
    
     <!-- <h1>LAB - X - Titel</h1>
      <h2>TASK X: Installatie van de verschillende tools/packages op Ubuntu</h2>
      <h3>Task preparation en implementatie:</h3> 
      <h4></h4>
      <h5></h5>
       <ul>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
       </ul>
      <h5>Visual Studio code<h/5>
        <ul>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
       </ul>
        
        <h1>LAB - X - Titel</h1>
      <h2>TASK X: Installatie van de verschillende tools/packages op Ubuntu</h2>
      <h3>Task preparation en implementatie:</h3> 
      <h4></h4>
      <h5></h5>
       <ul>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
       </ul>
      <h5>Visual Studio code<h/5>
        <ul>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
       </ul>
        
        
        <h1>LAB - X - Titel</h1>
      <h2>TASK X: Installatie van de verschillende tools/packages op Ubuntu</h2>
      <h3>Task preparation en implementatie:</h3> 
      <h4></h4>
      <h5></h5>
       <ul>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
       </ul>
      <h5>Visual Studio code<h/5>
        <ul>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
       </ul>
        
        <h1>LAB - X - Titel</h1>
      <h2>TASK X: Installatie van de verschillende tools/packages op Ubuntu</h2>
      <h3>Task preparation en implementatie:</h3> 
      <h4></h4>
      <h5></h5>
       <ul>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
       </ul>
      <h5>Visual Studio code<h/5>
        <ul>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
       </ul>
        
        <h1>LAB - X - Titel</h1>
      <h2>TASK X: Installatie van de verschillende tools/packages op Ubuntu</h2>
      <h3>Task preparation en implementatie:</h3> 
      <h4></h4>
      <h5></h5>
       <ul>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
       </ul>
      <h5>Visual Studio code<h/5>
        <ul>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
       </ul>
        
        <h1>LAB - X - Titel</h1>
      <h2>TASK X: Installatie van de verschillende tools/packages op Ubuntu</h2>
      <h3>Task preparation en implementatie:</h3> 
      <h4></h4>
      <h5></h5>
       <ul>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
       </ul>
      <h5>Visual Studio code<h/5>
        <ul>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
        <li><p></p></li>
       </ul> -->
  </body>
</html>
