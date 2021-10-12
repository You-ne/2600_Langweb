/*#include<stdio.h>*/



int my_utf8_count_char(const char *s)
{
  int   n_chars = 0;

  while(*s)
    n_chars += ((*s++ & 0xc0) != 0x80); #everything that does not start as 10
  return(n_chars);                      #is a valid utf-8 char to count
}






/*
int main()
{
  const char *s1 = "la chaîne est trés bien encodé";
  const char *s2 = "♚ move to B12 take ♙";
  const char *s3 = "earing 🎵";
  
  printf("Number of UTF-8 characters : %d\n", my_utf8_count_char(s1));
  printf("Number of UTF-8 characters : %d\n", my_utf8_count_char(s2));
  printf("Number of UTF-8 characters : %d\n", my_utf8_count_char(s3));
  return (0);
}
*/
