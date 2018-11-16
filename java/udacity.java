public class udacity {

public static void main(String[] args) {

boolean condition = true;
// a boolean

double div = 9.7 / 2;
// a division fraction

int num = 9;
// a full number

double frc = 99.357;
// a fraction

int apfrc = (int) frc;
// a full number fraction

String str = "*@*";
// a word

String xstr = "crash";
// another word

char chr = 'a';
// just one letter and only one letter

System.out.println(num);
System.out.println(str);
System.out.println(condition);
System.out.println(str);
System.out.println(div);
System.out.println(str);
System.out.println(frc);
System.out.println(str);
System.out.println(xstr);
System.out.println(str);
System.out.println(chr);
System.out.println(str);
System.out.println(apfrc);
System.out.println(str);

int strconfig = str.length();
System.out.println(strconfig);

System.out.println(str);
System.out.println(strconfig * frc);
System.out.println(str);
System.out.println(xstr);
System.out.println(str);

xstr = xstr.toUpperCase();

System.out.println(xstr);
System.out.println(str);
System.out.println(num + frc);
System.out.println(str);

num = num + 3;

System.out.println(num);
System.out.println(str);

String x_str = "xstr and str = " + xstr + str;
System.out.println(x_str);

}
}