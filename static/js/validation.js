function validation()
{
	
	if(alpha())
	{	
				return true;								
	}
	
	if(alphabetic())
	{
			return true;								
	}
	
	if(num())
	{
						return true;								
	}	
	
	if(pass_validation())
	{
		return true;								
		
	}
	
	if(passid_validation())
	{
		return true;								
	}
	if(validateEmail())
	{
		
		return true;
	}
	
	
	return false;

}

function alpha()
{

f = document.register.name;
fl = f.value.length;

var alphaExpe = /^[a-zA-Z]+$/;

	if(f.value.match(alphaExpe)) 
	{
		f.style.color = "black";			
		return true; 
		
		
	}
	else if(fl == "")
	{
	f.value = "Could not be Empty";
	f.style.color = "red";	
	
	return false; 		
	}
	else
	{
		 
	f.value = "Only Letter are aceepted";
	f.style.color = "red";	
	
	return false; 
	
	}
	
}



function alphabetic()
{

l = document.signin.lname;
len = l.value.length;	
var alphaExp = /^[a-zA-Z]+$/;


		if(l.value.match(alphaExp)) 
		{ 
			l.style.color = "black";	
			return true; 
			
		}
		else if(len == 0)
		{
			
			l.value = "Could not be Empty";
			l.style.color = "red";	
	
			return false; 
			
		}
		else
		{
		
		 
			l.value = "Only Letter are aceepted";
			l.style.color = "red";	
	
			return false; 
			
		}
}


function num()
{

 c = document.signin.contact;
 
 cl = c.value.length;
 
var nExp = /^[0-9]+$/;


		if(c.value.match(nExp)) 
		{ 
	
			c.style.color = "black";
			return true; 
		
		} 
		else if(cl == 0) 
		{
			c.value = "Could Not be Empty";	
			c.style.color = "red";	
	
			return false; 		
		}

		else
		{
			c.value = "Only Numbers are accepted";	
			c.style.color = "red";	
	
			return false; 
			
		}


}


function validateEmail()
{
var uemail = document.signin.email;
var el = uemail.value.length;
var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;

		if(uemail.value.match(mailformat))
		{
			uemail.style.color = "black";		
			return true;
		}
		else if(el == 0)
		{
			uemail.value = "Could Not be Empty";	
			uemail.style.color = "red";		

	
				return false;
			
		}
		else
		{
			uemail.value = "Invalid Email id";	
			uemail.style.color = "red";			

	
				return false;
		}
}


function pass_validation()
{
	
p = document.register.password;
pl = p.value.length;

		if(pl == 0)
		{		
				alert("Please Enter Password...");		
				
				p.style.color = "red";	
	
				return false;
		}
		else
		{
			p.style.color = "black";	
			return true;
		}
	
}

function passid_validation()
{
	
p = document.register.password;
cp = document.register.repassword;

cl = cp.value.length;
		
		if(cl == 0)
		{
			alert("Please Enter Confirm Password...");
			cp.style.color = "red";	
	
			return false;
		}
		else if(p.value.match(cp.value))
		{
			cp.style.color = "black";	
			return true;
		}
		else
		{

		cp.style.color = "red";	
		alert("Sorry Password Not match...");
		return false;
		}

}


function validateEmail2()
{
var uemail = document.login.Email_id;

var el = uemail.value.length;

var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;

		if(el == 0)
		{
			uemail.value = "Could Not be Empty";	
			uemail.style.color = "red";		
			document.login.Email_id.focus();
				return false;
			
		}
		else if(uemail.value.match(mailformat))
		{
			uemail.style.color = "black";		
			return true;
		}
		else
		{		
			uemail.value = "Invalid Email id";	
			uemail.style.color = "red";		
			document.login.Email_id.focus();
				return false;
		}
}
