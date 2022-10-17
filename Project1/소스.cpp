#include <stdio.h>

typedef struct {
    const char* name;
    int x, y;
} City;

City cities[] = {
    {"Write", 1336, 536}, {"Prosy", 977, 860},  {"Rabbi", 6, 758},    {"Addle", 222, 261},
    {"Smell", 1494, 836}, {"Quite", 905, 345},  {"Lives", 72, 714},   {"Cross", 23, 680},
    {"Synth", 1529, 785}, {"Tweak", 1046, 426}, {"Medic", 1485, 514}, {"Glade", 660, 476},
    {"Breve", 1586, 448}, {"Hotel", 1269, 576}, {"Toing", 398, 561},  {"Scorn", 617, 373},
    {"Cress", 1253, 403}, {"Zilch", 1289, 29},  {"React", 296, 659},  {"Fiche", 787, 278},
};

void City_print(City* c)
{
    printf("%s(%d,%d)", c->name, c->x, c->y);
}
void City_printAll(City* p, int count)
{
    for (int i = 0; i < count; i++, p++) {
        City_print(p);
        putchar(' ');
    }
    putchar('\n');
}

int main(void)
{
    City_printAll(cities, sizeof(cities) / sizeof(cities[0]));
    // sort here by name
    City_printAll(cities, sizeof(cities) / sizeof(cities[0]));
    // sort here by y coordinate
    City_printAll(cities, sizeof(cities) / sizeof(cities[0]));

    return 0;
}