#!/usr/bin/perl

use warnings;	# get warnings
use Digest::SHA qw (sha512256_base64);#Module to for allow 256 bit, 64 character SHA encryption
use Cwd;	#Current Working Directory

&menu();

sub menu
{

	system ('clear');		# Clears screen.. Below printf statement prints Team Name with logo
	printf "\033[1;33m
 _______  _        _______  _______    _______           _______  _        _       	       _.-''|''-._
(  ____ \\( \\      (  ___  )(       )  (  ____ \\|\\     /|(  ____ \\( \\      ( \\    	    .-'     |     `-.
| (    \\/| (      | (   ) || () () |  | (    \\/| )   ( || (    \\/| (      | (             .'\\       |       /`.
| |      | |      | (___) || || || |  | (_____ | (___) || (__    | |      | |           .'   \\      |      /   `. 
| |      | |      |  ___  || |(_)| |  (_____  )|  ___  ||  __)   | |      | |      	\\     \\     |     /     /   
| |      | |      | (   ) || |   | |        ) || (   ) || (      | |      | |            `\\    \\    |    /     /'
| (____/\\| (____/\\| )   ( || )   ( |  \/\\____) || )   ( || (_____\/\| (____\/\\\| (____\/\\         `\\  \\ \  |   /   /'
(_______/(_______/|/     \\||/     \\|  \\_______)|/     \\|(_______/(_______/(_______/	      `\\ \\  |  /  /'
									                    _.-`\\ \\ | / /'-._
 _______  _______  _______           _______ __________________                            {_____`\\\\|//'_____}
(  ____ \\(  ____ \\(  ____ \\|\\     /|(  ____ )\\__   __/\\__   __/|\\     /|	   	           '-'
| (    \\/| (    \\/| (    \\/| )   ( || (    )|   ) (      ) (   ( \\   / )    	
| (_____ | (__    | |      | |   | || (____)|   | |      | |    \\ (_) /               
(_____  )|  __)   | |      | |   | ||     __)   | |      | |     \\   /               
      ) || (      | |      | |   | || (\\ (      | |      | |      ) (                   
/\\____) || (____/\\| (____/\\| (___) || ) \\ \\_____) (___   | |      | |                   
\\_______)(_______\/(_______\/(_______)|\/   \\__/\\_______\/   )_(      \\_/		      
																					        																					     
	\033[0m\n";
	printf "\033[1;33m+------------------------------------------------+\033[0m\n";	# prints program information
	printf "\033[1;32m|------- Made by Jeremi Folta & Josh Cook -------|\033[0m\n";
	printf "\033[1;36m|-------          Version 1.8.1           -------|\033[0m\n";
	printf "\033[1;35m|-------        1 tool 3 programs         -------|\033[0m\n\n";
	printf "\033[1;34m|-------   Welcome to Clam Shell Security -------| \033[0m\n";
	printf "\033[1;39m|-------         Enter an option:         -------| \033[0m\n";
	printf "\033[1;33m+------------------------------------------------+\033[0m\n\n";
	printf "\033[1;36mPassword\033[0m";		# display options for user
	printf "\033[1;33m -- Generate a password\033[0m\n";
	printf "\033[1;36mFirewall\033[0m";
	printf "\033[1;33m -- Configure advanced firewall settings\033[0m\n";
	printf "\033[1;36mScan\033[0m";
	printf "\033[1;33m -- Scan file for viruses\033[0m\n";
	printf "\033[1;31mQuit\033[0m";
	printf "\033[1;33m -- Exit The Program\033[0m\n\n";
	################################################################# End menu
	
	print ("CSS> ");	#custom prompt string
	chomp ($_ = <STDIN>);	#gets input from user on the above options
	if($_=~/Q/i)	#if statement to close program
	{
		system("clear");	#clears screen
		exit;	#exit program
	}#end if
	
	while ()	#infinite while loop to initialize program
	{
		SWITCH:			#switch to handle user input and call the subroutine
		{			#switch uses $_ which is perl special scalar (variable) to store standard input from keyboard
		
			($_=~/PASSWORD/i) and do	#Subroutine to Run Password generator Program. =~/ / is for matching, i ignore case
			{
				&passGen();			# call passGen, to start password generator
				last;				#break. exit loop
			};#end $_=~/PASSWORD/i
			
			($_=~/FIREWALL/i) and do	#Subroutine to Run Firewall
			{
				&firewall();		#call firewall, to start firewall configuration
				last;			#break.. exit loop
			};#end $_=~/FIREWALL/i
			
			($_=~/SCAN/i) and do		#Subroutine to Run Virus Scanner 
			{
				&scan();		#call scan, to start virus scanner
				last;		#break... exit loop
			};#end $_=~/SCAN/i
			
			{
				print ("Error, $_ is not a valid option..\n"); 	#error check statment is $_ is not a call
				last;	#break.... exit loop
			};#end error check statement
			
		}#end switch
		
	print ("CSS> ");	#custom prompt. This line is used again outside of the switch. Prompt will be CSS> after stepping 							out of the switch
	$_ = (<STDIN>);		#gets user input for option, after stepping outside of the switch
	
	}#end loop	
}#end sub menu
############################################## Password Generator ##########################################
sub passGen
{
	system ("clear");
	$filename = 'ClamShell_Database';	#file name of Password database
	printf "\033[1;33m+------------------------------------------------+\033[0m\n";	#welcome header
	printf "\033[1;32m|-------    				  -------|\033[0m\n";
	printf "\033[1;36m|------- 	Welcome to the CSS        -------|\033[0m\n";
	printf "\033[1;35m|------- 	Password Generator        -------|\033[0m\n\n";
	printf "\033[1;34m|-------   				  -------| \033[0m\n";
	printf "\033[1;39m|-------          		          -------| \033[0m\n";
	printf "\033[1;33m+------------------------------------------------+\033[0m\n\n";
	
	while()		#infinite loop to start password generator
	{
		print"Please Enter the User Name for your login:\n";	#prompt for username
		print ("CSS> ");	#custom prompt
		chomp($Username = <STDIN>);		#get username from standard in and assigns value to $Username
		print"Your User Name is: $Username\n";	  #display $Username
		print"Is This Ok? [Enter 'y' to continue, or 'n' to re-enter]:\n";	#username conformation
		print ("CSS> ");	#custom prompt
		chomp($Choice=<STDIN>);		#get choice from standard in(user)
		&PassSub($Choice,$Username);	#Passes Choice and username to subroutine for username re-entry
		
		sub PassSub		#subroutine for username re-entry
		{
			
			$now = (`date`);	#date linux command assigned to $now
			@now = split / /,$now;	#splits $now on white space and assigns the values into an array
			if ($now[2] eq "")	#if statment, to check if day is one number and one space or two numbers
			{
				@now = ($now[1],$now[3],$now[6]);	# 2nd,4th, and 7th values from the system date assigned to @now
			}#end if statment for date
			
			else
			{
				@now = ($now[1],$now[2],$now[5]);	#2nd,3rd, and 6th values from the system date assigned to @now
			}#end else
			
			$date = join " ",@now;	#join values on whitespace, assigns the one value into $date 
			
			SWITCH:		#Switch for choice if user is satisfied with their username or not
			{
				($Choice=~ /Y/i) and do	#choice is y, i = ignore case
				{
					print"Enter your password encryption of choice:\n'Hex','ASCII','Hash':\n";	#password choices displayed
					print ("CSS> ");	#custom promp
					chomp($PassType=<STDIN>);	#gets $PassType from standard in, based on choices
					
					if ($PassType=~/Hex/i)	#if statement for Hexadecimal encryptiion choice
					{	
						@aryValues = ('0'..'9', 'A'..'F');	#the .. gets the range of '0' to '9' and 'A' to 'F' (hex) 																assigns those values to array @aryValues
						
						$rand_Hex = join '' , map $aryValues[rand @aryValues], 1..64;
			#the map function allows you to build a new list from another list while modifying the elements, simultaneously
			#the rand function randomizes the values in array @aryValues, assigns those values to scalar $rand_Hex 64 chars 			only
											
						if (-e $filename) #if filename exist
						{
							system("chattr -i ClamShell_Database");	#chattr -i command allows changes to be made to file 																		where passwords will be stored automatically (mutable)
						}
						else	#if file does not exist
						{
							@header=("\033[1;36m Welcome To The CSS Password Database\033[0m\n");	#header text for file
							unshift(@header,"\033[1;33m +------------------------------------+\033[0m\n"); 								#unshift adds to the bottom of the array @header (top of the header)
							
							push(@header,"\033[1;33m+------------------------------------+\033[0m\n");	# header 								#push adds to the top of the array @header (bottom of header) aka footer
							open(OUTFILE,">> ClamShell_Database") or die "$! in line $.\n";
							#open password database with filehandle OUTFILE. or die $! error checks if file cannot be 								opened. '$.' tells what line error is found
							print OUTFILE"@header";	#prints @header array to the OUFILE
							close OUTFILE;	#closes OUTFILE
						}#end else
						
						open(OUTFILE,">> ClamShell_Database") or die "$! in line $.\n";	#open ClamShell_Database to append
						
						system("chmod 000 ClamShell_Database");		#chmod 000 denies read, write, and execute permissions 																		for everyone. This prevents database to be accessed 																	without root.  
						system("chattr -i ClamShell_Database");	#chattr -i command allows changes to be made to file 																	where passwords will be stored automatically (mutable)
						
						print OUTFILE"$Username-->$rand_Hex";	#prints $Username, $rand_Hex to Clam_ShellDatabase file
						print OUTFILE"-->$date\n";		#prints $date to Clam_ShellDatabase
						system("chattr +i ClamShell_Database");	#chattr +i makes file imutable (unchangeable)
						print"Username is:";
						print"\033[1;33m $Username\033[0m\n";	#prints $Username
						print"Password is:";
						print"\033[1;36m $rand_Hex\033[0m\n\n";	#prints the random generated hex password
						print"Your credentials have been saved in a file named:";
						print"\033[1;32m 'ClamShell_Database'\033[0m\n\n";
						close OUTFILE;	#close Clam_ShellDatabase
						
						print "Would You like to Generate a new Password?\nEnter: 'y' if yes\nEnter 'n' if no\n\n";
						print ("CSS> ");		#custom prompt
						chomp($Choice=<STDIN>);		#gets $choice from standard in
						if($Choice=~/Y/i)		#if choice matches 'y' -i for ignore case
						{
							system("clear");	#clears screen
						}
						
						elsif($Choice=~/N/i)	#if $choice matches 'n' 
						{
							system("clear");	#clears screen
							&menu();	#calls menu, to return to main menu of CSS
						}
						
						else	#error checking statement
						{
							system("clear");	#clears screen
							&menu();	#calls menu, to return to main menu of CSS
						}
					}#end if PassType=~/Hex/i
					
					elsif ($PassType=~/ASCII/i)		#if $PassType matches ascii -i ignore case
					{
						@aryValues = ('0'..'9','A'..'F','!','@','#','$','%','&','*','?');	#array of specific ASCII values
						$rand_Ascii = join '' , map $aryValues[rand @aryValues], 1..64; 
						#the map function allows you to build a new list from another list while modifying the elements, 							simultaneously
						
						#the rand function randomizes the values in array @aryValues, assigns those values to scalar 							$rand_Ascii, 64 chars only
						
						if (-e $filename) #if filename exist
						{
							system("chattr -i ClamShell_Database");	#chattr -i makes file mutable.
						}
						else	#else statment to print header and footer to ClamShell_Database
						{
							@header=("\033[1;36m Welcome To The CSS Password Database\033[0m\n");
							unshift(@header,"\033[1;33m +------------------------------------+\033[0m\n");
							push(@header,"\033[1;33m+------------------------------------+\033[0m\n");
							open(OUTFILE,">> ClamShell_Database") or die "$! in line $.\n";	#open OUTFILE to append
							print OUTFILE"@header";		#print @header to OUTFILE
							close OUTFILE;	#close OUTFILE
							
						}
						open(OUTFILE,">> ClamShell_Database") or die "$! in line $.\n";		#open OUTFILE to append
						system("chmod 000 ClamShell_Database");		#change permissions to deny read, write, and execute
						system("chattr -i ClamShell_Database");		#chattr -i makes file mutable.
						print OUTFILE"$Username-->$rand_Ascii";		#print $Username, $rand_Ascii to OUTFILE
						print OUTFILE"-->$date\n";					#print $date to OUTFILE
						system("chattr +i ClamShell_Database");		#chattr +i makes file immutable
						print "\n\nUsername is:";
						print"\033[1;33m $Username\033[0m\n";		#prints $Username
						print"Password is:";
						print"\033[1;36m $rand_Ascii\033[0m\n\n";		#prints ascii generated password
						print"Your credentials have been saved in a file named:";
						print"\033[1;32m 'ClamShell_Database'\033[0m\n\n";
						close OUTFILE;		#close OUTFILE
						print "Would You like to Generate a new Password?\nEnter: 'y' if yes\nEnter 'n' if no\n\n";
						print ("CSS> ");
						chomp($Choice=<STDIN>);	#gets $choice from standard in
						if($Choice=~/Y/i)	#if $choice matches 'y' i ignore case
							{
								system("clear");	#system clear
							}
							
							elsif($Choice=~/N/i)	#if $choice matches 'n' i ignore case
							{
								system("clear");
								&menu();	#calls menu, to return to main menu of CSS
							}
							
							else	#error checking statement
							{
								system("clear");
								&menu();	#calls menu, to return to main menu of CSS
							}
					}#end if $PassType=~/ASCII/i
					
					elsif ($PassType=~/HASH/i)	#if $PassType matches 'hash' i ignore case
					{	
						$rand_Hash = sha512256_base64(rand);	#Generates a 512 bit encryption, truncates to be 256 bit, 64 																	characters long, then randomizes.  
				   			if (-e $filename) 	#if filename exists
							{
								system("chattr -i ClamShell_Database");		#chattr -i makes file ClamShell_Database mutable
							}
							
							else		#if filename does not exist
							{
								@header=("\033[1;36m Welcome To The CSS Password Database\033[0m\n");
								unshift(@header,"\033[1;33m +------------------------------------+\033[0m\n");
								push(@header,"\033[1;33m+------------------------------------+\033[0m\n");
								open(OUTFILE,">> ClamShell_Database") or die "$! in line $.\n";	#open OUFILE to append
								print OUTFILE"@header";	#prints @header array to OUTFILE
								close OUTFILE;	#close OUTFILE
							}#end else
														
				   		open(OUTFILE,">> ClamShell_Database") or die "$! in line $.\n";	#open ClamShell_Database to append 
				   		system("chmod 000 ClamShell_Database");	# chmod 000 changes permissions to deny read, write, and 																	execute to ClamShell_Database
				   		system("chattr -i ClamShell_Database");		#chattr -i makes file mutable
				   		%cred=($Username=>$rand_Hash);		#assigns $Username, $rand_Hash, assigns to %cred hash
				   											# => is fat comma binds key value pair 
				   		foreach my $Uniquename (sort keys %cred) 	#sorts %cred hash by keys
				   		{	
				   			print "\n\nUsername is:";
				   			print"\033[1;33m $Uniquename\033[0m\n";	#prints $Uniqename
							print"Password is:";
							print "\033[1;36m $cred{$Uniquename}\033[0m\n\n";	#prints hash generated password
						}
				  	   	print OUTFILE"$Username-->$rand_Hash";	#prints $Username, $rand_Hash to OUTFILE
				  	   	print OUTFILE"-->$date\n";		#prints $date to OUTFILE
				  	   	system("chattr +i ClamShell_Database");		#chattr +i makes file immutable
						print"Your credentials have been saved in a file named:";
						print"\033[1;32m 'ClamShell_Database'\033[0m\n\n";
						close OUTFILE;	#close OUTFILE
						print "Would You like to Generate a new Password?\nEnter: 'y' if yes\nEnter 'n' if no\n\n";
						print ("CSS> ");
						chomp($Choice=<STDIN>);	#gets $choice from standard in, if user wants to generate new password
						if($Choice=~/Y/i)		#if $choice matches 'y' i ignore case
						{
							system("clear");	#clears screen
						}
						
						elsif($Choice=~/N/i)	#if $choice matches 'n' i ignore case
						{
							system("clear");	#clears screen
							&menu();	#calls menu, to return to main menu of CSS
						}
						
						else	#else
						{
							system("clear");	#clears screen
							&menu();		#calls menu, to return to main menu of CSS
						}
					}#end $PassType=~/HASH/i
						
					else	#error checking statement
					{
						&PassSub();	#if Password choice is not recognized calls subroutine to prompt again
					}
						last;	#steps out of switch
				};#end if $Choice=~ /Y/i
		 
				($Choice=~/N/i) and do #prompt for username again if choice = 'N'
				{
					last;	#steps out of switch
				};
			}#end switch
		}#end passSub
	}#end loop
		
}#end passGen()

######################################### FIRE-WALL ###########################################
sub firewall
{
	my ($Choice,
		$IPaddy,
		@arystars);
	system("ufw enable");	#enables firewall as soon as program starts
	system("clear");	#clears screen
	@arystars=("*")x30;		#repeat operator
	
	while()		#infinite while loop to start program
	{
		#+-- menu --+
		printf "\033[1;33m=\033[0m" x 45; # 033[1;33m] prints in bold and yellow
		print "\n";
		printf "\033[1;33m=====\033[0m"; # yellow
		printf "\t\033[1;04;36mClam Shell Firewall Manager\033[0m\t"; #light blue text
		printf "\033[1;33m=====\033[0m\n"; # yellow
		printf "\033[1;33m========\033[0m"; # yellow
		print "    Select an Option";
		printf "\033[1;33m\t=============\033[0m\n"; # yellow
		printf "\033[1;33m=\033[0m" x 45; # 033[1;33m] prints in bold and yellow
		printf "\n\033[1;33m+------------------------------------------------+\033[0m\n";
		printf "\033[1;32mTurn Firewall ON: Enter 'ON'\n\033[0m";
		printf	"\033[1;31mTurn Firewall OFF: Enter 'OFF'\n\033[0m";
		printf	"\033[1;33mRestart The Firewall: Enter 'Restart'\n\033[0m";
		printf "\033[1;33m+------------------------------------------------+\033[0m\n";
		printf "\033[1;36mFirewall Options are:\n'SSH','PING','Mail','WEB'\n\033[0m";
		printf "\033[1;33m+------------------------------------------------+\033[0m\n";
		printf "\033[1;34mTo view Current ufw Cofiguration: Enter 'Config'\n\033[0m";
		printf "\033[1;33m+------------------------------------------------+\033[0m\n";
		printf "\033[1;35mTo view Network configuration: Enter 'ifconfig'\n\033[0m";
		printf "\033[1;33m+------------------------------------------------+\033[0m\n";
		printf "\033[1;31mTo quit: Enter 'q'\n\033[0m";
		printf "\033[1;33m+------------------------------------------------+\033[0m\n";
		print ("\nCSS> ");	#custom prompt
		chomp($Choice=<STDIN>);		#gets $choice from standard in. chomp removes trailing \n
		SWITCH:		#switch for firewall choices
		{
			($Choice=~/IFCONFIG/i)and do	#if $Choice matches 'ifconfig' i ignore case, Decision Block for NetWork 											Configuration
			{
				system ("ifconfig|head -8");	#Displays first 8 lines of network configuration
				print"\n\nTo continue: press 'enter'\nTo quit: enter 'q'\n";
				print ("CSS> ");	#custom prompt
				chomp($Choice=<STDIN>);		#gets $Choice from standard in
				
				if ($Choice eq"")	#if $Choice equals "" (nothing) return to firewall menu
					{
						system("clear");	#clears screen
					}
						
					elsif ($Choice=~/Q/i)	#if $Choice matches 'q' i ignore case, return to CSS Main Menu
					{
						system("clear");	#clears screen
						&menu();	#calls menu, returns to main CSS menu
					}
					last;	#steps out of switch
					
			};#end $Choice=~/IFCONFIG/i
			
			($Choice =~/SSH/i) and do	#if $Choice matches 'ssh' ,Decision Block for SSH Protocol Configuration
			{	
				print "Would you like to Block or Allow SSH?\nEnter 'A' for Allow or 'B' for Block:\n";
				print ("CSS> ");	#custom prompt
				chomp($Choice=<STDIN>);		#gets $Choice from standard in
				if ($Choice=~/A/i)	#ALLOW SSH
				{
					system("ufw allow OpenSSH");	#command in Linux, uncomplicated firewall allow OpenSSH
					print"SSH Network protocol has been allowed\n\nTo continue: press 'enter'\nTo quit: enter 'q'\n";
					print ("CSS> ");	#custom prompt
					chomp($Choice=<STDIN>);		#gets $Choice from standard in
					if ($Choice eq"")		#if $choice eq "" (nothing)
					{
						system("clear");	#clears screen
					}
					
					elsif ($Choice=~/Q/i)	#if $Choice matches 'q' i ignore case 
					{
						system("clear");	#clears screen
						&menu();		#calls menu, to return to CSS menu
					}
				}#end if $Choice=~/A/i
				
				elsif($Choice=~/B/i)	#BLOCK SSH
				{
					system("ufw deny OpenSSH");		#command in Linux, uncomplicated firewall deny OpenSSh
					print"SSH Network protocol has been blocked\n\nTo continue: press 'enter'\nTo quit: enter 'q'\n";
					print ("CSS> ");	#custom prompt
					chomp($Choice=<STDIN>);		#gets $Choice from standard in. chomp removes trailing newline '\n'
					if ($Choice eq"")	#if $Choice equals ""
					{
						system("clear");	#clears screen
					}
					
					elsif ($Choice=~/Q/i)	#if $Choice matches 'q' i ignore case
					{
						system("clear");	#clears screen
						&menu();		#calls menu, to return to main menu of CSS
					}
					
				}#end elsif $Choice=~/B/i 
				last;	#break, exit loop
				
			};#end $Choice =~/SSH/i
			
			($Choice=~/PING/i) and do		#if $Choice matches 'ping' i ignore case
			{
				print "Would you like to Block or Allow PING (ICMP) protocol\nEnter 'A' for Allow or 'B' for Block:\n";
				print ("CSS> ");	#custom prompt
				chomp($Choice=<STDIN>);		#gets $Choice from standard in, chomp removes trialing newline
				
				if ($Choice=~/A/i)	#if $Choice matches 'a' i ignore case, ALLOW PING
				{
					system("echo '0' > /proc/sys/net/ipv4/icmp_echo_ignore_all");	#system command in Linux to allow PING
					system("ufw allow 443/tcp comment 'PING IS ALLOWED'");	#reports block to config			
					print"PING protocol has been successfully Allowed\n\nTo continue: press 'enter'\nTo quit: enter 'q'\n";
					print ("CSS> ");	#custom prompt
					chomp($Choice=<STDIN>);		#gets $Choice from standard in, chomp removes trailing \n
					
					if ($Choice eq"")		#if $Choice equals ""
					{
						system("clear");	#system clear
					}
						
					elsif ($Choice=~/Q/i)	#if $Choice matches 'q' i ignore case
					{
						system("clear");	#system clear
						&menu();		#calls menu, to return to main menu of CSS
					}
				}#end $Choice=~/A/i
				
				elsif ($Choice=~/B/i)	#BLOCK PING
				{
					system("echo '1' > /proc/sys/net/ipv4/icmp_echo_ignore_all");	#system command in Linux to BLOCK PING
					system("ufw deny 443/tcp comment 'PING IS BLOCKED'");	#reports block to config			
					print ("The PING protocol has been succesfully denied\n\nTo continue: press 'enter'\nTo quit: enter 'q'\n");
					print ("CSS> ");
					chomp($Choice=<STDIN>);
					
					if ($Choice eq "")
					{
						system("clear");
					}
						
					elsif ($Choice=~/Q/i)
					{
						system("clear");
						&menu();
					}
				}#end elsif $Choice=~/B/i
				
				last;#break, step out of switch
					
			};#end $Choice=~/PING/i
			($Choice=~/MAIL/i)and do	#Decision Block for Mail Protocol configuration
			{
				print "Would you like to Block or Allow Simple Mail Transfer Protocol?\nEnter 'B' for Block or 'A' for Allow\n";
				print ("CSS> ");	#custom prompt
				chomp($Choice=<STDIN>);		#gets $Choice from standard in
				if ($Choice=~/A/i)	#ALLOW SMTP
				{
					system("ufw allow smtp");
					print "Simple Mail Transfer Protocol has been allowed\n\nTo continue: press 'enter'\nTo quit: enter 'q'\n";
					print ("CSS> ");
					chomp($Choice=<STDIN>);
					if ($Choice eq"")
					{
						system("clear");
					}	
					elsif ($Choice=~/Q/i)
					{
						system("clear");
						&menu();
					}
				}#end $Choice=~/A/i
				
				elsif ($Choice=~/B/i)	#BLOCK SMTP
				{
					system("ufw deny smtp");
					print "Simple Mail Transfer Protocol has been blocked\n\nTo continue: press 'enter'\nTo quit: enter 'q'\n";
					print ("CSS> ");
					chomp($Choice=<STDIN>);
					if ($Choice eq "")
					{
						system("clear");
					}	
					elsif ($Choice=~/Q/i)
					{
						system("clear");
						&menu();
					}
				}
				last;#break, step out of switch
				
			};#end $Choice=~/MAIL/i
				
			($Choice=~/WEB/i)and do		#Decision Block for Web Server Access Configuration
			{
				print "Would you like to Block or Allow Apache Web Server Access?\nEnter 'B'for Block or 'A' for Allow\n";
				print ("CSS> ");
				chomp($Choice=<STDIN>);
				if ($Choice=~/A/i)		#ALLOW APACHE
				{
					system("ufw allow Apache comment 'APACHE!'");
					print "Web Server Access has been allowed\n\nTo continue: press 'enter'\nTo quit: enter 'q'\n";
					print ("CSS> ");
					chomp($Choice=<STDIN>);
					if ($Choice eq"")
					{
						system("clear");
					}	
					elsif ($Choice=~/Q/i)
					{
						system("clear");
						&menu();
					}
				}#end $Choice=~/A/i
				elsif($Choice=~/B/i)	#BLOCK APACHE
				{
					system("ufw deny Apache comment 'APACHE!'");
					print "Apache Server Access has been blocked\n\nTo continue: press 'enter'\nTo quit: enter 'q'\n";
					print ("CSS> ");
					chomp($Choice=<STDIN>);
					if ($Choice eq"")
					{
						sleep 2;
						system("clear");
					}	
					elsif ($Choice=~/Q/i)
					{
						system("clear");
						&menu();
					}
				}#end $Choice=~/B/i
				
				last;#break, step out of switch
					
			};#end $Choice=~/WEB/i
			
			($Choice=~/CONFIG/i)and do		#Decision Block to show ufw configuration table
			{
				system ("ufw status verbose");
				print"\n\nTo continue: press 'enter'\nTo quit: enter 'q'\n";
				print ("CSS> ");
				chomp($Choice=<STDIN>);
				if ($Choice eq"")
					{
						system("clear");
					}	
					elsif ($Choice=~/Q/i)
					{
						system("clear");
						&menu;
					}
				last;
			};
			($Choice=~/ON/i)and do#Decision Block to turn ON firewall
			{
				system("ufw enable");
				print"\n\nTo continue: press 'enter'\nTo quit: enter 'q'\n";
				print ("CSS> ");
				chomp($Choice=<STDIN>);
				if ($Choice eq"")
					{
						system("clear");
					}	
					elsif ($Choice=~/Q/i)
					{
						system("clear");
						&menu;
					}
				last;
			};
			($Choice=~/OFF/i)and do#Decision Block to turn OFF firewall
			{
				system("ufw disable");
				print"\n\nTo continue: press 'enter'\nTo quit: enter 'q'\n";
				print ("CSS> ");
				chomp($Choice=<STDIN>);
				if ($Choice eq"")
					{
						system("clear");
					}	
					elsif ($Choice=~/Q/i)
					{
						system("clear");
						&menu;
					}
				last;
			};
			($Choice=~/RESTART/i)and do##Decision Block to reset ufw configuration table
			{
				system("ufw reset");#resets ufw configuration and backs up previous configuration
				system("ufw enable");
				print"\n\nTo continue: press 'enter'\nTo quit: enter 'q'\n";
				print ("CSS> ");
				chomp($Choice=<STDIN>);
				if ($Choice eq"")
					{
						system("clear");
					}	
					elsif ($Choice=~/Q/i)
					{
						system("clear");
						&menu;
					}
				last;
			};
			($Choice=~/Q/i)and do#Decision Block to Return to CSS menu
			{
				system("clear");
				&menu;
				last;
			};
		}
	}
	
}#end firewall

########################################## VIRUS SCANNER #################################################
sub scan	
{
	system ('clear');
	& startScan();	#Calls subroutine to start program
	sub startScan
	{
		printf "\033[1;33m=\033[0m" x 45; # 033[1;33m] prints in bold and yellow
		print "\n";

		printf "\033[1;33m=====\033[0m"; # yellow
		printf "\t\033[1;36mWelcome To Clam Shell Scanner\033[0m\t"; #light blue text
		printf "\033[1;33m=====\033[0m\n"; # yellow

		printf "\033[1;33m========\033[0m"; # yellow
		print "  Press Enter to Start";
		printf "\033[1;33m\t=============\033[0m\n"; # yellow
		printf "\033[1;33m=\033[0m" x 45; # 033[1;33m] prints in bold and yellow
		$_=(<STDIN>);	# Special Scalar used by STDIN to get user input from keyboard
		if ($_=~'')		# This line is to signal a start/run sequence to run the Virus Scanner tool
		{
			&getHash();	# Calls getHash subroutine
		}
	}
	&getHash();	# Exception, Used for error checking. To prevent error

	sub getHash	#This subroutine gets the checksum SHA1 hash from the contents of a file.
	{
	
		print ("Enter directory of file to scan:\n");
		print ("CSS> ");
		chomp($dir=<STDIN>);		# Gets directory from users keyboard.
		if (-d $dir)	# Checks if $dir is a directory
		{
			chdir ($dir);	# if $dir is a directory, changes to that directory
		}
		else	# if $dir is not a directory
		{
			print ("$dir is not a directory..\n");
			&getHash();		# if $dir is not a directory, returns to getHash, for prompt for directory.
		}
	
		system ('ls -p | grep -v /');	#ls -p list all files in current directory with / at the end of all directories. grep -v inverts the match, greps all files without / , thus listing only files that can be scanned, not directories.
		print ("Is this the correct directory: ");
		print ("\t [y] \t[n]\n");	#ask user if this is the correct directory.
		print ("CSS> ");
		chomp ($option = <STDIN>);
	
	
			SWITCH:
			{
				($option=~/n/i) and do		# if $option is 'n' or 'N' call getHash() to prompt user for new directory
				{
					&getHash();
					last;
				};
		
	
				($option=~/y/i) and do 		# if $option is 'y' or 'Y' system clears screen and continues on
				{
					system ('clear');
					last;
				};
		
		
				{
					print("Error, invalid option\n");	# error check block statement, if none of the options are chosen
					&scanAgain();						# call scanAgain()
					last;
				}
		
			}	#End switch
	
	
		
		system ('ls -p | grep -v /');	#ls -p list all files in current directory with / at the end of all directories. grep -v inverts the match, greps all files without / , thus listing only files that can be scanned, not directories.
		print "Enter file you wish to scan:\n";
		print ("CSS> ");
		my $fileToScan = (<STDIN>);		#asks user for which file they wish to scan
		chomp $fileToScan;	#chomps (removes) trailing /n from user input
	
		$file = $fileToScan;	# the contents of $fileToScan also gets assigned to $file, this is because later in the code $fileToScan will be modified, and we will still need to know the original contents of $fileToScan later in the code
	
		if (-e $fileToScan)	# checks to see if $fileToScan exists
		{
			print ("Scanning File...\n\n");	# if $fileToScan file DOES exist
			sleep 1;						# sleep/wait 1 second (for dramatic effect)
		}
		else
		{
			print ("File Not Found..\n");	# if $fileToScan file DOES NOT exist
			&getHash();						# call getHash()
		}

	
		open ($fh, $fileToScan);
		binmode ($fh);	#Arranges for FILEHANDLE to be read or written in "binary" or "text" mode on systems where the run-time libraries distinguish between binary and text files.

		$checksum = Digest::SHA->new->addfile($fh)->hexdigest;		#This grabs scalar $checksum and calculates its checksum, using SHA cryptographic hash function.. "->hexdigest" converts the base64 hash to hex, so it can be read by us.

		while (length($checksum) % 4) 	#This is padding. while the length of a Base64-encoded digest is not a multiple of 4, append "+" characters to the end of the digest until it is.
		{
			$checksum .= '+';	# Using the "+" character as padding
		}
		print "SHA1 checksum: ";
		printf "\033[1;29m$checksum\033[0m\n"; #Prints the checksum hash of the file (in bold)
		close $fh;	#close filehandle
	
		&scanFile(\$checksum, $file);	#calls scanFile passing ($checksum, $file) to the next part
	}#end checkHash()

	sub scanFile	#This subroutine checks and compares the __DATA__ data base to the checksum of the file that was scanned
	{
		#my $knownViruses = "/root/Project/VirusDataBase.txt";	#File with known viruses based on checksum SHA1 hashes
		#open (VDB, $knownViruses) || die "File does not exist $!";
	
		# The above commented code is used if you wish to use your own database to check for viruses, instead of the one built into the code
	
		my @virusDataBase=<DATA>;#Assigns the virus data base to an array (<DATA> can be found at the end of code in __DATA__)
		$infected = 0;		# $infected represents how many viruses are within the scanned file, initially set to 0
	
		foreach(@virusDataBase)	#foreach line in the array @virusDataBase
		{
			if(grep /$checksum/, @virusDataBase) #attempt to match $checksum (which holds the checksum of the file) with the virus database array @virusDataBase
			{
				$infected++;	#if there is a mactch within the database, increment $infected by 1
			}
		
		}
			if ($infected>1)
			{
				print "$file is a ";					#if $infected is greater than 1, file is is a VIRUS,
				printf "\033[1;41mVIRUS!!\033[0m\n\n";	# prints in red color white background
			}
				else
			{
				print "$file is ";						#else file is CLEAN,
				printf "\033[1;32mCLEAN!!\033[0m\n\n";	# prints in green color bold
			}
	
		&scanAgain();	#calls subroutine scanAgain
	}	

	sub scanAgain		#This subroutine asks user if they want to scan another file
	{
		print ("Do you wish to scan another file? \n");
		print ("\t [y] \t[n]\n");
		print ("CSS> ");
		chomp ($option = <STDIN>);


		SWITCH:
		{
			($option=~/y/i) and do		#if $option = 'y' or 'Y'
			{
				&getHash();				#call getHash()
				last;
			};
		
	
			($option=~/n/i) and do 		#if $option = 'n' or 'N' return to CSS main menu
			{
				&menu();		#calls subroutine to return to main menu of CSS
				last;
			};
		
		
			{
				print("Error, invalid option\n");	#Error checking <STDIN>, if $option = an invalid option,
				&scanAgain();						# call scanAgain()
				last;
			}
		
		}	#End switch
	}	#End scanAgain()
}#end scan

	#Below is the data that is inside the @knownViruses
	# __DATA__ is used for data base of known viruses. This data could easily be inside a seperate file. The use of __DATA__ is to be able to run the program without having to download a seperate database and store on your computer, this also makes it easier and user friendly, instead of having to use a file handle and making sure file is in correct location. Becuase of ___DATA__ we can run the program on a seperate computer without the hassel of changing any code to point to the database file.

__DATA__
cf8bd9dfddff007f75adf4c2be48005cea317c72
cf8bd9dfddff007f75adf4c2be48005cea317c62
7e3bc5f8b9a36c3b157ae55e3b1393a32bb8019e
7a9318b1774733d68a185b55548421e215bfce44
6f6cc3352a5378d2fb35cd4162fd288055e1087c
c875243df43d7a0baababf7488df884acffae2f9
			

	
