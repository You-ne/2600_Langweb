#ifndef _MY_READINI_H
#define _MY_READINI_H

#include "my_tokenize.h"

enum val_type
{
    ID,
    STRING,
    INT,
};

union val_union
{
    int         val_int;
    char        *val_str; // les ID ou STRING sont stockés sous la même forme
};

struct val
{
    enum val_type       type;
    union val_union     uval;
};

struct key_val_list
{
    char                    *key;
    struct val              *value;
    struct key_val_list     *next;
};

struct section_list
{
    char                *section_name;
    struct key_val_list *values;
    struct section_list *next;
};

struct section_list     *my_readini(struct token_list *tokens);

// recherche dans la liste la section et la retourne
// retourne NULL en cas d'erreur
struct section_list     *my_section_lookup(
                                    struct section_list *ls,
                                    const char *section_name
                        );

// recherche dans la liste de key/value et la retourne
// retourne NULL en cas d'erreur
struct key_val_list     *my_key_val_lookup(
                                struct key_val_list *ls,
                                const char *key
                        );

// affiche le contenu des sections dans l'ordre de parsing
void    print_sections(struct section_list *s);

#endif /* _MY_READINI_H */
