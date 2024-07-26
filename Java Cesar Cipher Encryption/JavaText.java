import java.util.Scanner;

public class JavaText
{
    public static void main(String[] args)
    {
        Scanner scan= new Scanner(System.in);
        System.out.print("Enter Message: ");
        String message = scan.nextLine();
        System.out.print("Enter Code[1-26]: ");
        int key = scan.nextInt();
        System.out.print("1] Encrypt \n2] Decrypt \nChoice: ");
        int ch = scan.nextInt();
        scan.close();
        Crypt ed= new Crypt();
        if (ch==1)
        System.out.println("Your Code: "+ed.encrypt(message,key));
        else if (ch==2)
        System.out.println("Your Message: "+ed.decrypt(message,key));
        else
        System.out.print("Wrong choice");
    }
}

class Crypt
{
    String Cap="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    String Num=" 0123456789_-=+/*";
    String LETTER=Cap+Num+Cap.toLowerCase();
    int end=LETTER.length();

    String encrypt(String message, int key)
    {
        String encrypted = "";
        char chars;
        int num,i;
        for (i=0;i<message.length();i++)
        {
            chars = message.charAt(i);
            if (LETTER.contains(chars+""))
            {
                num = LETTER.indexOf(chars);
                num += key;
                if (num>end-1)
                {
                    num-=end;
                    encrypted +=  '?';
                }
                encrypted +=  LETTER.charAt(num);
            }
        }
        return encrypted;
    }

    String decrypt(String message, int key)
    {
        String decrypted = "";
        char chars;
        int num=0,i,cc=0;
        for (i=0;i<message.length();i++)
        {
            chars = message.charAt(i);
            if (chars=='?')
            {
                cc=1;
                continue;
            }
            if (LETTER.contains(chars+""))
            {
                num = LETTER.indexOf(chars);
                num -= key;
                if (cc==1)
                {
                    num=end+num;
                    cc=0;
                }
                decrypted +=  LETTER.charAt(num);
            }
        }
        return decrypted;
    }
}