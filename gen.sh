# Getting code and cutting
echo
echo "<<<<<( YOUR INVITE CODE )>>>>>" | lolcat -a -d 7
echo
curl -s -XPOST https://www.hackthebox.eu/api/invite/generate | sed -e 's/{"success":1,"data":{"code":"//g'|sed -e 's/","format":"encoded"},"0":200}//g' | base64 -d | lolcat -a -d 50
echo
echo
echo "<<<( THANKYOU FOR USING )>>>" | lolcat -a -d 5
echo
echo "I hope you liked it Follow  [ J O P R A V E E N ] in GITHUB For More COOL stuffs :D " | lolcat -a -d 120
