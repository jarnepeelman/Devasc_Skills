<html>
  <body>
    <h1>Peelman Jarne - LAB - 1 - Python Expirements</h1>
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
  <h2>PART 3: Gebruik Python om 100 boeken aan de API-simulator toe te voegen</h2>
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
 
<h1>LAB 3 - PYTHON REVIEW – DEVELOPMENT TOOLS AND CLASSES</h1>
   <h2>PART 1: Python Programming Review</h2>
	<h3>Task preparation en implementatie:</h3>
    <h4>Hieronder is een lijst van algemene commando's alsook commando's die ik heb gebruikt per programma:</h4>
	  <ul>
  <li><code>Python3 -V</code> &rarr; Toont welke versie van Python er aanwezig is op het systeem.</li>
  <li><code>Which python3</code> &rarr; Toont de locatie met het pad naar het uitvoerbare bestand van Python.</li>
  <li><code>python3</code> &rarr; Aanspreken van de Python interpreter.</li>
  <li>><code>print("Hello World")</code> &rarr; Tonen van de output Hello World</li>
  <li>><code>quit()</code> &rarr; Verlaten van de Python interpreter.</li>
</ul>
<h5>Visual Studio Code en Python</h5>
<ol>
<li>Aanmaken van HelloWorld.py file in Visual Studio</li>
<li>Run --> run and debug
</ol>
<h5>Python Data types</h5>
<ul>
 <li><code>type(x)</code> &rarr; Op de plaats van de X kan je nummers, waarden, letters meegeven. Dit commando geeft ons terug welke type variabele dit is.</li>
 <li><code>print(str1+space+str2+space+str3)</code> &rarr; Samenvoegen van meerdere strings</li>
<h5>Maken van arrays in Python</h5>
<ul>
 <li><code>my_array = [1, 2, 3, 4, 5]</code> &rarr; Dit maakt een array aan.</li>
</ul>
<h5>If-else in Python</h5>
<ul>
 <li> Waarde controleren --> als dit waar is voer dan dit uit, als dit niet waar is voer dan de else uit. </li>
</ul>
<h5>For Loop in Python</h5>
<p>De <code>for</code>-loop wordt gebruikt om een blok code voor elk element in een reeks uit te voeren.</p>
<pre><code>for element in reeks:
    # Code om uit te voeren voor elk element
    # ...</code></pre>

<h5>While Loop in Python</h5>
<p>De <code>while</code>-loop wordt gebruikt om een blok code te herhalen zolang een bepaalde voorwaarde waar is.</p>
<pre><code>while voorwaarde:
    # Code om uit te voeren zolang de voorwaarde waar is
    # ...</code></pre>

<h5>Do-While Loop in Python</h5>
<p>In Python is er geen ingebouwde <code>do-while</code>-loop zoals in sommige andere programmeertalen. Je kunt echter een <code>do-while</code>-achtig gedrag simuleren met een <code>while</code>-loop en een extra controle na de lus.</p>
<pre><code>while True:
    # Code om uit te voeren
    # ...

    # Controleer de voorwaarde voor de do-while-lus
    if not voorwaarde:
        break
</code></pre>
<h5>strip() in Python</h5>
<ul>
<li><p>De <code>strip()</code>-methode wordt gebruikt om leidende en volgende spaties (of andere opgegeven karakters) van een tekenreeks te verwijderen.</p></li>
</ul>
<h5>append() in Python</h5>
<ul>
<li><p>De <code>append()</code>-methode wordt gebruikt om een element aan het einde van een lijst toe te voegen.</p></li>
</ul>
<h3>Task troubleshooting:</h3>
<ul>
 <li>Code uitvoeren en kijken welke foutmeldingen we te zien krijgen.</li>
</ul>
<h3>Task verification:</h3>
<ul>
 <li>Uitvoeren van het script, als de waarden overeenkomen met de gewenste output dan weet je voor elk programma of dit klopt.</li>
</ul>	
<h2>PART 2: Explore Python Development Tools</h2>
<h3>De gedocumenteerde bevindingen:</h3>
<h4>In deze taks is troubleshooting niet echt mogelijk, daarom een lijst met de doorgelopen stappen belangrijk voor deze opdracht</h4>
<h5>Nuttige commando's</h5>
<ul>
  <li><code>Python3 -V</code> &rarr; Toont welke versie van Python er aanwezig is op het systeem.</li>
  <li><code>Which python3</code> &rarr; Toont de locatie met het pad naar het uitvoerbare bestand van Python.</li>
  <li><code>Pip3 freeze</code> &rarr; Dit is een commando dat geïnstalleerde packages uit een virtuele omgeving weergeeft, samen met hun moduleversie.</li>
  <li><code>Pip3 install requests</code> &rarr; Commando gebruikt om de Python-module "requests" te installeren.</li>
  <li><code>Python3 -m venv devfun</code> &rarr; Commando dat een Python virtual environment genaamd "devfun" creëert.</li>
  <li><code>Source devfun/bin/activate</code> &rarr; Commando dat de Python virtual environment activeert en je er naartoe verwijst.</li>
  <li><code>Deactivate</code> &rarr; Commando dat ons uit de virtuele omgeving haalt en terugkeert naar de terminal.</li>
  <li><code>Python3 -m pip freeze | grep request</code> &rarr; Toont de geïnstalleerde modules, maar zoekt specifiek naar het woord "request".</li>
  <li><code>Pip3 freeze > requirements.txt</code> &rarr; Dit commando slaat alle geïnstalleerde pip freeze-modules op in een tekstbestand genaamd "requirements.txt".</li>
  <li><code>Pip3 install -r requirements.txt</code> &rarr; Commando dat wordt gebruikt in een nieuwe virtuele omgeving om de opgeslagen packages in het bestand "requirements.txt" te installeren.</li>
</ul>
	  
<h2>PART 3: Explore Python Classes</h2>
<h3>Task implementation en documentation</h3>
<h4>Belangrijke commando's voor het werken met functies:</h4>
<h5>Functies in Python</h5>
<ul>
 <li>Functie --> Blok code dat kan worden aangesproken. </li>
 <li><code>def functie</code> &rarr; Definiëren van een functie.</li>
 <li><code>functie()</code> &rarr; Aanspreken van de functie</li>
</ul>
<h5>Methoden in Python</h5>
<ul>
 <li>Elke functie bestaat uit meerdere methoden. Stukjes code die elk op hun beurt een aparte taak uitvoeren.</li>
</ul>	  
<h4>Task troubleshooting:</h4>
<h5>Uitleg:</h5>
<ul>
 <li>Om dit onderdeel te troubleshooten kan je de code uitvoeren en kijken of er errors worden meegegeven.</li>
 <li>Voorkomende error: Vergeten importeren van een module</li>
</ul>		
<h4>Task Verification:</h4>
<h5>Scripts:</h5>
<ul>
 <li>De geschreven scripts en output zijn terug te vinden in de mappen. Hierin zal je zien dat de getestte zaken werken.</li>
</ul>	

<h1>LAB 4 – NETWORK INFRASTRUCTURE AND TROUBLESHOOTING </h1>
<h2>PART 1: Network Infrastructure</h2>
<h3>Hieronder vind je de uitleg over onze netwerktekening alsook de geconfigureerde zaken op de netwerk devices</h3>
<h4>Task preparation en implentation:</h4>
<h5>Netwerk tekening</h5>
<ul>
 <li>De netwerk tekeningen van onze netwerkconfiguratie is te vinden in de bijhorende map.
 <li>Deze bevat een ip tabel, poortnummers, subnets en area nummer</li>
</ul>
<h5>De netwerk configuratie: switch</h5>
<ul>
	<li>Vlan 10 voor management</li>
	<li>Vlan 40 voor data users</li>
	<li>Default gateway</li>
	<li>Management IP</li>
</ul>
<h5>De netwerk configuratie: Router</h5>
<ul>
	<li>Encapsulatie op g0/0.10 en g0/40</li>
	<li>OSPF enabled <li>
	<li>Default gateway ingesteld</li>
	<li>OSPF 10</li>
	<li>Router id 7.7.7.7
	<li>Routes naar andere netwerken</li>
</ul>	
<h5>De netwerk configuratie: security features op de switch</h5>
<ul>
	<li>Port security</li>
	<li>BPDU guard</li>
	<li>Vlans toewijzen op enkel de poorten die nodig zijn</li>
	<li>Niet gebruikte poorten op shutdown in apparte vlan.</li>
	<li>SSH enabled</li>
	<li>Wachtwoorden voor de lines, ssh en enable</li>
</ul>
<h5>De netwerk configuratie: security features op de router</h5>	
<ul>
	<li>Down zetten van niet gebruikte poorten.</li>
	<li>SSH enabled</li>
	<li>Wachtwoorden voor de lines, ssh en enable</li>
</ul>	
<h4>Task troubleshooting:</h4>
<h5>Switch troubleshoot commando's</h5>
<ul>
	<li><b>Show interfaces</b>: Geeft informatie over de status van de interfaces op de switch. Hiermee kun je controleren of de interfaces correct zijn geconfigureerd en of er fouten of problemen worden gedetecteerd.</li>
	<li><b>Show vlan</b>: Toont de VLAN-configuratie op de switch. </li>
	<li><b>Show spanning-tree</b>: Geeft informatie over het Spanning Tree Protocol (STP) op de switch.</li>
	<li><b>Show running-config</b>: Geeft de huidige configuratie van de switch weer.</li>
	<li><b>Show ip ssh</b>: Toont de SSH-configuratie op de switch. Hiermee kun je controleren of SSH is ingeschakeld en of de juiste versie en beveiligingsinstellingen zijn geconfigureerd.</li>
	<li><b>Show line vty</b>: Geeft de configuratie van de virtuele terminal (VTY) lines weer.</li>
	<li><b>Show running-config | include enable secret</b>: Toont het configuratiegedeelte met het enable secret-wachtwoord.</li>
  <li><b>Ping</b>: Hiermee kun je de connectiviteit testen tussen de switch en een specifiek IP-adres. Bijvoorbeeld: <code>ping 192.168.1.1</code></li>
  <li><b>Traceroute</b>: Hiermee kun je het pad traceren dat een pakket volgt vanaf de switch naar een bepaald IP-adres. </li>
  <li><b>Show ip route</b>: Toont de IP-routetabel op de switch. </li>
</ul>
<h5>Router troubleshoot commando's</h5>
<ul>
  <li><b>Show interfaces</b>: Geeft informatie over de status van de interfaces op de router. </li>
  <li><b>Show ip route</b>: Toont de IP-routetabel op de router.</li>
  <li><b>Show running-config</b>: Geeft de huidige configuratie van de router weer. </li>
  <li><b>Show ip ssh</b>: Toont de SSH-configuratie op de router.</li>
  <li><b>Show running-config | include enable secret</b>: Toont het configuratiegedeelte met het enable secret-wachtwoord. </li>
  <li><b>Ping</b>: Hiermee kun je de connectiviteit testen tussen de router en een specifiek IP-adres. Bijvoorbeeld: <code>ping 192.168.1.1</code></li>
  <li><b>Traceroute</b>: Hiermee kun je het pad traceren dat een pakket volgt vanaf de router naar een bepaald IP-adres. Bijvoorbeeld: <code>traceroute 192.168.1.1</code></li>
  <li><b>Show ip OSPF</b>: Toont de OSPF-configuratie op de router.</li>	
</ul>

<h1>LAB 5 – Software Development and Design Content</h1>
<h2>PART 1: Software Version Control with Git</h2>
  <h3>Task preparation en implementatie:</h3>	
<h4>Git Commando's:</h4>
<h5>Basic Commando's:</h5>
<ul>
  <li><p><b>Git init:</b> Commando om Git te laten weten in welke directory de huidige directory zich bevindt.</p></li>
  <li><p><b>Git status:</b> Commando om te controleren of de status van bestanden is gewijzigd.</p></li>
  <li><p><b>Git add:</b> Hiermee wordt een bestand klaargemaakt om te worden gecommit.</p></li>
  <li><p><b>Git commit:</b> Hiermee wordt een bestand daadwerkelijk gecommit, met een uniek ID.</p></li>
  <li><p><b>Git log:</b> Toont de geschiedenis van de commits.</p></li>
  <li><p><b>Git diff:</b> Toont het verschil tussen twee bestanden met behulp van de gegeven ID's.</p></li>
</ul>
<h5>Branches en Merging Commando's:</h5>
<ul>
  <li><p><b>Git branch:</b> Maakt een nieuwe branch aan. Er is altijd één master branch.</p></li>
  <li><p><b>Git checkout:</b> Stelt je in staat om naar de master branch te gaan.</p></li>
  <li><p><b>Git merge:</b> Voegt de code samen van verschillende branches.</p></li>
  <li><p><b>Git branch -d:</b> Verwijdert een Git branch.</p></li>
</ul>
<h5>Andere Commando's:</h5>
<ul>
  <li><p><b>Sed:</b> Commando dat ervoor zorgt dat je een woord kunt vervangen.</p></li>
  <li><p><b>VIM:</b> Optie 'dd' om regels te verwijderen.</p></li>
  <li><p><b>Cp:</b> Kopieert een bestand uit de bovenliggende directory.</p></li>
  <li><p><b>Git remote add:</b> Maakt een alias voor een Git URL.</p></li>
  <li><p><b>Git push origin master:</b> Commando om een bestand naar de GitHub repository te pushen.</p></li>
</ul>
<h3>Task troubleshooting:</h3>
<ul>
  <li>
    <b>"fatal: not a git repository (or any of the parent directories): .git"</b><br>
    <b>Oplossing:</b> Dit betekent dat je niet in een Git-repository-directory staat. Zorg ervoor dat je je in de juiste map bevindt of initialiseer een nieuwe Git-repository met het commando "git init".
  </li>
  <li>
    <b>"fatal: refusing to merge unrelated histories"</b><br>
    <b>Oplossing:</b> Deze fout treedt op wanneer je probeert twee niet-gerelateerde Git-repositories samen te voegen. Voeg de optie "--allow-unrelated-histories" toe aan je merge-commando: "git merge --allow-unrelated-histories &lt;branch&gt;".
  </li>
  <li>
    <b>"error: failed to push some refs to &lt;remote&gt;"</b><br>
    <b>Oplossing:</b> Dit geeft aan dat er problemen zijn bij het pushen naar de externe repository. Zorg ervoor dat je de juiste toegangsrechten hebt en dat de externe repository correct is geconfigureerd. Mogelijk moet je de repository eerst pullen en conflicten oplossen voordat je kunt pushen.
  </li>
  <li>
    <b>"error: Your local changes to the following files would be overwritten by merge"</b><br>
    <b>Oplossing:</b> Deze foutmelding geeft aan dat er conflicten zijn tussen je lokale wijzigingen en de branch die je wilt mergen. Je kunt de conflicten oplossen door de betreffende bestanden handmatig te bewerken en vervolgens een commit uit te voeren.
  </li>
  <li>
    <b>"error: pathspec '&lt;file&gt;' did not match any file(s) known to git"</b><br>
    <b>Oplossing:</b> Dit betekent dat het opgegeven bestand niet bekend is in de Git-repository. Controleer of je de juiste bestandsnaam hebt opgegeven en of het bestand daadwerkelijk aanwezig is.
  </li>
  <li>
    <b>"fatal: remote origin already exists."</b><br>
    <b>Oplossing:</b> Deze fout treedt op wanneer je probeert een externe repository toe te voegen met een naam die al in gebruik is. Je kunt de bestaande configuratie verwijderen en opnieuw toevoegen met het commando "git remote remove origin" en vervolgens "git remote add origin &lt;repository-url&gt;" gebruiken.
  </li>
</ul>
<h3>Task Verification:</h3>
<h4> Belangrijke troubleshoot commando's</h4>
<ul>
  <li>
    <b>"git config --list"</b><br>
    Geeft een lijst weer van de Git-configuratie-instellingen op het systeem.
  </li>
  <li>
    <b>"git status"</b><br>
    Toont de status van het werkende directorygebied, inclusief wijzigingen, toevoegingen en commits.
  </li>
  <li>
    <b>"git log"</b><br>
    Toont een overzicht van de commit-geschiedenis met informatie zoals auteur, datum en commit-berichten.
  </li>
  <li>
    <b>"git diff"</b><br>
    Vergelijkt de wijzigingen tussen het werkende directorygebied en de laatste commit.
  </li>
  <li>
    <b>"git branch"</b><br>
    Toont een lijst van branches in de repository en geeft de huidige branch aan met een asterisk (*).
  </li>
  <li>
    <b>"git remote -v"</b><br>
    Geeft de URL's weer van de externe repositories die aan de lokale repository zijn gekoppeld.
  </li>
</ul>
<h2>PART 2: Create a Python Unit Test</h2>
<h3>Task implementation en preparation:</h3>
<h4>Belangrijke opmerkingen van dit Labo</h4>
<ul>
<li>Het plakken van de python code moet gebeuren met dezelde inspiring regels als in de pdf anders gaat dit niet werken.</li>
<li>Zorg voor duidelijke commentaar regels in de code. </li>
</ul>

<h2>
<h3>Task implementation en preparation:<h3>
<h4>Belangrijke opmerkingen en commando's van dit Labo</h4>
<ul>
<li><code>XML</code> &rarr; XML extensible markup language</li>
<li><code>import re </code> &rarr; importeren van de regular expression engine</li>
<li><code>Json</code> &rarr; Werkt aan de hand van Access Tokens, zoals github met de Personal access token</li>
<li><code>import json</code> &rarr; importeren van de json module</li>
<li><code>import yaml</code> &rarr; importeren van de yaml module.</li>
</ul>
	
<h1>LAB 6 – Python Network automation with netmiko</h1>
<h2>PART 1: Connecting to a single iOS device</h2>
<h3>Task implementation en preparation:</h3>
<h4>Belangrijke opmerkingen bij dit labo</h4>
<ul>
<li><code>from netmiko import Connecthandler </code> &rarr; Het importeren van de connecthandler uit de netmiko module.</li>
<li><code>Cisco_881 = {} </code> &rarr; Hierin de gegevens meegeven voor de router of switch. Het device dat we willen configureren.</li>
<li><code>ConnectHandler(**cisco_881)</code> &rarr; Aanspreken van de ConnectHandler module</li>
</ul>
<h3>Task troubleshooting:</h3>
<h4>Belangrijkste troubleshootopties</h4>
<ul>
<li><code>Traceback (most recent call last):
  File "script.py", line 7, in module</code> &rarr; Controleren of de module aanwezig is.</li>
<li><code>ImportError: No module named 'module_name'</code> &rarr; Deze fout treedt op wanneer je probeert een module te importeren die niet kan worden gevonden.</li>
    <li><code>SyntaxError: invalid syntax</code> &rarr; Deze fout treedt op wanneer de syntaxis van de Python-code ongeldig is.</li>
    <li><code>AttributeError: 'str' object has no attribute 'some_attribute'</code> &rarr; Deze fout treedt op wanneer je probeert een attribuut te gebruiken dat niet bestaat voor het gegeven object.</li>
    <li><code>KeyError: 'key_name'</code> &rarr; Deze fout treedt op wanneer je probeert een sleutel te gebruiken die niet aanwezig is in een woordenboek.</li>
 </ul>
<h3>Task Verification:</h3>
<h4>Belangrijkste manieren om te testen of de zaken werken:</h4>
<ul>
<li>Voer het script uit en zorg ervoor dat je geen errors krijgt.</li>
<li><code>Python --version</code> &rarr; Controleer voor alle zekerheid of de juiste Python versie aanwezig is.</li>
</ul>
	
<h2>PART 2: Connect to multiple IOS devices</h2>
<h3>Task implementation en preparation:</h3>
<ul>
<li><code>from netmiko import Connecthandler </code> &rarr; Het importeren van de connecthandler uit de netmiko module.</li>
<li><code>Cisco_881 = {} </code> &rarr; Hierin de gegevens meegeven voor de router of switch. Het device dat we willen configureren.</li>
<li>De configuratie van beide devices, wachtwoord en username moet aanwezig zijn.</li>
<li><code>ConnectHandler(**cisco_881)</code> &rarr; Aanspreken van de ConnectHandler module</li>
<li>Files voor het opslaan van Output klaarzetten</li>
</ul>
<h3>Task troubleshooting:</h3>
<h4>Belangrijkste troubleshootopties</h4>
<ul>
<li>Zorg ervoor dat de juiste wachtwoorden en usernames aanwezig zijn voor de SSH calls.</li>
<li>Let op de Authentication failed melding bij het verkeerd ingeven van wachtwoord of username</li>
<li>Geef de correcte IP's mee </li>
<li>Geef de correcte uitvoerbare commando's mee</li>
</ul>
<h3>Task Verification:</h3>
<h4>Belangrijkste manieren om te testen of de zaken werken:</h4>
<ul>
<li>Voer het script uit en zorg ervoor dat je geen errors krijgt.</li>
<li><code>Python --version</code> &rarr; Controleer voor alle zekerheid of de juiste Python versie aanwezig is.</li>
<li><code>pip list</code> &rarr; Geeft een lijst van de geïnstalleerde pip modules. </li>
<li>De scriptjes tonen of alles juist geconfigureerd is. Deze vind je in de LAB folders.</li>
</ul>

<h1>LAB 7 - NETCONFIG and YANG</h1>
<h2>PART 1: Install the CSR1000v VM</h2>
<h3>Task implementation en preparation</h3>
<ul>
<li>Downloaden van de VM ova file </li>
<li>Downloaden van de ISO file</li>
<li>Zorgen voor de juiste toetsenbord instellingen</li>
<li>Toewijzen van Ip address</li>
<li>Host-Only adapter wijzigen op VM ware.</li>
</ul>
<h4>Commando's:</h4>
<ul>
<li><code>Show ip interface brief</code>  &rarr; Verschillende interfaces tonen.</li>
<li>code>ssh cisco@192.168.56.101</code> &arr; Maken van de SSH connectie met de machine</li>
</ul>
<h3>Task troubleshooting:</h3>
<h4>Belangrijkste troubleshoot opmerkingen</h4>
<ul>
<li>Check de instellingen van de Virtual box</li>
<li>Toch overschakelen naar VM ware omwille van Ip toewijzing interface probleem.</li>
<li>Zorgen dat VMware/VirtualBox up to date is </li>
</ul>
<h3>Task Verification:</h3>
<h4>Checken of alles werkt:</h4>
<ul>
<li>Machine opstarten en kijken of de installatie erdoor komt</li>
<li>Screenshot SSH toont de oplossing</li>
<li>Web ui: surfen naar https://192.168.40.128. Zie screenshot</li>
</ul>

<h2>Part 2: Explore YANG Models</h2>
<h3>Task preparation en implementation</h3>
<h4>Nodige commando's</h4>
<ul>
<li><code>wget</code> &arr; Tool voor het downloaden van bestanden.</li>
<li><code>pip3 install pyang --upgrade</code> &arr; Upgraden van Pyang naar de laatste nieuwe versie</li>
<li><code>pyang -h | more</code> &arr; Meerdere opties van het Yang model tonen.</li>
</ul>
<h3>Task troubleshooting:</h3>
<ul>
<li><code>pyang -v</code> &arr; Checken van de juiste versie van Yang.</li>
<li>De nodige python installaties doen indien deze nog niet waren geinstalleerd.</li>
<li><code>pyang -f tree <yang_file></code> &arr; Toont een boomstructuurweergave van het YANG-model in het opgegeven <code><yang_file></code>.</li>
</ul>	
<h3>Task verification:</h3>
<ul>
<li><code>pyang -v</code>: Controleer de juiste versie van Yang.</li>
<li><code>pyang -f tree yang_file</code> &arr; Toont een boomstructuurweergave van het YANG-model.</li>
<li><code>pyang -f yin yang_file</code> &arr; Converteert het YANG-model naar het YIN-formaat.</li>
<li><code>pyang -f yang yin_file</code> &arr; Converteert het YIN-model terug naar het YANG-formaat.</li>
<li><code>pyang -f jsonx yang_file</code> &arr; Converteert het YANG-model naar het JSONX-formaat.</li>
</ul>

<h2>Part 3: Use NETCONF to Access an IOS XE Device</h2>
<h3>Task preparation en implementation</h3>
<h4>Nodige commando's</h4>
<ul>
<li><code>SSH</code> &arr; Verbinding maken vanop afstand</li>
<li><code>Ping</code> &arr; Connectiviteit checken</li>
<li><code>ssh cisco@10.176.176.209 -p 830 -s netconf</code> &arr; Connectie maken met yang via sshop poort 830</li>
<li><code>Print()</code> &arr; Gebruikt om een printstatement toe te voegen</li>
<li><code>For</code> &arr; Maken van een lus om code meermaals uit te voeren.</li>
</ul>
<h3>Task Troubleshooting:</h3>
<h4>Nodige commando's</h4>
<ul>
<li><code>netconf-yang</code> &arr; Commando uitvoeren in config terminal als netconfig van yang niet geïnstalleerd zou zijn. </li>
<li>Lezen van de python errors &arr; Deze zijn eerder al besproken.</li>
</ul>
<h3>Task verification:</h3>
<h4>Nodige commando's</h4>
<ul>
<li><code>ping -c 5 10.176.176.209</code> &arr; Check de connectiviteit naar het IOS XE device</li>
<li><code>ssh cisco@10.176.176.209</code> &arr; Checken of ssh naar het IOS XE device werktt</li>
<li><code>show platform software yang-management process</code> &arr; Checken van de aanwezige yang management processen.</li>
<li><code>show netconf-yang sessions</code> &arr; Tonen van de netconfig yang sessions</li>
<li><code>pip3 list --format=columns | more</code> &arr; Verifiëren of de ncclient geïnstalleerd is</li>
<li><code>for - print</code> &arr; Checken of de lus weldegelijk het gevraagd aantal keer wordt uitgevoerd.</li>
<li><code> python3 ncclient-netconf.py</code> &arr; Uitvoeren en checken of de gewenste output getoond wordt.</li>
<li>Checken of het script de loopback interface heeft aangemaakt.</li>
<li><code>show ip int brief</code> &arr; Uitvoeren en checken of de loopback er is bijgekomen.</li>
</ul>

<h2>Part 4: Use RESTCONF to Access an IOS XE Device</h2>
<h3>Task preparation en implementation</h3>
<h4>Nodige commando's</h4>
<ul>
<li><code>ping -c 5 192.168.56.102</code> &arr; Checken of er nog connectiviteit is naar ons device.</li>
<li><code>ssh cisco@192.168.56.101</code> &arr; Verifiëren van de SSH connectie.</li>
<li><code>config t</code> &arr; Naar de configuration terminal.</li>
<li><code>restconf</code> &arr; Checken of de restconf deamons runnende zijn.</li>
<li><code>show platform software yang-management process</code> &arr; Tonen van de Yang processen</li>
<li><code>ip http secure-server</code> &arr; Commando om http te enablen</li>
<li><code>ip http authentication local</code> &arr; Commando om lokale authorisatie te kunnen gebruiken</li>
<li>Basic Authentication &arr; Postman setting om basis authenticatie te gebruiken</li>
<li>Header &arr; content-type toevoegen. &arr; application/yang-data+json &arr; Dit zegt postman om json te gebruiken.</li>
</ul>

<h3>Task Troubleshooting:</h3>
<h4>Nodige commando's</h4>
<ul>
<li><code>restconf</code> &arr; Dit kan helpen om te vergelijken met bepaalde deamons die niet aan staan.</li>
<li><code>show platform software yang-management process</code> &arr; Tonen van de Yang processen bij eventuele problemen.</li>
<li><code>show ip int brief</code> &arr; Check de ip's op bepaalde interfaces</li>
<li>Gebruik visual studio om code op de juiste lijn te kunnen krijgen.</li>
<li>Status code 400 &arr; Bad Request: Deze statuscode geeft aan dat de server het verzoek van de client niet begrijpt of niet kan verwerken vanwege een slecht geformuleerd verzoek.</li>
<li>Status code 401 &arr; Unauthorized: Deze statuscode geeft aan dat de client niet geautoriseerd is om toegang te krijgen tot de gevraagde bron.</li>
<li>Status code 403 &arr; Forbidden: Deze statuscode geeft aan dat de server het verzoek begrijpt maar weigert deze.</li>
<li>Status code 404 &arr; Not Found: Deze statuscode geeft aan dat de server de gevraagde bron niet kan vinden. Het wordt vaak gebruikt om aan te geven dat de opgegeven URL niet overeenkomt met een geldige bron op de server.</li>
<li>Status code 500 &arr; Internal Server Error: Deze statuscode geeft aan dat er een onverwachte fout is opgetreden aan de kant van de server. </li>
<li>Status code 503 &arr; Service Unavailable: Deze statuscode geeft aan dat de server tijdelijk niet beschikbaar is om het verzoek te verwerken. </li>
</ul>
	
<h3>Task verification:</h3>
<h4>Nodige commando's</h4>
<ul>
<li><code>ping -c 5 192.168.56.102</code> &arr; Checken of er nog connectiviteit is naar ons device.</li>
<li><code>ssh cisco@192.168.56.101</code> &arr; Verifiëren van de SSH connectie.</li>
<li><code>restconf</code> &arr; Zijn de restconf aan het runnen?</li>
<li>Status code 400 &arr; Error meldingen zitten in de 400 of 500 bij servers</li>
<li>Status code 200 &arr; De api call heeft succesvol gewerkt.</li>
</ul>
