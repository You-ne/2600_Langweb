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
};

struct token_list
{
    // le token lu
    enum token          token;
    // capture de la sous-chaîne de caractère correspondant au token
    char                *data; 
    // token suivant
    struct token_list   *next;
};

/* retourne une liste de token correspondant à l'analyse de text, 0 en cas d'erreur */
struct token_list   *get_token_list(const char *text);

#endif /* _MY_TOKENIZE_H */
