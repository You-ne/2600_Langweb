#ifndef _MY_TOKENIZE_H
#define _MY_TOKENIZE_H

/* Liste des tokens identifiables */
enum token {
    SQUOTE_STRING,
    DQUOTE_STRING,
    INTEGER,
    IDENTIFIER,
    SPACE,
    NEWLINE,
    OBRACKET,
    CBRACKET,
    EQUAL,
    ERROR, // token non reconnu
};

struct token_list
{
    enum token          token; // le token lu
    char                *data; // capture de la sous-chaîne de caractère correspondant au token
    int                 line; // ligne où survient le token
    int                 cols; // colonne dans la ligne
    struct token_list   *next; // token suivant
};

/* retourne une liste de token correspondant à l'analyse de text, 0 en cas d'erreur */
struct token_list   *get_token_list(const char *text);

#endif /* _MY_TOKENIZE_H */
