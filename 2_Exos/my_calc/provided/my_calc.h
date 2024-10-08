#ifndef _MY_CALC_H
#define _MY_CALC_H
#include "my_parser.h"

struct def_list
{
    const char      *name;
    long int        val;
    struct def_list *next;
};

struct scope
{
    struct def_list     *defs;
    long int            current_val;
};

int     my_calc(struct parser *p, struct scope *s);

#endif /* _MY_CALC_H */
