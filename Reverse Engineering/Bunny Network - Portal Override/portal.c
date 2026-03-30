/*
 * CTF Challenge: "Bunny Network - Portal Override"
 * Difficulty: Beginner (RE)
 *
 * The portal requires an emergency override key. Your job is to find it
 * WITHOUT reading this source code - use a debugger like GDB!
 *
 * Compile:
 *   gcc -o portal portal.c -fno-stack-protector -g
 *
 * Solve with GDB:
 *   gdb ./portal
 *   (gdb) break validate_key
 *   (gdb) run
 *   Breakpoint 1 at 0x...
 *   (gdb) run
 *   Starting program...
 *   Enter emergency override key: anything
 *
 *   Breakpoint 1, validate_key (input=0x...) at challenge.c:35
 *   (gdb) next          ← step past build_key() so `expected` is populated
 *   (gdb)<F12> print expected
 *   $1 = "H34P_M4CC1PH3R_BYS74ND3R"
 *   (gdb) quit
 *
 *   $ ./challenge
 *   Enter emergency override key: H34P_M4CC1PH3R_BYS74ND3R
 *   [+] Override accepted! Routing tables restoring...
 *   FLAG: WICYS{m4c_c1ph3r_c4nt_h1d3_fr0m_gd6}
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* The "secret" is built at runtime so strings aren't trivially findable */
void build_key(char *buf) {
    /* Spells out: H34P_M4CC1PH3R_BYS74ND3R */
    const int parts[] = {
        0x48, 0x33, 0x34, 0x50, 0x5f, 0x4d,
        0x34, 0x43, 0x43, 0x31, 0x50, 0x48,
        0x33, 0x52, 0x5f, 0x42, 0x59, 0x53,
        0x37, 0x34, 0x4e, 0x44, 0x33, 0x52,
        0x00
    };
    for (int i = 0; parts[i] != 0; i++) {
        buf[i] = (char)parts[i];
    }
    buf[24] = '\0';
}

int validate_key(const char *input) {
    char expected[32];
    build_key(expected);                   /* <-- set a breakpoint here! */
    return strcmp(input, expected) == 0;
}

/* The "secret" is built at runtime so strings aren't trivially findable */
void build_flag(char *buf) {
    const int parts[] = {
        0x57, 0x49, 0x43, 0x59, 0x53, 0x7b, 0x6d, 0x34, 0x63, 0x5f, 0x63, 0x31, 0x70, 0x68, 0x33, 0x72, 0x5f, 0x63, 0x34, 0x6e, 0x74, 0x5f, 0x68, 0x31, 0x64, 0x33, 0x5f, 0x66, 0x72, 0x30, 0x6d, 0x5f, 0x67, 0x64, 0x36, 0x7d, 0x00
    };
    for (int i = 0; parts[i] != 0; i++) {
        buf[i] = (char)parts[i];
    }
    buf[36] = '\0';
}

void print_banner() {
    printf("\n");
    printf("  [=================================================]\n");
    printf("  [ BUNNY NETWORK - EMERGENCY ROUTING PORTAL v2.4.1 ]\n");
    printf("  [ STATUS: OFFLINE - MANUAL OVERRIDE REQUIRED      ]\n");
    printf("  [=================================================]\n");
    printf("\n");
}

int main(void) {
    char input[256];

    print_banner();
    printf("  [!] Warning: Routine connections disrupted.\n");
    printf("  [?] Enter emergency override key to restore node access:\n");
    printf("  > ");
    fflush(stdout);

    if (!fgets(input, sizeof(input), stdin)) {
        printf("  [!] Input error.\n");
        return 1;
    }

    /* Strip newline */
    size_t len = strlen(input);
    if (len > 0 && input[len - 1] == '\n') input[len - 1] = '\0';

    if (validate_key(input)) {
        char flag[64];
        build_flag(flag);
        printf("\n  [+] Override accepted! Routing tables restoring...\n");
        printf("  FLAG: %s\n\n", flag);
    } else {
        printf("\n  [-] Invalid override key. Incident response logged.\n\n");
    }

    return 0;
}
