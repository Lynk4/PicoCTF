# vault-door-1

---

AUTHOR: MARK E. HAASE

Description
This vault uses some complicated arrays! I hope you can make sense of it, special 
agent. The source code for this vault is here: VaultDoor1.java




---


**VaultDoor1.java**
```java
import java.util.*;

class VaultDoor1 {
    public static void main(String args[]) {
        VaultDoor1 vaultDoor = new VaultDoor1();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
	String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
	}
    }

    // I came up with a more secure way to check the password without putting
    // the password itself in the source code. I think this is going to be
    // UNHACKABLE!! I hope Dr. Evil agrees...
    //
    // -Minion #8728
    public boolean checkPassword(String password) {
        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '9' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '5' &&
               password.charAt(30) == '2' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == '0' &&
               password.charAt(26) == '7' &&
               password.charAt(31) == 'e';
    }
}

```

---

here we can calculate our flag based on the positions..

It will be a hardwork...

let's make a script for that....

---

**vaultsolution.java**
```java
public class vaultsolution {

	public static void main(String[] args ) {
		char[] password = new char[32];
		password[0]  = 'd';
		password[29] = '9';
		password[4]  = 'r';
		password[2]  = '5';
		password[23] = 'r';
		password[3]  = 'c';
		password[17] = '4';
		password[1]  = '3';
		password[7]  = 'b';
		password[10] = '_';
		password[5]  = '4';
		password[9]  = '3';
		password[11] = 't';
		password[15] = 'c';
		password[8]  = 'l';
		password[12] = 'H';
		password[20] = 'c';
		password[14] = '_';
		password[6]  = 'm';
		password[24] = '5';
		password[18] = 'r';
		password[13] = '3';
		password[19] = '4';
		password[21] = 'T';
		password[16] = 'H';
		password[27] = '5';
		password[30] = '2';
		password[25] = '_';
		password[22] = '3';
		password[28] = '0';
		password[26] = '7';
		password[31] = 'e';
		System.out.println(password);

	}
}
```

---





