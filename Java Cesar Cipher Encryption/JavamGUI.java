import java.awt.*;
import java.awt.datatransfer.*;
import javax.swing.*;
import java.awt.event.*;

public class JavamGUI
{
    public static void main(String[] args)
    {
        GUI sw = new GUI();
        sw.startGUI();
        System.out.println("Prog Over");
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

class GUI extends JFrame implements ActionListener
{
    JFrame frame;
    JTextField messagetext, keytext, pmessagetest;
    JLabel key, message;
    JButton next;
    JPanel inputPanel ,bottomPanel;
    JRadioButton Enc,Dnc;

    
    static void clip(String text)
    {
        StringSelection selection = new StringSelection(text);
        Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
        clipboard.setContents(selection, selection);
    }

    void startGUI()
    {
        frame = new JFrame("Crytography Manager");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 150);
        frame.setLayout(new BorderLayout());
        
        inputPanel = new JPanel();
        inputPanel.setLayout(new GridLayout(3,2));

        message = new JLabel("Enter Message:");
        messagetext = new JTextField(0);
        key = new JLabel("Enter Key:");
        keytext = new JTextField(10);
        
        inputPanel.add(message);
        inputPanel.add(messagetext);
        inputPanel.add(new JLabel());
        inputPanel.add(key);
        inputPanel.add(keytext);
        inputPanel.add(new JLabel());
        
        Enc=new JRadioButton("Encrypt");
        inputPanel.add(Enc);

        Dnc=new JRadioButton("Decrypt");
        inputPanel.add(Dnc);

        ButtonGroup G = new ButtonGroup();
        G.add(Enc);
        G.add(Dnc);
        
        pmessagetest = new JTextField(25);
        pmessagetest.setEditable(false);
        inputPanel.add(pmessagetest);
        
        
        bottomPanel = new JPanel(new BorderLayout());
        frame.add(bottomPanel, BorderLayout.SOUTH);
        frame.add(inputPanel, BorderLayout.NORTH);
        
        
        next = new JButton("Procced");
        bottomPanel.add(next);
        next.addActionListener(this);
        frame.setVisible(true);
    }

    public void actionPerformed(ActionEvent e)
    {
        Crypt ed= new Crypt();
        String message=messagetext.getText();
        int key=Integer.parseInt(keytext.getText());
        String result="";

        if(Enc.isSelected())
        {
            result = ed.encrypt(message, key);
        }
        else if(Dnc.isSelected())
        {
            result = ed.decrypt(message, key);
        }
        else
        {
            JOptionPane.showMessageDialog(this, "Enter Choice");
        }

        clip(result);
        pmessagetest.setText(result);
    }
}
