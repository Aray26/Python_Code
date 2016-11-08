
Stack Overflow
Questions
 
Jobs
 
Tags
 
Users
 
Badges
 
Ask Question
Find Pythagorean triplet for which a + b + c = 1000


up vote
20
down vote
favorite
4
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

Source: http://projecteuler.net/index.php?section=problems&id=9

I tried but didn't know where my code went wrong. Here's my code in C:

#include <math.h>
#include <stdio.h>
#include <conio.h>


void main()
{
    int a=0, b=0, c=0;
    int i;
    for (a = 0; a<=1000; a++)
    {
        for (b = 0; b<=1000; b++)
        {
            for (c = 0; c<=1000; c++)
            {
                if ((a^(2) + b^(2) == c^(2)) && ((a+b+c) ==1000)))
                    printf("a=%d, b=%d, c=%d",a,b,c);
            }
        }
    }
getch();    
}
c operators pythagorean
shareedit
edited May 12 '15 at 8:38

Stijn
10.6k74689
asked May 12 '10 at 10:22

Rahul
1921414
3	 	
+1 just for the short snippet demonstrating the problem. – sharptooth May 12 '10 at 10:28
3	 	
Needs homework tag though ? – Paul R May 12 '10 at 10:29
14	 	
Do Project Euler questions need homework tags? – sharptooth May 12 '10 at 10:32
1	 	
don't use pow, it will cast your results to floating point and equality is unlikely to work as expected! – fortran May 12 '10 at 10:41
7	 	
I recognised the problem straightaway - maybe we could have a ProjectEuler tag, indicating that the question isn't homework per se but an exercise from that problem set; and of course there should always be code posted for the attempt that isn't working as expected, to prevent 'plz send me teh codez' questions. – Eight-Bit Guru May 12 '10 at 10:46 
show 3 more comments
14 Answers
active oldest votes
up vote
21
down vote
accepted
#include <math.h>
#include <stdio.h>

int main()
{
    const int sum = 1000;
    int a;
    for (a = 1; a <= sum/3; a++)
    {
        int b;
        for (b = a + 1; b <= sum/2; b++)
        {
            int c = sum - a - b;
            if ( a*a + b*b == c*c )
               printf("a=%d, b=%d, c=%d\n",a,b,c);
        }
    }
    return 0;
}
explanation:

b = a;
if a, b (a <= b)) and c are the Pythagorean triplet, 
then b, a (b >= a) and c - also the solution, so we can search only one case
c = 1000 - a -b; it's one of the conditions of the problem (don't need to scan all possible 'c': just calculate it)
shareedit
edited Aug 5 '14 at 8:23
answered May 12 '10 at 12:32

Oleg Razgulyaev
2,61721627
  	 	
Dude can you explain me the logic: a=1 Ok; But b=a & c=1000-a-b ? Can you please elaborate. Thanks – Rahul May 13 '10 at 5:01
  	 	
@Rahul: I've added few lines of explanation – Oleg Razgulyaev May 13 '10 at 9:09
  	 	
@ oraz: Thanks dude. I got it – Rahul May 14 '10 at 4:28
2	 	
If a < b and b < c, a can't be greater/equals than 1000/3 and b can't be greater/equals than 1000/2. And since a, b, c aren't used outside their loops, just declare them in the for-head. – user unknown May 18 '10 at 6:18 
1	 	
"for (b = a; b<=1000; b++)" - part of the problem description is that a < b < c so b cannot be equal to a. Make that b = a+1 – Wallacoloo May 22 '10 at 5:52 
show 2 more comments

up vote
26
down vote
I'm afraid ^ doesn't do what you think it does in C. Your best bet is to use a*a for integer squares.

shareedit
answered May 12 '10 at 10:26

Paul Stephenson
28.7k73443
  	 	
Edited dude. Thanks. – Rahul May 12 '10 at 10:33
  	 	
And with automatic truncation to integers, I've even seen use use of ^ to 'square' floating point values. – Pete Kirkham May 13 '10 at 22:18
add a comment
up vote
15
down vote
Here's a solution using Euclid's formula (link).

Let's do some math: In general, every solution will have the form

a=k(x²-y²)
b=2kxy
c=k(x²+y²)
where k, x and y are positive integers, y < x and gcd(x,y)=1 (We will ignore this condition, which will lead to additional solutions. Those can be discarded afterwards)

Now, a+b+c= kx²-ky²+2kxy+kx²+ky²=2kx²+2kxy = 2kx(x+y) = 1000

Divide by 2: kx(x+y) = 500

Now we set s=x+y: kxs = 500

Now we are looking for solutions of kxs=500, where k, x and s are integers and x < s < 2x. Since all of them divide 500, they can only take the values 1, 2, 4, 5, 10, 20, 25, 50, 100, 125, 250, 500. Some pseudocode to do this for arbitrary n (it and can be done by hand easily for n=1000)

If n is odd
  return "no solution"
else
  L = List of divisors of n/2
for x in L
  for s in L
    if x< s <2*x and n/2 is divisible by x*s
      y=s-x
      k=((n/2)/x)/s      
      add (k*(x*x-y*y),2*k*x*y,k*(x*x+y*y)) to list of solutions
sort the triples in the list of solutions
delete solutions appearing twice
return list of solutions
You can still improve this:

x will never be bigger than the root of n/2
the loop for s can start at x and stop after 2x has been passed (if the list is ordered)
For n = 1000, the program has to check six values for x and depending on the details of implementation up to one value for y. This will terminate before you release the button.

shareedit
edited Jun 20 '14 at 22:53

Gandora
436
answered May 14 '10 at 14:49

do_the_math
1913
add a comment
up vote
13
down vote
As mentioned above, ^ is bitwise xor, not power.

You can also remove the third loop, and instead use c = 1000-a-b; and optimize this a little.

Pseudocode

for a in 1..1000
    for b in a+1..1000
        c=1000-a-b
        print a, b, c if a*a+b*b=c*c
shareedit
edited May 12 '10 at 12:18
answered May 12 '10 at 10:28

Dogbert
66.1k24126157
add a comment
up vote
8
down vote
There is a quite dirty but quick solution to this problem. Given the two equation

a*a + b*b = c*c

a+b+c = 1000.

You can deduce the following relation

a = (1000*1000-2000*b)/(2000-2b)

or after two simple math transformation, you get:

a = 1000*(500-b) / (1000 - b)

since a must be an natural number. Hence you can:

for b in range(1, 500):
    if 1000*(500-b) % (1000-b) == 0:
        print b, 1000*(500-b) / (1000-b) 
Got result 200 and 375.

Good luck