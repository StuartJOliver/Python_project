import time
import random
import os
import pygame.mixer
import colorama
from colorama import Fore, Back, Style

# Ascii art - All ascii art was collected from multiple internet sources. Sounds are from Super Castlevania on SNES and Metal Gear Solid from Playstation. 
title_art = rf"""













                                          ██████  ██░ ██  ▄▄▄      ▓█████▄{Fore.RED}  ▒{Style.RESET_ALL}█████   █     █{Fore.RED}░{Style.RESET_ALL}   ▓█████▄ ▓█████  ██▓███  ▄▄▄█████▓ ██{Fore.RED}░{Style.RESET_ALL} ██   ██████ 
                                        {Fore.RED}▒{Style.RESET_ALL}██    {Fore.RED}▒ {Style.RESET_ALL}▓██{Fore.RED}░{Style.RESET_ALL} ██{Fore.RED}▒▒{Style.RESET_ALL}████▄    {Fore.RED}▒{Style.RESET_ALL}██▀ ██{Fore.RED}▌▒{Style.RESET_ALL}██{Fore.RED}▒ {Style.RESET_ALL} ██{Fore.RED}▒{Style.RESET_ALL}▓█░ █ ░█{Fore.RED}░   {Style.RESET_ALL}██▀ ██▌▓█   ▀ ▓██░  ██{Fore.RED}▒{Style.RESET_ALL}▓  ██{Fore.RED}▒ {Style.RESET_ALL}▓▒▓██{Fore.RED}░{Style.RESET_ALL} ██{Fore.RED}▒▒{Style.RESET_ALL}██    ▒ 
                                        {Fore.RED}░{Style.RESET_ALL} ▓██▄ {Fore.RED}  ▒{Style.RESET_ALL}██▀▀██{Fore.RED}░▒{Style.RESET_ALL}██  ▀█▄  {Fore.RED}░{Style.RESET_ALL}██   █{Fore.RED}▌▒{Style.RESET_ALL}██░  ██{Fore.RED}▒▒{Style.RESET_ALL}█{Fore.RED}░{Style.RESET_ALL} █ {Fore.RED}░{Style.RESET_ALL}█  {Fore.RED}  ░{Style.RESET_ALL}██   █▌{Fore.RED}▒{Style.RESET_ALL}███   ▓██░ ██▓{Fore.RED}▒▒ {Style.RESET_ALL}▓██{Fore.RED}░ ▒░▒{Style.RESET_ALL}██▀▀██{Fore.RED}░░ {Style.RESET_ALL}▓██▄   
                                        {Fore.RED}  ▒ {Style.RESET_ALL}  ██{Fore.RED}▒░{Style.RESET_ALL}▓█{Fore.RED} ░{Style.RESET_ALL}██ ░██▄▄▄▄██{Fore.RED} ░{Style.RESET_ALL}▓█▄   ▌{Fore.RED}▒{Style.RESET_ALL}██   ██{Fore.RED}░░{Style.RESET_ALL}█░ █{Fore.RED} ░{Style.RESET_ALL}█ {Fore.RED}   ░{Style.RESET_ALL}▓█▄   ▌{Fore.RED}▒{Style.RESET_ALL}▓█  ▄{Fore.RED} ▒{Style.RESET_ALL}██▄█▓{Fore.RED}▒ ▒░{Style.RESET_ALL} ▓██▓ {Fore.RED}░ ░{Style.RESET_ALL}▓█ {Fore.RED}░{Style.RESET_ALL}██ {Fore.RED}  ▒ {Style.RESET_ALL}  ██{Fore.RED}▒{Style.RESET_ALL}
                                        {Fore.RED}▒{Style.RESET_ALL}██████{Fore.RED}▒▒░{Style.RESET_ALL}▓█{Fore.RED}▒░{Style.RESET_ALL}██▓ ▓█   ▓██{Fore.RED}▒░▒{Style.RESET_ALL}████▓{Fore.RED} ░{Style.RESET_ALL} ████▓{Fore.RED}▒░░░{Style.RESET_ALL}██{Fore.RED}▒{Style.RESET_ALL}██▓  {Fore.RED}  ░▒{Style.RESET_ALL}████▓{Fore.RED} ░▒{Style.RESET_ALL}████{Fore.RED}▒▒{Style.RESET_ALL}██{Fore.RED}▒ ░  ░  ▒{Style.RESET_ALL}██{Fore.RED}▒ ░ ░{Style.RESET_ALL}▓█{Fore.RED}▒░{Style.RESET_ALL}██▓{Fore.RED}▒{Style.RESET_ALL}██████{Fore.RED}▒▒{Style.RESET_ALL}
                                        {Fore.RED}▒ ▒{Style.RESET_ALL}▓{Fore.RED}▒ ▒ ░ ▒ ░░▒░▒ ▒▒  {Style.RESET_ALL} ▓▒█{Fore.RED}░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒      ▒▒▓  ▒ ░░ ▒░ ░▒▓▒░ ░  ░  ▒ ░░    ▒ ░░▒░▒▒ ▒▓▒ ▒ ░
                                        {Fore.RED}░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░      ░ ▒  ▒  ░ ░  ░░▒ ░         ░     ▒ ░▒░ ░░ ░▒  ░ ░
                                        {Fore.RED}░  ░  ░   ░  ░░ ░  ░   ▒    ░ ░  ░ ░ ░ ░ ▒    ░   ░      ░ ░  ░    ░   ░░         ░       ░  ░░ ░░  ░  ░  
                                        {Fore.RED}    ░   ░  ░  ░      ░  ░   ░        ░ ░      ░          ░       ░  ░                   ░  ░  ░      ░  
                                                                    ░                            ░                                                
"""
castle_art = rf"""
                                                                            .                                                                         
                                                                        .   -.                                                                        
                                                                        -  :=.         {Fore.MAGENTA} .  {Style.RESET_ALL}                                                           
                                                                    . :=+..=+=         {Fore.MAGENTA} -. {Style.RESET_ALL}                                                           
                                                                    - :++++=+*=:       {Fore.MAGENTA}.== {Style.RESET_ALL}                                                           
                                                                    =.::=+=+=*-.       {Fore.MAGENTA}--*.{Style.RESET_ALL}                                                          
                                                                   :=-:-=*+==*+:     {Fore.MAGENTA} :==+={Style.RESET_ALL}                                                           
               {Fore.MAGENTA}                        .      {Style.RESET_ALL}                     ==*:-=**=+*+      {Fore.MAGENTA} -==++. {Style.RESET_ALL}                                                         
               {Fore.MAGENTA}                        :      {Style.RESET_ALL}                    -+=*-:-=-:==:      {Fore.MAGENTA} ==++*: {Style.RESET_ALL}                 {Style.RESET_ALL}..     {Style.RESET_ALL}                                 
               {Fore.MAGENTA}                        =      {Style.RESET_ALL}                   .-==***=*=====.     {Fore.MAGENTA}-=-=+++{Style.RESET_ALL}                 {Fore.MAGENTA} :-     {Style.RESET_ALL}                                 
               {Fore.MAGENTA}                       :=-     {Style.RESET_ALL}               .  .+++++**=+####=      {Fore.MAGENTA}.++***:{Style.RESET_ALL}                 {Fore.MAGENTA} -+     {Style.RESET_ALL}                                 
               {Fore.MAGENTA}                       -=*     {Style.RESET_ALL}               -  ===*****=-*+=-.       :--*-                 {Fore.MAGENTA} :-+:    {Style.RESET_ALL}                                 
               {Fore.MAGENTA}                      .-+*:    {Style.RESET_ALL}              .=-:+===-#*%*=+=+=.  .:  :--=*=:                 {Fore.MAGENTA}--++    {Style.RESET_ALL}                                 
               {Fore.MAGENTA}                      --=*=    {Style.RESET_ALL}              -=++*+=+**#@#*+**+:  :=  ==+=+*=                {Fore.MAGENTA}.=-+*.   {Style.RESET_ALL}                                 
               {Fore.MAGENTA}                     .-:-+#    {Style.RESET_ALL}              -=+***+***#@#+*=+*+--=+. -*+**+.               {Fore.MAGENTA} --:=+=   {Style.RESET_ALL}                                 
               {Fore.MAGENTA}                     -::-=*=   {Style.RESET_ALL}              ==++=*=***%#**=:-+***+=+.++--+:                {Fore.MAGENTA}.=::-+*.  {Style.RESET_ALL}                                 
               {Fore.MAGENTA}                    :-::-=+#-. {Style.RESET_ALL}           :  =#*+++-*##*##++=++*#*=+**+*=-+:               {Fore.MAGENTA}:=-::-=*+: {Style.RESET_ALL}                                 
               {Fore.MAGENTA}                   .=::-+++*#. {Style.RESET_ALL}          .+: -+:.:::+####**#**#+**+*###*=-=.         :     {Fore.MAGENTA}==::=+=+*= {Style.RESET_ALL}                                 
               {Fore.MAGENTA}                   :-::-++++#= {Style.RESET_ALL}          .+--*+:.:+:=************+-*+*%#===:        .=:   {Fore.MAGENTA}.+-::=+=+++{Style.RESET_ALL}                                  
                                .++====++**##+. -       .=+*=+::-+++**#++===+++****##%#+=+:  :     ==*. {Fore.MAGENTA}-*+====+++***-{Style.RESET_ALL}                                
                                 -###########- :*:     :=-+=+*====+-*+*++=:--++==+*#@#****=::+.   -+*** :*####%#%%##=.                                
                                  .++++*****. :+**.    :++=+*%#+##*=++**#*===#*++++*%%#+##*++*+.  :-*++   =+++**#**-                                  
                                  .====*=#+#: :+*#=:...-++-=%%*-##*++***++==++**++*#%%*=+*#+++#-.:--++*-. =-+-+++**=                                  
                                  .+++***#*#:.--=+#+-+=+====##=-+*++++=++++++++++++**+=-==*+--++==+=*=+*= +++++**#*=                                  
                                  :=+=++****-.-=+##****#**++%+--++++*#*##%#####*#*++++--=+**+*#%%#%##***-.++=++++**+                                  
                                   =*+**##**  .-:*#+**+#+=--#=+***===++##***+**=*==--+++*#*+=+#%#*#*+++*. =++*+*##*-                                  
                                   .:.::=++=  .--*#++++*=-:-#:-*++*%#*+###***##=*#%#=--*+++===#%###*+**=  .....:===                                   
                                   .::::-===  .-=*#+++=+==-=#::#=+*%#*+#%######+####+::*++====*#*******-  ....::-==                                   
                                 =:=-=+-=+=+**+--==-==-===+:::::===++=-*--+=-==-=--=::::-==+*+==-==--=-==-=-==-=+=+=+:                                
                                .==++++***#####************---==++**#*+++++++**+++*+--===+**####*********+=++*******+.                                
                                 :****###%%%%@%%#######%#%%#***####%%########**######**####%@%%%##########***#######=                                 
                                  ....::-=**#@%#+====+++++**+::-=+##**++===---===+*##-:--=*%%#**+===--==+=:--:::--==.                                 
                                  .....::-+*%%#*+====---==++-...:=#*+++====-=-=-===++:..:-+%#**+==-::--=+=:::...::-=.  ..                             
                          ..   .=+:...::-=+*%%#*+==+==--=++*-....-##*+===++*++==++=++:...:+%##*+++-----=*=--...::--=******=.                          
                        -+**+=++==....*#-=+**%#*++++=======+-...:-##+-+*######**+=+++:..:-+%%#*+++=--=-=+=-:..-@=--+#%###*+*--:.                      
                     .+++++++++=+*-.::======+%%*+**++==*+=++-...:=##=#**{Fore.RED}%@@@@@@#{Style.RESET_ALL}+*=+#-:::-+%%{Fore.GREEN}#**#{Style.RESET_ALL}*+=+++#*==--+=====*%%@%%****==++-:                   
                     :==+**+*#*#*+++++++*#*#%%%*++===={Fore.GREEN}+#*{Style.RESET_ALL}+**-:.::=###**{Fore.RED}@@@@@@@@@*{Style.RESET_ALL}+*+#=::-=*%{Fore.GREEN}@#*#%#{Style.RESET_ALL}*+++#%#+==*%*++###*###%*+=+==*==+.                  
                    -*+++=:-{Fore.GREEN}##{Style.RESET_ALL}+=**##**######*++={Fore.GREEN}+#{Style.RESET_ALL}+==+{Fore.GREEN}%%%{Style.RESET_ALL}###=-::-=%#*+{Fore.RED}#@@%%%%%%@**{Style.RESET_ALL}*+*=::-=*{Fore.GREEN}%@%%%%%#*{Style.RESET_ALL}*++*%#+=*####*++**######**++**##                   
                  .==-:..:-*{Fore.GREEN}#%#{Style.RESET_ALL}###+=++*###*==+*{Fore.GREEN}##@#{Style.RESET_ALL}++*{Fore.GREEN}#%%#{Style.RESET_ALL}#%=-:--+%##*{Fore.RED}%@@%%%%%@@#*{Style.RESET_ALL}*+*=---=*{Fore.GREEN}%@%%%%%#*{Style.RESET_ALL}*+*%%#++*##%#++*%%%##++#**+**###:                  
                 .===::-=-={Fore.GREEN}####{Style.RESET_ALL}++===+*###*+++*{Fore.GREEN}#*%@%#{Style.RESET_ALL}*{Fore.GREEN}#%%%%##{Style.RESET_ALL}+-::-+#%#*{Fore.RED}%@@%%%%@@%**{Style.RESET_ALL}#+*==++*{Fore.GREEN}*%@@%%%@%#*{Style.RESET_ALL}**#%%#**#%%%##%**####*#**#%%###*:                 
              .::=**+++==+{Fore.GREEN}#%##%#{Style.RESET_ALL}****+**+=++**{Fore.GREEN}#%%%%*#{Style.RESET_ALL}*{Fore.GREEN}#%#%%%#{Style.RESET_ALL}**+++*#%#*{Fore.RED}%@%%#%%%%%#*{Style.RESET_ALL}#+*+*{Fore.GREEN}###%%@%%%%@#####*{Style.RESET_ALL}%#####%%%%##**#%#%#**#%%###*#*=.               
           ---=+**+====++{Fore.GREEN}*%%##%@%{Style.RESET_ALL}%#*++==---={Fore.GREEN}*#%%####{Style.RESET_ALL}{Fore.GREEN}#%%######{Style.RESET_ALL}###**#%%*{Fore.RED}%@@%#%%#%%#*{Style.RESET_ALL}##**{Fore.GREEN}#%%%%%#####%###%%%*{Style.RESET_ALL}##%#*#%#%*###%%%%%####+==**++*.               
           +*******+=+*#*{Fore.GREEN}+#%%%@%%{Style.RESET_ALL}%########{Fore.GREEN}###########*{Style.RESET_ALL}*##%%%%%%###%%####**********####%%%%%#######%####**##%######%%%%%%%%%%#++######=               
           ......::::::::::-----------::-:::::::::-:-:----:::::::::..................::::------:::::::::::----:----------::::::::::::.."""

dungeon_art =rf"""{Fore.BLACK}     ______
   ,-' ;  ! `-.
  * :  !  :  . *
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##) {Fore.YELLOW} _{Fore.BLACK}  |
 |  :  ;`'  {Fore.YELLOW}(_){Fore.BLACK} (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|{Style.RESET_ALL}
"""

well_art = rf"""{Fore.YELLOW}
                 __
               .'/\'.
             .'-/__\-'.
           .'--/____\--'.
         .'--./______\.--'.
       .'--../________\..--'.
     .'--.._/__________\_..--'.
   .'--..__/____________\__..--'.
 .'--..___/______________\___..--'.
'========'================'========'{Style.RESET_ALL}
      {Fore.BLACK}[_|__]            [_|__]{Style.RESET_ALL}
     ={Fore.BLACK}[__|_]{Style.RESET_ALL}=====""====={Fore.BLACK}[__|_]{Style.RESET_ALL}==.
      {Fore.BLACK}[_|__] {Style.RESET_ALL}    '|     {Fore.BLACK}[_|__]{Style.RESET_ALL}  |
      {Fore.BLACK}[__|_] {Style.RESET_ALL}    |'     {Fore.BLACK}[__|_]{Style.RESET_ALL}  |
      {Fore.BLACK}[_|__]  {Fore.RED}.--JL--.  {Fore.BLACK}[_|__]{Style.RESET_ALL}  '===O
     {Fore.BLACK} [__|_]  {Fore.RED} \====/   {Fore.BLACK}[__|_]
      [_|__]_.-{Fore.RED}| .; |{Fore.BLACK}-._[_|__]
      [__|_]'._{Fore.RED} \__/{Fore.BLACK}(_.'[__|_]
     {Fore.BLUE} [.-._]            [_.-.]
      [_.-.'--..____..--'.-._]{Style.RESET_ALL}


"""
torture_art = rf"""
{Fore.GREEN}                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"{Style.RESET_ALL}
{Fore.RED}.....   -~~:<`{Fore.GREEN} !    ~?T#$$@@W@*?$$      /`{Style.RESET_ALL}
{Fore.RED}W$@@M!!! .!~~ {Fore.GREEN}!!     .:XUW$W!~ `"~:    :{Style.RESET_ALL}
{Fore.RED}#"~~`.:x%`!!  {Fore.GREEN}!H:   !WM$$$$Ti.: .!WUn+!`{Style.RESET_ALL}
{Fore.RED}:::~:!!`:X~ .: {Fore.GREEN}?H.!u "$$$B$$$!W:U!T$$M~{Style.RESET_ALL}
{Fore.RED}.~~   :X@!.-~  {Fore.GREEN} ?@WTWo("*$$$W$TH$! `{Style.RESET_ALL}
{Fore.RED}Wi.~!X$?!-~    : {Fore.GREEN}?$$$B$Wu("**$RM!{Style.RESET_ALL}
{Fore.RED}$R@i.~~ !     :  {Fore.GREEN} ~$$$$$B$$en:``{Style.RESET_ALL}
{Fore.RED}?MXT@Wx.~    :   {Fore.GREEN}  ~"##*$$$$M~{Style.RESET_ALL}
"""
dining_art = rf"""
                      {Fore.YELLOW}(*)                  (*){Style.RESET_ALL}
   {Fore.GREEN}(__)                  {Fore.YELLOW}^                    ^   {Style.RESET_ALL}             
   {Fore.GREEN}(oo) {Style.RESET_ALL}                 |      |             |               
   {Fore.GREEN}[..]  {Style.RESET_ALL}                |      =             |                
\ |  {Fore.GREEN}U           {Fore.YELLOW}(-){Style.RESET_ALL}     |     | |            | {Fore.YELLOW}(-) {Style.RESET_ALL}            
 ||   ==<_\=====/_|______=_____|=|____________=__|____\====/_      ||
 ||   )  {Fore.RED}||||||||||||||||||||||||||||||||||||||||||||||||||||{Style.RESET_ALL}      ||
 ||___)=={Fore.RED}||||||||||||||||||||||||||||||||||||||||||||||||||||{Style.RESET_ALL}  ____||
 |\====| {Fore.RED}||||||||||||||||||||||||||||||||||||||||||||||||||||{Style.RESET_ALL} |=====|
 |  \  |     |                                          |     |     |
 =   * =     =                                          =     =     =
"""
armoury_art = rf"""
                          {Fore.YELLOW} ___
                          ( ((
                           ) ))
  .::.                    / /(
 'M .-;-.-.-.-.-.-.-.-.-/| (({Style.RESET_ALL} ::::::::::::::::::::::::::::::::::::::::::::::.._
{Fore.YELLOW}(J ( ( ( ( ( ( ( ( ( ( ( |  ))   {Fore.YELLOW}-====================================-{Style.RESET_ALL}      _.>
{Fore.YELLOW} `P `-;-`-`-`-`-`-`-`-`-\| (({Style.RESET_ALL}::::::::::::::::::::::::::::::::::::::::::::::''
 {Fore.YELLOW} `::'                    \ \(
                           ) ))
                          (_(({Style.RESET_ALL}
"""
jail_art =rf"""
{Fore.RED}____________________
_]|  |  |  |  |  |{Fore.RED}[_
_]{Style.RESET_ALL}|==|==|==|==|==|{Fore.RED}[_
_]{Style.RESET_ALL}|_ _  |  |  |  |{Fore.RED}[_
_]{Style.RESET_ALL}|_|_[ |  |  |  |{Fore.RED}[_
_]{Style.RESET_ALL}|_|_[ |  |  |  |{Fore.RED}[_
_]{Style.RESET_ALL}|  |  |  |  |  |{Fore.RED}[_
_]{Style.RESET_ALL}|  |  |  |  |  |{Fore.RED}[_
_]{Style.RESET_ALL}|==|==|==|==|==|{Fore.RED}[_
_]{Style.RESET_ALL}|  |  |.-|--|  |{Fore.RED}[_
_]{Style.RESET_ALL}|  |  | `.  |  |{Fore.RED}[_
_]{Style.RESET_ALL}|  |  |  |`.|  |{Fore.RED}[_
_]{Style.RESET_ALL}|  |  |  |  |`.|{Fore.RED}[_
_]{Style.RESET_ALL}|  |  |  |  |  |{Fore.RED}[_
_]{Style.RESET_ALL}|==|==|==|==|==|{Fore.RED}[_
_]{Style.RESET_ALL}|__|__|__|__|__|{Fore.RED}[_ {Style.RESET_ALL}
"""

sleeping_art = rf"""
{Fore.RED}        ||
        ||                   ||
     ||{Style.RESET_ALL}/{Fore.RED}||{Style.RESET_ALL}___  {Fore.RED}              ||
     ||{Style.RESET_ALL} /`   )____________{Fore.RED}||_/|
     ||{Style.RESET_ALL}/___ //_/_/_/_/_/_/{Fore.RED}||/ |
     ||{Style.RESET_ALL}(___)/_/_/_/_/_/_/_{Fore.RED}||  |
     ||{Style.RESET_ALL}     |_|_|_|_|_|_|_{Fore.RED}|| /|
     ||{Style.RESET_ALL}     | | | | | | | {Fore.RED}||/||
     ||{Style.RESET_ALL}~~~~~~~~~~~~~~~~~~~{Fore.RED}||
     ||                   ||{Style.RESET_ALL}
"""

kitchen_art =rf"""
                                 {Fore.YELLOW} \\\{Style.RESET_ALL}
        ____               ________{Fore.YELLOW}```{Style.RESET_ALL}
        \  =|-            [________]{Fore.RED} \{Style.RESET_ALL}
        |  =| |     _     |        | {Fore.RED} \  {Style.RESET_ALL}         __
        |__=|-  O--(_)    `.______.'  {Fore.RED} \{Style.RESET_ALL} O=======(__)
               /|\
             (/(|(\
"""

outer_vault_art = rf"""
                            {Fore.RED} ,==.
                             \\//
                        {Fore.YELLOW}    .-~~-.
                          ,",-""-.".
                         | |      | |
                         | |      | |
                         ". `, ,-" ,'
                           `-,_,-'  
                    {Style.RESET_ALL}
"""

vault_art = rf"""
{Fore.GREEN}                                      ____________
                                 (`-..________....---''  ____..._.-`
                                  \\`._______.._,.---'''     ,'
                                  ; )`.      __..-'`-.      /
                                 / /     _.-' _,.;;._ `-._,'
                                / /   ,-' _.-'  //   ``--._``._
                              ,','_.-' ,-' _.- (( =-    -. `-._`-._____
                            ,;.''__..-'   _..--.\\.--'````--.._``-.`-._`.
             _          |\,' .-''        ```-'`---'`-...__,._  ``-.`-.`-.`.
  _     _.-,'(__)\__)\-'' `     ___  .          `     \      `--._
,',)---' {Fore.RED}/|){Fore.GREEN}          `     `      ``-.   `     /     /     `     `-.
\_____--.  '`  `               __..-.  \     . (   < _...-----..._   `.
 \_,--..__. \\ .-`.\----'';``,..-.__ \  \      ,`_. `.,-'`--'`---''`.  )
           `.\`.\  `_.-..' ,'   _,-..'  /..,-''(, ,' ; ( _______`___..'__
                   ((,(,__(    ((,(,__,'  ``'-- `'`.(\  `.,..______  
                                                      ``--------..._``--.__
{Style.RESET_ALL}"""

lose = rf"""{Fore.RED}















                                                         ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
                                                         ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
                                                        ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
                                                        ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
                                                        ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
                                                         ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
                                                          ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
                                                        ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
                                                              ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                                                                                    ░                   
{Style.RESET_ALL}"""

win = fr"""{Fore.YELLOW}
















                                                                ▓██   ██▓ ▒█████   █    ██     █     █░ ██▓ ███▄    █  ▐██▌ 
                                                                 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓█░ █ ░█░▓██▒ ██ ▀█   █  ▐██▌ 
                                                                  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒█░ █ ░█ ▒██▒▓██  ▀█ ██▒ ▐██▌ 
                                                                  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░█░ █ ░█ ░██░▓██▒  ▐▌██▒ ▓██▒ 
                                                                  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░░██▒██▓ ░██░▒██░   ▓██░ ▒▄▄  
                                                                   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▓░▒ ▒  ░▓  ░ ▒░   ▒ ▒  ░▀▀▒ 
                                                                 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░      ▒ ░ ░   ▒ ░░ ░░   ░ ▒░ ░  ░ 
                                                                 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░   ░   ▒ ░   ░   ░ ░     ░ 
                                                                 ░ ░         ░ ░     ░            ░     ░           ░  ░    
                                                                 ░ ░                                                       
{Style.RESET_ALL}"""

storage_art =rf"""
⠀⠀⠀{Fore.RED}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⡤⠤⠴⠶⣶⣶⣶⣶⣶⣶⣶⣦⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣤⣄⣉⠉⠙⠛⠛⠛⠛⠛⠛⠛⠛⠋⠉⣉⣠⣤⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⣿⣿⡇⢰⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⡆⢸⣿⣿⣇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣈⣉⡉⠁⠘⠛⠻⠿⠿⠇⠸⠿⠿⠟⠛⠓⠀⢉⣉⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠛⠛⠿⠿⠿⢷⣶⣶⣶⣶⣶⣶⣶⣶⣾⠿⠿⠿⠛⠛⠁⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣿⣷⡆⢀⣦⣤⣤⣤⣤⡄⢠⣤⣤⣤⣤⣴⡆⢰⣾⣿⣦⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⢻⣿⣿⡇⢸⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⡇⠀⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⡇⢸⣿⣿⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣈⡉⠛⠀⠛⠿⠿⠿⠿⠇⠸⠿⠿⠿⠿⠟⠀⠘⠉⣉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⠿⣿⣿⣶⣶⣶⣶⣦⣤⣤⣤⣶⣶⣶⣶⣾⣿⡿⠿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠐⣦⣤⡄⢈⣉⣉⠉⠙⠛⠛⠛⠉⢉⣉⡉⢀⣤⣤⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠃⠈⠿⠿⠿⠿⠇⠸⠿⠿⠿⠿⠁⠘⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀{Style.RESET_ALL}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

#Shadow depths

dungeon_entrance = False
well = False
torture = False
dining = False
armoury = False
jail = False
sleeping = False
storage = False
kitchen = False
outer_vault = False
vault = False
inventory = ["map", "sword", "torch", "compass",]
swords = []
answer = ""
player_health=10
monster_health=15

def add_to_inventory(item):
     inventory.append(item)

def scroll(text):
    for char in text:
        print(char, end="", flush=True,)
        time.sleep(0.01) 
    return "...> "

def rolling(room):
    global monster_health,player_health
    while True:
        Player_roll=input("**ROLL** to hit  ").lower()
        if Player_roll=="roll":
            diceroll=random.randint(1,20)
            print(diceroll)
            #this is the players attacks on the enemy
            if diceroll <= 5:
                print(f"You swing your sword at the enemy, but completely {Fore.RED}miss{Style.RESET_ALL}")
            elif diceroll > 5  and diceroll <=10 :
                print (f"You swipe at the enemy, landing glancing blow  and dealing{Fore.GREEN} 1 point of damage{Style.RESET_ALL}")
                monster_health -=1
            elif diceroll > 10 and diceroll <= 15:
                print (f"You sink your blade into the enemy, dealing{Fore.GREEN} 2 points of damage{Style.RESET_ALL}")
                monster_health -=2
            elif diceroll >15 and diceroll <=19:
                print(f"You land a heavy hit on the enemy dealing{Fore.GREEN} 3 points of damage{Style.RESET_ALL}")
                monster_health -=3
            else:
                print(f"You strike a devastating blow at the monsters weakest point, dealing{Fore.GREEN} 6 points of damage{Style.RESET_ALL}")
                monster_health -=6
            # print("The Monster takes some damage, hp remaining "+ str(monster_health))
 
            #Monster attack on player
 
            diceroll=random.randint(1,20)
            print(diceroll)
            if diceroll <= 5:
                print(f"The Monster Strikes back in your direction, but you manage to{Fore.GREEN} dive{Style.RESET_ALL}out of the way")
            elif diceroll > 5  and diceroll <=10 :
                print (f"The monster, swings. you try to parry with the sword but you get nicked fo{Fore.RED} 1 hit point{Style.RESET_ALL}")
                player_health -=1
            elif diceroll > 10 and diceroll <= 15:
                print (f"The monster manages to land a decent hit on you dealing{Fore.RED} 2 points of damage{Style.RESET_ALL}")
                player_health -=2
            elif diceroll >15 and diceroll <=19:
                print(f"The monster lands a strong hit on you, knocking the wind out of your lungs for{Fore.RED} 3 points of damage{Style.RESET_ALL}")
                player_health -=3
            else:
                print(f"The monster hits a devastating blow at your weakest point, dealing{Fore.RED} 6 points of damage{Style.RESET_ALL}")
                player_health -=6
            # print("You take some damage, hp remaining "+ str(player_health))
            if monster_health <=0:
                print(f"{Fore.RED}You have slain the monster{Style.RESET_ALL}")
                room()
                break
            elif player_health <=0:
                print(f"{Fore.RED}The Monster dances on your grave.{Style.RESET_ALL}")
                time.sleep(3)
                game_over()
                # restart()
                break
            print("Your hp remaining after the attack = "+ str(player_health))
            print("The Monsters remaining hp after that attack = "+ str(monster_health))     

os.system("cls")
time.sleep (2)

def titles():
    # pygame.mixer.init()
    # pygame.mixer.music.load("./audio/Theme.mp3")
    # pygame.mixer.music.play()
    print (title_art)
    time.sleep(8.5)
    os.system("cls")
    print (castle_art)
    time.sleep(8)
    os.system("cls")
    dungeon_entrance_room()

#DUNGEON ENTRANCE
def dungeon_entrance_room():
    os.system("cls")
    print (dungeon_art)
    count = 0
    max_count = 2
    global dungeon_entrance
    if not dungeon_entrance:
        scroll (f"Your adventure has brought you to this place, the map taken from the thieves' guild spoke of a long thought lost treasure and you decided that this treasure was rightfully yours!\nArmed with a {Fore.BLUE}short sword{Style.RESET_ALL}, a {Fore.BLUE}torch{Style.RESET_ALL} and your {Fore.BLUE}compass{Style.RESET_ALL} you had made your way to the dungeon of this long-abandoned castle and as you had passed through the rusted iron door behind you, it had slammed shut with a loud CLUNK.\nIndicating you are now locked in this chamber, looking down at your trusty compass, you know you are facing {Fore.GREEN}south{Style.RESET_ALL}.\nThe room is stone and holds the memories of a past tyrannical king.\nThe room seems empty but for a closed iron gate and some old chains ominously dangling from the walls.")
        dungeon_entrance = True
        choice = input (scroll(f"\nWhat would you like to do?\nGo {Fore.RED}\n     NORTH    \n{Style.RESET_ALL}{Fore.RED}WEST       EAST {Style.RESET_ALL}{Fore.GREEN}\n     SOUTH    {Style.RESET_ALL}     Or {Fore.GREEN} STAY{Style.RESET_ALL} where you are.....")).lower()

    else:
        os.system("cls")
        print (dungeon_art)
        scroll("You have returned to the start of your adventure. The same iron gate and the same ominous chains dangling from the wall.")
        choice = input (scroll(f"\nWhat would you like to do?\nGo {Fore.RED}\n     NORTH    \n{Style.RESET_ALL}{Fore.RED}WEST       EAST {Style.RESET_ALL}{Fore.GREEN}\n     SOUTH    {Style.RESET_ALL}     Or {Fore.GREEN} STAY{Style.RESET_ALL} where you are.....")).lower()

   
    while count < max_count:
        if choice == "south":
            os.system("cls")
            scroll ("The old iron gate swings open with a creak. |\nYou begin walking along the corridor, seeing old torches on the walls spring to life in a magical glow. \nYou reach another door passing through into ")
            well_room()
            break
        elif choice == "stay":
            os.system("cls")
            do_nothing()
            break
        else:
            os.system("cls")
            count +=1
            scroll ("That is not an option. Choose again and choose wisely!.")
            choice = input (scroll(f"\nWhat would you like to do?\nGo {Fore.RED}\n     NORTH    \n{Style.RESET_ALL}{Fore.RED}WEST       EAST {Style.RESET_ALL}{Fore.GREEN}\n     SOUTH    {Style.RESET_ALL}     Or {Fore.GREEN} STAY{Style.RESET_ALL} where you are.....")).lower()

    if count == max_count:
                os.system("cls")
                scroll(f"Your ability to not follow basic commands has settled your {Fore.RED}fate{Style.RESET_ALL} as the {Fore.RED}door locks{Style.RESET_ALL} and your {Fore.RED}torch {Fore.RED}dies{Style.RESET_ALL}. Enjoy the last of your days in darkness....")
                game_over()

 

#WELL ROOM
def well_room():
    os.system("cls")
    print (well_art)
    global well
    if not well:
        scroll(f"As you Enter this room, you notice in the centre is an old {Fore.GREEN}well{Style.RESET_ALL}, the bucket dangling from old rope. \nIt seems that the dungeon workers here, would use this well to collect water for themselves and the prisoners. \nYou see a couple of rotted tables, and the remains of someone who used to be here, the skeleton of a person lies shattered on the ground.")
        well = True
    else:
        os.system("cls")
        print (well_art)
        scroll(f"Once more you return to the {Fore.GREEN}well{Style.RESET_ALL}. The shattered bones remain undisturbed.")
    while True:
         os.system("cls")
         print (well_art)
         choice = input (scroll(f"\nWhat would you like to do?\nGo {Fore.GREEN}\n     NORTH    \n{Style.RESET_ALL}{Fore.GREEN}WEST       EAST {Style.RESET_ALL}{Fore.GREEN}\n     SOUTH    {Style.RESET_ALL}     Or {Fore.GREEN} SEARCH{Style.RESET_ALL} the well\nEnter your choice: ")).lower()

         if choice == "north":
            os.system("cls")
            scroll (f"You head for the {Fore.GREEN}northern door{Style.RESET_ALL}. It opens with ease (since you just came this way).")
            time.sleep(3)
            dungeon_entrance_room()
            break
         elif choice == "east":
            os.system("cls")
            scroll (f"You head through the {Fore.GREEN}east door{Style.RESET_ALL} and continue down the passage to the next room.")
            time.sleep(3)
            dining_room()
            break
         elif choice == "south":
            os.system("cls")
            if "key" not in inventory:
              scroll (f"The heavy door is locked and wont open. Maybe you can find the {Fore.YELLOW}key{Style.RESET_ALL}.")
              time.sleep(3)
            else:
              os.system("cls")
              scroll (f"You put the {Fore.YELLOW}rusty key{Style.RESET_ALL} in the lock and turn it. With a little effort the lock gives and the door opens so you continue through the {Fore.GREEN}south door{Style.RESET_ALL} on your quest.")
              time.sleep(3)
              jail_room()
              break
         elif choice == "west":
            os.system("cls")
            scroll (f"You head through the {Fore.GREEN}west door{Style.RESET_ALL} and continue down the passage to the next room.")
            time.sleep(3)
            torture_room()
            break
         elif choice == "search":
            if  "key" not in inventory:
                os.system("cls")
                print (well_art)
                inventory.append("key")
                scroll(f"You {Fore.GREEN}search{Style.RESET_ALL} around in the putrid slime of the well and find a {Fore.YELLOW}rusty key{Style.RESET_ALL}. Maybe it opens one of these doors?")
                time.sleep(3)
            else:
                os.system("cls")
                print (well_art)
                scroll (f"You {Fore.GREEN}search{Style.RESET_ALL} the well and find nothing more.")
                time.sleep(3)

         else:
            os.system("cls")
            print (well_art)
            scroll("That is not a choice. Choose again.\n ")
            
#TORTURE ROOM
def torture_room():
    os.system("cls")
    print (torture_art)
    global torture
    if not torture:
        scroll("As you enter this room the first thing that you notice is the large amounts of dried blood on the floor.\nyou see large metal shelves with doors and old skeletons laying inside.\nLying around the room you see large stone tables covered in old blood, long serrated blades, meat hooks, strange devices connected to winches and other instruments of torture.\nYou also notice cabinets filled with vials and bottles of strange liquids.\nThe smell of iron hits your nose and you also see in this moment that some of the corpses in this room are beginning to shift, readying their attack. ")
        torture = True
        time.sleep(3)
    else:
        os.system("cls")
        print (torture_art)
        scroll("\n\nYou stand victorious in the room, recovering from the recent battle, you decide where to go next\n\n")
        choice = input (scroll(f"\nWhat would you like to do?\nGo {Fore.RED}\n     NORTH    \n{Style.RESET_ALL}{Fore.GREEN}WEST       EAST {Style.RESET_ALL}{Fore.GREEN}\n     SOUTH    {Style.RESET_ALL}")).lower()
        if choice == "east":
            os.system("cls")
            scroll(f"You return through the {Fore.GREEN}door{Style.RESET_ALL} you came though.")
            time.sleep(3)
            well_room()
            return
        elif choice == "south":
            os.system("cls")
            scroll(f"You move through the {Fore.GREEN}southern{Style.RESET_ALL} door relieved to get away from the repugnant stench.")
            time.sleep(3)
            armoury_room()
            return
        elif choice == "west":
            os.system("cls")
            scroll(f"You open the door and {Fore.GREEN}leave{Style.RESET_ALL} this abomination of a room....")
            time.sleep(3)
            crushing_room()
            return
        else:
            scroll("That is not a choice. Choose again. ")
        return
    while True:
         choice = input (scroll(f"\nWhat would you like to do?\nGo {Fore.RED}\n     NORTH    \nWEST       EAST \n     SOUTH    {Style.RESET_ALL}      {Fore.GREEN} FIGHT    {Fore.GREEN}RUN{Style.RESET_ALL}")).lower()
         if choice == "run":
            os.system("cls")
            scroll (f"You head back through the {Fore.GREEN}east door{Style.RESET_ALL}, seemingly fleeing from death that surely awaited!")
            torture = False
            time.sleep(3)
            well_room()
         elif choice == "fight":
            os.system("cls")
            print (torture_art)
            scroll (f"You decided to {Fore.GREEN}fight!{Style.RESET_ALL}\n\n")
            rolling(torture_room)
            break

#DINING AREA
def dining_room():
    os.system("cls")
    print (dining_art)
    global dining
    if not dining:
        scroll("You enter this dusty room, the smell of rotted meat and vegetables hits your nose like a punch to the face, it takes everything in you to not gag.\n As you look around you see an old wooden table withered by age and mould. On the table lies the remnants of food that can no longer be distinguished as food, flies and other small insects crawl around looking for whatever shreds of plant matter or meat they can find.\n There are is a dead soldier sat in one of the seats that are still around the table, posed in a mockery of life and that of a jovial evening meal.\n The room is dark other than a couple of everlight torches that sit in sconces on the walls. As you take in the scene, the soldier begins to move!\nWhat do you do?")
        choice = input (scroll(f"\nWhat would you like to do?\nGo {Fore.RED}\n     NORTH    \n{Style.RESET_ALL}{Fore.RED}WEST       EAST {Style.RESET_ALL}{Fore.RED}\n     SOUTH    {Style.RESET_ALL}      {Fore.GREEN} FIGHT     RUN{Style.RESET_ALL}")).lower()
        dining = True
        if choice == "run":
            os.system("cls")
            scroll (f"You {Fore.GREEN}run in fear through the west door")
            time.sleep(3)
            dining = False
            well_room()
        elif choice == "fight".lower():
            os.system("cls")
            print (dining_art)
            scroll (f"You take up your sword and prepare to {Fore.GREEN}battle{Style.RESET_ALL} against this vile foe")
            rolling(dining1)
    else:
        os.system("cls")
        print (dining_art)
        scroll ("As you enter the dining hall you feel slight relief the soldier remained dead. You decide where to go next")
        choice = input (scroll(f"\nWhat would you like to do?\nGo {Fore.GREEN}\n     NORTH    \n{Style.RESET_ALL}{Fore.GREEN}WEST       EAST {Style.RESET_ALL}{Fore.GREEN}\n     SOUTH    {Style.RESET_ALL}"))
    if choice == "north".lower():
        os.system("cls")
        scroll (f"You decide to go {Fore.GREEN}north{Style.RESET_ALL}")
        time.sleep(3)
        dungeon_entrance_room()
    elif choice == "west".lower():
        os.system("cls")
        scroll (f"You decide to go {Fore.GREEN}west{Style.RESET_ALL}")
        time.sleep(3)
        well_room()
    elif choice == "south".lower(): 
        os.system("cls")       
        scroll (f"You decide to go {Fore.GREEN}south{Style.RESET_ALL}")
        time.sleep(3)
        sleeping_room()
    elif choice == "east":
        os.system("cls")
        scroll (f"You decide to go {Fore.GREEN}east{Style.RESET_ALL}")
        time.sleep(3)
        spike_pit()         
       
def rolling(room):
        global monster_health, player_health
        player_health=10
        monster_health=15
        while True:
            Player_roll=input("**ROLL** to hit  ").lower()
            if Player_roll=="roll":
                diceroll=random.randint(1,20)
                print(diceroll)
                #this is the players attacks on the enemy
                if diceroll <= 5:
                    print(f"You swing your sword at the enemy, but completely {Fore.RED}miss{Style.RESET_ALL}")
                elif diceroll > 5  and diceroll <=10 :
                    print (f"You swipe at the enemy, landing glancing blow  and dealing{Fore.GREEN} 1 point of damage{Style.RESET_ALL}")
                    monster_health -=1 
                elif diceroll > 10 and diceroll <= 15:
                    print (f"You sink your blade into the enemy, dealing{Fore.GREEN} 2 points of damage{Style.RESET_ALL}")
                    monster_health -=2
                elif diceroll >15 and diceroll <=19:
                    print(f"You land a heavy hit on the enemy dealing{Fore.GREEN} 3 points of damage{Style.RESET_ALL}")
                    monster_health -=3
                else: 
                    print(f"You strike a devastating blow at the monsters weakest point, dealing{Fore.GREEN} 6 points of damage{Style.RESET_ALL}")
                    monster_health -=6 
                # print("The Monster takes some damage, hp remaining "+ str(monster_health))

                #Monster attack on player 

                diceroll=random.randint(1,20)
                print(diceroll)
                if diceroll <= 5:
                        print(f"The Monster Strikes back in your direction, but you manage to {Fore.GREEN}dive{Style.RESET_ALL} out of the way")
                elif diceroll > 5  and diceroll <=10 :
                    print (f"The monster, swings. you try to parry with the sword but you get nicked for{Fore.RED} 1 hit point{Style.RESET_ALL}")
                    player_health -=1 
                elif diceroll > 10 and diceroll <= 15:
                    print (f"The monster manages to land a decent hit on you dealing{Fore.RED} 2 points of damage{Style.RESET_ALL}")
                    player_health -=2
                elif diceroll >15 and diceroll <=19:
                    print(f"The monster lands a strong hit on you, knocking the wind out of your lungs fo{Fore.RED}r 3 points of damage{Style.RESET_ALL}")
                    player_health -=3
                else: 
                    print(f"The monster hits a devastating blow at your weakest point, dealing{Fore.RED} 6 points of damage{Style.RESET_ALL}")
                    player_health -=6 
                # print("You take some damage, hp remaining "+ str(player_health))
                if monster_health <=0:
                    print(f"{Fore.GREEN}You have slain the monster{Style.RESET_ALL}")
                    room()
                    break
                elif player_health <=0:
                    print(f"{Fore.RED}The Monster dances on your grave.{Style.RESET_ALL}")
                    time.sleep(3)
                    game_over()
                    # restart()
                    break
                print(f"You take some {Fore.RED}damage{Style.RESET_ALL}, hp remaining "+ str(player_health))
                print(f"The Monster takes some {Fore.GREEN}damage{Style.RESET_ALL}, hp remaining "+ str(monster_health))

def dining1():
    scroll("You stand victorious in the room, recovering from the recent battle, you decide where to go next")
    choice = input (scroll(f"\nWhat would you like to do?\nGo {Fore.GREEN}\n     NORTH    \n{Style.RESET_ALL}{Fore.GREEN}WEST       EAST {Style.RESET_ALL}{Fore.GREEN}\n     SOUTH    {Style.RESET_ALL}"))
    if choice == "north".lower():
        scroll (f"You decide to go {Fore.GREEN}north{Style.RESET_ALL}")
        dungeon_entrance_room()
    elif choice == "west".lower():
        scroll (f"You decide to go {Fore.GREEN}west{Style.RESET_ALL}")
        well_room()
    elif choice == "south".lower():        
        scroll (f"You decide to go {Fore.GREEN}south{Style.RESET_ALL}")
        sleeping_room()
    elif choice == "east":
        scroll (f"You decide to go {Fore.GREEN}east{Style.RESET_ALL}")
        spike_pit()

#ARMOURY
def armoury_room():
    os.system("cls")
    print (armoury_art)
    global armoury
    if not armoury:
        scroll(f"This stone chamber that you enter has {Fore.YELLOW}three beautiful paintings{Style.RESET_ALL} on the wall, dulled by age and covered in cobwebs but beautiful none the less,\nbeneath them are empty slots that look like they could hold {Fore.YELLOW}swords{Style.RESET_ALL}\n\n.\nThese paintings depict different things;\nThe first, a scene showing several knights clashing in a fierce battle.\nThe second a heroic knight kneeling before a king being knighted.\nThe third, shows the same knight from the knighting photo in a coffin, surrounded by other people at his funeral.\nAll around this room are shelves and cabinets filled with everything from sets of armour, to shields, bows, arrows and other various weapons like great axes and morning stars.\nThe door out of this room is locked and you see 3 unlit torches above the door, what do you do?")
        armoury=True
    else:
        os.system("cls")
        print (armoury_art)
        scroll ("You return to the stone chamber. Which way will you go? ")
    while True:
        os.system("cls")
        print (armoury_art)
        choice = input (scroll(f"\nWhat would you like to do?\nGo {Fore.GREEN}\n     NORTH    \n{Style.RESET_ALL}{Fore.RED}WEST{Style.RESET_ALL}       {Fore.GREEN}EAST {Style.RESET_ALL}{Fore.RED}\n     SOUTH    {Style.RESET_ALL}     Search: {Fore.GREEN} ARMOUR     WEAPONS     ROOM{Style.RESET_ALL}")).lower()
        if choice =="north".lower():
            os.system("cls")
            scroll ("You decide to head north")
            time.sleep(3)
            torture_room()
            break        
        elif choice == "east".lower():
            os.system("cls")
            scroll ("You go through the door heading east")
            time.sleep(3)
            jail_room()
            break
        elif choice == "armour":
            if "bloody" in swords:
                os.system("cls")
                scroll(f"You have already found the {Fore.YELLOW}old sword{Style.RESET_ALL}.")
                time.sleep(3)
            else:
                os.system("cls")
                scroll(f"You find an {Fore.YELLOW}old sword{Style.RESET_ALL}, covered in dried blood")
                swords.append("bloody")
                time.sleep(3)
        
        elif choice=="weapons".lower():
            if "rusted" in swords:
                os.system("cls")
                scroll (f"You have already found the {Fore.YELLOW}rusted sword{Style.RESET_ALL}.")
                time.sleep(3)
            else:
                os.system("cls")
                scroll(f"you find a {Fore.YELLOW}rusted sword{Style.RESET_ALL}, crippled with age")
                swords.append("rusted")
                time.sleep(3)
        
        elif choice=="room".lower():
            if "pristine" in swords:
                os.system("cls")
                scroll(f"You have already found the {Fore.YELLOW}pristine sword{Style.RESET_ALL}.")
                time.sleep(3)
            else:
                os.system("cls")
                scroll(f"You find a {Fore.YELLOW}pristine sword{Style.RESET_ALL} that has beautiful ceremonial carvings on it")
                swords.append("pristine")
                time.sleep(3)
        else:
            scroll("That is not a choice. Choose again! ")
    
        if len(swords) == 3:
            while True:
                os.system("cls")
                print (armoury_art)
                time.sleep(3)
                scroll("Solve the puzzle!\n")
                scroll(f"A: {Fore.YELLOW}Pristine sword{Style.RESET_ALL} with Funeral Painting, {Fore.YELLOW}Rusted sword{Style.RESET_ALL} with knight painting, {Fore.YELLOW}Bloodied sword{Style.RESET_ALL} with War  painting\n")
                time.sleep(0.5)
                scroll(f"B: {Fore.YELLOW}Pristine sword{Style.RESET_ALL} with War Painting, {Fore.YELLOW}Rusted sword{Style.RESET_ALL} with Knight painting,{Fore.YELLOW} Bloodied sword with Funeral painting\n")
                time.sleep(0.5)
                scroll(f"C: {Fore.YELLOW}Pristine sword{Style.RESET_ALL} with Knight Painting, {Fore.YELLOW}Rusted sword{Style.RESET_ALL} with Funeral painting, {Fore.YELLOW}Bloodied sword with War painting\n")
                time.sleep(0.5)
                scroll(f"D: {Fore.YELLOW}Pristine sword{Style.RESET_ALL} with Funeral Painting, {Fore.YELLOW}Rusted sword{Style.RESET_ALL} with War painting, {Fore.YELLOW}Bloodied sword with Knight painting\n")
                time.sleep(0.5)
                choice=input ("**A** **B** **C** **D**")
                if choice.lower() == "c":
                    os.system("cls")
                    print (armoury_art)
                    scroll("The lights above the door flash into life and you watch as the door itself, begins to creak open.\n What do you do?")
                    break
            choice=input (scroll(f"\nWhat would you like to do?\nGo {Fore.GREEN}\n     NORTH    \n{Style.RESET_ALL}{Fore.RED}WEST{Style.RESET_ALL}       {Fore.GREEN}EAST {Style.RESET_ALL}{Fore.GREEN}\n     SOUTH    {Style.RESET_ALL}     Or {Fore.GREEN} STAY{Style.RESET_ALL} where you are.....")).lower()
            if choice == "north":
                os.system("cls")
                scroll(f"you decide to go {Fore.GREEN}north{Style.RESET_ALL}")
                time.sleep(3)
                torture_room()
                break
            elif choice=="east":
                os.system("cls")
                scroll(f"you decide to go {Fore.GREEN}east{Style.RESET_ALL}")
                time.sleep(3)
                jail_room()
                break
            elif choice == "south":
                os.system("cls")
                scroll(f"You head {Fore.GREEN}south through the now open door{Style.RESET_ALL}")
                time.sleep(3)
                storage_room()
                break   

#JAIL CELLS
def jail_room():
    os.system("cls")
    print (jail_art)
    global jail
    if not jail:
        scroll(f"You enter a large, long room. Rusted metal bars on either side of the corridor show this to be the cells of the dungeon.\n Inside the cells are the skeletal remains of old prisoners. The doors to these cells all sit open, seemingly already raided and looted. Ahead of you is a solid iron door, bolted closed and seemingly flush with the wall.\n Above the door, words are carved into the stone, glowing with a faint arcane energy. They read:\n\n{Fore.CYAN}I get cut but I never bleed.\nI have teeth but I don't bite.\nI get put on a ring but I'm not a diamond.\nI get turned but I'm not a page.{Style.RESET_ALL}\nWhat am I?\n\nTo the east is a corridor that heads into a different room, and directly opposite to the west is a door with a sign above it that reads \"Armoury.\" There is nothing else in this space. What do you do?")
        jail = True
    else:
        os.system("cls")
        print (jail_art)
        scroll("Back in the cells You ponder the riddle..")
    while True:
        choice = input (scroll(f"\nWhat would you like to do?\nGo {Fore.GREEN}\n     NORTH    \n{Style.RESET_ALL}{Fore.GREEN}WEST       EAST {Style.RESET_ALL}{Fore.RED}\n     SOUTH    {Style.RESET_ALL}     Or {Fore.GREEN} Solve{Style.RESET_ALL} the riddle.")).lower()
        if choice == "north":
            os.system("cls")
            scroll(f"You return to the room with the well, but the door locks as you close it.")
            time.sleep(3)
            well_room()
        elif choice == "east":
            os.system("cls")
            scroll(f"You go {Fore.GREEN}east{Style.RESET_ALL}.")
            time.sleep(3)
            acid_pit()
        elif choice == "west":
            os.system("cls")
            scroll(f"You go {Fore.GREEN}west{Style.RESET_ALL}.")
            time.sleep(3)
            armoury_room()
        elif choice == "solve":
            os.system("cls")
            print (jail_art)
            riddle = input(f"{Fore.CYAN}I get cut but I never bleed.\nI have teeth but I don't bite.\nI get put on a ring but I'm not a diamond.\nI get turned but I'm not a page.{Style.RESET_ALL}\nWhat am I? ")
            if riddle.lower() == "key":
                os.system("cls")
                print(f"As you speak the word '{riddle}', the words above the door flash in a bright green light, and the door before you opens.\nYou walk through.")
                time.sleep(3)
                outer_vault_room()
            else:
                os.system("cls")
                print(f"You speak the word '{riddle}', but the words above the door flash red, and you find yourself back in the first room of the dungeon.")
                time.sleep(3)
                dungeon_entrance_room()
        else:
                scroll("That is not a choice. Choose again. ")

#SLEEPING AREA
def sleeping_room():
    os.system("cls")
    print (sleeping_art)
    global sleeping
    if not sleeping:
        os.system("cls")
        scroll(f"You enter a large barracks room and see several uncomfortable-looking mattresses on the ground. The material is worn and ragged with age. Atop these mattresses, you see the bones of old guards still in their armor, representing the emblem of the old king. Old chests lie open and looted, and you notice the bodies of the {Fore.RED}skeletons{Style.RESET_ALL} beginning to shift and move.")
        sleeping = True
        time.sleep(3)
    else:
        os.system("cls")
        print (sleeping_art)
        scroll(f"The barracks are quiet now that you have killed the {Fore.RED}skeletons{Style.RESET_ALL}.")
        choice = input (scroll(f"\nWhat would you like to do?\nGo {Fore.GREEN}\n     NORTH    \n{Style.RESET_ALL}{Fore.RED}WEST       EAST {Style.RESET_ALL}{Fore.GREEN}\n     SOUTH    {Style.RESET_ALL}")).lower()
        if choice == "north":
            os.system("cls")
            scroll(f"You go {Fore.GREEN}north{Style.RESET_ALL} through the door...")
            time.sleep(3)
            dining_room()
            return
        elif choice == "south":
            os.system("cls")
            scroll(f"You proceed through the {Fore.GREEN}southern{Style.RESET_ALL} door.")
            time.sleep(3)
            kitchen_room()
            return

    while True:
        os.system("cls")
        print (sleeping_art)
        choice = input (scroll(f"\nWhat would you like to do?\nGo {Fore.RED}\n     NORTH    \n{Style.RESET_ALL}{Fore.RED}WEST       EAST {Style.RESET_ALL}{Fore.RED}\n     SOUTH    {Style.RESET_ALL}      {Fore.GREEN} FIGHT     RUN     GIVE UP{Style.RESET_ALL}")).lower()
        if choice == "run":
            scroll(f"You run back {Fore.GREEN}north{Style.RESET_ALL} and through the door. Cowardly behavior.")
            time.sleep(3)
            os.system("cls")
            sleeping = False
            dining_room()
            break
        elif choice == "give up":
            give_up()
            break
        elif choice == "fight":
            os.system("cls")
            print (sleeping_art)
            scroll(f"You decided to {Fore.GREEN}fight!{Style.RESET_ALL}\n\n")
            rolling(sleeping_room)
            break

#STORAGE AREA
def storage_room():
    os.system("cls")
    print (storage_art)
    global storage
    if not storage:
        print("This room is a large area full of shelves, old barrels, old crates and just various bits and pieces scatter the stone floor.\n Again, its like everything here has been looted, the only valuable things taken and lost to time.\n There are 3 doors in this room, the one you came through, one that heads west, the other, east.\nWhat do you do?")
        storage=True
    else:
        os.system("cls")
        print (storage_art)
        scroll ("Back in the storage room. You don't need to be here, unless you fancy a spot of spring cleaning. Choose your path. ")
    while True:     
        choice = input (scroll(f"\nWhat would you like to do?\nGo {Fore.GREEN}\n     NORTH    \n{Style.RESET_ALL}{Fore.GREEN}WEST       EAST {Style.RESET_ALL}{Fore.RED}\n     SOUTH    {Style.RESET_ALL}")).lower()
        if choice =="north".lower() :
            os.system("cls")
            scroll (f"you decide to head {Fore.GREEN}north{Style.RESET_ALL}")
            time.sleep(3)
            armoury_room()        
        elif choice == "west".lower():
            os.system("cls")
            scroll (f"you decide to go {Fore.GREEN}west{Style.RESET_ALL}\n This was a mistake\n  You leave the storage room and walk down a short corridor before entering another smaller room.\n It is empty entirely so, but as you entered, you stepped on a trip wire, looking up, the last thing you see is the giant axes swinging towards you, slicing you in half!\n GAME OVER ")
            time.sleep(3)            
        elif choice == "east".lower():
            os.system("cls")
            scroll(f"you decide to head {Fore.GREEN}{Style.RESET_ALL}east.")
            time.sleep(3)
            outer_vault_room()
        else:
            scroll("I think the fumes in this room have gone to your head. That is not an option.")

#KITCHEN AREA
def kitchen_room():
    os.system("cls")
    print (kitchen_art)
    global kitchen
    if not kitchen:
        scroll("You enter a large stone kitchen, counter tops around the sides of the room covered in partially prepared food thats rotted with time, the large cast iron ovens rusted with time, in the centre is a large island with what looks like what used to be edible fully prepared meals but now rotted beyond recognition. There is a pantry the stench of rot and decay eminating from within.")
        kitchen = True
        choice = input (scroll(f"\nWhat would you like to do?\nGo {Fore.GREEN}\n     NORTH    \n{Style.RESET_ALL}{Fore.GREEN}WEST{Style.RESET_ALL}       {Fore.RED}EAST {Style.RESET_ALL}{Fore.RED}\n     SOUTH    {Style.RESET_ALL}     Or {Fore.GREEN} EAT{Style.RESET_ALL} the food.")).lower()
    elif kitchen == True:
        os.system("cls")
        print (kitchen_art)
        scroll ("Well, you're back in the kitchen. Maybe there is something to eat. Maybe it's poisonous. Who knows.")
        choice=input (scroll(f"\nWhat would you like to do?\nGo {Fore.GREEN}\n     NORTH    \n{Style.RESET_ALL}{Fore.GREEN}WEST{Style.RESET_ALL}       {Fore.RED}EAST {Style.RESET_ALL}{Fore.RED}\n     SOUTH    {Style.RESET_ALL}     Or {Fore.GREEN} EAT{Style.RESET_ALL} the food.")).lower()
    if choice == "eat":
        scroll("Well it looks appetising enough....")
        eat_food()
    elif choice=="west":
        os.system("cls")
        scroll(f"You go {Fore.GREEN}west{Style.RESET_ALL} through the door...")
        time.sleep(3)
        outer_vault_room()
    elif choice== "north":
        os.system("cls")
        scroll(f"You travel {Fore.GREEN}north{Style.RESET_ALL} back towards the beginning.")
        time.sleep(3)
        sleeping_room()

#OUTER VAULT AREA
def outer():
    os.system("cls")
    print (outer_vault_art)
    scroll(f"\nYou stand in the outer vault, the {Fore.YELLOW}ring{Style.RESET_ALL} on your finger giving you a renewed level of strength, the main vault ahead of you.")

def outer_vault_room():
    os.system("cls")
    print (outer_vault_art)
    global outer_vault, player_health
    if not outer_vault:
        scroll("You enter a large stone room and see ahead of you a circular iron vault door that sits slightly ajar.\nThere are old shelving units that housed crates of gold that's long been taken; you see a large wooden desk in front of the vault door.\nA single ring sits on top of it, engraved with some arcane runes.\nYou also notice that this room is somehow cleaner than the rest of the dungeon; there's less dust, fewer cobwebs, and less of a bad scent. It's weird, but no weirder than anything else you've seen.")
        outer_vault = True
    else:
        os.system("cls")
        print (outer_vault_art)
        scroll("You return to the outer vault room. Nothing has changed. What will you do now?")
    
    while True:
        os.system("cls")
        print (outer_vault_art)
        choice = input (scroll(f"\nWhat would you like to do?\nGo {Fore.GREEN}\n     NORTH    \n{Style.RESET_ALL}{Fore.GREEN}WEST       EAST {Style.RESET_ALL}{Fore.RED}\n     SOUTH    {Style.RESET_ALL}     Or {Fore.GREEN} ENTER{Style.RESET_ALL} Vault     pick up{Fore.GREEN} RING{Style.RESET_ALL}")).lower()
        
        if choice == "north":
            os.system("cls")
            scroll(f"You head {Fore.GREEN}north{Style.RESET_ALL}.")
            time.sleep(3)
            jail_room()
            break
        elif choice == "east":
            os.system("cls")
            scroll(f"You go {Fore.GREEN}east{Style.RESET_ALL}.")
            time.sleep(3)
            kitchen_room()
            break
        elif choice == "west":
            os.system("cls")
            scroll(f"You go {Fore.GREEN}west{Style.RESET_ALL}.")
            time.sleep(3)
            storage_room()
            break
        elif choice == "enter":
            os.system("cls")
            scroll(f"You pull the door fully open and {Fore.GREEN}enter{Style.RESET_ALL} the vault.")
            time.sleep(3)
            vault_room()
            break
        elif choice == "ring":
            os.system("cls")
            print (outer_vault_art)
            scroll(f"Putting on the {Fore.GREEN}ring{Style.RESET_ALL}, you feel more energized, hardier, like the attacks of enemies would hurt you less, or at least, that they'd have to hurt you more.")
            time.sleep(3)
            player_health = 30
            outer()
            choice = input (scroll(f"\nWhat would you like to do?\nGo {Fore.GREEN}\n     NORTH    \n{Style.RESET_ALL}{Fore.GREEN}WEST       EAST {Style.RESET_ALL}{Fore.RED}\n     SOUTH    {Style.RESET_ALL}     Or {Fore.GREEN} ENTER{Style.RESET_ALL} Vault")).lower()
            if choice =="north".lower():
                os.system("cls")
                scroll (f"you head {Fore.GREEN}north{Style.RESET_ALL}")
                time.sleep(3)
                jail_room()
                break
            elif choice == "east".lower():
                os.system("cls")
                scroll (f"you go {Fore.GREEN}east{Style.RESET_ALL}")
                time.sleep(3)
                kitchen_room()
                break
            elif choice=="west".lower():
                os.system("cls")
                scroll(f"you go {Fore.GREEN}west{Style.RESET_ALL}")
                time.sleep(3)
                storage_room()
                break
            elif choice =="Enter".lower():
                os.system("cls")
                scroll(f"You pull the door fully open and {Fore.GREEN}enter{Style.RESET_ALL} the vault")
                time.sleep(3)
                vault_room()
                break
        else:
            scroll("Invalid choice. Please choose again.")

#VAULT AREA
def vault_room():
    os.system("cls")
    print(vault_art)
    global vault
    if not vault:
        scroll(f"This room is the most beautiful thing you have ever seen, the {Fore.YELLOW}map{Style.RESET_ALL} was right!\nThe long lost {Fore.YELLOW}treasure{Style.RESET_ALL} still remains!\nLooking around you see nothing but piles upon piles upon piles of {Fore.YELLOW}gold{Style.RESET_ALL}, floor to ceiling the cascading light as the everburn torches around the room reflect from the {Fore.YELLOW}coins{Style.RESET_ALL}.\nYou see {Fore.YELLOW}gems{Style.RESET_ALL}, magical artifacts from {Fore.YELLOW}weapons{Style.RESET_ALL} to {Fore.YELLOW}wands{Style.RESET_ALL}.\nYou see {Fore.YELLOW}art pieces{Style.RESET_ALL} that had been lost to time, your dreams have come true!\nYou are rich now! The wealthiest person in the lands.\nBut then you notice something else, something much, much scarier.\nIn the centre of the vault, beginning to move you see the {Fore.RED}rotted bones{Style.RESET_ALL}, of a {Fore.RED}dragon{Style.RESET_ALL}, slowly shifting, the eyes in the {Fore.RED}long dead skull{Style.RESET_ALL} of this dragon bursting to light with a sickly green spark.\nIt begins to stand. Ready to defend its hoard.")
        vault = True
        time.sleep(3)
    else:
        os.system("cls")
        print (outer_vault_art)
        scroll(f"You see the dragons' bones crumple to the ground lifeless once more, you stand victorious in what is now YOUR hoard of {Fore.YELLOW}treasure{Style.RESET_ALL}. You see two doors at the other end of the room, they must lead to freedom, as you approach you see that there is something wrong. The doors are locked, but there are no key holes. Instead, there is another riddle. \n")
        while True:
            os.system("cls")
            print (outer_vault_art)
            choice = input (scroll(f"\nWhat would you like to do?\nGo {Fore.RED}\n     NORTH    \n{Style.RESET_ALL}{Fore.RED}WEST       EAST {Style.RESET_ALL}{Fore.RED}\n     SOUTH    {Style.RESET_ALL}      {Fore.GREEN} SOLVE{Style.RESET_ALL} the puzzle     {Fore.GREEN}WAIT{Style.RESET_ALL}")).lower()
            if choice == "solve":
                global answer
                os.system("cls")
                print (outer_vault_art)
                answer = input("You measure my life in hours and I serve you by expiring.\nI'm quick when I'm thin and slow when I'm fat.\nThe wind is my enemy.")
                if answer == "candle":
                    os.system("cls")
                    good_ending()
                    return
                else:
                    os.system("cls")
                    bad_ending()
                return            
            elif choice == "wait":
                os.system("cls")
                print (outer_vault_art)
                scroll("You wait. So close to the end but now you want to rest. As you wait you watch the riddle fades.\nAs the riddle disappears you hear the vault lock engage.\nIt looks like you are the new gaurdian of the vault...")
                time.sleep(5)
                game_over()
                return
            else:
                scroll("That is not a choice. Choose again. ")
    while True:
         os.system("cls")
         print(vault_art)
         choice = input (scroll(f"\nWhat would you like to do?\nGo {Fore.RED}\n     NORTH    \n{Style.RESET_ALL}{Fore.RED}WEST       EAST {Style.RESET_ALL}{Fore.RED}\n     SOUTH    {Style.RESET_ALL}      {Fore.GREEN} FIGHT{Style.RESET_ALL}      {Fore.GREEN}RUN{Style.RESET_ALL}")).lower()
         if choice == "run":
            os.system("cls")
            print(vault_art)
            scroll ("You try to leave but with your back to the dragon you're a pretty easy target.\nYou don't feel him bite you in half.\nYou do feel the life leaving your body.")
            time.sleep(3)
            game_over()
            break
         elif choice == "fight":
            os.system("cls")
            print(vault_art)
            scroll ("You decided to fight!\n\n")
            rolling(vault_room)
            break

#DEATHS.............
def crushing_room():
    os.system("cls")
    scroll ("You pass through a corridor and find yourself in a small room.\nAs soon as you step in the ground began to raise, more quickly than you were able to react to and now you are trapped. \nTe ceiling above coming down to greet you as the floor rises. \nYou realise you are about to be crushed, in your final moments, you panic and scream in abject terror before it swiftly being cut short.")
    time.sleep(5)
    game_over()

def spike_pit():
    os.system ("cls")
    scroll ("As you enter the room the door shuts behind you, triggering a mechanical grinding as the floor slowly slides open.\nAs you try to cling on you realise there is no way to grip the smooth walls.\nYou fall to your death as you hit the floor in a pit full of spikes.\nEach one pucturing you until you slowely bleed out and die.")
    time.sleep(5)
    game_over()

def acid_pit():
    os.system ("cls")
    scroll ("As you pass down the corridor, your foot sinks into the ground as you realise you have stepped on to a pressure plate.nAs you realise this, the ground beneath you crumbles to dust, and you plummet, 30 feet into a pool of caustic green liquid.\nThe last thing you feel, is your flesh melting from your body within this pool of acid!")
    time.sleep(5)
    game_over()

def axe_blades():
    os.system("cls")
    scroll ("You leave the storage room and walk down a short corridor before entering another smaller room.\nIt is empty entirely but as you entered, you stepped on a trip wire.\nLooking up, the last thing you see is the giant axes swinging towards you, slicing you in half!")
    time.sleep(5)
    game_over()

def do_nothing():
    os.system ("cls")
    scroll ("You decide that the adventuring life is actually not for you,\nthis room is scary and dark and you don’t want to proceed further,\nbut you can't leave as the door behind you is locked,\nso you do what any sane person would do in this moment,\nyou sit down and begin to cry, You do this for a week straight before dying of starvation and dehydration.")
    time.sleep(5)
    game_over()

def eat_food():
    os.system ("cls")
    scroll ("You eat some of the food,\nThe flavour is so vile, that you immediately puke.\As you throw up , you slip in the puddle of vomit and crack your head open on the side of one of the ovens\nYou lie there bleeding out and in your final moments you think to yourself “How Embarrassing”")
    time.sleep(5)
    game_over()

def give_up():
    os.system ("cls")
    scroll ("You decide to just give up. As the skeletons rip in to you, the pain is excruciating.\nLuckily for you, you pass out quickly and your end comes whilst you aren't conscious.")
    time.sleep(5)
    game_over()


#ENDINGS..........
def good_ending():
    scroll (f"You speak your answer out loud, {answer}, the door to your right swings open.\nYou see two large bags behind the door, opening them, you realise them to be bags of holding, bags of extra dimensional space.\nYou spend the next several days emptying this vault of all of its treasure, shovelling it into the bags.\nThe room empty you take one final breath and walk into the tunnel, it takes you several hours, but you find your way out, back in the wild, Victorious.\nYou make your way back to town where you begin to spend your gold, you build yourself a magnificent keep, with stables and horses and servants, you gain a position of power within government and spend the rest of your life wealthy and famous!")
    time.sleep(5)
    os.system("cls")
    you_win()

def bad_ending():
    scroll (f"You speak your answer out loud, {answer}, and the door on the left springs open.\nyou see a light at the end of the tunnel, a glow, that of daylight, you pass through the door, as much of the treasure as you can carry in tow, and the door slams shut behind you...\nYou find yourself in a dark room, the only light coming from a solitary lit candle in the centre.\nYou look around there is no way out, the skeletons of past adventurers litter the ground here.\nIt dawns on you, you are trapped, the answer was candle and now you're going to die, alone, trapped in this room...\nThe Next week drives you to madness and when you finally expire you imagine yourself having got the answer correct.")
    time.sleep(5)
    os.system("cls")
    game_over()

def game_over():
    os.system("cls")
    print (lose)
    # pygame.mixer.init()
    # pygame.mixer.music.load("./audio/Death.mp3")
    # pygame.mixer.music.play()
    time.sleep(4)

def you_win():
    os.system("cls")
    print (win)
    # pygame.mixer.init()
    # pygame.mixer.music.load("./audio/Victory.mp3")
    # pygame.mixer.music.play()
    time.sleep(4)

vault_room()