#include <stdio.h>
#include <string.h>

const char* flag = "WICYS{H34p_M4cCiph3r_H4ck5_Th3_Pr0b4b1l1ty}";

int main() {
    char input[100];
    printf("--- Heap MacCipher's Luck Engine ---\n");
    printf("Enter the luck validation code: ");
    if (scanf("%99s", input) == 1) {
        if (strcmp(input, "7777777") == 0) {
            printf("Access granted to the Rainbow Vault... just kidding. You think luck is that easy?\n");
        } else {
            printf("Error: Probability misaligned. Luck level too low.\n");
        }
    }
    return 0;
}
