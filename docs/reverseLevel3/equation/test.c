#include "stdio.h"

int main() {
  printf("%x\n", 255 << 8 * 0);
  printf("%x\n", 255 << (8 * 0));
  printf("%x\n", ~(255 << 8 * 0));
  printf("%x\n", (unsigned int)~(255 << 8 * 0));
}