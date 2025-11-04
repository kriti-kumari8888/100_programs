#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s source dest\n", argv[0]);
        return 1;
    }
    FILE *in = fopen(argv[1], "rb");
    if (!in) { perror("fopen source"); return 1; }
    FILE *out = fopen(argv[2], "wb");
    if (!out) { perror("fopen dest"); fclose(in); return 1; }

    char buf[4096];
    size_t r;
    while ((r = fread(buf, 1, sizeof(buf), in)) > 0) {
        if (fwrite(buf, 1, r, out) != r) { perror("fwrite"); fclose(in); fclose(out); return 1; }
    }

    fclose(in);
    fclose(out);
    return 0;
}
